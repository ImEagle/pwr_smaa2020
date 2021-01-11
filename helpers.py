import pandas


def make_flat(df: pandas.DataFrame):
    df_flat = df.unstack()
    df_flat.columns = ['_'.join(col).strip() for col in df_flat.columns.values]
    return df_flat