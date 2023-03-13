# Выведите список файлов в указанной директории.

import os
from os.path import isfile, join
path = 'my_tasks'
print(*[f'{file}\n' for file in os.listdir(path) if isfile(join(path, file))])
