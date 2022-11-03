import model

def division_be_zero():
    ''' Функция для отработки ошибки деления на 0'''
    print("Деление на ноль!")
    exit()

def printResult():
    '''Функция вывода решения выражение = результат'''
    print(f'{model.string} = {model.result}')