import controller

df = controller.get_table()
df = controller.converting_table(df)
print(df.info())
controller.creating_new_file(df)

