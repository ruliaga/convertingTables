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



