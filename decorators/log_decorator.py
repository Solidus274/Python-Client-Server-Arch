import os
import sys
from datetime import datetime
sys.path.append('../')

# Подготовка имени файла для логирования
PATH = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(PATH, 'decorator.txt')

enable_tracing = True
if enable_tracing:
    debug_log = open(PATH, "w", encoding='UTF-8')


def log(func):
    if enable_tracing:
        def call_func(*args, **kwargs):
            res = func(*args, **kwargs)
            debug_log.write(f'{datetime.now()} ')
            debug_log.write('Функция: {} Аргументы: {} '.format(func.__name__, args))
            debug_log.write('Вызвана функцией: {}\n'.format(sys._getframe(1).f_code.co_name))
            return res

        return call_func
    else:
        return func
