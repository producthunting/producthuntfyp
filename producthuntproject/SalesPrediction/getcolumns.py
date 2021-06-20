import pandas as pd

def get_columns(path):
    df=pd.read_csv(path)
    print(list(df.columns))
    return list(df.columns)

# get_columns('advertising.csv')