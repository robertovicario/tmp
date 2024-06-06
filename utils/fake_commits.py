import os

from torch import rand

def operation():
    with open('tmp.txt', 'a') as file:
        file.write('#\n')

    os.system("git add .")
    os.system(f'git commit --date="2024-5-{str(rand)}" -m updates')

for i in range(10):
    operation()

for i in range(20):
    operation()

for i in range(30):
    operation()
