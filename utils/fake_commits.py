import os

def fake_commits(n, year, month, day):
    date = f"{year}-{month}-{day}T00:00:00"
    for i in range(n):
        with open('tmp.txt', 'a') as tmp:
            tmp.write("#" + str(i) + "\n")

        os.system('git add .')
        os.system(f'git commit -m updates --date="{date}"')

fake_commits(10, "2024", "03", "01")
