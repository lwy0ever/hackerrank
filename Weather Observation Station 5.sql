/*
Enter your query here.
*/
select city,char_length(city) from station
 order by char_length(city),city
 limit 1;
select city,char_length(city) from station
 order by char_length(city) desc,city
 limit 1;