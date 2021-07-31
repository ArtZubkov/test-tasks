import json
import sys
import os.path

#Основная функция
def task3(f1,f2):
    #Читаем первый файл
    with open(f1) as f1:
        voc1 = f1.read()
        voc1 = json.loads(voc1) #Словарь из 1 файла
    #Читаем второй файл    
    with open(f2) as f2:
        voc2 = f2.read()
        voc2 = json.loads(voc2) #Словарь из 2 файла
      
    #Функция, заполняющая значения элемента с ключом 'value'
    def fill(class_list):   
        
        there_are_values = False #Флаг отвечающий за наличие ключа 'values'
        
        #Пробегаем по ключам в 2-х файлах и сравниваем 'id'
        for item1 in class_list:         
                value_id = item1['id']
                  
                for item2 in voc2['values']:
                    v = item2['id']
                    m = item2['value']
                                 
                    if v == value_id: #Если значения 'id' совпадают
                        item1['value'] = m #Вписываем значение 'value'
                        
                there_are_values = 'values' in item1.keys() 
                
                #Рекурсия функции, пока не заполнятся все содержимое 'values'
                if there_are_values:
                    fill(item1['values'])                   
    
    fill(voc1['tests']) #Запуск функции заполнения
    
    #Запись в файл результата
    with open('report.json', 'w') as file:
        json.dump(voc1, file, indent = 3) #Собираем в файл заполненный 1 словарь 
        

        
#Обработка ввода аргументов
if len(sys.argv) != 3:
    print('Input correct number of arguments')
else:
    exist_file1 = os.path.exists(sys.argv[1])
    exist_file2 = os.path.exists(sys.argv[2])
    if not exist_file1 or not exist_file2:
        print('Incorrect arguments')
    else:
        task3(sys.argv[1], sys.argv[2]) #Запуск основной функции

#task3('tests.json','values.json')