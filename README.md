pingpongproject
===============

Ping Pong Project Repository

##Clone the project
===================
In the terminal, execute the command:

`git clone git@github.hogarthww.prv:lukeperrottet/pingpongproject.git`

##Virtual environment
=====================
```
pip install virtualenvwrapper==4.3
export WORKON_HOME=~/Envs
source /usr/local/bin/virtualenvwrapper.sh
mkvirtualenv venv
workon venv
```

##Install the requirements
==========================
`pip install -r requirements.txt`

##Create the database
=====================
Before running the poject, you need to create the database.
To achieve this, you have to execute this command in the terminal:

`python manage.py migrate`

"manage.py" is in the pingpongproject/pingpongproject/ directory

##Run the project locally
===============================
In the terminal,  execute the command:

`python manage.py runserver`

On your browser, enter the url:
`http://localhost:8000`

You will be redirected to the Homepage of the website.

##Run the project with a Vagrant box
====================================
In the terminal, run:

`vagrant up`

When this is finished, run:

`fab vagrant_settings setup`

And finally :

`fab vagrant_settings runserver`

Then you need to go to your vagrant box to get the ip address:

```
vagrant ssh
ifconfig | grep 10.105
```

Then copy the resulting ip address to your browser:

`http://VAGRANT_IP_ADDRESS`

You will be redirected to the Homepage of the website.

###Update to the last version of the project

`fab vagrant_settings deploy`

##Run the project in production
====================================
In the terminal, run:

```
fab prod_settings setup

fab prod_settings runserver
```

With this command, you can go to your browser and enter :

`http://10.9.4.107`

You will be redirected to the Homepage of the website.

###Update to the last version of the project

`fab prod_settings deploy`
