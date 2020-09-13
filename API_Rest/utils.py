import weakref

from rest_framework import serializers

dic = {}
listaDuration = []
lista_timestamp = []


def Criar_lista_video(duracao, timestamp):
    global dic
    listaDuration.append(float(duracao))
    lista_timestamp.append(float(timestamp))

    dic = {"duration": listaDuration, "timestamp": lista_timestamp}

    return dic


def Statistica():
    global dic
    try:
        resultado = {
            "sum": sum(dic['duration']),
            'avg': sum(dic['duration']) / len(dic['duration']),
            "max": max(dic['duration']),
            "min": min(dic['duration']),
            "count": len(dic['duration'])}

    except KeyError:
        resultado = {
            "sum": 0,
            'avg': 0,
            "max": 0,
            "min": 0,
            "count": 0}

    return resultado


def limpar():
    global dic
    dic.clear()
