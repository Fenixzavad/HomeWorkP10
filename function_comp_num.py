def insert_numbers(): 
    print('Тип комплексного числа: a + bi\n')
    comp1 = input('Введем первое комплексное число: ')
    comp2 = input('Введем второе комплексное число: ')
    operation = input('Какое действие выберите? (+, -, *, / )')
    with open('results.txt', 'a') as data:
            data.write(f'({comp1}) {operation} ({comp2}) = ')
    return [comp1, comp2, operation]

def take_rational_part(user_number):
    rational_part = []
    for k in range(0, len(user_number)):
        if user_number[k] != ' ':
            rational_part.append(user_number[k])
        else:
            break
    rational_part = float(''.join(rational_part))
    return rational_part

def take_imaginary_part(user_number):   
    imaginary_part = []
    for i in range(0, len(user_number)):
        if user_number[i] == 'i':
            while user_number[i] != ' ':
                imaginary_part.insert(0,user_number[i - 1])
                i-= 1
    imaginary_part.pop(0)
    imaginary_part = float(''.join(imaginary_part))
    return imaginary_part

def take_symbol(user_number):
    symbol = []
    for l in range(0, len(user_number)):
        if user_number[l] == '-' and l !=0 or user_number[l] == '+' and l != 0:
            symbol.append(user_number[l])
    symbol = ''.join(symbol)
    return symbol

def addition(r1, s1, i1, r2, s2, i2):
    result = []
    result.append(r1+r2)
    if s1 == '+' and s2 == '+':
        result.append(i1+i2)
    elif s1 == '+' and s2 == '-':
        result.append(i1-i2)
    elif s1 == '-' and s2 == '+':
        result.append(i2-i1)
    else:
        result.append(-(i1+i2))
    return result

def deduction(r1, s1, i1, r2, s2, i2):
    result = []
    result.append(r1-r2)
    if s1 == '+' and s2 == '+':
        result.append(i1-i2)
    elif s1 == '+' and s2 == '-':
        result.append(i1+i2)
    elif s1 == '-' and s2 == '+':
        result.append(-i2-i1)
    else:
        result.append(i2-i1)
    return result

def mult(r1, s1, i1, r2, s2, i2):
    result = []
    result.append(r1*r2)
    if s1 == "+" and s2 == "+" or s1 == "-" and s2 == "-":
        result.append(-i1*i2)
    else:
        result.append(i1*i2)
    if s1 == "+":
        result.append(r2*i1)
    else:
        result.append(-r2*i1)
    if s2 == "+":
        result.append(r1*i2)
    else:
        result.append(-r1*i2)
    result[0] = result[0] + result[1]
    result[1] = result[2] + result[3]
    result.pop(3)
    result.pop(2)
    return result    
    
def division(r1, s1, i1, r2, s2, i2):
    numerator = []
    denominator = []
    result = []
    numerator.append(r1*r2)
    if s1 == "+" and s2 == "+" or s1 == "-" and s2 == "-":
        numerator.append(i1*i2)
    else:
        numerator.append(-i1*i2)
    if s1 == "-":
        numerator.append(-r2*i1)
    else:
        numerator.append(r2*i1)
    if s2 == "+":
        numerator.append(-r1*i2)
    else:
        numerator.append(r1*i2)
    numerator[0] = numerator[0] + numerator[1]
    numerator[1] = numerator[2] + numerator[3]
    numerator.pop(3)
    numerator.pop(2)
    denominator.append(r2**2+i2**2)
    result.append(numerator[0]/denominator[0])
    result.append(numerator[1]/denominator[0])
    return result

def rec_in_file(result):
    with open('results.txt\n', 'a\n') as data:
        if result[1] != 0:
            for i in range(0, 2):
                if result[i] > 0 and i == 1:
                    data.write('+ ')
                elif result[i] < 0 and i == 1:
                    result[i] = -result[i]
                    result[i] = str(result[i])
                    data.write('- ')
                    data.write(result[i])
                else:
                    result[i] = str(result[i])
                    data.write(result[i])
                if i != 1:
                    data.write(' ')
            data.write('i\n')
        else:
            result[0] = str(result[0])
            data.write(f'{result[0]}\n')
            
def repeat_or_no():
    user_choice = 'Неудовлетворительный ответ'
    while user_choice != 'Y' or user_choice != 'N':
        user_choice = input('Будете работать с каркулятором комплексных чисел? (Y or N)')
        if user_choice == 'N':
            return False
        elif user_choice == 'Y':
            return True
        else:
            print('Неверный ответ, будете пользоваться каркулятором комплексных чисел? (Y or N)' )