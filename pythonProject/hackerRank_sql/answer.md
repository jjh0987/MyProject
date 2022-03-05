#### 1
select name from city where countrycode = 'USA' and population > 120000;
#### 2
select * from city;
#### 3
select * from city where id = 1661;
#### 4
select * from city where countrycode = 'JPN';
#### 5
select name from city where countrycode = 'JPN';
#### 6
select city,state from station;
#### 7
select distinct a.city from 
(select city,id%2 as x from station) a
where a.x = 0;
#### 8
select count(city)-count(distinct city) from station;