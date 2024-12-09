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
	