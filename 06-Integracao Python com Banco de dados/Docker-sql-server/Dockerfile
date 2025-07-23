# Use a imagem oficial do SQL Server 2022
FROM mcr.microsoft.com/mssql/server:2022-latest

# Aceite o Contrato de Licença de Usuário Final (EULA)
ENV ACCEPT_EULA=Y

# Exponha a porta padrão do SQL Server
EXPOSE 1433

# Comando para iniciar o SQL Server quando o contêiner for executado
CMD [ "/opt/mssql/bin/sqlservr" ]