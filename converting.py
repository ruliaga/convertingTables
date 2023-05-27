import pandas as pd 
import model


xlsx_directory = model.get_xlsx_directory() #получаем директорию файла
df = model.xlsx_reading(xlsx_directory) #пандас создает датафрэйм


def converting_date_column(df):
    # df = df.astype({"Ссылка.Дата":"datetime64"})
    df['Ссылка.Номер'] = df['Ссылка.Номер'].apply(lambda x: str(x)[4:]).astype(int)
    df['Ссылка.Дата'] = pd.to_datetime(df['Ссылка.Дата'], format="mixed")
    df['Дата операции'] = pd.to_datetime(df['Дата операции'], format="mixed")
    print(df)

    print(df.dtypes)

converting_date_column(df)

