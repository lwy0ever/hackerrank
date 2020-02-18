/*
Enter your query here.
*/
select c.hacker_id,h.name,count(1) as challenges_created from hackers h
 join challenges c on h.hacker_id = c.hacker_id
 group by c.hacker_id,h.name
 having
 challenges_created =
 (select max(x.cnt) from
 (select count(1) as cnt from challenges
  group by hacker_id) x)
  or
  challenges_created in
 (select x.cnt from
  (select count(1) as cnt from challenges
   group by hacker_id) x
  group by x.cnt
  having count(1) = 1)
 order by challenges_created desc,c.hacker_id