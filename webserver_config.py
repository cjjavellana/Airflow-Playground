"""
AUTH_ROLE_ADMIN: the role of the bind user (should be Admin)
AUTH_USER_REGISTRATION: boolean for automatically creating users on first log-in
AUTH_USER_REGISTRATION_ROLE: the role which first-time users logging in will be assigned
                             Possible Values: Admin, Viewer, User, Op, Public 
AUTH_LDAP_SERVER: the LDAP server URI
AUTH_LDAP_SEARCH: update with the LDAP path under which you’d like the users to have access to Airflow. Example: dc=example,dc=com.
AUTH_LDAP_BIND_USER: the path of the LDAP proxy user to bind on to the top level. Example: cn=airflow,ou=users,dc=example,dc=com.
AUTH_LDAP_BIND_PASSWORD: the password of the bind user
AUTH_LDAP_UID_FIELD: the UID (unique identifier) field in LDAP
AUTH_LDAP_USE_TLS: boolean whether TLS is being used
AUTH_LDAP_ALLOW_SELF_SIGNED: boolean to allow self-signed certificates
AUTH_LDAP_TLS_CACERTFILE: location of the certificate
"""


import os
from airflow import configuration as conf
from flask_appbuilder.security.manager import AUTH_LDAP

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = conf.get('core', 'SQL_ALCHEMY_CONN')
CSRF_ENABLED = True
AUTH_TYPE = AUTH_LDAP

AUTH_ROLE_ADMIN = 'Admin'
AUTH_USER_REGISTRATION = True

AUTH_USER_REGISTRATION_ROLE = 'Viewer'

AUTH_LDAP_SERVER = 'ldap://ldap:389'
AUTH_LDAP_SEARCH = 'ou=People,dc=cjavellana,dc=me'
AUTH_LDAP_BIND_USER = 'cn=admin,dc=cjavellana,dc=me'
AUTH_LDAP_BIND_PASSWORD = 'secret'
AUTH_LDAP_UID_FIELD = 'uid'

# LDAPS
AUTH_LDAP_USE_TLS = False
AUTH_LDAP_ALLOW_SELF_SIGNED = False
AUTH_LDAP_TLS_CACERTFILE = '/etc/ssl/certs/ldap.crt'
