## How to
To install this project, you will need:

1. `pip` package, available with your package manager (e.g. apt-get install python-pip).

## Deployment
    $ cd <path_to_matterllo_repository>

    $ pip install -r requirements.txt

    $ python manage.py migrate

    # automatically create a default superuser.
    $ python manage.py loaddata admin

    # set the necessary Trello stuff.
    $ export TRELLO_APIKEY=<your_api_key>

    $ export TRELLO_TOKEN=<your_token>

    $ python manage.py runserver

    # you must public expose the webserver to receive trello callbacks.
    # - use nginx with a proxy pass
    # - use ngrok for test (ngrok http 8000)
    # - etc.. 

## Trello callback
### Premise
* By default, Matterllo take the `django request host` to create the trello callback and receive notifications. Example with a localhost URL:
```
# bad
create trello hook :: callback=http://localhost:8000/callback/1/ :: board=tutorial-board-start-here :: result=False

# good
create trello hook :: callback=http://4308dac9.ngrok.io/callback/2/ :: board=test :: result=<trello[...]>
```

### Solutions
* You could public expose the webserver to receive trello callbacks. (nginx with a proxy pass, ngrok to test...)

* You can override the host address also.
```
$ export MATTERLLO_HOST=matterllo-foo.com
```

## Production ready
### Change your admin password
1. Go to the Admin page
2. Use the default account: `admin`/`admin`
3. Go to the `User` part and change the password through the form

### Change the secret
    $ export SECRET=<your_secret>

## Technical overview
* `sqlite` is the default database.
* All database objects can be directly manipulated through the admin interface.
