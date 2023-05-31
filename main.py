import controller

df = controller.get_table()
df = controller.converting_table(df)
print(df.info())
controller.creating_new_file(df)

# def categories(df):
#     for i in range(0,df.shape[0]-1):
#         if df['Технологическая операция.Наименование'].values[i].find('Сверление')!=-1:
#             df['Технологическая операция.Наименование'].values[i] = "Сверление"
#     return df
# categories(df)
# print(df[df['Технологическая операция.Наименование']])

