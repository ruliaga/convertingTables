import model
import view

def get_table():
    xlsx_directory = model.get_xlsx_directory() #получаем директорию файла
    df = model.xlsx_reading(xlsx_directory) #пандас создает датафрэйм
    view.message(df)
    return df

# def converting_columns(df):

