select COUNTRY.Continent,FLOOR(avg(city.population)) from country
 join city on country.code = city.countrycode
 group by country.Continent