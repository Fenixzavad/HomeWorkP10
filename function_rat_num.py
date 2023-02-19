import function_rat_num as fr 
import sys

def x():
    global first_num
    first_num = float(input('Введите первое число: ').replace(',', '.'))
    return first_num

def y():
    global second_num
    second_num = float(input('Введите второе число: ').replace(',', '.'))
    return second_num


def select_operation():
    global operation
    operation = (input(f'Выбирите действие: +, -, *, /: '))
    if operation == '+' or '-' or '/' or '*':
        return operation
    else:
        print('Неправильный ввод')


def res(first_num, second_num):
        if  operation == '+':
            res = first_num + second_num
            result = round(res, 3)
            return result
        elif operation == '-':
            res = first_num - second_num
            result = round(res, 3)
            return result
        elif operation == '*':
            res = first_num * second_num
            result = round(res, 3)
            return result
        elif operation == '/':
            res = first_num / second_num
            result = round(res, 3)
            return result
        else:
            print('Неправильный ввод')

def main_terminal():
    global file
    x = fr.x()
    while True:
        y = fr.y()
        oper = fr.select_operation()
        res = fr.res(x, y)
        file = 'results.txt'
        with open('results.txt', 'a') as data:
            data.write(f'Результат {x} {oper} {y} = {res}\n')
        print(f'Результат действия {x} {oper} {y} = {res}\n(Сделаем запись в фай с результатами)' )
        again = input('Использовать калькулятор еще раз? Yes/No: ').lower()
        if again == 'yes':
            useresult = input('ВЫ хотите использовать последнее дейстиве? (Yes/No): ').lower()
            if useresult == 'yes':
                x = res
                continue
            elif useresult == 'no':
                break
            else:
                sys.exit()           
        else:  
                sys.exit()        
