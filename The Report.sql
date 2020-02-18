/*
Enter your query here.
*/
select (CASE g.grade >= 8 WHEN TRUE THEN s.name ELSE null END),g.grade,s.marks from students s
 join grades g on s.marks between g.min_mark and g.max_mark
 order by g.grade desc,s.name,s.marks