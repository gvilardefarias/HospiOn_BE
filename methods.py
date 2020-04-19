import os.path
import json

def userRegistered(email):
    return os.path.exists('users/' + email + '.json')

def register(name, surname, email, tipo):
    data = {'name': name, 'surname': surname, 'email': email, 'type': tipo}

    arquivo = open('users/' + email + '.json', 'w')

    arquivo.write(json.dumps(data))

    arquivo.close()

def getUser(email):
    arquivo = open('users/' + email + '.json', 'r')
    data    = json.load(arquivo)
    arquivo.close()

    return data

