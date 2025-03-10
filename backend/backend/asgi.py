"""
ASGI config for backend project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""
#this is a configuration file that tells the server how to communicate with the application.
#handle the ASGI(Asynchronous Server Gateway Interface) protocol
#In simple terms, ASGI allows the django application to communicated with the server in real time which enable features such as live updates 
#and other async tasks

#Allows code to interact witht he OS so you can work with files and enviroment settings
import os

from django.core.asgi import get_asgi_application

#sets environment variable to the settings file so djnago knows where to find it
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

application = get_asgi_application()#a fucniton that allows django to handle async communication with websockets
