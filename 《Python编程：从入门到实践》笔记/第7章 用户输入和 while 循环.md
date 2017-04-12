# 第7章 用户输入和 while 循环

- input():

  ```python
  >>> name = input('Please input your nanme: ')
  Please input your nanme: mimi
  >>> name
  'mimi'
  >>> prompt = "If you tell us who you are, we can personalize the messages you see."
  >>> prompt += "\nWhat is your first name? "
  >>> name = input(prompt)
  If you tell us who you are, we can personalize the messages you see.
  What is your first name? mimi
  >>> name
  'mimi'
  >>> age = input('Please input your age: ') # 使用函数input() 时，Python将用户输入解读为字符串。
  Please input your age: 23
  >>> age
  '23'
  ```

- while 循环

  break: 不再执行余下的代码并退出整个循环

  continue: 忽略余下的代码，并返回到循环的开头

  ```python
  >>> prompt = "\nPlease enter the name of a city you have visited:"
  >>> prompt += "\n(Enter 'quit' when you are finished.) "
  >>> # break 用法
  >>> while True: 
  ...     city = input(prompt)
  ...     if city == 'quit':
  ...         break
  ...     else:
  ...         print(city)
  ... 

  Please enter the name of a city you have visited:
  (Enter 'quit' when you are finished.) dalian
  dalian

  Please enter the name of a city you have visited:
  (Enter 'quit' when you are finished.) beijing
  beijing

  Please enter the name of a city you have visited:
  (Enter 'quit' when you are finished.) shanghai
  shanghai

  Please enter the name of a city you have visited:
  (Enter 'quit' when you are finished.) quit
  >>> # continue 用法
  >>> current_number = 0
  >>> while current_number < 10:
  ...     current_number += 1
  ...     if current_number % 2 == 0:
  ...         continue
  ...     print(current_number)
  ... 
  1
  3
  5
  7
  9
  ```

- 使用 while 循环来处理列表和字典: 

  for 循环是一种遍历列表的有效方式，但**在for 循环中不应修改列表**，否则将导致Python难以跟踪其中的元素。要在遍历列表的同时对其进行修改，可使用while 循环。

  ```python
  >>> unconfirmed_users = ['alice', 'brian', 'candace']
  >>> while unconfirmed_users:
  ...     pop_elem = unconfirmed_users.pop()
  ...     print(pop_elem)
  ... 
  candace
  brian
  alice
  >>> pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
  >>> while 'cat' in pets:
  ...     pets.remove('cat')
  ... 
  >>> print(pets)
  ['dog', 'dog', 'goldfish', 'rabbit']
  >>> person = {'name': 'mimi', 'location': 'xiamen'}
  >>> flag = 1
  >>> while flag:
  ...     person['location'] = 'fuzhou'
  ...     if person['location'] != 'xiamen':
  ...         print(person['name'] + ' went to ' + person['location'] + ' yesterday')
  ...         flag = 0
  ... 
  mimi went to fuzhou yesterday
  >>>
  ```