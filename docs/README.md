# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a


## Структура проекта:
Проект состоит из четырех файлов:
	_1_. _circle.py
	2. rectangle.py
	3. square.py
	4. triangle.py_
	
В каждом файле содержатся функции по нахождению периметра и площади, каждой соответствующей фигуры, по формулам записанным выше. 
# _circle.py_

В данном файле содержаться функции для нахождения площади и периметра **круга**
Используется библиотека _math_, для использования константы $pi$

```python
import math

def area(r):
'''Принимает число r - радиус круга, возвращает его площадь'''
	return math.pi * r * r
  

def perimeter(r):
'''
Возвращает периметр круга.

	Параметры:
		r (int) : Радиус круга.

	Возвращаемое значение:
		per (float) : Периметр круга.

'''
per = 2 * math.pi * r

return per
```
### Примеры работы:
```cmd
>> area(5)
>> 78.53981633974483
>> -----------------
>> perimeter(5)
>> 31.41592653589793
```

# _rectangle.py
_
В данном файле содержаться функции для нахождения площади и периметра **прямоугольника**

```python
def area(a, b):
'''
Вовращает площадь прямоугольника.
	Параметры:
		a (int) : Первая сторона прямоугольника
		b (int) : Вторая сторона прямоугольника

	Возвращаемое значение:
		s (int) : Произведение a и b
'''

s = a * b

return s

def perimeter(a, b):
''' Принимает числа a и b, возвращает их удвоенную сумму - периметр прямоугольника'''

return (a+b) * 2
```
### Пример работы:
```cmd
>> area(10, 7)
>> 70
>> ---------------
>> perimeter(5, 8)
>> 26
```

# _square.py_

В данном файле содержаться функции для нахождения площади и периметра **квадрата**

```python
def area(a):
'''Принимает число a - сторона квадрата, возвращает его произведение самого на себя - площадь квадрата'''
return a * a

  
  

def perimeter(a):
'''Принимает число a(сторона квадрата), возвращает произведение 4 * a (периметр квадрата)'''
return 4 * a
```
### Пример работы:
```cmd
>> area(7)
>> 49
>> ---------------
>> perimeter(5)
>> 20
```

# _triangle.py_

В данном файле содержаться функции для нахождения площади и периметра **треугольника**

```python
def area(a, h):
'''
Возвращает площадь треугольника
	Параметры:
		a (int) : Сторона треугольника
		h (int) : Высота треугольника

	Возвращаемое значение:
		s (float) : Половина произведения a и h
'''
s = a * h / 2

return s

def perimeter(a, b, c):

'''Принимает числа a, b, c(строны треугольника), возвращает их сумму (периметр треугольника)'''

return a + b + c
```
## Пример работы
```cmd
>> area(7, 8)
>> 28.0
>> perimeter(5, 3, 4)
>> 12
```

## Commits

* 44af26f (HEAD -> new_features_465089) Added docs and readme
* 7133360 Documentation for triangle.py
* e316f49 Documentation for: rectangle.py, circle.py, square.py

| * f4895e1 (origin/new_feature-465089) final commit
| * 97d6ac7 Added new file: triangle.py. Fix error in def perimetr in rectangle.py file
| * 1cd5d8d Added new file: rectangel.py
|/ 
* d078c8d (origin/main, origin/HEAD, main) L-03: Docs added
* 8ba9aeb L-03: Circle and square added
