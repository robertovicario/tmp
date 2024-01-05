from datetime import datetime, timedelta
import os
import random

def generate_commit_dates(year, month):
    start_date = datetime(year, month, 1)
    end_date = (start_date + timedelta(days=32)).replace(day=1) - timedelta(days=1)
    
    dates = []
    current_date = start_date

    while current_date <= end_date:
        week_dates = []
        for _ in range(7):
            if current_date.month == month:
                week_dates.append(current_date)
            current_date += timedelta(days=1)
        
        if len(week_dates) >= 3:
            random_days = random.sample(week_dates, 3)
            dates.extend(random_days)
        else:
            dates.extend(week_dates)

    return dates

def create_fake(n, year, month, day):
    date = f"{year}-{month}-{day}T12:00:00"
    for i in range(n):
        with open('tmp.txt', 'a') as tmp:
            tmp.write("#" + str(i) + "\n")

        os.system('git add .')
        os.system(f'git commit -m "updates" --date="{date}"')

def commit(year, month):
    commit_dates = generate_commit_dates(year, month)
    commit_options = [10, 20, 30]
    
    for date in commit_dates:
        num_commits = random.choice(commit_options)
        create_fake(num_commits, date.year, date.strftime('%m'), date.strftime('%d'))

commit(2024, 1)
