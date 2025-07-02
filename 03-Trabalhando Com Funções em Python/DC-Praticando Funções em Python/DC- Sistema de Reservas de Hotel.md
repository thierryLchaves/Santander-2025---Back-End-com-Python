# Organizador de Eventos

## Princípios Básicos 
__Descrição__   
Uma pousada deseja automatizar seu sistema de reservas. Crie uma função que receba uma lista de quartos disponíveis e uma lista de reservas solicitadas. A função deve verificar quais reservas podem ser aceitas e quais devem ser recusadas por falta de disponibilidade.

__Entrada__  
- Uma lista contendo os números dos quartos disponíveis.
- Uma lista contendo os números dos quartos solicitados pelos clientes.

__Saída__  
- Uma mensagem informando quais reservas foram confirmadas e quais foram recusadas.

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
        101 102 103 104 </br>
        102 105 101 103
    </td>
    <td style="text-align: center;">
       Reservas confirmadas: 102 101 103 </br>
       Reservas recusadas: 105
    </td>
<tr> 
<tr> 
    <td style="text-align: center;">
        201 202 203 204 205 </br>
        205 202 208 201 203
    </td>
    <td style="text-align: center;">
        Reservas confirmadas: 205 202 201 203 </br>
        Reservas recusadas: 208
    </td>
<tr> 
<tr> 
    <td style="text-align: center;">
        10 20 30 40 50 </br>
        25 30 10 40 50 60
    </td>
    <td style="text-align: center;">
        Reservas confirmadas: 30 10 40 50 </br>
        Reservas recusadas: 25 60
    </td>
<tr> 
</table>

__Atenção:__  É extremamente importante que as entradas e saídas sejam exatamente iguais às descritas na descrição do desafio de código.

[Código](DC-%20Sistema%20de%20Reservas%20de%20Hotel.py)