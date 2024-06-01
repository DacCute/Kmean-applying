import pandas as pd

def pro_df(df, features):
    try:
        data_table = df[features]
        return data_table
    except KeyError:
        print("Cannot process!")
        return None
    
def data_in(floca):
    data = pd.read_csv(floca,sep=';')
    return data

