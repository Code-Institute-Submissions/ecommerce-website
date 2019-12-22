# ecommerce-website



Link to project: https://ecommerce-10.herokuapp.com/



This project is built using Django. The Django project has 5 applications: 1)storages - this app stores and retrieves static files (css,js and media/images) from Amazon AWS. 2) accounts - this app contains the reference to all the users's information on their accounts and credentials that are used to create, modify and use login and signup information. 3) products -this app contains and stores all the references to products (id,category,price,quantity) in the 'stock' database of the website. 4) cart - this app contains and stores all the information that connects the products to the cart and to finally the (last) app 'checkout'. 5) checkout - this app contains and stores all the information that related to products, accounts and carts so that products can be ordered and purchased using Stripe's API.

Project is connected to a PostgresSQL database that can be modified locally or through cloud. Project also takes staticfiles that are served from an online AWS Amazon Bucket. Project implements the STRIPE api configurations that allow purchases to be made for the products stored in the APPs.

The project ignores any senstive commits to github and preserves private keys. Requirements.txt file allow for a quick installation of the requirements for the projects using 'pip -r install requirements.txt'



Project's requirements:
asgiref==3.2.3
boto3==1.10.40
botocore==1.13.40
certifi==2018.10.15
chardet==3.0.4
dj-database-url==0.5.0
Django==3.0
django-forms-bootstrap==3.1.0
django-mssql==1.8
django-storages==1.8
docutils==0.15.2
envs==1.3
gunicorn==19.9.0
idna==2.7
jmespath==0.9.4
numpy==1.17.4
pandas==0.25.3
pbr==5.4.4
Pillow==6.2.1
postgres==3.0.0
psycopg2-binary==2.8.4
psycopg2-pool==1.1
python-dateutil==2.8.0
python-decouple==3.3
pytz==2018.7
requests==2.20.1
s3transfer==0.2.1
six==1.13.0
sqlparse==0.3.0
stevedore==1.31.0
stripe==2.12.1
urllib3==1.24.3
virtualenv==16.7.9
virtualenv-clone==0.5.3
virtualenvwrapper==4.8.4
whitenoise==5.0.1


Project can be run locally by cloning/downloading this repository and by cd'ing into the main project directory (where manage.py is contained) that is the main directory for project.From there project can be run locally by using the command python manage.py runserver on the terminal.

Project is connected to heroku.git (from which it is automatically deployed). This repo is a new copy of the existing heroku.git repo (https://git.heroku.com/ecommerce-10.git). If you desire to see the existing branches of the project, you can go to ecommerce-latest to see the updates.



Credit to: Richard Dalton 
For providing a preliminary project structure and basic guidelines
(from https://github.com/richardadalton/com-devjoy-ecommerce)
