# iitg-main-website
Main webpage of the Indian Institute of Technology Guwahati, India by SWC Team

To develop and use the application perform the following commands on your terminal:
```
sudo apt-get update

sudo apt-get install python-pip python-dev libpq-dev postgresql postgresql-contrib

sudo su - postgres

psql

CREATE DATABASE iitg_main_page_db;

CREATE USER adminadmin WITH PASSWORD 'adminadmin';

\q

exit

sudo python3 manage.py makemigrations

sudo python3 manage.py migrate

sudo python3 manage.py runserver
```
