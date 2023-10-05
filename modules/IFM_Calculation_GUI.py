import pandas as pd
import numpy as np
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.cm as cm

import os


def check(f_path):
    file_names = ['X1', 'X2', 'Y1', 'Y2', 'Z1', 'Z2',
                  'DX1', 'DX2', 'DY1', 'DY2', 'DZ1', 'DZ2']
    for file_name in file_names:
        file_path = os.path.join(f_path, file_name + '.txt')
        if not os.path.exists(file_path):
            return f"Error: File {file_name}.txt not found."
        try:
            data = pd.read_csv(file_path, sep='\t')
            if len(data.columns) != 5:
                return f"Error: File {file_name}.txt must have 5 columns."
        except Exception as e:
            return f"Error: Cannot read file {file_name}.txt. {str(e)}"
    return "OK"


def import_data(f_path, i):
    data_series = pd.DataFrame()
    file_names = ['X', 'Y', 'Z', 'DX', 'DY', 'DZ']
    for file_name in file_names:
        file = f_path + '/' + file_name + i + '.txt'
        try:
            if file_name == 'X':
                data = pd.read_csv(file, sep='\t', usecols=[0, 4])
            else:
                data = pd.read_csv(file, sep='\t', usecols=[4])
            data_series = pd.concat(
                [data_series, data], axis=1, ignore_index=True)
        except (FileNotFoundError, IOError):
            error_msg = f"Error: Cannot read file {file}."
            return error_msg
    data_series.columns = ['Node number', 'LOCX', 'LOCY',
                           'LOCZ', 'DEF_LOCX', 'DEF_LOCY', 'DEF_LOCZ']
    return data_series


def pairing(dfa, dfb):  # Pairing nodes
    if len(dfa) <= len(dfb):
        df1 = dfa
        df2 = dfb
    else:
        df1 = dfb
        df2 = dfa
    p1 = np.array(df1.loc[:, ['LOCX', 'LOCY', 'LOCZ']])
    p2 = np.array(df2.loc[:, ['LOCX', 'LOCY', 'LOCZ']])
    dist = np.sqrt(((p1[:, None, :] - p2) ** 2).sum(axis=2))
    idx = np.argmin(dist, axis=1)
    df2_matched = df2.iloc[idx].reset_index(drop=True)
    df_matched = pd.concat([df1, df2_matched], axis=1)
    df_matched['distance'] = dist[np.arange(len(df1)), idx]
    df_matched.columns = ['Node number1', 'LOCX1', 'LOCY1', 'LOCZ1', 'DEF_LOCX1', 'DEF_LOCY1', 'DEF_LOCZ1', 'Node number2',
                          'LOCX2', 'LOCY2', 'LOCZ2', 'DEF_LOCX2', 'DEF_LOCY2', 'DEF_LOCZ2', 'distance']
    print('Nodes pairing success! \n')
    print(df_matched)
    return df_matched


def IFM_Calculation(df_matched):  # Calculate IFM
    displacement = np.sqrt(((df_matched['DEF_LOCX1'] - df_matched['DEF_LOCX2']) - (df_matched['LOCX1'] - df_matched['LOCX2'])) ** 2 + (
        (df_matched['DEF_LOCY1'] - df_matched['DEF_LOCY2']) - (df_matched['LOCY1'] - df_matched['LOCY2'])) ** 2)
    detachment = np.sqrt(((df_matched['DEF_LOCZ1'] - df_matched['DEF_LOCZ2']) - (
        df_matched['LOCZ1'] - df_matched['LOCZ2'])) ** 2)
    IFM = np.sqrt(displacement ** 2 + detachment ** 2)
    output = df_matched.assign(
        Displacement=displacement, Detachment=detachment, IFM=IFM)
    output.columns = ['Node Number1', 'X Location1 (mm)', 'Y Location1 (mm)', 'Z Location1 (mm)', 'Deformed X Location1 (mm)', 'Deformed Y Location1 (mm)', 'Deformed Z Location1 (mm)', 'Node Number2', 'X Location2 (mm)',
                      'Y Location2 (mm)', 'Z Location2 (mm)', 'Deformed X Location2 (mm)', 'Deformed Y Location2 (mm)', 'Deformed Z Location2 (mm)', 'Distance (mm)', 'Displacement (mm)', 'Detachment (mm)', 'IFM (mm)']
    print('IFM output \n', output)
    return output


def calculate_extreme_values(df_matched, accu):  # Calculate extreme nodes
    x = df_matched.query('abs(LOCX1) < @accu')
    y = df_matched.query('abs(LOCY1) < @accu')
    df_max = pd.concat([x.nlargest(1, 'LOCY1'), x.nsmallest(
        1, 'LOCY1'), y.nlargest(1, 'LOCX1'), y.nsmallest(1, 'LOCX1')])
    print('Extreme nodes \n', df_max)
    return df_max


def calculate_angle(n1, n2):  # Calculate angle using extreme nodes
    dot_1 = np.linalg.norm(n1)
    dot_2 = np.linalg.norm(n2)
    cos_x = np.dot(n1, n2) / (dot_1 * dot_2)
    angle_rad = np.arccos(cos_x)

    cross_product = np.cross(n1, n2)
    if cross_product < 0:
        angle_rad *= -1

    angle = angle_rad * 180 / np.pi
    return angle


def calculate_normal(df):  # Calculate normal vector
    x = df.loc[:, 'DEF_LOCX'].values
    y = df.loc[:, 'DEF_LOCY'].values
    z = df.loc[:, 'DEF_LOCZ'].values
    A = np.vstack((x, y, np.ones(len(x)))).T
    normal = np.linalg.lstsq(A, z, rcond=None)[0]
    print("Normal vector:", normal)
    print("Point on plane:", (0, 0, -normal[2]/normal[2]))
    return normal


# Calculate angle between two normal vectors
def calculate_theta(normal_a, normal_b):
    cos_theta = np.dot(normal_a, normal_b) / \
        (np.linalg.norm(normal_a) * np.linalg.norm(normal_b))
    theta = np.arccos(cos_theta)
    return np.array([theta])


def calculate_rotation_matrix(normal_a, normal_b):  # Calculate rotation matrix
    v = np.cross(normal_a, normal_b)
    s = np.linalg.norm(v)
    c = np.dot(normal_a, normal_b)
    vx = np.array([[0, -v[2], v[1]], [v[2], 0, -v[0]], [-v[1], v[0], 0]])
    R = np.eye(3) + vx + np.dot(vx, vx) * (1 - c) / (s ** 2)
    print("Rotation Matrix = \n", R)
    return R


def calculate_eulerangles(R):  # Calculate Euler angles
    sy = np.sqrt(R[0, 0] ** 2 + R[1, 0] ** 2)
    singular = sy < 1e-6
    if not singular:
        x = np.arctan2(R[2, 1], R[2, 2])
        y = np.arctan2(-R[2, 0], sy)
        z = np.arctan2(R[1, 0], R[0, 0])
    else:
        x = np.arctan2(-R[1, 2], R[1, 1])
        y = np.arctan2(-R[2, 0], sy)
        z = 0
    Eulerangles = np.degrees(np.array([x, y, z]))
    print('Eulerangles', Eulerangles)
    return Eulerangles


def export(ExportFolder, ExportName, output, row3, angle_x, angle_y, angle_z1, theta, Eulerangles, IFM_summary, Gap_summary, SD_summary):  # Export results
    try:
        file_name = ExportName + '.csv'
        Summary_name = 'Output Summary_' + file_name
        Sum = pd.DataFrame({'Nodes count': [row3],
                            'IFM averaged': [IFM_summary['mean']],
                            'IFM maximum': [IFM_summary['max']],
                            'IFM minimum': [IFM_summary['min']],
                            'IFM std': [IFM_summary['std']],
                            'Gap averaged': [Gap_summary['mean']],
                            'Gap maximum': [Gap_summary['max']],
                            'Gap minimum': [Gap_summary['min']],
                            'Gap std': [Gap_summary['std']],
                            'SD averaged': [SD_summary['mean']],
                            'SD maximum': [SD_summary['max']],
                            'SD minimum': [SD_summary['min']],
                            'SD std': [SD_summary['std']],
                            'X axis angle': [angle_x],
                            'Y axis angle': [angle_y],
                            'Z axis rotation': [angle_z1],
                            'theta': [theta],
                            'Euler angles': [Eulerangles]})
        output.to_csv(os.path.join(ExportFolder, file_name))
        Sum.to_csv(os.path.join(ExportFolder, Summary_name))
        return 'Success'
    except Exception as e:
        return e


def plot(data, target):  # Plot 3D scatter plot
    x1 = data.loc[:, 'Deformed X Location1 (mm)']
    y1 = data.loc[:, 'Deformed Y Location1 (mm)']
    z1 = data.loc[:, 'Deformed Z Location1 (mm)']
    x2 = data.loc[:, 'Deformed X Location2 (mm)']
    y2 = data.loc[:, 'Deformed Y Location2 (mm)']
    z2 = data.loc[:, 'Deformed Z Location2 (mm)']
    c = data.loc[:, target]

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    cmap = cm.get_cmap('turbo')
    scatter1 = ax.scatter(x1, y1, z1, c=c, s=40, alpha=1, cmap=cmap)
    scatter2 = ax.scatter(x2, y2, z2, s=10, alpha=0.5)
    # tri1 = ax.plot_trisurf(x1, y1, z1, edgecolor='grey',
    #                        linewidth=0.2, antialiased=True, alpha=0.2)

    vmin = c.min()
    vmax = c.max()
    fig.colorbar(scatter1, ax=ax, pad=0.05, ticks=np.linspace(vmin, vmax, 10))

    ax.set_title(target)
    ax.set_axis_off()
    ax.auto_scale_xyz([x1.min(), x1.max()], [
                      x1.min(), x1.max()], [x1.min(), x1.max()])
    return fig
