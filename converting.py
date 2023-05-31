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
    

def add_1234_column(df):
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

def add_1_column(df):
    df.insert(21, '1', 0)
    for i in range(0,df.shape[0]-6):
        if df['1234'].values[i+5] == 4 or df['1234'].values[i+4] == 4 or df['1234'].values[i+3] == 4 or df['1234'].values[i+2] == 4 or df['1234'].values[i+1] == 4 or df['1234'].values[i] == 4:
            df['1'].values[i]=1
        else:
            df['1'].values[i]=0
    return df 

def add_repeat_column(df):
    df.insert(22, 'Повторение', 0)
    for i in range(0,df.shape[0]-1):
        if df['Ссылка.Номер'].values[i] == df['Ссылка.Номер'].values[i-1] and df['Номер операции'].values[i] == df['Номер операции'].values[i-1] and df['Рабочий центр'].values[i] == df['Рабочий центр'].values[i-1]:
            df['Повторение'].values[i]=1
        else:
            df['Повторение'].values[i]=0
    return df 
 
def add_sumOfOperation_column(df):
    df.insert(23, 'Сумма операции', float(0))
    for i in range(0,df.shape[0]-1):
        if df['Повторение'].values[i] == 0:
            df['Сумма операции'].values[i] = df['Количество предъявленных'].values[i]
        else:
            df['Сумма операции'].values[i] = float(df['Сумма операции'].values[i-1]) + df['Количество предъявленных'].values[i]
    return df 

def add_percentOfReady_column(df):
    df.insert(24, '% готовности', round(df['Сумма операции']*100/df['Ссылка.Количество'],2))
    
    return df 

def add_statusOfReady_column(df):
    df.insert(25, 'Статус готовности', '')
    for i in range(0,df.shape[0]-2):
        if  (df['% готовности'].values[i] > 0 and df['% готовности'].values[i] < 92 and df['1234'].values[i] ==1 and df['1234'].values[i+1] == 2) or df['1234'].values[i] == 2 or df['1234'].values[i] == 3 or df['1234'].values[i] == 4:
            df['Статус готовности'].values[i] = 'Не готово'
        else:
            df['Статус готовности'].values[i] = ''
    return df 

def add_mustToDo_column(df):
    df.insert(26, 'Осталось сделать', df['Ссылка.Количество'] - df['Сумма операции'])
    return df 

def add_trudoemkost2_column(df):
    df.insert(27, 'Трудоемкость2', 0.0)
    for i in range(0,df.shape[0]-1):
        if df['Осталось сделать'].values[i]>0:
            df['Трудоемкость2'].values[i] = df['Осталось сделать'].values[i]*df['Технологическая операция.Норма времени (час)'].values[i]*df['Увеличение норм'].values[i]
        else:
            df['Трудоемкость2'].values[i] = 0.0
    return df 

def add_timeOf_operation_column(df):
    df.insert(28, 'Время операции', df['Трудоемкость2']/24)
    return df 

def add_nowOperation_column(df):
    df.insert(29, 'Текущая операция', df['Номер + операция'])
    return df 

def add_backOperation_column(df):
    df.insert(30, 'Предыдущая операция', '')
    for i in range(0,df.shape[0]-1):
        if df['Текущая операция'].values[i]!=df['Текущая операция'].values[i-1]:
            df['Предыдущая операция'].values[i]=df['Текущая операция'].values[i-1]
        elif df['Текущая операция'].values[i]!=df['Текущая операция'].values[i-2]:
            df['Предыдущая операция'].values[i]=df['Текущая операция'].values[i-2]
        elif df['Текущая операция'].values[i]!=df['Текущая операция'].values[i-3]:
            df['Предыдущая операция'].values[i]=df['Текущая операция'].values[i-3]
        elif df['Текущая операция'].values[i]!=df['Текущая операция'].values[i-4]:
            df['Предыдущая операция'].values[i]=df['Текущая операция'].values[i-4]
        elif df['Текущая операция'].values[i]!=df['Текущая операция'].values[i-5]:
            df['Предыдущая операция'].values[i]=df['Текущая операция'].values[i-5]
        elif df['Текущая операция'].values[i]!=df['Текущая операция'].values[i-6]:
            df['Предыдущая операция'].values[i]=df['Текущая операция'].values[i-6]
        elif df['Текущая операция'].values[i]!=df['Текущая операция'].values[i-7]:
            df['Предыдущая операция'].values[i]=df['Текущая операция'].values[i-7]
        else:
            df['Предыдущая операция'].values[i]=df['Текущая операция'].values[i-8]
    return df 

def add_nextOperation_column(df):
    df.insert(31, 'Следущая операция', '')
    for i in range(0,df.shape[0]-1):
        if df['Ссылка.Номер'].values[i] == df['Ссылка.Номер'].values[i+1]:
            df['Следущая операция'].values[i] = df['Текущая операция'].values[i+1]
        else:
            df['Следущая операция'].values[i] = 'Выполнено'
    return df

def add_key_column(df):
    df.insert(32, 'Ключ', '')
    for i in range(0,df.shape[0]-1):
        df['Ключ'].values[i] = str(df['МПК + продукция'].values[i]) + " " + str(df['Номер + операция'].values[i])
    return df