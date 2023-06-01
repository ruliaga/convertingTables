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
    df = converting.add_1234_column(df)
    df = converting.add_1_column(df)
    df = converting.add_repeat_column(df)
    df = converting.add_sumOfOperation_column(df)
    df = converting.add_percentOfReady_column(df)
    df = converting.add_statusOfReady_column(df)
    #добавить в условие операция "Токарная" в столбец 'статус готовности'
    df = converting.add_mustToDo_column(df)
    #пересмотреть значение столбца "Осталось сделать"
    df = converting.add_trudoemkost2_column(df)
    df = converting.add_timeOf_operation_column(df)
    df = converting.add_nowOperation_column(df)
    df = converting.add_backOperation_column(df)
    df = converting.add_nextOperation_column(df)
    df = converting.add_key_column(df)    
    df = converting.categories(df)
    return df

def creating_new_file(df):
    model.create_xlsx(df)



