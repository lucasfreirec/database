# Sistema de Gerenciamento de Clínicas Veterinárias

![Python](https://img.shields.io/badge/Python-3.11-blue.svg) ![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green.svg) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-blue.svg) ![Docker](https://img.shields.io/badge/Docker-20.10+-blue.svg)

## 1. Descrição do Projeto

Este projeto consiste em um sistema completo para gerenciar atendimentos em uma rede de clínicas veterinárias. A aplicação foi desenvolvida com uma API RESTful utilizando FastAPI, o ORM SQLAlchemy para interação com o banco de dados PostgreSQL e está totalmente containerizada com Docker para garantir um ambiente de desenvolvimento e execução padronizado e de fácil configuração.

O sistema permite:
* Cadastrar clínicas e seus respectivos veterinários.
* Cadastrar tutores de animais e seus pets.
* Registrar atendimentos realizados pelos veterinários aos pets.

O foco do projeto é a aplicação de boas práticas de modelagem de dados, organização de código em camadas (Modelos, Repositórios, Serviços e API) e desenvolvimento de API.

## 2. Arquitetura do Projeto

O projeto foi estruturado em uma arquitetura de camadas para promover a separação de responsabilidades e a manutenibilidade do código:

* **`models/`**: Contém as classes de mapeamento Objeto-Relacional (ORM) do SQLAlchemy, que definem a estrutura das tabelas no banco de dados.
* **`repositories/`**: Isola a lógica de acesso a dados. É a única camada que interage diretamente com os modelos ORM para realizar operações no banco (CRUD).
* **`services/`**: Orquestra a lógica de negócio da aplicação, utilizando os repositórios para manipular os dados e aplicando as regras de negócio necessárias.
* **`api/`**: Expõe a funcionalidade da aplicação através de endpoints RESTful, lidando com as requisições HTTP, validação de dados (com Pydantic) e formatação das respostas.
* **`schemas/`**: Contém os modelos Pydantic, que definem os "contratos" de dados para as requisições e respostas da API, garantindo a validação e a serialização dos dados.

## 3. Endpoints da API

A API expõe os seguintes endpoints principais para interação com o sistema:

#### Clínicas
* `POST /clinicas`: Cadastra uma nova clínica.
* `GET /clinicas`: Lista todas as clínicas cadastradas.
* `GET /clinicas/{id}`: Busca uma clínica específica pelo seu ID.
* `GET /clinicas/{id}/veterinarios`: Lista todos os veterinários de uma clínica específica.

#### Veterinários
* `POST /veterinarios`: Cadastra um novo veterinário.
* `GET /veterinarios`: Lista todos os veterinários.
* `GET /veterinarios/{id}/atendimentos`: Lista os atendimentos de um veterinário específico.

#### Tutores
* `POST /tutores`: Cadastra um novo tutor.
* `GET /tutores/{id}/pets`: Lista os pets de um tutor específico.

#### Pets
* `POST /pets`: Cadastra um novo pet.
* `GET /pets`: Lista todos os pets.
* `GET /pets/{id}/atendimentos`: Lista os atendimentos de um pet específico.

#### Atendimentos
* `POST /atendimentos`: Cria um novo registro de atendimento.
* `GET /atendimentos`: Lista todos os atendimentos.

---

## 4. Como Executar com Docker (Recomendado)

O projeto é totalmente containerizado, então a única dependência real na sua máquina é o Docker.

### Pré-requisitos
* **Docker & Docker Compose:** Garanta que você tenha o Docker Desktop (Windows/macOS) ou o Docker Engine com o plugin Compose (Linux) instalado.

### Guia de Execução

**1. Clone o Repositório**
```bash
git clone <URL_DO_SEU_REPOSITORIO_NO_GITHUB>
cd <NOME_DA_PASTA_DO_PROJETO>
```

**2. Inicie o Banco de Dados em Background**

Este comando irá construir as imagens (se necessário) e iniciar o contêiner do PostgreSQL em modo "detached" (`-d`).
```bash
docker compose up -d --build db
```
*Na primeira vez, este comando também executará o `schema.sql` para criar toda a estrutura do banco de dados automaticamente.*

**3. Execute a Aplicação**

Com o banco de dados rodando, execute a aplicação FastAPI. Este comando conecta seu terminal à aplicação, permitindo a visualização dos logs em tempo real.
```bash
docker compose up --build app
```

Após a inicialização, a API estará disponível em `http://localhost:8000`.

**4. Acesse a Documentação Interativa**

Abra seu navegador e acesse a seguinte URL para ver a documentação interativa do Swagger UI, onde você pode testar todos os endpoints:
[**http://localhost:8000/docs**](http://localhost:8000/docs)

### 5. Teste Automatizado via Script

Para verificar rapidamente se todos os endpoints principais estão funcionando, você pode usar o script de teste `demo.sh`.

**a. Dê permissão de execução ao script (apenas na primeira vez):**
```bash
chmod +x demo.sh
```
**b. Execute o script (em um novo terminal, com a API rodando):**
```bash
./demo.sh
```
O script simulará um fluxo completo de cadastro e consulta, exibindo os resultados no terminal.

### 6. Encerrar o Ambiente
Quando terminar, para parar e remover todos os contêineres e a rede criada, execute:
```bash
docker compose down
```
Se quiser apagar também os dados do banco de dados para um "reset" completo, use a flag `-v`:
```bash
docker compose down -v
```
---

## 7. Estrutura de Arquivos
```
/veterinaria
├── api/
│   ├── __init__.py
│   ├── atendimento_router.py
│   ├── clinica_router.py
│   ├── pet_router.py
│   ├── tutor_router.py
│   └── veterinario_router.py
├── models/
│   ├── __init__.py
│