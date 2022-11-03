import datetime

import string

import model


path = 'log.txt'
string = model.string

def logger(info:str):
    '''Функция для логирования записи в файл. удалось отвельно записать 
       выражение и отдельно записать ответ в след строку. функция проставляет дату и время [:-7] -> отсекает лишнее 
       из записи времени и даты'''
    model.string
    datetime.datetime.now()
    string = str(datetime.datetime.now())[:-7] + ' ' +  info

    with open (path,'a', encoding='UTF-8') as data:
        data.write(f'{string}\n')
