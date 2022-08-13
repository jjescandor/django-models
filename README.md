## LAB - Class 27

#### Project: Snacks Project with Database
#### Author: JJ Escandor


#### Description

 - This is project is an extension to Snack Project where we added a database 

### Run the app

 - pip install -r requirements.txt
 - python manage.py runserver
 - go to http://127.0.0.1:8000/ in the browser

#### Feature task and Requirements

1. Model
    - create snack_tracker_project project
    - create snacks app
    - Add snacks app to project
    - create Snack model
    - add model to admin
    - modify Snack model have user friendly display in admin
    - create migrations and migrate data
    - create a super user
    - run development server
    - Add a few snacks via Admin panel
    - create another user and more snacks via Admin panel
    - confirm that snacks behave as expected with proper name, purchaser and description.
    - Looks like your model in good shape. Congrats!
1. Views for Snacks App
    - create SnackListView
    - update url patterns for project   
    - update snacks app urls
    - add detail view
    - update app urlpatterns to handle detail view

### Tests

1. run python3 manage.py test in the terminal
