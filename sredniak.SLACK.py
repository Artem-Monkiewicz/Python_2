#%%
    
import urllib.request
import ssl
import json
import argparse

def get_from_url(url):
    context = ssl._create_unverified_context()
    req = urllib.request.Request(url=url, method='GET')
    with urllib.request.urlopen(req, context=context) as f:
        if f.status == 200:
            content = f.read().decode()
        else:
            return False
    return content

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Program do przeliczania walut.")
    parser.add_argument('--value', '-v', dest='value', help='Wartość w PLN', type=float, required=True)
    parser.add_argument('--code', '-c', dest='code', help='Kod waluty', type=str, required=True)
    args = parser.parse_args()

    json_data = json.loads(get_from_url(f'https://api.nbp.pl/api/exchangerates/rates/a/{args.code}?format=json'))
    rate = float(json_data['rates'][0]['mid'])
    print(f'{args.value}[PLN] = {args.value / rate}[{args.code}] po kursie {rate}')

#%%
    
import re


pattern = r"[A-Za-z0-9\.]+@[A-Za-z0-9][A-Za-z0-9\.]*[A-Za-z0-9]\.[a-z]{2,3}"
text = '''shjk@alskjd.pl,aoi@wksda.com,qawsjk.ssd@io.pl, skajh@kj@kjh.pl,@hui.pl,dnjewdk.neje@wejn,wejk!(@jio.pl,joijopoio@..pl'''

result = re.search(pattern, text)
if result != None:
    print(f'Found: {result}')
    print(f'result: {result.group(0)}')
else:
    print('Not found')

#%%

import re


pattern = r"^[A-Za-z0-9\.]+@[A-Za-z0-9][A-Za-z0-9\.]*[A-Za-z0-9]\.[a-z]{2,3}$"
text = '''shjk@alskjd.pl
aoi@wksda.com
qawsjk.ssd@io.pl
skajh@kj@kjh.pl,@hui.pl
dnjewdk.neje@wejn
wejk!(@jio.pl,joijopoio@..pl'''

result = re.search(pattern, text, re.MULTILINE)
if result != None:
    print(f'Found: {result}')
    print(f'result: {result.group(0)}')
else:
    print('Not found')

#%%
    
content = codecs.decode(content, encoding='utf-8', errors='ignore')

#%%

import urllib.request
import ssl
import json
import argparse
import codecs
import re

def get_from_url(url):
    context = ssl._create_unverified_context()
    req = urllib.request.Request(url=url, method='GET')
    with urllib.request.urlopen(req) as f:
        if f.status == 200:
            content = f.read()
            content = codecs.decode(content, encoding='utf-8', errors='ignore')
        else:
            return False
    return content

if __name__ == '__main__':
    content = str(get_from_url("https://www.gazeta.pl/"))
    content = content.replace('\r','')
    content = content.replace('\n', '')
    pattern1 = r'<div class=\"timeline__title\">Najnowsze</div><div class="timeline__list">    <div class="timeline__box">(.*)</div>\s+</div>'
    result1 = re.search(pattern1, content)
    links = result1.group(1)

#%%
    
import urllib.request
import ssl
import json
import argparse
import codecs
import re

def get_from_url(url):
    context = ssl._create_unverified_context()
    req = urllib.request.Request(url=url, method='GET')
    with urllib.request.urlopen(req) as f:
        if f.status == 200:
            content = f.read()
            content = codecs.decode(content, encoding='utf-8', errors='ignore')
        else:
            return False
    return content

if __name__ == '__main__':
    content = str(get_from_url("https://www.gazeta.pl/"))
    content = content.replace('\r','')
    content = content.replace('\n', '')
    pattern1 = r'<div class=\"timeline__title\">Najnowsze</div><div class="timeline__list">    <div class="timeline__box">(.*)</div>\s+</div>'
    result1 = re.search(pattern1, content)
    links = result1.group(1)
    print(links)
    pattern2 = r'<a class=\"timeline__link\" title=\"([^\"]+)\" id=\"LinkArea:BoxOpLink\" href=\"([^\"]+)\">'
    result2 = re.findall(pattern2, links)
    for item in result2:
        print(item[0], item[1])

#%%
        
pattern1 = r'<div class=\"timeline__title\">Najnowsze</div><div class="timeline__list">\s+<div class="timeline__box">(.*)</div>\s+</div>'

#%%

import urllib.request
import ssl
import json
import argparse
import codecs
import re

def get_from_url(url):
    context = ssl._create_unverified_context()
    req = urllib.request.Request(url=url, method='GET')
    with urllib.request.urlopen(req, context=context) as f:
        if f.status == 200:
            content = f.read()
            content = codecs.decode(content, encoding='utf-8', errors='ignore')
        else:
            return False
    return content

if __name__ == '__main__':
    content = get_from_url("https://www.gazeta.pl/").replace('\r', '').replace('\n', '')

    news_block_pattern = r'<div class=\"timeline__title\">Najnowsze</div><div class="timeline__list">\s+<div class="timeline__box">(.*)</div>\s+</div>'
    news_block = re.search(news_block_pattern, content)

    links = news_block.group(1)
    n

#%%
        
def print_menu(menu: dict):
    print('===========================')
    for option in menu.values():
        print(option)
    while True:
        result = input('Podaj opcje:')
        for key in menu.keys():
            if result == str(key):
                print(f'Wybrałeś opcję {key}')
                print('===========================')
                return key
        else:
            print('Podales zla wartosc!')

#%%
            
import urllib.request
import ssl
import json
import argparse
import codecs
import re

def print_menu(menu: dict):
    print('===========================')
    for option in menu.values():
        print(option)
    while True:
        result = input('Podaj opcje:')
        for key in menu.keys():
            if result == str(key):
                print(f'Wybrałeś opcję {key}')
                print('===========================')
                return key
        else:
            print('Podales zla wartosc!')

def get_from_url(url):
    context = ssl._create_unverified_context()
    req = urllib.request.Request(url=url, method='GET')
    with urllib.request.urlopen(req, context=context) as f:
        if f.status == 200:
            content = f.read()
            content = codecs.decode(content, encoding='utf-8', errors='ignore')
        else:
            return False
    return content

if __name__ == '__main__':
    content = get_from_url("https://www.gazeta.pl/").replace('\r', '').replace('\n', '')
    news_block_pattern = r'<div class=\"timeline__title\">Najnowsze</div><div class="timeline__list">\s+<div class="timeline__box">(.*)</div>\s+</div>'
    news_block = re.search(news_block_pattern, content)
    links = news_block.group(1)
    news_pattern = r'<a class=\"timeline__link\" title=\"([^\"]+)\" id=\"LinkArea:BoxOpLink\" href=\"([^\"]+\.html)[^\"]+\">\s+<div class="timeline__linkTime">(\d{1,2}:\d{1,2})</div>'
    news = re.findall(news_pattern, links)

    menu = {}
    index = 1
    MAX_ITEMS = 5
    for item in news:
        menu[index] = f'{index}. {item[2]}-{item[0]}'
        index += 1
        if index > MAX_ITEMS:
            menu[index] = f'{index}. Wyjdź'
            break

    while True:
        option = print_menu(menu)
        if option == MAX_ITEMS + 1:
            break
    
#%%
import urllib.request
import ssl
import json
import argparse
import codecs
import re
import os

def print_menu(menu: dict):
    print('===========================')
    for option in menu.values():
        print(option)
    while True:
        result = input('Podaj opcje:')
        for key in menu.keys():
            if result == str(key):
                os.system('cls')
                print(f'Wybrałeś opcję {menu[key]}')
                print('===========================')
                return key
        else:
            print('Podales zla wartosc!')

def get_from_url(url):
    context = ssl._create_unverified_context()
    req = urllib.request.Request(url=url, method='GET')
    with urllib.request.urlopen(req, context=context) as f:
        if f.status == 200:
            content = f.read()
            content = codecs.decode(content, encoding='utf-8', errors='ignore')
        else:
            return False
    return content

if __name__ == '__main__':
    content = get_from_url("https://www.gazeta.pl/").replace('\r', '').replace('\n', '')
    news_block_pattern = r'<div class=\"timeline__title\">Najnowsze</div><div class="timeline__list">\s+<div class="timeline__box">(.*)</div>\s+</div>'
    news_block = re.search(news_block_pattern, content)
    links = news_block.group(1)
    news_pattern = r'<a class=\"timeline__link\" title=\"([^\"]+)\" id=\"LinkArea:BoxOpLink\" href=\"([^\"]+\.html)[^\"]+\">\s+<div class="timeline__linkTime">(\d{1,2}:\d{1,2})</div>'
    news = re.findall(news_pattern, links)

    menu = {}
    index = 1
    MAX_ITEMS = 5
    for item in news:
        menu[index] = f'{index}. {item[2]}-{item[0]}'
        index += 1
        if index > MAX_ITEMS:
            menu[index] = f'{index}. Wyjdź'
            break

    while True:
        option = print_menu(menu)
        if option == MAX_ITEMS + 1:
            break
        news_content = get_from_url(news[option][1])
        news_desc_pattern = r'<meta name="Description" content="([^\"]+)"/>'
        news_desc = re.search(news_desc_pattern, news_content)
        print(news_desc.group(1))


#%%
        
import threading
import multiprocessing
my_VAR = 'MK'

class MyThread(threading.Thread):
    def __init__(self, target, args=(), kwargs=None):
        if kwargs == None:
            kwargs = {}
        self.target = target
        self.args = args
        self.kwargs = kwargs
        super().__init__()

    def run(self):
        self.result = self.target(*self.args, **self.kwargs)

    def join(self, timeout=None):
        super().join(timeout)
        return self.result


def print_it(iter, code):
    count = 0
    for item in iter:
        print(f'{my_VAR}{code}{item}{code}')

        count += item

    return count


t1 = MyThread(target=print_it, args=(range(0, 1000), 'A'))
t2 = MyThread(target=print_it, args=(range(2000, 3000), 'B'))

t1.start()
t2.start()
print('START')
print_it(range(4000, 5000), 'C')

print(f't1 {t1.join()}')
print(f't2 {t2.join()}')

#%%

import multiprocessing

def print_it(iter, code, queue):

    count = 0
    for item in iter:
        count +=1
        print(f'{code}{count}{code}')
        count += item
        queue.put(item)

if __name__ == '__main__':
    q1 = multiprocessing.Queue()

    p1 = multiprocessing.Process(target=print_it, args=(range(0, 10), 'A', q1))
    #p2 = multiprocessing.Process(target=print_it, args=(range(2000, 3000), 'B', val2))

    p1.start()
    #p2.start()

    p1.join()
    #p2.join()
    while True:
        try:
            print(f'element z kolejki {q1.get_nowait()}')
        except:
            print('Koniec kolejki')
            break

#%%
        
# 27 = esc
# 299 lewo
# 301 prawo
# 296 gora
# 304 dol
# pip install py-getch
from multiprocessing.dummy import Process, Value
import os
import getch
import time
wait = lambda:time.sleep(0.5)
clear_console = lambda: os.system('cls')
class get_key:
    key = Value('d', 0)
    key2 = Value('d', 0)
    p = None
    def __init__(self):
        self.p = Process(target=self.GetKeyThread, args=(self.key,))
        self.p.start()
    def GetKeyThread(self, key):
        while True:
            key.value = ord(getch.getch())
            if key.value == 224:
                key.value = key.value + ord(getch.getch())
            if key.value == 27:
                break
    def __call__(self):
        value = self.key.value
        self.key.value = 0
        return value
    

    #%%

import multiprocessing
import time
import random
import getkey

def waiter(q1, q2):
    while True:
        item = q1.get()
        time.sleep(random.randint(0, 2))
        print(f'Waiter {item}')
        q2.put(item)

def cook(q2, q3):
    while True:
        item = q2.get()
        time.sleep(random.randint(0, 6))
        print(f'Cook {item}')
        q3.put(item)


if __name__ == '__main__':
    q1 = multiprocessing.Queue()
    q2 = multiprocessing.Queue()
    q3 = multiprocessing.Queue()

    p_waiter = multiprocessing.Process(target=waiter, args=(q1, q2))
    p_cook = multiprocessing.Process(target=cook, args=(q2, q3))



    p_waiter.start()
    p_cook.start()
    gk = getkey.get_key()
    index = 0
    while True:
        key = gk()
        print(f'key: {key}')
        if key == 27:
            break
        q1.put(index)
        time.sleep(random.randint(0, 3))
        index +=1
        try:
            item = q3.get_nowait()
            print(f'client eat: {item}')
        except:
            pass

    p_cook.kill()
    p_waiter.kill()

#%%

import timeit
import random

def quick_sort(my_list):
#O(n * log(n))
    if len(my_list) <= 1:
        return my_list
    pivot = my_list[0]
    lo = []
    hi = []
    eq = []
    for item in my_list:
        if item < pivot:
            lo.append(item)
        elif item > pivot:
            hi.append(item)
        else:
            eq.append(item)
    return quick_sort(lo) + eq + quick_sort(hi)

def bubble_sort(my_list):
#O(n^2)
    changed = True
    while changed: #for index in range(len(my_list)-1):
        changed = False
        for index in range(len(my_list)-1):
            if my_list[index] > my_list[index + 1]:
                my_list[index], my_list[index + 1] = my_list[index + 1], my_list[index]
                changed = True
    return my_list



if __name__ == '__main__':
    my_list = [random.randint(0,1000) for i in range(0,100)]

    setup = '''from __main__ import bubble_sort, quick_sort
import random
my_list = [random.randint(0,1000) for i in range(0,10000)]
    '''
    bubble_str = "bubble_sort(my_list)"
    quick_str = "quick_sort(my_list)"

    bubble_time = timeit.timeit(stmt=bubble_str, setup=setup, number=100)
    quick_time = timeit.timeit(stmt=quick_str, setup=setup, number=100)
    print(bubble_time)
    print(quick_time)

#%%
    
# 27 = esc
# 299 lewo
# 301 prawo
# 296 gora
# 304 dol
# pip install py-getch
from multiprocessing.dummy import Process, Value
import os
import getch
import time
wait = lambda:time.sleep(0.5)
clear_console = lambda: os.system('cls')
class get_key:
    key = Value('d', 0)
    key2 = Value('d', 0)
    p = None
    def __init__(self):
        self.p = Process(target=self.GetKeyThread, args=(self.key,))
        self.p.start()
    def GetKeyThread(self, key):
        while True:
            key.value = ord(getch.getch())
            if key.value == 224:
                key.value = key.value + ord(getch.getch())
            if key.value == 27:
                break
    def __call__(self):
        value = self.key.value
        self.key.value = 0
        return value
    
#%%
    
# 27 = esc
# 299 lewo
# 301 prawo
# 296 gora
# 304 dol
# pip install py-getch

from multiprocessing.dummy import Process, Value
import os
import getch
import time

wait = lambda:time.sleep(0.5)

clear_console = lambda: os.system('cls')

class GetKey:
    key = Value('d', 0)
    key2 = Value('d', 0)
    p = None
    def __init__(self):
        self.p = Process(target=self.GetKeyThread, args=(self.key,))
        self.p.start()
    def GetKeyThread(self, key):
        while True:
            key.value = ord(getch.getch())
            if key.value == 224:
                key.value = key.value + ord(getch.getch())
            if key.value == 27:
                break
    def __call__(self):
        value = self.key.value
        self.key.value = 0
        return value
    

#%%
    
from getkey import GetKey, clear_console, wait







if __name__=='__main__':
    my_get_key = GetKey()


    while True:

        key = my_get_key()
        if key != 0:
            print(key)
        if key == 27:
            break

#%%

from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int
    char: str

#%%
    
class Map:
    def __init__(self, size_x, size_y, empty_char=' '):
        self.__size_x = size_x
        self.__size_y = size_y
        self.__empty_char = empty_char
        #self.map = [[self.__empty_char] * self.__size_x] * self.__size_y
        self.__map = []
        for y in range(self.__size_y):
            self.__map.append([])
            for x in range(self.__size_x):
                self.__map[y].append(self.__empty_char)

    def clean(self):
        for y in range(self.__size_y):
            for x in range(self.__size_x):
                self.__map[y][x] = self.__empty_char

    def print(self):
        for y in range(self.__size_y):
            for x in range(self.__size_x):
                print(self.__map[y][x], end='')
            print()

    def set_point(self, point):
        self.__map[point.y][point.x] = point.char

#%%
        
from getkey import GetKey, clear_console, wait
from point import Point
from apple import Apple
from map import Map

SIZE_X = 10
SIZE_Y = 10

if __name__ == '__main__':
    my_get_key = GetKey()
    my_apple = Apple(SIZE_X - 1, SIZE_Y - 1)
    my_map = Map(SIZE_X, SIZE_Y, '*')

    print(my_apple)

    my_map.clean()
    my_map.set_point(my_apple)
    my_map.print()


    while True:

        key = my_get_key()
        if key != 0:
            print(key)
        if key == 27:
            break

#%%
        
from getkey import GetKey, clear_console, wait
from point import Point
from apple import Apple
from map import Map

SIZE_X = 10
SIZE_Y = 10

if __name__ == '__main__':
    my_get_key = GetKey()
    my_apple = Apple(SIZE_X - 1, SIZE_Y - 1)
    my_map = Map(SIZE_X, SIZE_Y, '*')
    my_score = 0

    while True:
        # clear screen and map
        clear_console()
        my_map.clear()

        #get_key
        key = my_get_key()

        # action
        if key != 0:
            print(key)
        if key == 27:
            break

        #put all to map
        my_map.set_point(my_apple)

        # print map
        my_map.print()
        # wait
        wait(0.5)

#%%
        
class Map:
    def __init__(self, size_x, size_y, empty_char=' '):
        self.__size_x = size_x
        self.__size_y = size_y
        self.__empty_char = empty_char
        #self.map = [[self.__empty_char] * self.__size_x] * self.__size_y
        self.__map = []
        for y in range(self.__size_y):
            self.__map.append([])
            for x in range(self.__size_x):
                self.__map[y].append(self.__empty_char)

    def clear(self):
        for y in range(self.__size_y):
            for x in range(self.__size_x):
                self.__map[y][x] = self.__empty_char

    def print(self):
        for y in range(self.__size_y):
            for x in range(self.__size_x):
                print(self.__map[y][x], end='')
            print()

    def set_point(self, point):
        self.__map[point.y][point.x] = point.char

#%%
        
from point import Point
import random


class Apple(Point):
    def __init__(self, max_x, max_y):
        super().__init__(0, 0, 'A')
        self.__max_x = max_x
        self.__max_y = max_y
        self.x = random.randint(0, self.__max_x)
        self.y = random.randint(0, self.__max_y)

    def set_new_place(self):
        self.x = random.randint(0, self.__max_x)
        self.y = random.randint(0, self.__max_y)

#%%
        
from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int
    char: str

#%%
    

# 27 = esc
# 299 lewo
# 301 prawo
# 296 gora
# 304 dol
# pip install py-getch

from multiprocessing.dummy import Process, Value
import os
import getch
import time

wait = lambda x:time.sleep(x)

clear_console = lambda: os.system('cls')

class GetKey:
    key = Value('d', 0)
    key2 = Value('d', 0)
    p = None
    def __init__(self):
        self.p = Process(target=self.GetKeyThread, args=(self.key,))
        self.p.start()
    def GetKeyThread(self, key):
        while True:
            key.value = ord(getch.getch())
            if key.value == 224:
                key.value = key.value + ord(getch.getch())
            if key.value == 27:
                break
    def __call__(self):
        value = self.key.value
        self.key.value = 0
        return value
    
    #%%

from point import Point


class Snake:
    def __init__(self, max_x, max_y, start_x, start_y):
        self.__max_x = max_x
        self.__max_y = max_y
        self.body = [Point(start_x, start_y, '@'), Point(start_x, start_y, 'x'), Point(start_x, start_y, 'x')]
        self.direction = Point(1, 0, '')
        self.speed = 0.5

    def move(self):
        # move tail
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y

        # move head
        self.body[0].x += self.direction.x
        self.body[0].y += self.direction.y

        # check map ranges

#%% 1 getkey
        
# 27 = esc
# 299 lewo
# 301 prawo
# 296 gora
# 304 dol
# pip install py-getch

from multiprocessing.dummy import Process, Value
import os
import getch
import time

wait = lambda x:time.sleep(x)

clear_console = lambda: os.system('cls')

class GetKey:
    key = Value('d', 0)
    key2 = Value('d', 0)
    p = None
    def __init__(self):
        self.p = Process(target=self.GetKeyThread, args=(self.key,))
        self.p.start()
    def GetKeyThread(self, key):
        while True:
            key.value = ord(getch.getch())
            if key.value == 224:
                key.value = key.value + ord(getch.getch())
            if key.value == 27:
                break
    def __call__(self):
        value = self.key.value
        self.key.value = 0
        return value
    
#%% 2 main
    from getkey import GetKey, clear_console, wait
from point import Point
from apple import Apple
from map import Map
from snake import Snake

SIZE_X = 10
SIZE_Y = 10

if __name__ == '__main__':
    my_get_key = GetKey()
    my_apple = Apple(SIZE_X - 1, SIZE_Y - 1)
    my_map = Map(SIZE_X, SIZE_Y, ' ')
    my_snake = Snake(SIZE_X - 1, SIZE_Y - 1, 5, 5)
    my_score = 0
    game_over = False
    while True:
        # clear screen and map
        clear_console()
        my_map.clear()

        # get_key
        key = my_get_key()

        # action
        # 27 = esc
        # 299 lewo
        # 301 prawo
        # 296 gora
        # 304 dol

        # sprawdz ktory klawisz i czy NIE idzie w przeciwnym kierunku
        if key == 299 and not(my_snake.direction.x == 1 and my_snake.direction.y == 0):
            my_snake.direction.x = -1
            my_snake.direction.y = 0
        if key == 301 and not(my_snake.direction.x == -1 and my_snake.direction.y == 0):
            my_snake.direction.x = 1
            my_snake.direction.y = 0
        if key == 296 and not(my_snake.direction.x == 0 and my_snake.direction.y == 1):
            my_snake.direction.x = 0
            my_snake.direction.y = -1
        if key == 304 and not(my_snake.direction.x == 0 and my_snake.direction.y == -1):
            my_snake.direction.x = 0
            my_snake.direction.y = 1
        if key == 27:
            break

        my_snake.move()

        # sprawdz czy game_over
        game_over = my_snake.is_dead()
        if game_over:
            break

    # jezeli @==a to dodaj body do snake i ustaw nowe miejsce jabłka i dodaj punkt
        if my_apple.x == my_snake.body[0].x and my_apple.y == my_snake.body[0].y:
            my_snake.add_body()
            my_apple.set_new_place(my_snake.body)
            my_score += 1
            if my_snake.delay > 0.1:
                my_snake.delay -= 0.02


        # put all to map
        my_map.set_point(my_apple)

        for i in range(len(my_snake.body) - 1, -1, -1):
            my_map.set_point(my_snake.body[i])

        # print map
        my_map.print()
        print(f"SCORE: {my_score}")
        # wait
        wait(my_snake.delay)
    if game_over:
        clear_console()
        print(f"GAME OVER!!! YOUR SCORE {my_score}")

#%% 3 map

class Map:
    def __init__(self, size_x, size_y, empty_char=' '):
        self.__size_x = size_x
        self.__size_y = size_y
        self.__empty_char = empty_char
        #self.map = [[self.__empty_char] * self.__size_x] * self.__size_y
        self.__map = []
        for y in range(self.__size_y):
            self.__map.append([])
            for x in range(self.__size_x):
                self.__map[y].append(self.__empty_char)

    def clear(self):
        for y in range(self.__size_y):
            for x in range(self.__size_x):
                self.__map[y][x] = self.__empty_char

    def print(self):
        for y in range(self.__size_y):
            for x in range(self.__size_x):
                print(self.__map[y][x], end='')
            print()

    def set_point(self, point):
        self.__map[point.y][point.x] = point.char


#%% 4 point
        
from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int
    char: str

    #%% 5 snake 

from point import Point


class Snake:
    def __init__(self, max_x, max_y, start_x, start_y):
        self.__max_x = max_x
        self.__max_y = max_y
        self.body = [Point(start_x, start_y, '@')]
        self.direction = Point(1, 0, '')
        self.delay = 0.5

    def move(self):
        # move tail
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y

        # move head
        self.body[0].x += self.direction.x
        self.body[0].y += self.direction.y

        # check map ranges
        if self.body[0].x > self.__max_x:
            self.body[0].x = 0

        if self.body[0].x < 0:
            self.body[0].x = self.__max_x

        if self.body[0].y > self.__max_y:
            self.body[0].y = 0

        if self.body[0].y < 0:
            self.body[0].y = self.__max_y

    def add_body(self):
        self.body.append(Point(self.body[0].x, self.body[0].y, 'X'))

    def is_dead(self):
        for i in range(1, len(self.body)):
            if self.body[0].x == self.body[i].x and self.body[0].y == self.body[i].y:
                return True
        return False
    
    #%% 6 apple

from point import Point
import random


class Apple(Point):
    def __init__(self, max_x, max_y):
        super().__init__(0, 0, 'A')
        self.__max_x = max_x
        self.__max_y = max_y
        self.x = random.randint(0, self.__max_x)
        self.y = random.randint(0, self.__max_y)

    def set_new_place(self, points):
        is_wrong = True
        while is_wrong:
            is_wrong = False
            self.x = random.randint(0, self.__max_x)
            self.y = random.randint(0, self.__max_y)
            for point in points:
                if self.x == point.x and self.y == point.y:
                    is_wrong = False

#%%
                    
def sum(*arg, **kwargs):
    print(arg, kwargs)


sum(2, 3, 4)
sum(2, 3, a=6, b=7, c=8)


# %%
def sum(*arg, **kwargs):
    result = 0
    for i in arg:
        result += i
    for i in kwargs.values():
        result += i
    return result


print(sum(2, 3, 4, 4, 5, 4, 3, 2, 3, 4))
sum(2, 3, a=6, b=7, c=8)

print()

# lambda - "anonim funkcja"
import functools

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#lamb
map_list = list(map(lambda x: x+2, my_list))
reduced_list = functools.reduce(lambda x, y: x+y, my_list)
filtered_list = list(filter(lambda x: x % 2 == 0, my_list))

print('map', map_list)
print('reduced', reduced_list)
print('filtered', filtered_list)

# min, max, sort

new_list2 = [(1,2,3), (4,5,6), (7,8,9)]

print('MIN')
my_min = min(new_list2, key=lambda x: x[0] + x[1])
print(my_min)
print('MAX')
my_max = max(new_list2, key=lambda x: x[0] * x[1])
print(my_max)
print('SORTED')
my_sorted = sorted(new_list2, key=lambda x: x[0] + x[1])
print(my_sorted)
#%%

# CZWICZENIE 1 map at Upper
list_family = ['Oliwer', 'Taja', 'Artem', "Maja", "Lucifer"]
map_family = list(map(lambda x: x.upper(), list_family))
print('UPPER_FAM: ', map_family)

# CZWICZENNIE 2 sort by last litr
sorted_family = sorted(list_family, key=lambda x: x[-1])
print('SORTED_FAM: ', sorted_family)

#%%
def last_char(x):
    return x[-1]
#1
name = 'Zenek'
last_character = last_char(name)
print('Last character: ', last_character)

#2
last_character_sorted = sorted(name, key=last_char)
last_character_sorted2 = sorted(name, key=lambda x: x[-1])
print('Last character sorted: ', last_character_sorted)
print('Last character sorted 2(lambba): ', last_character_sorted2)

#3
lamb_last_character_sorted = lambda x: x[-1]
last_character_sorted3 = sorted(name, key=lamb_last_character_sorted)
print('Last character sorted 3(lambba): ', last_character_sorted3)

#%% Iterator

class MyIterator:
    def __init__(self, max, start):
        self.max = max
        self.number = start

    def __iter__(self):
        return self

    def __next__(self):
        self.number += 1
        if self.number < self.max:
            return self.number
        else:
            raise StopIteration

my_iter = MyIterator(4, 10)
for elem in my_iter:
    print(elem)