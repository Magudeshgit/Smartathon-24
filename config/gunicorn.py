wsgi_app = "smartreg.wsgi:application"
workers = 2
bind = "0.0.0.0:8000"
reload = True
daemon = True
accesslog = "../logs/access.log"
errorlog = "../logs/error.log"
loglevel = "debug"
