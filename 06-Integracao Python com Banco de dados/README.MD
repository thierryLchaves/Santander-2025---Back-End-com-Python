# Módulo 06: Integração Python com Banco de Dados
---

### Principais Aprendizados

-   Conceitos fundamentais de bancos de dados.
-   Características e diferenças entre os modelos **SQL** e **NoSQL**.
-   Introdução prática ao **MongoDB** como exemplo de banco de dados NoSQL.
-   Como usar a **Python Database API (DB-API)**, a interface padrão para acesso a bancos de dados relacionais em Python.
-   Gerenciamento de um ambiente de desenvolvimento com **Docker e Docker Compose**.

---
### Instruções para acompanhamento e replicação dos conteúdos aprendidos ###

Para realizar os exercícios de integração com banco de dados relacional, é necessário iniciar o container do SQL Server.

1.  **Pré-requisitos:** Garanta que o [Docker](https://www.docker.com/products/docker-desktop/) esteja instalado e em execução na sua máquina.

2.  **Inicie o Banco de Dados:**
    Navegue até a pasta de configuração do Docker e execute o comando para subir o serviço em segundo plano.
    Importante adicionar o arquivo `.env`com as devidas configurações

    ```bash
    # A partir da pasta '06-Integracao-Python-com-Banco-de-dados'
    cd Docker-sql-server/
    docker-compose up -d
    ```

3.  **Confirmação:** Após alguns instantes, o SQL Server estará rodando e pronto para receber conexões da sua aplicação Python.

4.  **Para Desligar:**
    Quando não estiver mais usando, lembre-se de desligar o container para liberar recursos da sua máquina.
    ```bash
    # Dentro da pasta 'Docker-sql-server'
    docker-compose down
    ```

---

###  Estrutura do Módulo

Abaixo está a descrição de cada pasta deste módulo. **As anotações detalhadas de cada tópico estão no arquivo Markdown dentro da respectiva pasta.**

-   `01-Introducao-Banco-de-Dados/`
    > Anotações sobre os conceitos básicos e a importância dos sistemas de gerenciamento de bancos de dados (SGBDs).

-   `02-Introducao-Banco-de-Dados-Relacional-(SQL)/`
    > Estudo do modelo relacional, da linguagem SQL e de seus principais comandos.

-   `03-Introducao-ao-MongoDB-e-Banco-de-dados-NoSQL/`
    > Exploração do modelo não relacional, com foco nas características e casos de uso do MongoDB.

-   `04-Explorando-Banco-de-dados-relacionais-com-Python-DB-API/`
    > Exercícios práticos de conexão, consulta e manipulação de dados em um banco SQL usando código Python.

-   `Docker-sql-server/`
    > **Pasta de infraestrutura.** Contém todos os arquivos (`Dockerfile`, `docker-compose.yml`) para criar o ambiente do SQL Server necessário para a aula 04.

---

<table style="text-align: center; width: 100%;"> 
<caption><b>Skils do projeto </b></caption>
<tr>
    <td style="text-align: center;">
    <img alt="Markdown" src="https://img.shields.io/badge/markdown-%23000000.svg?style=for-the-badge&logo=markdown&logoColor=white"/>
    </td>
    <td style="text-align: center;">
    <img alt="Python" src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54"/>
    </td>
    <td style="text-align: center;">
    <img alt="VSCode" src="https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white"/>
    </td>
<tr> 
<tr>
    <td style="text-align: center;">
    <img alt="Docker" src="https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white"/>
    </td>
    <td style="text-align: center;">
    <img alt="MongoDB" src="https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white"/>
    </td>
    <td style="text-align: center;">
    <img alt="Microsoft SQL Server" src="https://img.shields.io/badge/Microsoft%20SQL%20Server-CC2927?style=for-the-badge&logo=microsoft%20sql%20server&logoColor=white"/>    
    </td>
<tr>

</table>
