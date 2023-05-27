import pandas as pd 


def converting_type_column(df):
    df['Ссылка.Номер'] = df['Ссылка.Номер'].apply(lambda x: str(x)[4:]).astype(int)
    df['Ссылка.Дата'] = pd.to_datetime(df['Ссылка.Дата'], format='mixed')
    df['Дата операции'] = pd.to_datetime(df['Дата операции'], format="mixed")
    df['Номер оперции'] = pd.to_numeric(df['Номер операции'], errors="coerce")
    df['Номер операции'] = df['Номер операции'].apply(lambda x: x if str(x).isdigit() else 0).astype(int)
    return df

def add_new_columns(df):
    df.insert(4,'МПК + продукция', df['Ссылка.Номер'].map(str) + " " + df['Ссылка.Продукция'].map(str) + " " +df['Ссылка.Количество'].map(str) + "шт")
    df.insert(10,'Трудоемкость',round((df['Ссылка.Количество']*df['Технологическая операция.Норма времени (час)']*df['Увеличение норм']),2))
    df.insert(12,'Номер + операция', df['Номер операции'].map(str) + " " + df['Технологическая операция.Наименование'].map(str))
    return df
    

    




