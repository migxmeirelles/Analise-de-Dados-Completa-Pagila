### Objetivo do Projeto:
Conectar Python a banco de dados, extrair dados e criar análises.
### Contexto:
Pagila é um banco de dados que pode ser baixado online, e extraído para dentro do PostgreSQL via comandos CMD.
Pagila contem diversas tabelas que simulam uma locadora de filmes.
### Código:
Postegre:
* baixamos o banco de dados Pagila e adicionamos ao postegre via comandos cmd.
* criamos uma query simples para obter informações legais para análise.
![image](https://github.com/user-attachments/assets/0b4cc8ca-bb3d-4825-92d4-cbaae1aacf8f)
query pode ser vista completa no arquivo ''query_postgre.sql" ou no arquivo .py

Python:
* começamos importando as bibliotecas necessárias.
* passamos as informações para conexão como servidor, usuário e senha (senha ocultado por motivos lógicos).
* passamos a query do postegre.
* salvamos esse resultado em um dataframe do pandas, não sendo necessário criar transformações.
* acabei criando um segundo dataframe chamado "df_apenas_alugados" para realizar a análise de filmes com menos lucro, já que usando o dataframe geral a análise ficou com gráficos vazios por conter filmes com aluguéis = 0.
* printamos os dois dataframes, e assim já podemos conferir se a conexão deu certa e também o número de linhas (o segundo dataframe deve, logicamente, conter menas linhas).
![image](https://github.com/user-attachments/assets/281fe8eb-a205-4d94-8e16-06100357d734)
* agora finalizamos a conexão e damos início as análises.
* primeiramente agrupamos os valores que devem ser analisados, e depois usamos comandos do pyplot para criar os gráficos, definindo as cores, proporções e legendas.
* a análise de "Top Mais" e "Top Menos" foi definida apenas mudando o comando ".sort.values(ascending=)" usando False para top mais, e true para top menos.
* a análise de filmes menos alugados é a única a usar o dataframe "df_apenas_alugados" por motivos de no dataframe original vir filmes que não foram alugados nenhuma vez, assim deixando o gráfico vazio.
* por fim, salvamos o resultado como imagem na pasta "resultados".
### Observações:
* necessário ter o driver ODBC para Postegre instalado.
### Tecnologias Usadas:
* Banco de dados PostegreSQL com banco de dados Pagila baixado.
* Python com bibliotecas PYODBC para conexão com banco de dados Postegre, Pandas pra extrair e transformar os dados e Matplotlib Pyplot para criar gráficos de Análises.
