# Validador de Formato de E-mails

## Princípios Básicos 
__Descrição__   
Uma empresa quer validar se os e-mails cadastrados pelos usuários estão no formato correto. Crie uma função que receba um e-mail e verifique se ele é válido, seguindo as regras:

📌 Regras para um e-mail válido:

Deve conter o caractere "@" e um domínio, como gmail.com ou outlook.com.
Não pode começar ou terminar com "@".
Não pode conter espaços.  

__Entrada__  
- Uma string contendo o e-mail a ser validado.  

__Saída__  
- "E-mail válido" se o e-mail estiver no formato correto.
- "E-mail inválido" caso contrário.  

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
        usuario@gmail.com	
    </td>
    <td style="text-align: center;">
        E-mail válido
    </td>
<tr> 
<tr> 
    <td style="text-align: center;">
        user@outlook.com	
    </td>
    <td style="text-align: center;">
        E-mail válido
    </td>
<tr> 
<tr> 
    <td style="text-align: center;">
        usuario gmail.com	
    </td>
    <td style="text-align: center;">
        E-mail inválido
    </td>
<tr> 
</table>

__Atenção:__  É extremamente importante que as entradas e saídas sejam exatamente iguais às descritas na descrição do desafio de código.