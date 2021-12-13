### About

A logbook web app with ActiveDirectory auth and Slack notifications for logged tasks.

### Built on

- [Django](https://docs.djangoproject.com/en/3.1/)
- [django-auth-ldap](https://django-auth-ldap.readthedocs.io)
- [BootstrapVue](https://bootstrap-vue.org)
- [SQLite](https://www.sqlite.org/quickstart.html)

### Python virtual environment setup

0. `sudo apt install libsasl2-dev python3-dev libldap2-dev libssl-dev`
1. `python3 -m venv .venv`
2. `pip install -r requirements.txt`
3. `./manage.py makemigrations devops_logbook`
4. `./manage.py migrate`

### Clean installation

1. `django-admin startproject devops_logbook_conf`
2. `./manage.py createsuperuser`
3. `./manage.py startapp devops_logbook`
4. `./manage.py runserver`
