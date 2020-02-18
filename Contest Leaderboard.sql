/*
Enter your query here.
*/
select h.hacker_id,h.name,sum(s.sc) from hackers h
 join (
select hacker_id,challenge_id,max(score) as sc from submissions
 group by hacker_id,challenge_id) s
 on h.hacker_id = s.hacker_id
 group by h.hacker_id,h.name
 having sum(s.sc) != 0
 order by sum(s.sc) desc,h.hacker_id