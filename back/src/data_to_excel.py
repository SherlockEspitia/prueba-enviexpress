import pandas as pd

def convert_to_df(data, colums):
    df = pd.DataFrame(data, columns=colums)
    return df

def save_to_excel(df):
    file_path = "pedidos_eliminados.xlsx"
    df.to_excel(file_path,index=False)
    return file_path