# property-app-backend

1. This project was created using Python Flask
2. Making use of Python Flask Eve library for MongoDB REST API
3. Making use of JWT as access token for restricted API calls
4. Making use of JWT library to generate the access token
5. For more info on the list of library used please read requirements.txt

# Heroku deployment
1. Create Heroku account
2. Clone the repo
3. Let's install pip, virtualenv, foreman, and the heroku Ruby gem
    $ sudo easy_install pip
    $ sudo pip install virtualenv
    $ sudo gem install foreman heroku
4. Login to your heroku account from the terminal
    $ heroku login
5. Install all the dependency lib by using pip install, by right you shouldn't need to freeze the requirements.txt anymore, but should you have additional lib, please do so
    $ virtualenv --no-site-packages env
    $ source env/bin/activate
    $ pip freeze > requirements.txt
6. Go to the project root directory, make sure you have the Procfile (with no extension)
    $ heroku create
    
    The content of the Procfile
    web: python app.py
7. Adding in mLab as add-on, and grab the credentials
    $ heroku addons:create mongolab
    $ heroku config | grep MONGODB_URI
8. Edit your mongoDB connection config from setup.py
    $ git push heroku master
    $ heroku ps:scale web=1
    $ heroku ps //to check the status
    $ heroku open // to launch the app

# Deployed App
1. https://mighty-coast-50618.herokuapp.com/

# List of API
-Coming Soon-
