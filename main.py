import controller
import view

df = controller.get_table()
df = controller.converting_table(df)
print(df.info())
view.message('.....creating Operations.xlsx')
view.progressbar()
controller.creating_new_file(df)

