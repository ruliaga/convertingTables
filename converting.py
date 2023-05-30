import pandas as pd 


def converting_type_column(df):
    df['Ссылка.Номер'] = df['Ссылка.Номер'].apply(lambda x: str(x)[4:]).astype(int)
    df['Ссылка.Дата'] = df['Ссылка.Дата'].apply(lambda x: str(x)[:10]) 
    df['Ссылка.Дата'] = pd.to_datetime(df['Ссылка.Дата'], format='%d.%m.%Y') 
    df['Дата операции'] = df['Дата операции'].apply(lambda x: str(x)[:10]) 
    df['Дата операции'] = pd.to_datetime(df['Дата операции'], format='%d.%m.%Y')
    df['Номер оперции'] = pd.to_numeric(df['Номер операции'], errors="coerce")
    df['Номер операции'] = df['Номер операции'].apply(lambda x: x if str(x).isdigit() else 0).astype(int)
    return df

def add_new_columns(df):
    df.insert(4,'МПК + продукция', df['Ссылка.Номер'].map(str) + " " + df['Ссылка.Продукция'].map(str) + " " +df['Ссылка.Количество'].map(str) + "шт")
    df.insert(10,'Трудоемкость',round((df['Ссылка.Количество']*df['Технологическая операция.Норма времени (час)']*df['Увеличение норм']),2))
    df.insert(12,'Номер + операция', df['Номер операции'].map(str) + " " + df['Технологическая операция.Наименование'].map(str))
    return df
    

def add_1234(df):
   
    df.insert(20, '1234', 0)
    for i in range(0,df.shape[0]-1):

        if not pd.isnull(df['Дата операции'].values[i]) and pd.isnull(df['Дата операции'].values[i+1]):
            df['1234'].values[i] = 1    
        elif int(df['1234'].values[i-1])==1 and pd.isnull(df['Дата операции'].values[i]):
            df['1234'].values[i] = 2
        elif int(df['1234'].values[i-1])==2 and pd.isnull(df['Дата операции'].values[i]) and df['Рабочий центр'][i-1]==df['Рабочий центр'][i]:
            df['1234'].values[i] = 2
        elif int(df['1234'].values[i-1])==2 and pd.isnull(df['Дата операции'].values[i]) and df['Рабочий центр'][i-1]!=df['Рабочий центр'][i]:
            df['1234'].values[i] = 3 
        elif int(df['1234'].values[i-1])==3 and pd.isnull(df['Дата операции'].values[i]):
            df['1234'].values[i] = 4  
        else:
            df['1234'].values[i] = 0
    return df
    




