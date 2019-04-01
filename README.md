# Sistema de varredura de arquivos JSON

Realiza a varredura contante da pasta `/json` em busca de arquivos de registro, posteriormente realiza requisição para a API com os dados do arquivo.

## Instalação

Use o gerenciador de pacotes [pip](https://pip.pypa.io/en/stable/) para instalar pacotes

```bash
$ git clone https://github.com/willianchan/milenio-bus-embarcado.git
$ cd milenio-bus-embarcado
$ pip install requests
$ pip install pathlib
```

## Uso

```python
$ python varredura.py
```

## Teste

Para fins de teste, cole um arquivo nomeado `registro*.json` dentro da pasta `/json` com seguinte estrutura:

```
{
    "id_transporte": 1,
    "porta": [
        {
            "id": 1,
            "entrada": 4,
            "saida": 3
        },
        {
            "id": 2,
            "entrada": 1,
            "saida": 2
        },
        {
            "id": 3,
            "entrada": 8,
            "saida": 5
        }
    ]
}
```

*qualquer nome de arquivo iniciado com "registro" e finalizado com ".json" será aceito pelo script

Exemplo: registro-7.json
