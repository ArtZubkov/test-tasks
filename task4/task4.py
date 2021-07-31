import sys
import os.path

#Основная функция
def task4(filename):
    
    #Открываем и читаем файл
    with open(filename) as file:
        nums = file.read()
    
    if nums == '':
        print('Empty file')
        sys.exit()
        
    nums = nums.split('\n')
    #Формируем целочисленный список
    for i in range(len(nums)):
       nums[i] = int(nums[i])
   
    #Цикл для подсчета разности элементов и выявление минимальной
    for i in range(len(nums)):
        diff = 0 #Сумма разностей между данным элементом с каждым в списке (модуль)
        for j in range(len(nums)):
            diff += abs(nums[i]-nums[j]) #Берем по модулю
            
        if i == 0:
            mindiff = diff #Минимальная сумма разностей (модуль)
            
        #Если подсчитанная сумма разностей меньше минимальной   
        if diff < mindiff:
            mindiff = diff #Обновляем минимальную сумму разностей
                      
    print(mindiff)        

#Обработка ввода аргументов
if len(sys.argv) != 2:
    print('Input correct number of arguments')
else:
    exist_file = os.path.exists(sys.argv[1])
    if not exist_file:
        print('Incorrect argument')
    else:        
        task4(sys.argv[1]) #Запуск основной функции