import os.path
import hashlib
import json

def userRegistered(email):
    return os.path.exists('users/' + email + '.json')

def register(name, surname, email, tipo):
    data = {'name': name, 'surname': surname, 'email': email, 'type': tipo}

    arquivo = open('users/' + email + '.json', 'w')

    arquivo.write(json.dumps(data))

    arquivo.close()

def registerPJ(name, email, password, cnpj):
    data = {'name': name, 'email': email, 'password': hashlib.sha224(password.encode('UTF-8')).hexdigest(),'type': 'PJ'}

    arquivo = open('users/' + email + '.json', 'w')

    arquivo.write(json.dumps(data))

    arquivo.close()


def getUser(email):
    arquivo = open('users/' + email + '.json', 'r')
    data    = json.load(arquivo)
    arquivo.close()

    data.pop('password', None)

    return data

def getUserP(email):
    arquivo = open('users/' + email + '.json', 'r')
    data    = json.load(arquivo)
    arquivo.close()

    if data['type']=='HS':
        data['name'] = getHospital(data['id'])['nome']

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
        return False, None

    user = getUserP(email)

    if hashlib.sha224(password.encode('UTF-8')).hexdigest()==user['password']:
        return True, user['name']

    return False, None

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

def isHospital(email):
    user = getUser(email)

    if user['type']=='HS':
        return True, user['id']

    return False, None

def addOrderInHospital(hID, oID):
    hosp = getHospital(hID)

    hosp['pedidos'].append(oID)

    arquivo = open('hosp/' + str(hID) + '.json', 'w')
    arquivo.write(json.dumps(hosp))
    arquivo.close()

def getOrderID():
    arquivo = open('orders/count', 'r')
    count   = int(arquivo.readline())
    arquivo.close()

    arquivo = open('orders/count', 'w')
    arquivo.write(str(count+1))
    arquivo.close()

    return count

def addOrder(hospID, order):
    orderID = getOrderID()

    data = {'id': orderID, 'hospitalID': hospID, 'doador': "", 'confirmada': False, 'titulo': order['titulo'], 'descricao': order['descricao']}

    arquivo = open('orders/' + str(orderID) + '.json', 'w')
    arquivo.write(json.dumps(data))
    arquivo.close()

    addOrderInHospital(hospID, orderID)
