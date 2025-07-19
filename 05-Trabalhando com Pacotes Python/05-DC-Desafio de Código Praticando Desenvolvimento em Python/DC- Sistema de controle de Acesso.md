# DC- Sistema de controle de Acesso

## Princípios Básicos 
__Descrição__   
Uma empresa deseja criar um sistema simples de login para permitir acesso de funcionários. O sistema precisa verificar se o usuário está cadastrado e a senha informada está correta. 

__Entrada__  
O programa recebe **duas linhas** de entrada.  
- **Primeira linha:** Nome do usuário cadastrado.  
- **Segunda linha:**  Senha correspondente ao usuário.  

__Saída__  
- **"Acesso permitido"** se as credencias estiverem corretas. 
- **"Usuário ou senha incorretos"** caso contrário.

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
        joao </br>
        1234
    </td>
    <td style="text-align: center;">
       Acesso permitido
    </td>
<tr> 
<tr> 
    <td style="text-align: center;">
        maria </br>
        senha123 
    </td>
    <td style="text-align: center;">
        Acesso permitido
    </td>
<tr> 
<tr> 
    <td style="text-align: center;">
        ana </br>
        1234
    </td>
    <td style="text-align: center;">
       Usuário ou senha incorretos
    </td>
<tr> 
</table>

__Atenção:__  É extremamente importante que as entradas e saídas sejam exatamente iguais às descritas na descrição do desafio de código.

[Código](DC-%20Sistema%20de%20controle%20de%20Acesso.py)