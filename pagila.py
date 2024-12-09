import pyodbc
import pandas as pd
import matplotlib.pyplot as plt

conn = pyodbc.connect(
    'DRIVER={Devart ODBC Driver for PostgreSQL};'
    'SERVER=localhost;'
    'PORT=5432;'
    'DATABASE=pagila;'
    'UID=postgres;'
    'PWD=*****;'
)

query = '''
        select
        a.first_name || ' ' || a.last_name as nome_completo
        ,f.title as filme
        ,f.release_year as ano
        ,c.name as categoria
        ,ROUND(AVG(p.amount), 2) as valor_aluguel
        ,COUNT(r.rental_id) as vezes_alugado
        ,ROUND(AVG(p.amount) * COUNT(r.rental_id), 2) as lucro_total_alugueis
    from
        actor a
    left join
        film_actor fa on fa.actor_id = a.actor_id
    left join
        film f on f.film_id = fa.film_id
    left join
        film_category fc on fc.film_id = f.film_id
    left join
        category c on c.category_id = fc.category_id
    left join
        inventory i on f.film_id = i.film_id
    left join 
        rental r on i.inventory_id = r.inventory_id
    left join
        payment p on r.rental_id = p.rental_id
    group by
        a.actor_id, f.film_id, c.category_id
    order by lucro_total_alugueis asc
'''

df = pd.read_sql(query, conn)
df_apenas_alugados = df[df['vezes_alugado'] > 0]
conn.close()

print(df)
print(df_apenas_alugados)
##fim da conexão

##inicio da analise:

#Top Mais Lucros (Ator)
lucro_por_ator = df.groupby('nome_completo')['lucro_total_alugueis'].sum().sort_values(ascending=False)
plt.figure(figsize=(10, 6))
lucro_por_ator.head(10).plot(kind='bar', color='green')
plt.title('Top 10 Atores que mais Geram Lucro', fontsize=14)
plt.xlabel('Ator', fontsize=12)
plt.ylabel('Lucro Total', fontsize=12)
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.subplots_adjust(bottom=0.267)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig("resultados/top_atores_lucro.png", dpi=300, bbox_inches='tight')
plt.show()

#Top Menos Lucros (Ator)
lucro_por_ator = df.groupby('nome_completo')['lucro_total_alugueis'].sum().sort_values(ascending=True)
plt.figure(figsize=(10, 6))
lucro_por_ator.head(10).plot(kind='bar', color='red')
plt.title('Top 10 Atores que menos Geram Lucro', fontsize=14)
plt.xlabel('Ator', fontsize=12)
plt.ylabel('Lucro Total', fontsize=12)
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.subplots_adjust(bottom=0.267)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig("resultados/top_atores_menor_lucro.png", dpi=300, bbox_inches='tight')
plt.show()

#top mais lucros (filmes)
lucro_por_filme = df.groupby('filme')['lucro_total_alugueis'].sum().sort_values(ascending=False)
plt.figure(figsize=(10, 6))
lucro_por_filme.head(10).plot(kind='bar', color='green')
plt.title('Top 10 Filmes que mais Geram Lucro', fontsize=14)
plt.xlabel('Filme', fontsize=12)
plt.ylabel('Lucro Total', fontsize=12)
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.subplots_adjust(bottom=0.267)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig("resultados/top_filmes_lucro.png", dpi=300, bbox_inches='tight')
plt.show()

#top menos lucros (filmes)
lucro_por_filme = df_apenas_alugados.groupby('filme')['lucro_total_alugueis'].sum().sort_values(ascending=True)
plt.figure(figsize=(10, 6))
lucro_por_filme.head(10).plot(kind='bar', color='red')
plt.title('Top 10 Filmes que menos Geram Lucro', fontsize=14)
plt.xlabel('Filme', fontsize=12)
plt.ylabel('Lucro Total', fontsize=12)
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.subplots_adjust(bottom=0.267)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig("resultados/top_filmes_menos_lucro.png", dpi=300, bbox_inches='tight')
plt.show()