-- Não é um sql funcional
-- Para que se torne funcional, é necessario ter as seguintes mudanças:
-- Inserir um alias para a coluna que será criada (count) com o comando AS
-- Remover a ',' no final do select (antes do from)
-- No where, deve-se trocar o == por IN
-- deve-se agrupar por mais de uma coluna
-- deve-se agrupar antes de ordenar
select 
  count(distinct origin_registration_id) as registration_count,
  new_status,
  old_status
from 
  registrations_fact
where 
  new_status in (1, 2, 3, 4, 5, 6)
group by 
  new_status, old_status
order by
  new_status;