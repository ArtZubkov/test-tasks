import sys

#Основная функция
def task1(n,m):  
    A = [] #Круговой массив
    
    f = False #Флаг для работы цикла while
    end_one = False #Отвечает за нахождение единицы в конце интервала
    
    S = [] #Путь
    
    i = 0
    while not f:
        i += 1
        
        #Заполняем круговой массив
        if i % n != 0:
            A.append(i % n)
        else:
            A.append(n)
            
        #Заполняем массив пути первой цифрой каждого интервала   
        if (i-1) % (m-1) == 0:
            if i == 1 or A[i-1] != 1:
                S.append(A[i-1])
            else:
                end_one = True #Когда интервал оканчивается на 1
                
        #Условие решения задачи  
        if len(A) % n == 1 and A[i-1] == 1 and end_one:
            f = True #Когда путь найден, задача выполнена
            break
        
    print(S)


#Обработка ввода аргументов
if len(sys.argv) != 3:
    print('Input correct number of arguments')
    sys.exit()
    
task1(int(sys.argv[1]), int(sys.argv[2])) #Запуск основной функции
