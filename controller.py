import model
import view

def start_program():
    xlsx_directory = model.get_xlsx_directory()
    df = model.xlsx_reading(xlsx_directory)
    view.message(df)