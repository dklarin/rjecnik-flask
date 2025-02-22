import os
import pygsheets

client_secret_file = os.getenv('CLIENT_SECRET_FILE')

print(client_secret_file)

#gc = pygsheets.authorize(service_file=client_secret_file)


def plahte():
    gc = pygsheets.authorize(service_file='creds.json')
    sh = gc.open('baza')
    wks = sh[2]
    return wks
