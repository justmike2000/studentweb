# StudentWeb 

## Project Info
Author: michael.mileusnich@gmail.com

Repo: [https://github.com/justmike2000/studentweb]

## Project Requirements
Python 2.7+
See requirements.txt for package dependencies

## Description
Python Django app which Keeps tracks of students/classes and their grades.

## Installation
    pip install -r requirements.txt

## Installation with new database
    pip install -r requirements.txt
    cd studentweb
    python manage.py syncdb

## Running
python manage.py runserver 0.0.0.0:8000 (or desired port)

## Endpoints
/ - Main 

/students/ - Endpoint which returns student information in JSON format.
             Parameters:
             first
             last
             average_gpa
