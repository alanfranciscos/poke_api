
python3.11

### Instale o virtualEnv

```bash:
  python3.11 -m venv venv
```

### Ative o virtualEnv

windows:

```bash:
  .\venv\Scripts\activate
```

linux:

```bash:
  source venv/bin/activate
```

### Instale as dependências

```bash:
pip install -r requirements.txt
```

1. Considere a query a seguir e responda. É um SQL funcional ou possui algum erro? Caso possua algum erro, comente e corrija.

- file = quey.sql

2. Conecte-se à PokeAPI através da biblioteca pokebase, e retorne em um gráfico de barras, os dados de tipo dominante dos 100 primeiros pokémons disponíveis, de forma a agrupá-los e mostrá-los em ordem decrescente.
  
- file = pokemons_chart.py

3. Ainda usando a PokeAPI, crie e retorne um dataframe com os dados dos 50 primeiros pokémons, incluindo, nome, peso, altura e tipo.
  
- file = data_frame_pokemons.py

4. transform_flask_to_fast_api

- rode o comando no terminal:

```bash
uvicorn transform_flask_to_fast_api:app --reload
````
