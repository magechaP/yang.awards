# Yang.Awards
###### Description
yang.awards is a platform where users can post their projects to be viewed by other users who can rate the 
project based on the usability, designed user interface and content of these posted projects. a user can also leave a comment behind for the project owner to know where they deserve a merit or where they 
need to improve on.
* As a signed up user you can be able to review and rate other peoples projects
* You can visit the live site of the projectand interact with it
* Post your projects and wait for the responses of others
###### Author
Peter Magecha

### Application Functionality
* The application aloows posting and rating of projects.
* The projects overall score is then computated to determine which project has the highest score
* A user can create their own profile wher they can view the projects they have ever posted
* As an external user or programmer you can fetch data from an api and use it to access data in the applications database aswell as use it in your application

## BEHAVIOUR DRIVEN DEVELOPMENT

| Behaviour | Input  | Output |
| -- |-- |--|
|Sign up| Create credentials| Successful sign up if credentials are viable|
|Login|Enter login credentials | Go to landing page|
|Upload project|Click post prroject on taskbar |access project post form|
|View projects|Click projects on navbar| Go to projects page|
|View a single project|Click on view button on the image|View a single project|
|Rate project|Click on rate project button|Access rate project form|
|Search projects|Enter project name on the search bar|Results of the search|
|View actual projects|Click live project button|access the actual project |

### Installations

1. Clone the repository with:
`git clone https://github.com/magechaP/yang.awards`
2. You will then have to unzip the zipped format of the repo.

3. You will need to install all dependencies by running this command:
* First make sure your requirements.txt file is like this:

`config==0.3.9`
`dj-database-url==0.5.0`
`Django==1.11`
`django-bootstrap3==10.0.1`
`django-heroku==0.3.1`
`gunicorn==19.9.0`
`Pillow==5.2.0`
`psycopg2==2.7.5`
`python-decouple==3.1`
`pytz==2018.5`
`whitenoise==4.0`
`pip install -r requirements.txt`
`django-mathfilters==0.4.0`
`pytz==2019.1`
`djangorestframework==3.9.4`

* If not use this command:
`pip freeze > requirements.txt`
* i would advice you to use python version 3.6 +
* Do not try to use django version above 1.11, it will result to errors due to compatibility
* For this cause, i recommend python 3.6 but specify `python3.6.8` in your `runtime.txt` file when deploying to heroku

4. To use the application locally you wil have to create a postgress database
follow these steps to get the app up and running:
* in your psql:
`CREATE DATABASE award;`
* in your terminal migrate with:
`python3.6 manage.py migrate`
* Make a `.env` file to store your environmental variables

* serve the application with:
`python manage.py runserver`
* open the app on localhost:8000

## Technologies used
1. Django 1.11
2. Python3.6
3. HTML and Css
4. Production deployment to heroku
## License
This project is licensed under the MIT Open Source license, (c) Peter Magecha