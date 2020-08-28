/*
Enter your query here.
*/
set @NUMBER:=0;
SELECT REPEAT('* ', @NUMBER := @NUMBER + 1) FROM information_schema.tables where @NUMBER < 20;