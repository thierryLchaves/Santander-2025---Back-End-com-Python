# DC-Sistema de Atendimento Médico

## Princípios Básicos 
__Descrição__   
Uma clínica médica quer automatizar seu sistema de atendimento. Crie uma função que organize os pacientes em ordem de prioridade com base na idade e na urgência do caso.

📌 Critérios de Prioridade:

Pacientes acima de 60 anos têm prioridade.
Pacientes que apresentam a palavra "urgente" na ficha têm prioridade máxima.
Os demais pacientes são atendidos por ordem de chegada.

__Entrada__  
- Um número inteiro n, representando a quantidade de pacientes.
- n linhas seguintes, cada uma contendo os dados de um paciente no formato: nome, idade, status
- nome: string representando o nome do paciente.
- idade: número inteiro representando a idade do paciente.
- status: string que pode ser "urgente" ou "normal".


__Saída__  
- A saída deve exibir a lista dos pacientes ordenada de acordo com as regras de prioridade, no formato: Ordem de Atendimento: nome1, nome2, nome3, ...

__Exemplos__  
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

<table style="text-align: center; width: 100%;"> 
<caption><b>Exemplos de Saída & Entrada </b></caption>
<tr> 
    <td style="text-align: center;">
        Entrada
    </td>
     <td style="text-align: center;">
        Saída
    </td>
<tr> 
<tr> 
    <td style="text-align: center;">
        3 </br>
        Carlos, 40, normal </br>
        Ana, 70, normal </br>
        Bruno, 30, urgente
    </td>
    <td style="text-align: center;">
        Ordem de Atendimento: Bruno, Ana, Carlos
    </td>
<tr> 
<tr> 
    <td style="text-align: center;">
        4 </br>
        Paula, 30, normal </br>
        Ricardo, 60, normal </br>
        Tiago, 60, urgente </br>
        Amanda, 50, urgente
    </td>
    <td style="text-align: center;">
        Ordem de Atendimento: Tiago, Amanda, Ricardo, Paula
    </td>
<tr> 
<tr> 
    <td style="text-align: center;">
        5 </br>
        João, 65, normal </br>
        Maria, 80, urgente </br>
        Lucas, 50, normal </br>
        Fernanda, 25, normal </br>
        Pedro, 90, urgente
    </td>
    <td style="text-align: center;">
        Ordem de Atendimento: Pedro, Maria, João, Lucas, Fernanda
    </td>
<tr> 
</table>

__Atenção:__  É extremamente importante que as entradas e saídas sejam exatamente iguais às descritas na descrição do desafio de código.

[Código](DC-Sistema%20de%20Atendimendo%20Médico.py)