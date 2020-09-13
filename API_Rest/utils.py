import time
from pytz import timezone
from datetime import datetime
# inicio as variavel
dic = {}
listaDuration = []
lista_timestamp = []

# reponsável por calcula a diferena entre data e retorna os segundo
def Diferenca_Em_Segundo(dt2, dt1):
    Diferenca = dt2 - dt1
    return Diferenca.days * 24 * 3600 + Diferenca.seconds

# metodo que recebe  os dados via post e retorna um dicionario contendo a duração e o timestamp
def Criar_lista_video(duracao, timestamp):
    global dic
    listaDuration.append(float(duracao))
    lista_timestamp.append(float(timestamp))

    dic = {"duration": listaDuration, "timestamp": lista_timestamp}

    return dic
# retorna os dados dos video dos ultimo 60 segundos
def Statistica():
    Timestamp_atual = datetime.fromtimestamp(time.time(), tz=timezone('America/Sao_Paulo'))
    resultado = {}
    global dic
    try:
        # loop em cada valor do dicionario com chave timestamp
        for a in dic['timestamp']:
            # converto o timestamp do dicionario e retorna como data para ser usada na funcao diferenca_Em_segundo
            Timestamp_para_data = datetime.fromtimestamp(a, tz=timezone('America/Sao_Paulo'))

            if Diferenca_Em_Segundo(Timestamp_atual, Timestamp_para_data) <= 60:
                try:
                    resultado = {
                        "sum": sum(dic['duration']),
                        'avg': sum(dic['duration']) / len(dic['duration']),
                        "max": max(dic['duration']),
                        "min": min(dic['duration']),
                        "count": len(dic['duration'])}

                except Exception:
                    pass

            else:
                resultado = {
                    "sum": 0,
                    'avg': 0,
                    "max": 0,
                    "min": 0,
                    "count": 0}
    except Exception:
        resultado = {
            "sum": 0,
            'avg': 0,
            "max": 0,
            "min": 0,
            "count": 0}



    return resultado

# limpa o dicionario.usado no classe api metodo delete.
def limpar():
    global dic
    for k in dic:
        dic[k].clear()


