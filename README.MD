# Notações gerais 

Neste repositório será adotada toda documentação em Markdown, sendo assim seguirei algumas diretrizes e comportamentos padrões

## Diretrizes
- ### 1. Do repositório
    O repositório está estruturado em pastas, onde cada uma das aulas acessadas/aprendidas, estão em suas respectiva pasta. 
- ### 2. Do documento 
    O documento contendo a estrutura geral da aula será em formato `.Md(Markdown)`, e seguira a premissa de CamelCase em seu nome.  
    - #### 2.1. Das pastas
         As pasta com os nomes da Matérias serão iguais as apresentadas no curso, porém sem acentuação 
    - #### 2.2. Do Readme
        Ao ser concluída uma nova aula deverá ser preenchido o [Check Box de conclusão](#3-lista-de-conclusão-de-aulas) informando que a aulas foi realizada.
    - ### 2.3.  Estrutura padrão de sub-diretório
        Em toda pasta deverão conter no mínimo **3**(três) outros sub-diretórios  
        - #### 2.3.1. Diretório de Imagens
            `**Diretório de Imagens**`: Este diretório sempre será nomeado de `imgs`, e nele será armazenado os prints utilizados no documento.   
        - #### 2.3.2. Diretório de Códigos
            `**Diretório de código**`:  Este diretório sempre será nomeado de `src`, neste diretório será armazenado os exemplos de códigos feitos nas aulas e seguira a recomendação as boas práticas de  nomeação (sem upper case, com _ entre os nomes, e descrição curta do objetivo do código) 
        - #### 2.3.3. Diretório de Dados
            `**Diretório de dados*`: Este diretório sempre será nomeado de `db`, e nele será armazenado os dados complementares a serem usados (arquivos pdf etc..)  
### 2.4 Estrutura de rodapé
    Em todo arquivo deverá conter em seu rodapé a seguinte estrutura 
   ```
    <table style="text-align: center; width: 100%;"> 
    <caption><b>Skls do projeto </b></caption>
    <tr>
        <td style="text-align: center;">
        <img alt="Skil utilizada" src="buscar estilo em: https://github.com/Ileriayo/markdown-badges"/>
        </td>
    </tr>
    <tr> 
       <td style="text-align: center; width: 100%;">
       <b>Metadados</b>
       </td>
    </tr>
    </table>
    ---
    titulo: "Nome do documentos"
    autor: "Thierry Lucas Chaves"
    data_criacao: "DD-MM-AAAA"
    data_modificacao: "DD-MM-AAAA"
    versao: "1.0"
    ---
```

### 3. Lista de conclusão de aulas
- [X] <b> [Operadores e manipulação de String com Python](01-Operadores%20e%20manipulação%20de%20String%20com%20Python/) </b>
    - [X] Tipos de Operadores com Python 
    - [X] Estrutura condicionais e de repetição em Python 
    - [X] Manipulando Strings com Python 
    - [X] Criando um Sistema Bancário com Python 
    - [X] Desafios de código: Aperfeiçoe sua lógica e Pensamento computacional 
    - [X] Desafio de Código: Explorando Operadores e Manipulação de Strings

- [X] <b>Estruturas de Dados e Lista com Python</b>
    - [X] Trabalhando com Listas em Python 
    - [X] Conhecendo tuplas em Python 
    - [X] Explorando conjuntos em Python 
    - [X] Aprendendo a utilizar Dicionários em Python 
    - [X] Desafio de Código: Aplicando Estruturas de dados e Listas
  
- [X] <b>Trabalhando com Funções em Python </b>
    - [x] Dominando Funções Python 
    - [X] Otimizando Sistema Bancário com funções Python 
    - [x] Desafio de Código: Praticando funções em Python

- [X] <b>Orientação a Objetos e Boas Práticas em Python </b>
    - [X] Introdução à Programação Orientada a Objetos (POO) com Python
    - [X] Aprendendo o Conceito de Herança com Python
    - [X] Aplicando Encapsulamento em Python
    - [X] Conhecendo Polimorfismo em Python
    - [X] Interfaces e Classes Abstratas com Python
    - [X] Modelando o Sistema Bancário em POO com Python 

- [ ] <b>Trabalhando com Pacotes Python </b>
    - [X] Decoradores, Iteradores e Geradores com Python
    - [X] Lidando com Data, Hora e Fuso Horário em Python 
    - [X] Manipulando Arquivos em Python
    - [ ] Gerenciamento de Pacotes, Convenções e Boas Práticas Python
    - [ ] Desafio de Código: Praticando Desenvolvimento em Python

- [ ] <b>Integração Python com Banco de Dados </b>
    - [ ] Introdução Banco de Dados
    - [ ] Introdução a Banco de Dados Relacionais (SQL)
    - [ ] Introdução ao MongoDB e Banco de Dados NoSQL
    - [ ] Explorando Banco de Dados Relacionais com Python DB API

- [ ] <b>Desenvolvimento Orientado a Teste com Python </b>
    - [ ] Introdução a Aplicação Rest
    - [ ] Desenvolvimento sua primeira API com FastAPI, Python e Docker
    - [ ] Criando uma API com FastAPI Utilizando TDD
    


## Observações:
Para esse projeto foi criado o [arquivo de automação](automacao_estrutura_pasta/cria_lista.py), para facilitar a criação dos arquivos de notações que serão adotados nas aulas, bem como a estrutura padrão mencionada em [Estruturas de diretórios](#23--estrutura-padrão-de-sub-diretório) seguindo o mesmo padrão
ao executar o código o usuário deverá inserir os caminho absolutos da pasta que corresponde ao módulo caso necessário modificar o arquivo de [template](automacao_estrutura_pasta/template_padrao.md)

<table style="text-align: center; width: 100%;"> 
<caption><b>Skils do projeto </b></caption>
<tr>
    <td style="text-align: center;">
    <img alt="Markdown" src="https://img.shields.io/badge/markdown-%23000000.svg?style=for-the-badge&logo=markdown&logoColor=white"/>
    </td>
<tr> 
</table>

---
<table style="text-align: center; width: 100%;"> 
    <caption><b>Skils do projeto </b></caption>
    <tr>
        <td style="text-align: center;">
        <img alt="Markdown" src="[https://img.shields.io/badge/markdown-%23000000.svg?style=for-the-badge&logo=markdown&logoColor=white](https://img.shields.io/badge/markdown-%23000000.svg?style=for-the-badge&logo=markdown&logoColor=white)"/>
        </td>
    </tr>
</table>

<div style="font-family: monospace; border-top: 1px solid #ddd; border-bottom: 1px solid #ddd; padding: 10px; margin-top:20px; margin-bottom: 20px;">
  <p><strong>titulo:</strong> "Nome do Documento"</p>
  <p><strong>autor:</strong> "Thierry Lucas Chaves"</p>
  <p><strong>data_criacao:</strong> <time id="data-criacao-html">...</time></p>
  <p><strong>data_modificacao:</strong> <time id="data-modificacao-html">...</time></p>
  <p><strong>versao:</strong> "1.0"</p>
</div>

<script>
  function formatarData(data) {
    const dia = String(data.getDate()).padStart(2, '0');
    const mes = String(data.getMonth() + 1).padStart(2, '0');
    const ano = data.getFullYear();
    return `${dia}-${mes}-${ano}`;
  }

  // Pega a data e hora atuais
  const agora = new Date();
  const dataFormatada = formatarData(agora);

  // --- LÓGICA PARA DATA DE MODIFICAÇÃO (Automático) ---
  const elementoModificacao = document.getElementById('data-modificacao-html');
  if (elementoModificacao) {
    elementoModificacao.textContent = `"${dataFormatada}"`;
    elementoModificacao.setAttribute('datetime', agora.toISOString());
  }
  
  // --- LÓGICA PARA DATA DE CRIAÇÃO (Manual) ---
  // IMPORTANTE: Defina a data de criação do seu arquivo aqui!
  const dataCriacaoFixa = "18-07-2025"; 
  
  const elementoCriacao = document.getElementById('data-criacao-html');
  if (elementoCriacao) {
    elementoCriacao.textContent = `"${dataCriacaoFixa}"`;
    elementoCriacao.setAttribute('datetime', '2025-07-18'); // Formato AAAA-MM-DD
  }
</script>
---