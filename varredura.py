from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from pathlib import Path
import json
import requests

url_API = "http://localhost:3000/milenio-bus-api/"
contador = 0


def check_server_connection(url):
    try:
        urlopen(url, timeout=1)
        return True
    except (HTTPError, URLError) as err:
        print(err)
        return False


while True:
    try:
        file_path = Path("json/registro-{}.json".format(contador))

        if file_path.is_file() and check_server_connection(url_API):

            with file_path.open() as json_file:
                data = json.load(json_file)

            r = requests.post(url_API + "registro/", json=data)

            if r.status_code == 201:
                file_path.unlink()
                contador += 1
        else:
            contador = 0

    except:
        print("Erro causou fechamento do programa")
        break
