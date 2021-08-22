### About

A logbook web app with ActiveDirectory auth and Slack notifications for logged tasks.

### Built on

- [Django](https://docs.djangoproject.com/en/3.1/)
- [django-auth-ldap](https://django-auth-ldap.readthedocs.io)
- [BootstrapVue](https://bootstrap-vue.org)
- [SQLite](https://www.sqlite.org/quickstart.html)

### Environment setup for a clean installation

0. `sudo apt install libsasl2-dev python3-dev libldap2-dev libssl-dev`
1. `python3 -m venv .venv`
2. `source .venv/bin/activate`
3. `pip install wheel`
3. `pip install -r requirements.txt`
4. `./manage.py makemigrations devops_logbook`
5. `./manage.py migrate devops_logbook`
6. Use `sqlitebrowser` to add dummy tags to the table `devops_logbook_tag`, otherwise they won't show up on the page
7. `./manage.py runserver`