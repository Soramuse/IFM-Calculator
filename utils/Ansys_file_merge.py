import os
import pandas as pd
import tkinter as tk
from tkinter import filedialog

def input_file():
    # GET FILE NAME by tkinter
    f_path = filedialog.askdirectory()
    return f_path


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

if __name__ == '__main__':
    f_path = input_file()
    check_result = check(f_path)
    if check_result == 'OK':
        data_series_1 = import_data(f_path, '1')
        data_series_2 = import_data(f_path, '2')
        # write to csv
        data_series_1.to_csv(f_path + '/data_series_1.csv', index=False)
        data_series_2.to_csv(f_path + '/data_series_2.csv', index=False)
        print('Data merge success! \n')
    else:
        print(check_result)
