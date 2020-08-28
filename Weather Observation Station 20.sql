/*
Enter your query here.
*/
/* 有奇数条记录 */
select round(s.lat_n,4) from station s
 where (select round(count(*)/2)-1 from station)
 = (select count(*) from station s1 where s1.lat_n > s.lat_n)