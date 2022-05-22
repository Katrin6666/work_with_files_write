from pprint import pprint
import os
BASE_PATH = os.getcwd()
DIR_NAME = 'catalog'
catalog_path = os.path.join(BASE_PATH, DIR_NAME)
FILE_NAME = 'merge.txt'
full_path = os.path.join(BASE_PATH, FILE_NAME)

def number (url):
    with open(url, encoding='utf-8') as document:
        n = 0
        for line in document:
            n += 1
    return n

def func(full_path):
    with open(full_path, 'a', encoding='utf-8') as merge:
        catalog = os.listdir(catalog_path)
        dict = {}
        for file in catalog:
            file_path = os.path.join(BASE_PATH, DIR_NAME, file)
            list = []
            with open(file_path, encoding='utf-8') as document:
                list.append(file)
                content = document.read()
                list.append(content)
                dict[number(file_path)] = list
        # pprint(dict)
        tuple = sorted(dict.items())
        for doc in tuple:
            merge.write(f'{doc[1][0]} \n')
            merge.write(f'{doc[0]} \n')
            merge.write(f'{doc[1][1]} \n')
        pprint(tuple)

func(full_path)