import time
from datetime import datetime

from django.shortcuts import render
from pytz import timezone
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .utils import Criar_lista_video, Statistica, limpar, Diferenca_Em_Segundo


def Pagina_inicial(request):
    return render(request, 'index.html')


# classe Responsável por retorna as statistica dos videos
class Video_statistics(APIView):

    def get(self, request):
        retorno = Statistica()
        try:
            return Response(retorno, status=status.HTTP_200_OK

            )
        except ZeroDivisionError:
            return Response(status=status.HTTP_204_NO_CONTENT)


# classe reponsável pelo metodo post e delete dos videos
class VideoViewSet(APIView):

    def delete(self, request):
        # chama o metodo da classe
        limpar()

        return Response(status=status.HTTP_204_NO_CONTENT)

    def post(self, request):

        try:
            # captura os dados enviado via post e atribuir em uma variavel
            get_arg1 = request.data['duration']
            get_arg2 = request.data['timestamp']
            # Data baseada no timestamp atual
            Timestamp_atual = datetime.fromtimestamp(time.time(), tz=timezone('America/Sao_Paulo'))
            # data baseada no timestamp passada via post
            Timesptamp_get = datetime.fromtimestamp(float(get_arg2),
                                                    tz=timezone('America/Sao_Paulo'))

            # valido se o timestamp é menor que 60 segundo

            try:
                if Diferenca_Em_Segundo(Timestamp_atual, Timesptamp_get) <= 60:
                    # se for menor então chamado funcao criar_lista de video

                    Criar_lista_video(
                        get_arg1, get_arg2

                    )

                    # caso o o timestamp seja menor que 60 segundo retorna o status 201
                    return Response(request.data, status=status.HTTP_201_CREATED)
            except:
                return Response(
                    status=status.HTTP_204_NO_CONTENT)

            else:
                # caso o o timestamp seja maior que 60 segundo retorna o status 204
                return Response(
                    status=status.HTTP_204_NO_CONTENT)
        except Exception:

            return Response(
                status=status.HTTP_204_NO_CONTENT)
