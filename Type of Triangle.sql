/*
Enter your query here.
*/
select (
    case
        when A <= 0 or B <= 0 or C <= 0 or A + B <= C or A + C <= B or B + C <= A then 'Not A Triangle'
        when A = B and B = C then 'Equilateral'
        when (A = B and B != C) or (A = C and A != B) or (B = C and A != B) then 'Isosceles'
        else 'Scalene'
    end
) from triangles