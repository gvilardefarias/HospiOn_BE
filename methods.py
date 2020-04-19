import os.path
import json

def userRegistered(email):
    return os.path.exists('users/' + email + '.json')

def register(name, surname, email, tipo):
    data = {'name': name, 'surname': surname, 'email': email, 'type': tipo}

    arquivo = open('users/' + email + '.json', 'w')

    arquivo.write(json.dumps(data))

    arquivo.close()

def registerPJ(name, email, password, cnpj):
    data = {'name': name, 'email': email, 'password': hash(password),'type': 'PJ'}

    arquivo = open('users/' + email + '.json', 'w')

    arquivo.write(json.dumps(data))

    arquivo.close()


def getUser(email):
    arquivo = open('users/' + email + '.json', 'r')
    data    = json.load(arquivo)
    arquivo.close()

    data.pop('password', None)

    return data

def getHospital(ID):
    arquivo = open('hosp/' + str(ID) + '.json', 'r')
    data    = json.load(arquivo)
    arquivo.close()

    return data

def getAllHospital():
    count     = open('hosp/count', 'r')
    num       = int(count.readline())
    count.close()

    hospitals = []

    for i in range(num):
        arquivo = open('hosp/' + str(i) + '.json', 'r')

        hospitals.append(json.load(arquivo))

        arquivo.close()

    return hospitals


def login(email, password):
    if not userRegistered(email):
        return False

    if hash(password)==getUser(email)['password']:
        return True

    return False

def getOrder(ID):
    arquivo = open('orders/' + str(ID) + '.json', 'r')
    data    = json.load(arquivo)
    arquivo.close()

    return data


def getAllOrders():
    count   = open('orders/count', 'r')
    num     = int(count.readline())

    orders = []

    for i in range(num):
        arquivo = open('orders/' + str(i) + '.json', 'r')

        orders.append(json.load(arquivo))

        arquivo.close()

    return orders

def updateOrder(ID, data):
    arquivo = open('orders/' + str(ID) + '.json', 'w')

    arquivo.write(json.dumps(data))

    arquivo.close()
    
    return data
