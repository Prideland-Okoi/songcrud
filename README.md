## Python Task: Pip, Virtual environments and intro to Django

# Task
Create a new Django project named “songcrud” and create an app in the project called “musicapp”. Your project must contain a requirements.txt file housing all the pinned dependencies from your project. Push the project to GitHub and submit your public GitHub repository link.

Note: Always create a virtual environment anytime you're working on a new Django project. You can get your requirements.txt file from your virtual environment 

# Solution

|S/No|Steps|
|---|----------|
|1|Either go to github.com and create the repository and clone on your CMD Line/gitbash/VS Code/ubuntu/powershell or go directly to these terminal - mkdir songcrud and later push to your github|
|2|mkdir songcrud && cd songcrud|
|3|virtualenv `virtual-environment-name` && source `virtual-environment-name`/bin/activate or source `virtual-environment-name`/Scripts/activate|
|4|pip install django|
|5|django-admin startproject `project-name` && cd `project-name`|
|6|python manage.py startapp `app-name`|
|a|pip install `dependencies of your choice`|
|b|`pip freeze > requirements.txt` to list dependencies in a file|
|c|add .gitignore file to include the word `virtual-environment-name` to avoid pushing it to your version control system|
