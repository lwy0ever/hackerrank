/*
Enter your query here.
*/
select ceil(avg(salary) - avg(convert(replace(convert(salary,char),'0',''),decimal))) from employees