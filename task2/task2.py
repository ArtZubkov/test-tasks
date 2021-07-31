import sys
import os.path

#Основная функция
def circle_points(f1,f2):
    #Открываем и читаем 1 файл
    with open(f1) as f1:
        line = f1.readline() #Координаты центра
        r = f1.readline() #Радиус окружности
        
    zerocoord = line.split(' ')
       
    x = zerocoord[0] #Координата x центра
    y = zerocoord[1] #Координата y центра

    if x == '' or y == '' or y == '\n' or r == '':
        print('Incorrect data in the file1')
        sys.exit()
        
    x = float(x)
    y = float(y)
    r = float(r)
    
    if r <= 0:
        print('Incorrect radius')
        sys.exit()
        
    #Работаем со 2 файлом, где находятся координаты точек
    with open(f2) as f2:
        i = 0 
        for point in f2:  
            i += 1 #Количество проходов цикла
            
            if i == 100:
                print('There should be no more than 100 points')
                break
            
            coord = point.split(' ') #Массив для координат точки
            
            if i != 1 and coord[0] == '\n':
                break
           
            if i == 1 and len(coord) != 2:
                print('Incorrect point coordinates in the file2')
                sys.exit()
                
            xp = coord[0] #Координата x точки
            yp = coord[1] #Координата y точки
            
            if xp == '' or yp == '' or yp == '\n':
                print('Incorrect data in the file2')
                sys.exit()
                
            xp = float(xp) 
            yp = float(yp) 
            
            #Точка лежит на окружности
            if xp*xp + yp*yp == r*r:
                print(0)
            #Точка лежит внутри окружности    
            if xp*xp + yp*yp < r*r:
                print(1)
            #Точка лежит вне окружности        
            if xp*xp + yp*yp > r*r:
                print(2) 
                      

#Обработка ввода аргументов
if len(sys.argv) != 3:
    print('Input correct number of arguments')
else:
    exist_file1 = os.path.exists(sys.argv[1])
    exist_file2 = os.path.exists(sys.argv[2])
    if not exist_file1 or not exist_file2:
        print('Incorrect arguments')
    else:
        circle_points(sys.argv[1], sys.argv[2]) #Запуск основной функции



