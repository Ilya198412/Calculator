
from logger import logger
import model, view, logger


def operation(list,i,oper):
    '''В данной функции принимается список, принимается индекс и оператор(+-*.)
    '''
    if list[i] == oper: # если наш элемент списка является оператором то выполняем действие. 
        list[i-1]= model.opSelect.get(oper)(int(list[i-1]), int(list[i+1])) # после выполнения вычисления наш результат встает на место [i-1]
        deleteElement(list,i) # передаем наш список и индекс в функцию deleteElement
        return True
    return False

def deleteElement(string, i): 
    ''' Функция для удаления элементов индекса с которыми уже выполнены математические действия'''
    string.pop(i) # удаляется число которое было справа от операнда
    string.pop(i) #  удаляется сам операнд

def  calculate(list: list):
    '''принимает список из def expression. пока длина нашего списка больше 1го индекса мы выполняем цикл. 1я проверка на наличие * 
    ИЛИ(or) /, если присутствует, то заходим в первый цикл '''
    while len(list)>1:
        if '*' in list or '/' in list:
            for i in range(len(list)):
                if operation(list, i, '*'): break # в функцию operatoion передается список, позиция и что нашел * или /  после отсекания элементов
                if operation(list, i, '/'): break #  в функции deleteElement делается break. если его не сделать, продолжится поиск и будет выход за границы списка
        elif '+' in list or '-' in list:
            for i in range(len(list)):
                if operation(list, i, '+'): break
                if operation(list, i, '-'): break
    
    return list
    
def sliceByParentheses(expression: list):
    open_par, close_par = None, None
    for index, item in enumerate(expression):
        if item == "(": open_par = index
        elif item == ")": close_par = index
        if open_par != None and close_par != None:
            expression1 = expression[:open_par]
            expression2 = calculate(expression[open_par+1:close_par])
            expression3 = expression[close_par+1:]
            expression = []
            expression.extend(expression1)
            expression.extend(expression2)
            expression.extend(expression3)
            break
    return expression


def solutionExpression(expression:str):
    ''' Принимает из модуля model функцию expression в формате str
        выполняет действия из выражения (+,-,/,*)'''
    
    logger.logger(f'Выражение для вычисления: {expression}')
    expression = model.stringToList(expression)
    while len(expression) > 1:
        if ('(' in expression) and (')' in expression):
            expression = sliceByParentheses(expression)
            
        else:
            expression = calculate(expression)
    model.result = expression[0]
    
    view.printResult()
    logger.logger(f'Результат вычисления : {model.result}\n')














# def input_integer(enter):
#     while True:
#         try:
#             a = int(input(enter))
#             return a
#         except:
#             view.error_value()



# def input_operation(enter):
#     while True:
#             a = input(enter)
#             if a in ['+', '-', '*', '/','=']:
#                 return a
#             else:
#                 view.error_value()
