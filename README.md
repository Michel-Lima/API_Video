
API Video

## Como rodar o projeto?

* Clone esse repositório.
* Crie um virtualenv com Python .
* Ative o virtualenv.
* Instale as dependências.
* Rode o servidor
```
git clone hhttps://github.com/Michel-Lima/API_Video.git
cd API_Video
python-m venv .venv
cd .venv/bin/activate
pip install -r requirements.txt
 
python manage.py runserver


Especificações
POST /videos
Body { "duration": 200.3, "timestamp": 1478192204000 }

Onde:
-Duration tempo de duração do vídeo

-Timestamp horário que o video foi adicionado. (UTC time zone)

Resposta
-Status 201 em caso de sucesso

-Status 204 caso o timestamp informado for mais antigo que 60 segundos.

DELETE /videos
Endpoint responsável por limpar a lista de todos videos inseridos.

Resposta
*204 - todos os vídeos removidos com sucesso.

GET /statistics
Este é o principal endpoint, ele retorna as estatísticas baseadas apenas nos últimos 60 segundos.

Resposta
{ "sum": 1000, "avg": 100, "max": 200, "min": 50, "count": 10 }
 
      
 
