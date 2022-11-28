import csv
csv_file =[]
#Открыть файл
def file_open(file_name):
    with open(file_name, newline='',ending='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            csv_file.append(row)
        print('Файл открыт. Записей:', len(csv_file))
#Добавление
def insert(fio,age,tel,otd):
    try:
        mx=max(csv_file,key=lambda x:int(x['ном']))
        csv_file.append({'ном':int(mx['ном'])+1,
                         'фио':,
                         'возраст':,
                         'телефон':,
                         'отдел':,
    except Exception as e:
        return f' Ошибка при добавлении записи' {e}
    print('Записи добавлены')

#Удаление
def drop_by_arg(val,col_name='фио'):
    try:
        csv_file = list(filter(lambda x:x[col_name] != val), csv_file)
    except Exception as e:
        return f'Строка с значением{val}поля {col_name} не найдена'
    return f'Строка с значением{val}поля {col_name} удалена'





#Сохранить
def save(file_name):
        with open(file_name,w,encoding='utf-8',newline='') as file:
            columns =[]
            writer=csv.DictWriter
            writer.writeheader()
            writer.writerows(csv_file)
            print('Файлы сохранены')

def shwo_rows():
        if len(csv_file) > 0:
            print('{:<5}{:<25}{:<8}{:<12}{:<15}'.format('ном','фио','возраст','телефон','отдел'))
            for el in csv_file:



                        })