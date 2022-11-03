import view


string: str = ''  # выражение подтягивается из модуля main (там происходит ввод с консоли)
result: int = 0

opSelect = { 
    '*': lambda x, y: int (x) * int (y), # в эту лямбда функцию передаются значения из def operation 
    '/': lambda x, y: int ((x) / int (y)) if int (y) !=0 else view.division_be_zero(), 
    '+': lambda x, y: int (x) + int (y),
    '-': lambda x, y: int (x) - int (y)} # словарик в котором ключами являются операнды(+-*,)


def stringToList (string: str):
    '''Принимает выражение с консоли для обработки, для начала удаляет все лишние символы из выражения(пробелы) 
       далее просталяет по 1 пробелу между символами'''
    string=string.replace(' ', '').strip() # replace - удаляет все пробелы в выражении введенного с консоли strip - отсекает все пробелы по краям выражения
    string = string.replace('+', ' + ')\
                    .replace('-', ' - ')\
                    .replace('*', ' * ')\
                    .replace('/', ' / ').replace('(', ' ( ').replace(')', ' ) ') # ограждаем каждый знак пробелами, для читабельности и верности работы алгоритма
    list = string.split()
    

    return list


