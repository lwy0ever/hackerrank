/*
Enter your query here.
*/
select months * salary,count(*) from employee
 where months * salary = (select max(months * salary) as ma from employee)
 group by months * salary