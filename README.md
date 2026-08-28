# csb-project-1

[Part 3 / Project I](https://cybersecuritybase.mooc.fi/module-3.1) of Cyber Security Base

## Testing instructions

1. Make sure you have installed all the dependencies
* Install Python and Django (as instructed in [the course guidelines](https://cybersecuritybase.mooc.fi/installation-guide))
* Install ```Bleach```
```
$ pip install bleach
```

2. Set up the database
```
$ python manage.py migrate
```

3. Start the server
```
$ python manage.py runserver
```

You can create new users directly in the app.
