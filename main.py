from collision.CorrectRect import isCorrectRect, RectCorrectError
from collision.CollisionRect import isCollisionRect
from collision.intersectionAreaRect import intersectionAreaRect
from collision.intersectionAreaMultiRect import intersectionAreaMultiRect
def main():
    while True:
        num = int(input("Выберите: 1. isCorrectRect, 2. isCollisionRect, 3. intersectionAreaRect, 4. intersectionAreaMultiRect, 5. Выход:"))
       
        if num == 1:
            rec = []
            x1 = float(input('Введите x1: '))
            y1 = float(input('Введите y1: '))
            x2 = float(input('Введите x2: '))
            y2 = float(input('Введите y2: '))
            rec.append([(x1,y1), (x2,y2)])
            try:
                print(isCorrectRect(rec))
            except RectCorrectError as e:
                print(e)
        
        elif num == 2:
            x1 = float(input('Введите x1: '))
            y1 = float(input('Введите y1: '))
            x2 = float(input('Введите x2: '))
            y2 = float(input('Введите y2: '))
            x3 = float(input('Введите x3: '))
            y3 = float(input('Введите y3: '))
            x4 = float(input('Введите x4: '))
            y4 = float(input('Введите y4: '))
            rectangles = [(x1, y1), (x2, y2)],[(x3, y3), (x4, y4)]
            print(f"Пересекаются ли прямоугольники: ", isCollisionRect(rectangles))
        
        elif num ==3:
            x1 = float(input('Введите x1: '))
            y1 = float(input('Введите y1: '))
            x2 = float(input('Введите x2: '))
            y2 = float(input('Введите y2: '))
            x3 = float(input('Введите x3: '))
            y3 = float(input('Введите y3: '))
            x4 = float(input('Введите x4: '))
            y4 = float(input('Введите y4: '))
            rectangles = [(x1, y1), (x2, y2) ],[(x3, y3), (x4, y4)]
            print(f"Площадь пересечения: ", intersectionAreaRect(rectangles))

        elif num == 4:
            n = int(input("Кол-во прямоугольников: "))
            rectangles = []
            for i in range(n):
                print(f"Прямоугольник {i + 1}:")
                x1 = float(input('Введите x1: '))
                y1 = float(input('Введите y1: '))
                x2 = float(input('Введите x2: '))
                y2 = float(input('Введите y2: '))
                rectangles.append([(x1, y1), (x2, y2)])
            else:  
                try:
                    print(f"Уникальная площадь пересечения: ", intersectionAreaMultiRect(rectangles))
                except RectCorrectError as e:
                    print(e)
                    return 0
        elif num == 5:
            print("Вы вышли из программы")
            break
        else:
            print("Некорректный пункт. Выберите другой")
main()