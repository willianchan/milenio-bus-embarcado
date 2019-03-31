from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from pathlib import Path

url_API = "http://www.google.com/"
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
        if file_path.is_file() and True:#check_server_connection(url_API)
                # faz request




                # deleta arquivo se tudo der certo
                file_path.unlink()
                # aumenta contador
                contador += 1
        else:
            contador = 0

    except:
        print("Erro causou fechamento do programa")
        break
