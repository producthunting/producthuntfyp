import pandas as pd

dtypes1=['Int8','Int16','Int32','Int64','UInt8','UInt16','UInt32','UInt64','Float32',
    'Float64','DatetimeTZ']

def get_columns(path):
    selected_columns = []
    df=pd.read_csv(path)
    for i in list(df.columns):
        if df[i].dtype in dtypes1:
            selected_columns.append(i)

    print(selected_columns)
    return selected_columns

# get_columns('advertising.csv')