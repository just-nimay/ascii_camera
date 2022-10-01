import cv2
import numpy as np


cap = cv2.VideoCapture(1) #определение камеры (по умолчанию "0")


#увеличте число пробелов, что бы сделать изображение более темным
ascii_grd = 'Ñ@#W$9876543210?!abc;:+=-,._               ' #символы, которые будут использоваться.

len_of_asii_grd = len(ascii_grd)
poeben = round(int(255 / len_of_asii_grd), None) + 1 #вычисляется количество цветов на один символ

while True:
    ret, frame = cap.read() #взятие кадра

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #преобразование кадра в черно-белый кадр
    invert = cv2.bitwise_not(gray) #инвертирование цветов

    ready = cv2.resize(invert, (68, 42)) #устанавливается ширина и высота кадра
  
    image = [] #список, в который будет помещены списки с символами
    for i in ready:
        arr_x = [] #список, в который помещаются символы
        for j in i:
            n = int(j / poeben) #получение id символа

            symb = ascii_grd[n] #получение символа по id
            
            arr_x.append(symb) #помещение символа в список

        image.append(arr_x) #помещение списка в список
    
    for row in image: #проходит по всем "строчкам" "изображения"
        string = ''.join(map(str, row)) #перевод списка с символами в строку с символами
        print(string) #вывод строки с символами в консоль

#что бы завершить процесс, нажмите сочитание клавиш cntr+c
cap.release()
cv2.destroyAllWindows()
