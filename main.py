from emp_csv import *
FILENAME= 'data.csv'
MENU = {
    '1':'Открыть файл',
    '2':'Добавить',
    '3':'Улдалить',
    '4':'Поиск',
    '5':'Средний возраст',
    '6':'Сохранить',
    '7':'',
    '0':''
    'exit':'Выход'
}
for k,v in MENU.items():
    print(k,'-',v)

while True:
    action =input('>_')
    if action=='1':
        file_open(FILENAME)
    elif action=='2':
        insert(input('ФИО:'),input('Возраст:'),input('Телефон:'),input('Отдел:'))
    elif action == '3':
        print(drop_by_arg(input("Значение"), input("Колонка")))
    elif action == '4':
        find(input("Значение"), input("Колонка"))
    elif action=='6':
        save(FILENAME)
    elif action=='7':
        show_rows()
    elif action == 'exit':
        break
