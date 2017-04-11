# 第5章 if 语句

- = , != , > , < , >= , <=

  ```python
  >>> age_0 = 19
  >>> age_1 = 23
  >>> age_0 == age_1
  False
  >>> age_0 < age_1
  True
  >>> age_0 > age_1
  False
  >>> age_0 != age_1
  True
  >>> age_0 = '19'
  >>> age_1 = '23'
  >>> age_0 != age_1
  True
  >>> age_1 == age_0
  False
  ```

- in,not in 

  ```python
  >>> requested_toppings = ['mushrooms', 'onions', 'pineapple']
  >>> 'mushrooms' in requested_toppings
  True
  >>> 'mushrooms' not in requested_toppings
  False
  ```

- and,or

  ```python
  >>> True and True
  True
  >>> True and False
  False
  >>> False and False
  False
  >>> True or True
  True
  >>> True or False
  True
  >>> False or False
  False
  ```

- if-elif-else:如果你只想执行一个代码块，就使用if-elif-else 结构；如果要运行多个代码块，就使用一系列独立的if 语句

  ```python
  >>> requested_toppings = []
  >>> # Python将在列表至少包含一个元素时返回True ，并在列表为空时返回False 
  >>> if requested_toppings:
  ...     print(1)
  ... else:
  ...     print(0)
  ... 
  0
  ```