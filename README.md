# set_timeout function in python

В файле `lib.py` я написал поверхностную эмитацию event loop в javascript.

## how to use

### Для использования у себя в проекте 
1. Скопируйте файл `lib.py` в свою директорию.
2. Импортируйте функцию `set_timeout` в файл в котором хотите её использовать
```py
from lib import set_timeout
```
3. Вызовите фуекцию и передайте в неё 2 параметра

Шаблон:
```py
set_timeout(<callback>, <time in seconds>)
```

Пример:
```py
def start():
    print('timeout text')

set_timeout(start, 3)
```

### Для теста используя код репозитория
1. `git clone https://github.com/igor0400/set-timeout-puthon.git`
2. `python index.py` или `python3 index.py`