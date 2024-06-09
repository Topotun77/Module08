# Домашнее задание по теме "Создание исключений".
# Задание:
#
# Создайте новый проект или продолжите работу в текущем проекте.
# Создайте минимум два своих собственных исключения, наследуя их от класса
# Exception
# .
# Например, InvalidDataException и ProcessingException.
# Напишите функцию, которая генерирует различные исключения в зависимости от передаваемых ей аргументов.
# Добавьте обработку исключений в функции, вызывающие вашу функцию, и передайте исключения дальше по стеку вызовов.
# В основной части программы вызовите эти функции и корректно обработайте

class InvalidDataException(Exception):
    def __init__(self, message='Invalid data exception', add_info=None):
        self.message = message
        self.add_info = add_info

    def __str__(self):
        return (f'Все, что известно об этой ошибке:\n\tКласс: {self.__class__.__name__}'
                f'\n\tОписание ошибки: {self.message}\n\tДополнительная информация: {self.add_info}')


class InvalidTypeData(Exception):
    def __init__(self, message='Processing exceptionn', add_info=None):
        self.message = message
        self.add_info = add_info

    def __str__(self):
        str_ = self.__class__.__name__ + ', ' + self.message
        if isinstance(self.add_info, dict):
            list_ = list(map(lambda x, y: '\t' + str(x) + ' = ' + str(y) + '\n', self.add_info.keys(),
                             self.add_info.values()))
            str_ += f'\nЗначения параметров:\n' + ' '.join(list_)
        else:
            str_ += str(self.add_info)
        return str_


def f1(*param_):
    if len(param_) > 3:
        raise InvalidDataException(message='Передано слишком много параметров', add_info=list(param_))
    elif False in list(map(lambda x: isinstance(x, int), param_)):
        raise InvalidTypeData(message='Неверный тип данных, ожидался тип int.',
                              add_info=dict(str1='Введенные данные: ', str2=param_))
    else:
        return sum(param_)


def sum_list(list_):
    try:
        res = f1(*list_)
    except Exception:
        print(f'\033[31mОбидно, произошла ошибка, обработаю ее там, откуда меня вызвали.\033[0m')
        raise
    else:
        print(f'\033[93mУРА! Наконец-то мы смогли посчитать без ошибок!!!\033[0m f1{tuple(list_)} = {res}\n')
        return res
    finally:
        print('='*60)


list_ = [[1, 2, 3, 4], [1, '2', 3], 1, [1, 2, 3]]
for l in list_:
    try:
        sum_list(l)
    except InvalidDataException as exp_:
        print('Возникла ошибка введенных данных. Ниже будет описание ошибки:\n' + str(exp_), end='\n\n')
        print('Но мы разобьем ваш список на 2 списка, Если и это не поможет, то, извините, но вы все сломали:')
        sum_list([sum_list(l[0:3]), sum_list(l[3:])])
    except InvalidTypeData as exp_:
        print('Неправильный тип данных:\n' + str(exp_), end='\n\n')
    except Exception as exp_:
        print(f'Возникла какая-то другая ошибка!\n'
              f'Вот вам данные ошибки: {exp_.__class__}, {exp_.args}', end='\n\n')

