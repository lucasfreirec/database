# Sistema de Gerenciamento de Biblioteca

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-blue.svg)
![Docker](https://img.shields.io/badge/Docker-20.10+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## Descrição do Projeto

Aplicação de console (CLI) para gerenciar um sistema de biblioteca, desenvolvida como parte da disciplina de Banco de Dados. O sistema permite realizar operações CRUD (Criar, Ler, Atualizar, Deletar) para alunos, livros e exemplares, além de gerenciar o processo de empréstimos e devoluções.

O projeto é **totalmente containerizado com Docker**, o que garante um ambiente de desenvolvimento e execução padronizado, simples e consistente em qualquer sistema operacional (Linux, Windows ou macOS).

## Tecnologias Utilizadas

* **Linguagem:** Python 3.11
* **Banco de Dados:** PostgreSQL 15
* **ORM:** SQLAlchemy
* **Driver PostgreSQL:** psycopg2
* **Containerização:** Docker & Docker Compose

---

## Pré-requisitos

Antes de começar, garanta que você tem o seguinte software instalado em sua máquina:

* **Docker Desktop** (para Windows e macOS) ou **Docker Engine** com o plugin **Compose** (para Linux).
    * [Instalar Docker no Windows/macOS](https://www.docker.com/products/docker-desktop/)
    * [Instalar Docker no Ubuntu](https://docs.docker.com/engine/install/ubuntu/)

---

## Como Executar o Projeto com Docker

O processo é dividido em duas etapas principais: iniciar o banco de dados em segundo plano e, em seguida, executar a aplicação interativa.

### Passo 1: Clonar o Repositório
```bash
git clone <URL_DO_SEU_REPOSITORIO_NO_GITHUB>
cd <NOME_DA_PASTA_DO_PROJETO>
```

### Passo 2: Iniciar o Banco de Dados
Este comando irá construir as imagens, se necessário, e iniciar o contêiner do PostgreSQL em segundo plano (`-d`).

```bash
docker compose up -d --build db
```
*Na primeira vez, este comando também executará o `schema.sql` para criar todas as tabelas.*

### Passo 3: Executar a Aplicação Interativa
Agora, com o banco de dados rodando, execute a aplicação. Este comando irá conectar seu terminal ao programa.

```bash
docker compose run --rm app
```
* `run app`: Inicia um novo contêiner para o serviço `app`.
* `--rm`: Remove o contêiner da aplicação automaticamente quando você sair do menu, mantendo o ambiente limpo.

O menu interativo da aplicação aparecerá e você poderá testar todas as funcionalidades.

### Passo 4: Encerrar o Ambiente
Quando terminar de usar a aplicação, você precisa parar o contêiner do banco de dados que ficou rodando em segundo plano.

```bash
docker compose down
```
Se quiser apagar também os dados do banco de dados (o volume `postgres_data`), use a flag `-v`:
```bash
docker compose down -v
```