import subprocess
import random
import datetime
import os

def run_command(command):
    subprocess.call(command, shell=True)

def create_commits(n, month, year):
    days_in_month = (datetime.date(year, month % 12 + 1, 1) - datetime.timedelta(days=1)).day
    commits_per_day = n // days_in_month

    for day in range(1, days_in_month + 1):
        commit_count = random.choice([10, 20, 30])
        date = datetime.date(year, month, day).strftime('%Y-%m-%d')
        
        for commit in range(commit_count):
            with open('tmp.txt', 'a') as file:
                file.write(f'{date} #{commit + 1}\n')
            run_command(f'git add .')
            run_command(f'git commit -m updates')

def main():
    n = int(input("commit_number: "))
    month = int(input("month: "))
    year = int(input("year: "))

    # Ensure the repository is clean before starting
    run_command('git reset --hard')
    
    create_commits(n, month, year)

if __name__ == "__main__":
    main()
