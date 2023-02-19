from datetime import datetime as dt
from time import time


def result_logger(data, result):
    x, oper, y = data
    data_str = f'{str(x)} {oper} {str(y)}'
    time = dt.now().strftime('%H:%M')
    with open('results.txt', 'a') as file:
        file.write('{}; операция : {} результат :{}\n'.format(time, data_str, result))