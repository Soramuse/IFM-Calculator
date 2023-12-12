import pandas as pd
import numpy as np
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.cm as cm
from scipy.spatial.transform import Rotation as R

import os


def import_data(f_path, file_name):
    """
    Import data from a CSV file.

    Args:
        f_path (str): The path to the directory containing the CSV file.
        file_name (str): The name of the CSV file (without the extension).

    Returns:
        tuple: A tuple containing a status message and the imported data as a pandas DataFrame.
            - If the file is not found, the status message will be an error message and the DataFrame will be empty.
            - If there is an error reading the file, the status message will be an error message and the DataFrame will be empty.
            - If the file does not have the expected columns, the status message will be an error message and the DataFrame will be empty.
            - If the file is successfully imported, the status message will be 'Success' and the DataFrame will contain the imported data.
    """
    file_path = os.path.join(f_path, file_name + '.csv')
    if not os.path.exists(file_path):
        return f"Error: File {file_name}.csv not found.", pd.DataFrame()
    try:
        data = pd.read_csv(file_path)
    except Exception as e:
        return f"Error: Cannot read file {file_name}.csv. {str(e)}", pd.DataFrame()
    expected_columns = ['Node number', 'LOCX', 'LOCY',
                        'LOCZ', 'DEF_LOCX', 'DEF_LOCY', 'DEF_LOCZ']
    if not data.columns.equals(pd.Index(expected_columns)):
        return f"Error: File {file_name}.csv must have columns {expected_columns}.", pd.DataFrame()
    return 'Success', data


def pairing(dfa, dfb):
    """
    Pair nodes from two dataframes based on their coordinates.

    Args:
        dfa (pd.DataFrame): First dataframe containing node information.
        dfb (pd.DataFrame): Second dataframe containing node information.

    Returns:
        tuple: A tuple containing the matched dataframe and a flag indicating if the dataframes were reversed.
    """
    if len(dfa) <= len(dfb):
        df1 = dfa
        df2 = dfb
        reverse = False
    else:
        df1 = dfb
        df2 = dfa
        reverse = True

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
    return df_matched, reverse


def IFM_Calculation(df_matched):
    """
    Calculate the Integrated Fracture Mechanics (IFM) using displacement and detachment.

    Args:
        df_matched (DataFrame): A pandas DataFrame containing matched data.

    Returns:
        DataFrame: A new DataFrame with calculated values including Displacement, Detachment, and IFM.
    """
    # Calculate displacement between deformed and original locations in X and Y directions
    displacement = np.sqrt(((df_matched['DEF_LOCX1'] - df_matched['DEF_LOCX2']) - (df_matched['LOCX1'] - df_matched['LOCX2'])) ** 2 + (
        (df_matched['DEF_LOCY1'] - df_matched['DEF_LOCY2']) - (df_matched['LOCY1'] - df_matched['LOCY2'])) ** 2)
    # Calculate detachment between deformed and original locations in Z direction
    detachment = np.sqrt(((df_matched['DEF_LOCZ1'] - df_matched['DEF_LOCZ2']) - (
        df_matched['LOCZ1'] - df_matched['LOCZ2'])) ** 2)
    # Calculate IFM (Integrated Fracture Mechanics) using displacement and detachment
    IFM = np.sqrt(displacement ** 2 + detachment ** 2)
    # Create a new dataframe with calculated values
    output = df_matched.assign(
        Displacement=displacement, Detachment=detachment, IFM=IFM)
    # Rename the columns of the output dataframe
    output.columns = ['Node Number1', 'X Location1 (mm)', 'Y Location1 (mm)', 'Z Location1 (mm)', 'Deformed X Location1 (mm)', 'Deformed Y Location1 (mm)', 'Deformed Z Location1 (mm)', 'Node Number2', 'X Location2 (mm)',
                      'Y Location2 (mm)', 'Z Location2 (mm)', 'Deformed X Location2 (mm)', 'Deformed Y Location2 (mm)', 'Deformed Z Location2 (mm)', 'Distance (mm)', 'Sliding distance (mm)', 'Gap distance (mm)', 'IFM distance (mm)']
    # Print the IFM output dataframe
    print('IFM output \n', output)
    return output


def calculate_extreme_values(df_matched, accu):
    """
    Calculate the extreme values of the given DataFrame based on the specified accuracy.

    Args:
        df_matched (DataFrame): The DataFrame containing the data to be analyzed.
        accu (float): The accuracy threshold for selecting extreme values.

    Returns:
        DataFrame: A DataFrame containing the extreme nodes based on the given accuracy.

    """
    x = df_matched.query('abs(LOCX1) < @accu')
    y = df_matched.query('abs(LOCY1) < @accu')
    df_max = pd.concat([x.nlargest(1, 'LOCY1'), x.nsmallest(
        1, 'LOCY1'), y.nlargest(1, 'LOCX1'), y.nsmallest(1, 'LOCX1')])
    print('Extreme nodes \n', df_max)
    return df_max


def vector_angle(n1, n2, reverse=False):
    """
    Calculate the angle between two vectors in degrees.

    Parameters:
    n1 (array-like): The first vector.
    n2 (array-like): The second vector.
    reverse (bool, optional): If True, reverse the order of the normal vectors. Defaults to False.

    Returns:
    float: The angle between the two vectors in degrees.
    """
    if reverse:  # Reverse the order of the normal vectors if paired nodes change the order
        n1, n2 = n2, n1

    dot_1 = np.linalg.norm(n1)
    dot_2 = np.linalg.norm(n2)
    cos_x = np.dot(n1, n2) / (dot_1 * dot_2)
    angle_rad = np.arccos(cos_x)

    cross_product = np.cross(n1, n2)
    if cross_product < 0:
        angle_rad *= -1

    angle = angle_rad * 180 / np.pi
    return angle


def calculate_angle(df_max, row1, row2, col1, col2, reverse=False):
    angle_0 = vector_angle(np.array((df_max.iat[row1, col1] - df_max.iat[row2, col1], df_max.iat[row1, col2] - df_max.iat[row2, col2])),
                           np.array((df_max.iat[row1, col1+7] - df_max.iat[row2, col1+7], df_max.iat[row1, col2+7] - df_max.iat[row2, col2+7])), reverse)
    angle_1 = vector_angle(np.array((df_max.iat[row1, col1+3] - df_max.iat[row2, col1+3], df_max.iat[row1, col2+3] - df_max.iat[row2, col2+3])),
                           np.array((df_max.iat[row1, col1+10] - df_max.iat[row2, col1+10], df_max.iat[row1, col2+10] - df_max.iat[row2, col2+10])), reverse)
    return angle_1 - angle_0


def calculate_normal(df):
    """
    Calculate the normal vector of a plane using least squares method.

    Args:
        df (pandas.DataFrame): DataFrame containing the coordinates of the plane.

    Returns:
        numpy.ndarray: The normal vector of the plane.

    """
    x = df.loc[:, 'DEF_LOCX'].values
    y = df.loc[:, 'DEF_LOCY'].values
    z = df.loc[:, 'DEF_LOCZ'].values
    A = np.vstack((x, y, np.ones(len(x)))).T
    normal = np.linalg.lstsq(A, z, rcond=None)[0]
    print("Normal vector:", normal)
    print("Point on plane:", (0, 0, -normal[2]/normal[2]))
    return normal


def calculate_theta(normal_a, normal_b):
    """
    Calculate the angle between two normal vectors.

    Parameters:
    normal_a (numpy.ndarray): The first normal vector.
    normal_b (numpy.ndarray): The second normal vector.

    Returns:
    numpy.ndarray: An array containing the angle between the two normal vectors.
    """
    cos_theta = np.dot(normal_a, normal_b) / \
        (np.linalg.norm(normal_a) * np.linalg.norm(normal_b))
    theta = np.arccos(cos_theta)
    return np.array([theta])


def calculate_rotation_matrix(points_initial, points_transformed):
    """
    Calculate the rotation matrix based on the given initial points and transformed points.

    Args:
        points_global (numpy.ndarray): Array of initial points.
        points_transformed (numpy.ndarray): Array of transformed points.

    Returns:
        numpy.ndarray: Rotation matrix.
    """
    x_initial = points_initial[1] - points_initial[0]
    x_initial /= np.linalg.norm(x_initial)

    z_initial = np.cross(x_initial, points_initial[3] - points_initial[2])
    z_initial /= np.linalg.norm(z_initial)

    y_initial = np.cross(z_initial, x_initial)

    x_transformed = points_transformed[1] - points_transformed[0]
    x_transformed /= np.linalg.norm(x_transformed)

    z_transformed = np.cross(
        x_transformed, points_transformed[3] - points_transformed[2])
    z_transformed /= np.linalg.norm(z_transformed)

    if np.dot(z_transformed, z_initial) < 0:
        z_transformed = -z_transformed

    y_transformed = np.cross(z_transformed, x_transformed)

    rotation_matrix_before = np.column_stack((x_initial, y_initial, z_initial))
    rotation_matrix_after = np.column_stack(
        (x_transformed, y_transformed, z_transformed))

    rotation_matrix = rotation_matrix_after @ np.linalg.inv(
        rotation_matrix_before)

    return rotation_matrix


def calculate_matrix_euler(df_max, reverse):
    """
    Calculate the relative rotation matrix and Euler angles between two sets of points.

    Args:
        df_max (pandas.DataFrame): DataFrame containing the maximum values.
        reverse (bool): Flag indicating whether to reverse the calculation.

    Returns:
        tuple: A tuple containing the relative rotation matrix and Euler angles.

    """
    points_1 = df_max.iloc[:4, 1:4].values
    points_2 = df_max.iloc[:4, 8:11].values
    def_points_1 = df_max.iloc[:4, 4:7].values
    def_points_2 = df_max.iloc[:4, 11:14].values

    rotation_matrix_1 = calculate_rotation_matrix(points_1, points_2)
    rotation_matrix_2 = calculate_rotation_matrix(def_points_1, def_points_2)
    relative_rotation_matrix = rotation_matrix_2 @ np.linalg.inv(
        rotation_matrix_1)
    rotation = R.from_matrix(relative_rotation_matrix)
    Eulerangles = rotation.as_euler('xyz', degrees=True)
    Eulerangles = -Eulerangles
    return relative_rotation_matrix, Eulerangles


def export(ExportFolder, ExportName, output, row3, angle_x, angle_y, angle_z1, theta, Eulerangles, IFM_summary, Gap_summary, SD_summary):
    """
    Export the results to a CSV file.

    Parameters:
    - ExportFolder (str): The folder path where the CSV file will be exported.
    - ExportName (str): The name of the CSV file.
    - output (pandas.DataFrame): The data to be exported.
    - row3 (int): The number of nodes.
    - angle_x (float): The angle in the X-axis.
    - angle_y (float): The angle in the Y-axis.
    - angle_z1 (float): The rotation angle in the Z-axis.
    - theta (float): The theta value.
    - Eulerangles (float): The Euler angles.
    - IFM_summary (dict): The summary statistics for IFM.
    - Gap_summary (dict): The summary statistics for Gap.
    - SD_summary (dict): The summary statistics for SD.

    Returns:
    - str: 'Success' if the export is successful, otherwise an exception message.
    """
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


def plot(data, target, reverse):
    """
    Plot a 3D scatter plot.

    Args:
        data (pandas.DataFrame): The data containing the coordinates and target values.
        target (str): The column name of the target values.
        reverse (bool): If True, reverse the order of the scatter plots.

    Returns:
        matplotlib.figure.Figure: The generated figure.
    """
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
    if reverse:
        scatter1 = ax.scatter(x1, y1, z1, c=c, s=40, alpha=1, cmap=cmap)
        scatter2 = ax.scatter(x2, y2, z2, s=10, alpha=0.5)
    else:
        scatter1 = ax.scatter(x2, y2, z2, c=c, s=40, alpha=1, cmap=cmap)
        scatter2 = ax.scatter(x1, y1, z1, s=10, alpha=0.5)

    vmin = c.min()
    vmax = c.max()
    fig.colorbar(scatter1, ax=ax, pad=0.05, ticks=np.linspace(vmin, vmax, 10))

    ax.set_title(target)
    ax.set_axis_off()
    ax.auto_scale_xyz([x1.min(), x1.max()], [
                      x1.min(), x1.max()], [x1.min(), x1.max()])
    return fig
