'''
Сформувати функцію, що буде обчислювати методом ітерації
факторіал заданого користувачем
натурального числа n.
Виконав : Канюка Р. 122В
'''
#Спецільна бібліотека для визначення кількості затраченої пам'яті.
import sys
from memory_profiler import memory_usage
from datetime import datetime
while True:
    #Ініціалізація n
    while True:
            try:
                n = int(input("Введіть n : "))  
                if(n >= 0):
                    break
                else : print("Факторіала відємного числа не існує.")
            except ValueError :
                print('Введіть число!')
    #Знаходження факторіалу
    sys.setrecursionlimit(10000)
    start = datetime.now()
    result = 1
    for i in range(1,n+1):
        result *= i
    print("Затрачений час :",datetime.now() - start)
    print("Кількість використаних МБ :",memory_usage())
    print("Результат =", result)
    quest = input('Завершити програму? Y/N : ')
    if(quest == 'Y' or quest == 'y'):
        break
'''
    Час розробки : 3хв.
    Простота алгоритму, дозволяє доволі легко реалізувати
    алгоритм методом ітерацій попри те, що читабельність майже не погіршується.
    Ітераційний метод факторіала ,швидше працює
    з великими значеннями факторіала ніж рекурсивний. 
    Проте для представлення алгоритму краще,
    використовувати ,інтуітивно зрозумілий, рекурсивний метод. 
'''
    
