/*
Enter your query here.
*/
select f.id,t.age,t.needed,t.power from
 (select w.id,p.age,w.power,w.coins_needed as needed from wands w
  join wands_property p on w.code = p.code) f
 join 
 (select p.age,min(w.coins_needed) as needed,w.power from wands w
 join wands_property p on w.code = p.code
 where p.is_evil = 0
 group by p.age,w.power) t
 on f.age = t.age and f.needed = t.needed and f.power = t.power
 order by f.power desc,t.age desc