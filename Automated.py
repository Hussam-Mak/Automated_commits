import os
import random
import datetime
import subprocess

# Configuration
repo_path = r"C:\Users\hussa\OneDrive\Automated_commits"  # Change this to your repo path
commit_message = "Automated commit to make my GitHub board green 🌱"
total_commits_per_day = 1  # Adjust for more commits per day

# Function to execute Git commands
def run_git_command(command):
    process = subprocess.Popen(command, shell=True, cwd=repo_path)
    process.wait()

# Function to generate commit dates
def get_commit_dates(start_date, days):
    return [start_date + datetime.timedelta(days=i) for i in range(days)]

# Set start date (e.g., 3 months ago) and number of days
start_date = datetime.date.today() - datetime.timedelta(days=90)
days_to_commit = 90  # Adjust to control how many days of commits you want

# Iterate over the days
for commit_date in get_commit_dates(start_date, days_to_commit):
    for _ in range(random.randint(1, total_commits_per_day)):  # Vary the commits per day
        # Modify a dummy file
        with open(os.path.join(repo_path, "dummy.txt"), "a") as file:
            file.write(f"Commit on {commit_date}\n")

        # Set Git environment to commit in the past
        env = os.environ.copy()
        env["GIT_COMMITTER_DATE"] = commit_date.strftime("%Y-%m-%dT12:00:00")
        env["GIT_AUTHOR_DATE"] = commit_date.strftime("%Y-%m-%dT12:00:00")

        # Run Git commands
        run_git_command("git add .")
        run_git_command(f'git commit -m "{commit_message}"')
        print(f"Committed for {commit_date}")

# Push to GitHub
run_git_command("git push origin main")  # Change 'main' to your default branch if necessary
print("All commits pushed!")
