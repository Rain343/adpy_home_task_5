import datetime
import os
import requests


FILENAME = 'logs.txt'
ENCODING = 'UTF-8'


def logger(folder=None):
    def logger_(func):    

        def call_func(*args, **kwargs):
            if folder:
                path = os.path.join(os.getcwd(), folder)
                if not os.path.exists(path):
                    os.makedirs(path)
                logs_path = os.path.join(path, FILENAME)
            else:
                logs_path = os.path.join(os.getcwd(), FILENAME)

            with open(logs_path, 'a', encoding=ENCODING) as f:
                call_date = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
                call_func_name = func.__name__
                call_args = f'{args}, {kwargs}'
                result = func(*args, **kwargs)
                f.write(f'Дата: {call_date}, Имя функции: {call_func_name}, Аргументы: {call_args}, Результат: {result}\n')

            return result

        return call_func
    return logger_


class Superheroes():
    def __init__(self):
        self.url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
        self.res = requests.get(self.url).json()

    @logger(folder='123')
    def get_intelligence(self, list_superheroes):
        superheroes = []
        for superhero in self.res:            
            if superhero['name'] in list_superheroes:
                superheroes.append(superhero)
                continue
        best_intelligence = max(superheroes, key=lambda x: x['powerstats']['intelligence'])
        return f'Самый умный супергерой - {best_intelligence["name"]}'


if __name__ == '__main__':

    list_superheroes = ['Hulk', 'Captain America', 'Thanos']
    superheroes = Superheroes()

    print(superheroes.get_intelligence(list_superheroes))