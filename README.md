### INFO



### Built on
- [Django](https://docs.djangoproject.com/en/3.1/)
- [django-auth-ldap](https://django-auth-ldap.readthedocs.io)
- [BootstrapVue](https://bootstrap-vue.org)
- [SQLite](https://www.sqlite.org/quickstart.html)

### Python virtual environment setup for a clean installation
0. `sudo apt install libsasl2-dev python-dev libldap2-dev libssl-dev`
1. `python3 -m venv .venv`
2. `pip install requirements.txt`
3. `django-admin startproject devops_logbook_conf`
4. `./manage.py createsuperuser`
5. `./manage.py runserver`
6. `./manage.py startapp devops_logbook`

### TODO

- Add restriction on message POST to only accept from certain number of characters and above
- Tags: `'cassandra', 'postgres', 'k8s-prod', 'jupyterhub', 'kafka', 'k8s-dev', 'azure-ops', 'jenkins/ci', 'monitoring', 'internal'`
- Add stats counter for each tag on tab "Stats"
- Add Slack integration for logbook entry update in channel devops in the form of `"@devops-team Log: cassandra vm node os upgrade"`
- Create k8s manifests
- Optimise the imported scripts from unpkg - either download them locally.
