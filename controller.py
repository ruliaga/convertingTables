import model
import view
import converting

def get_table():
    xlsx_directory = model.get_xlsx_directory() #получаем директорию файла
    df = model.xlsx_reading(xlsx_directory) #пандас создает датафрэйм
    view.message(df)
    return df

def converting_table(df):
    df = converting.converting_type_column(df)
    df = model.sort_dataframe(df)
    df = model.reindex_dataframe(df)
    df = converting.add_new_columns(df)
    df = converting.add_1234(df)
    df = converting.add_1(df)
    return df

def creating_new_file(df):
    model.create_xlsx(df)



