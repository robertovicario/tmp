import os

def fake_commits(n):
    for i in range(n):
        with open('tmp.txt', 'a') as tmp:
            tmp.write("#" + i + "\n")

        os.system('git add .')
        os.system('git commit -m updates')

fake_commits(10)