# Readme.md

# API - Vacinação

Api com rotas básicas para registrar e armazenar os cartões de vacinação.

# Url base \*\*\*

O url base dessa API será executada em **https://entrega-19-vagner-fabricio.herokuapp.com**

# Endpoints

O projeto consiste em 2 endPoints:

**`POST /vaccinations`** Para cadastrar uma nova vacina

**`GET /vaccinations`** Retorna as informações das vacinas

**\*Nenhuma das rotas exigem autenticação**

## Cadastro

Os cadastros de novas vacinas deverão ser feitos no seguinte endpoin:

```python
POST /vacctinations
```

Para o cadastro de vacinas, obrigatoriamente os seguintes campos deverão ser informados: cpf, name, vaccine_name e health_unit_name.

A requisição deverá seguir o seguinte formato:

```json
{
  "cpf": "01234567891",
  "name": "Chrystian",
  "vaccine_name": "Pfizer",
  "health_unit_name": "Santa Rita"
}
```

**Regras**:

- `cpf`: Deve conter **11 caracteres numéricos** e ser único.

Exemplos de respostas:

- **Status: 201 CREATED:** em caso de sucesso com a seguinte mensagem contendo os dados da vacina:
  ```json
  {
    "cpf": "01234567891",
    "name": "Chrystian",
    "first_shot_date": "Fri, 29 Oct 2021 16:36:13 GMT",
    "second_shot_date": "Thu, 27 Jan 2022 16:36:13 GMT",
    "vaccine_name": "Pfizer",
    "health_unit_name": "Santa Rita"
  }
  ```
- **Status: 401 CONFLICT**: caso o cpf cadastrado já exista na base de dados:
  ```json
  {
    "error": "cpf = 01234567891  already exists."
  }
  ```
- **Status: 400 BAD REQUEST:** Caso não tenha sido informado algum dos campos obrigatórios, informando qual campo está faltando.
  ```json
  {
    "error": "missing 3 required positional arguments: 'cpf', 'name', and 'vaccine_name'"
  }
  ```

## Listar todas as vacinas cadastradas

Para obter uma lista de todas as vacinas cadastradas, deve-se utilizar o seguinte endpoint:

```python
GET /vacctinations
```

- Não é necessário nenhuma informação no corpo da mensagem.

### Modelo de resposta:

- **Status: 200 OK : Retornando uma lista de todas as vacinas cadastradas no banco de dados.**

  ```json
  [
    {
      "cpf": "01234567891",
      "name": "Chrystian",
      "first_shot_date": "Fri, 29 Oct 2021 16:30:31 GMT",
      "second_shot_date": "Thu, 27 Jan 2022 16:30:31 GMT",
      "vaccine_name": "Pfizer",
      "health_unit_name": "Santa Rita"
    },
    {
      "cpf": "19876543210",
      "name": "Cauan",
      "first_shot_date": "Fri, 29 Oct 2021 16:31:30 GMT",
      "second_shot_date": "Thu, 27 Jan 2022 16:31:30 GMT",
      "vaccine_name": "Coronavac",
      "health_unit_name": "Santa Rita"
    },
    {
      "cpf": "54221194161",
      "name": "Eduardo",
      "first_shot_date": "Fri, 29 Oct 2021 16:35:24 GMT",
      "second_shot_date": "Thu, 27 Jan 2022 16:35:24 GMT",
      "vaccine_name": "Coronavac",
      "health_unit_name": "Santa Rita"
    }
  ]
  ```

- **Status: 200 OK : Retornando uma lista de todas as vacinas cadastradas no banco de dados.**
  ```json
  []
  ```
  Se nenhuma vacina estiver cadastrada no banco de dados uma lista vazia é retornada...
