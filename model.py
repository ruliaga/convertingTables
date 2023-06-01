import pandas as pd 
import glob 
import os


def get_xlsx_directory (): 
    path = os.path.dirname(os.path.realpath(__file__)) #функция читает текущее расположение файла py
    xlsx_directory = glob.glob(path + "\*.xlsx") #находит файлы xlsx и создает список из названий
    return xlsx_directory #возвращает этот список


def xlsx_reading(xlsx_directory): #функция создает датафрейм из файла xlsx
    df = pd.read_excel(xlsx_directory[0])
    return df

def create_xlsx(df):
    df.to_excel('Operations.xlsx')

def reindex_dataframe(df):
    df = df.reset_index(drop=True)
    return df

def sort_dataframe(df): # сортировка по трем столбцам
    df = df.sort_values(['Ссылка.Номер', 'Ссылка.Дата','Номер операции'])
    return df



