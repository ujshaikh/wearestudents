Django is a powerful web framework that can help you get your Python application or website off the ground quickly. Django includes a simplified development server for testing your code locally, but for anything even slightly production related, a more secure and powerful web server is required.

In this guide, we will demonstrate how to install and configure Django in a Python virtual environment. We’ll then set up Apache in front of our application so that it can handle client requests directly before passing requests that require application logic to the Django app. We will do this using the mod_wsgi Apache module that can communicate with Django over the WSGI interface specification.
## Ref: 
https://www.digitalocean.com/community/tutorials/how-to-serve-django-applications-with-apache-and-mod_wsgi-on-ubuntu-14-04

## Some useful command to make ready to deploy on server
`$ sudo apt-get update`

If you are using Django with Python 2, the commands you need are:

`$ sudo apt-get install python3-pip apache2 libapache2-mod-wsgi-py3`

If, instead, you are using Django with Python 3

`$ sudo apt-get install python3-pip apache2 libapache2-mod-wsgi-py3`

We need to install the virtualenv command to create these environments.

`$ sudo pip install virtualenv`

Run at root dir of project

`$ virtualenv venv'

`$ source myprojectenv/bin/activate`

`$ pip install -r requirements.txt`

`$ python manage.py makemigrations`

`$ python manage.py migrate`

`$ python manage.py createsuperuser`

`$ python manage.py collectstatic`

`$ python manage.py runserver 0.0.0.0:8000`

In your web browser, visit your server’s domain name or IP address followed by :8000
`http://server_domain_or_IP:8000`

`Alias /static /<project-root-dir-path>/tenurdu/static
<Directory /<project-root-dir-path>/tenurdu/static>
    Require all granted
</Directory>

<Directory /<project-root-dir-path>/app>
    <Files wsgi.py>
        Require all granted
    </Files>
</Directory>

WSGIDaemonProcess wearestudents python-path=/<project-root-dir-path> python-home=/<project-root-dir-path>/venv
WSGIProcessGroup wearestudents
WSGIScriptAlias / /<project-root-dir-path>/app/wsgi.py`

## Useful cmd for apache2
`$ sudo apache2ctl configtest`

`$ sudo service apache2 restart`

## Permission
`$ sudo chmod 664 /<project-root-dir-path>/db.sqlite3`

`$ sudo chown :www-data /<project-root-dir-path>/db.sqlite3`

`$ sudo chown :www-data /<project-root-dir-path>`

`$ sudo service apache2 restart`

## Conclusion
In this guide, we’ve set up a Django project in its own virtual environment. We’ve configured Apache with mod_wsgi to handle client requests and interface with the Django app.
