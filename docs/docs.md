


# Healthcheck Flask

- links: https://github.com/Runscope/healthcheck

A biblioteca healthcheck é feita para facilitar a criação de rotas de healthcheck em aplicações Flask, as dependências adicionadas ao `requirements.txt` são:

```
healthcheck
six
```

Para utilizar a biblioteca vamos partir de uma aplicação Flask simples como exemplo:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
```

A bibliotteca expõe uma classe `HealthCheck` que é responsável por criar a rota de healthcheck e executar as funções de checagem que forem desenvolvidas para checar a saúde da aplicação

```python
from flask import Flask
from healthcheck import HealthCheck

app = Flask(__name__)
health = HealthCheck(app, "/healthcheck")

@app.route('/')
def hello_world():
    return 'Hello, World!'

def test_sum():
  if 1 + 2 == 3:
    return True, "3"

def test_sum2():
  if 2 + 2 == 4:
    return True, "4"

health.add_check(test_sum)
health.add_check(test_sum2)

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
```

A classe espera que cada função de checagem retorne uma tupla contendo o resultado (True ou False) do teste e um output ou log sobre o resultado. Os resultados são apresentados em forma de json, com status 500 em caso de falha e status 200 caso haja sucesso.

![resultado teste]('./resultado.png')