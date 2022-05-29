import pandas as pd
import os

def cleaning():
    df=pd.read_csv(os.getcwd()+"\static\\EV_dataset.csv")
    #print(df)


    nans_indices = df.columns[df.isna().any()].tolist()
    print(nans_indices)

    print(df.isnull().sum(axis = 0))

    #df=df['Electric Utility'].dropna().reset_index(drop=True)
    df.drop(df.index[(df['Electric Utility']).isna()], inplace=True)

    print(df)
    print()
    print()
    print()
    df.drop(df.index[(df['Vehicle Location']).isna()], inplace=True)
    print(df)
    print(df.isnull().sum(axis = 0))

    df.to_csv(os.getcwd()+'\static\\Clean_data_EV.csv', index=False)


if __name__=='__main__':
    cleaning()




