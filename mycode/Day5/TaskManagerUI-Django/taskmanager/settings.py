# Add to INSTALLED_APPS
INSTALLED_APPS = [

    'tasks.apps.TasksConfig',
    'crispy_forms',
]

# Add at the bottom
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'