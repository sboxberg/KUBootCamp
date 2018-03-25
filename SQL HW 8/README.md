

```python
from sqlalchemy import create_engine
import pandas as pd
from warnings import filterwarnings
import pymysql
filterwarnings('ignore', category=pymysql.Warning)
import os
```


```python
engine = create_engine('mysql+pymysql://root:kcmo1728@localhost/sakila') 
```

##Question 1


```python
actors = pd.read_sql_query("select first_name,last_name from actor", engine)
actors.head()
#Only displaying head to save scrolling
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>first_name</th>
      <th>last_name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>PENELOPE</td>
      <td>GUINESS</td>
    </tr>
    <tr>
      <th>1</th>
      <td>NICK</td>
      <td>WAHLBERG</td>
    </tr>
    <tr>
      <th>2</th>
      <td>ED</td>
      <td>CHASE</td>
    </tr>
    <tr>
      <th>3</th>
      <td>JENNIFER</td>
      <td>DAVIS</td>
    </tr>
    <tr>
      <th>4</th>
      <td>JOHNNY</td>
      <td>LOLLOBRIGIDA</td>
    </tr>
  </tbody>
</table>
</div>




```python
actor = pd.read_sql_query("select concat(first_name, ' ',last_name) as ActorName from actor", engine)
actor.head()
#Only displaying head to save scrolling
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ActorName</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>PENELOPE GUINESS</td>
    </tr>
    <tr>
      <th>1</th>
      <td>NICK WAHLBERG</td>
    </tr>
    <tr>
      <th>2</th>
      <td>ED CHASE</td>
    </tr>
    <tr>
      <th>3</th>
      <td>JENNIFER DAVIS</td>
    </tr>
    <tr>
      <th>4</th>
      <td>JOHNNY LOLLOBRIGIDA</td>
    </tr>
  </tbody>
</table>
</div>



##Question 2


```python
sql_query = """
select actor_id, first_name, last_name from actor
where first_name = 'Joe';
"""

new_df = pd.read_sql_query(sql_query, engine)
new_df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>actor_id</th>
      <th>first_name</th>
      <th>last_name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>9</td>
      <td>JOE</td>
      <td>SWANK</td>
    </tr>
  </tbody>
</table>
</div>




```python
sql_query = """
select actor_id, first_name, last_name from actor
where last_name like '%%gen%%';
"""

new_df = pd.read_sql_query(sql_query, engine)
new_df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>actor_id</th>
      <th>first_name</th>
      <th>last_name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>14</td>
      <td>VIVIEN</td>
      <td>BERGEN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>41</td>
      <td>JODIE</td>
      <td>DEGENERES</td>
    </tr>
    <tr>
      <th>2</th>
      <td>107</td>
      <td>GINA</td>
      <td>DEGENERES</td>
    </tr>
    <tr>
      <th>3</th>
      <td>166</td>
      <td>NICK</td>
      <td>DEGENERES</td>
    </tr>
  </tbody>
</table>
</div>




```python
sql_query = """
select actor_id, last_name, first_name from actor
where last_name like '%%li%%'
order by last_name asc, first_name asc;
"""

new_df = pd.read_sql_query(sql_query, engine)
new_df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>actor_id</th>
      <th>last_name</th>
      <th>first_name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>86</td>
      <td>CHAPLIN</td>
      <td>GREG</td>
    </tr>
    <tr>
      <th>1</th>
      <td>82</td>
      <td>JOLIE</td>
      <td>WOODY</td>
    </tr>
    <tr>
      <th>2</th>
      <td>34</td>
      <td>OLIVIER</td>
      <td>AUDREY</td>
    </tr>
    <tr>
      <th>3</th>
      <td>15</td>
      <td>OLIVIER</td>
      <td>CUBA</td>
    </tr>
    <tr>
      <th>4</th>
      <td>172</td>
      <td>WILLIAMS</td>
      <td>HARPO</td>
    </tr>
    <tr>
      <th>5</th>
      <td>137</td>
      <td>WILLIAMS</td>
      <td>MORGAN</td>
    </tr>
    <tr>
      <th>6</th>
      <td>72</td>
      <td>WILLIAMS</td>
      <td>SEAN</td>
    </tr>
    <tr>
      <th>7</th>
      <td>83</td>
      <td>WILLIS</td>
      <td>BEN</td>
    </tr>
    <tr>
      <th>8</th>
      <td>96</td>
      <td>WILLIS</td>
      <td>GENE</td>
    </tr>
    <tr>
      <th>9</th>
      <td>164</td>
      <td>WILLIS</td>
      <td>HUMPHREY</td>
    </tr>
  </tbody>
</table>
</div>




```python
sql_query = """
select country_id, country from country
where country in ('Afghanistan', 'Bangladesh', 'China');
"""

new_df = pd.read_sql_query(sql_query, engine)
new_df            
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>country_id</th>
      <th>country</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Afghanistan</td>
    </tr>
    <tr>
      <th>1</th>
      <td>12</td>
      <td>Bangladesh</td>
    </tr>
    <tr>
      <th>2</th>
      <td>23</td>
      <td>China</td>
    </tr>
  </tbody>
</table>
</div>



##Question 3


```python
def RunSQL(sql_command):
    connection = pymysql.connect(host='localhost',
                             user='root',
                             password='kcmo1728',
                             db='sakila',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            commands = sql_command.split(';')
            for command in commands:
                if command == '\n': continue
                cursor.execute(command + ';')
                connection.commit()
    except Exception as e: 
        print(e)
    finally:
        connection.close()
```


```python
sql_command = """
alter table actor add middle_name varchar(45) after first_name; 
"""
RunSQL(sql_command)

new_df = pd.read_sql_query('select * from actor',engine)
new_df.head()    

```

    (1065, 'Query was empty')
    




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>actor_id</th>
      <th>first_name</th>
      <th>middle_name</th>
      <th>last_name</th>
      <th>last_update</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>PENELOPE</td>
      <td>None</td>
      <td>GUINESS</td>
      <td>2006-02-15 04:34:33</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>NICK</td>
      <td>None</td>
      <td>WAHLBERG</td>
      <td>2006-02-15 04:34:33</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>ED</td>
      <td>None</td>
      <td>CHASE</td>
      <td>2006-02-15 04:34:33</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>JENNIFER</td>
      <td>None</td>
      <td>DAVIS</td>
      <td>2006-02-15 04:34:33</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>JOHNNY</td>
      <td>None</td>
      <td>LOLLOBRIGIDA</td>
      <td>2006-02-15 04:34:33</td>
    </tr>
  </tbody>
</table>
</div>




```python
sql_command = """
alter table actor modify middle_name blob; 
"""
RunSQL(sql_command)

new_df = pd.read_sql_query('select * from actor',engine)
new_df.head()   
```

    (1065, 'Query was empty')
    




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>actor_id</th>
      <th>first_name</th>
      <th>middle_name</th>
      <th>last_name</th>
      <th>last_update</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>PENELOPE</td>
      <td>None</td>
      <td>GUINESS</td>
      <td>2006-02-15 04:34:33</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>NICK</td>
      <td>None</td>
      <td>WAHLBERG</td>
      <td>2006-02-15 04:34:33</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>ED</td>
      <td>None</td>
      <td>CHASE</td>
      <td>2006-02-15 04:34:33</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>JENNIFER</td>
      <td>None</td>
      <td>DAVIS</td>
      <td>2006-02-15 04:34:33</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>JOHNNY</td>
      <td>None</td>
      <td>LOLLOBRIGIDA</td>
      <td>2006-02-15 04:34:33</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Note:  I verified in MySQL workbench that middle name is blob datatype 
```


```python
sql_command = """
alter table actor drop column middle_name; 
"""
RunSQL(sql_command)

new_df = pd.read_sql_query('select * from actor',engine)
new_df.head()   

```

    (1065, 'Query was empty')
    




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>actor_id</th>
      <th>first_name</th>
      <th>last_name</th>
      <th>last_update</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>PENELOPE</td>
      <td>GUINESS</td>
      <td>2006-02-15 04:34:33</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>NICK</td>
      <td>WAHLBERG</td>
      <td>2006-02-15 04:34:33</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>ED</td>
      <td>CHASE</td>
      <td>2006-02-15 04:34:33</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>JENNIFER</td>
      <td>DAVIS</td>
      <td>2006-02-15 04:34:33</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>JOHNNY</td>
      <td>LOLLOBRIGIDA</td>
      <td>2006-02-15 04:34:33</td>
    </tr>
  </tbody>
</table>
</div>



##Question 4


```python
sql_query = """
select
a.last_name,
count(a.last_name) as count
from actor a
group by a.last_name;
"""

new_df = pd.read_sql_query(sql_query, engine)
new_df.head()
#Only displaying head to save scrolling
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>last_name</th>
      <th>count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>AKROYD</td>
      <td>3</td>
    </tr>
    <tr>
      <th>1</th>
      <td>ALLEN</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>ASTAIRE</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>BACALL</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>BAILEY</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>




```python
sql_query = """
select
a.last_name,
count(a.last_name) as count
from actor a
group by a.last_name
having count >= 2;

"""

new_df = pd.read_sql_query(sql_query, engine)
new_df.head()
#Only displaying head to save scrolling
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>last_name</th>
      <th>count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>AKROYD</td>
      <td>3</td>
    </tr>
    <tr>
      <th>1</th>
      <td>ALLEN</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>BAILEY</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>BENING</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>BERRY</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>




```python
sql_query = """
select actor_id, first_name, last_name from actor
where last_name ='williams';
"""

new_df = pd.read_sql_query(sql_query, engine)
new_df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>actor_id</th>
      <th>first_name</th>
      <th>last_name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>72</td>
      <td>SEAN</td>
      <td>WILLIAMS</td>
    </tr>
    <tr>
      <th>1</th>
      <td>137</td>
      <td>MORGAN</td>
      <td>WILLIAMS</td>
    </tr>
    <tr>
      <th>2</th>
      <td>172</td>
      <td>HARPO</td>
      <td>WILLIAMS</td>
    </tr>
  </tbody>
</table>
</div>




```python
sql_command = """
update actor
set first_name = 'HARPO'
where first_name = 'GROUCHO' and last_name = 'WILLIAMS';
"""
RunSQL(sql_command)

sql_query = """
select actor_id, first_name, last_name from actor
where last_name ='williams';
"""

new_df = pd.read_sql_query(sql_query, engine)
new_df

```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>actor_id</th>
      <th>first_name</th>
      <th>last_name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>72</td>
      <td>SEAN</td>
      <td>WILLIAMS</td>
    </tr>
    <tr>
      <th>1</th>
      <td>137</td>
      <td>MORGAN</td>
      <td>WILLIAMS</td>
    </tr>
    <tr>
      <th>2</th>
      <td>172</td>
      <td>HARPO</td>
      <td>WILLIAMS</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Question made no sense.  I slacked with Jeff and he agreed.  He shared the solution below, which I understand
#but it's worthless as you'll never hit the else.  I'll leave this hear, but it was not my work.
#Since you manually select actor_id = 172, it's not even a useful piece of code (it's specific to one line)

#UPDATE actor
#SET first_name =
#CASE
#WHEN first_name = 'HARPO'
# THEN 'GROUCHO'
#ELSE 'MUCHO GROUCHO'
#END
#WHERE actor_id = 172;
```

##Question 5


```python
#I ran  SHOW CREATE TABLE address; in MySQL Workbench

#It returned the following:

#CREATE TABLE `address` (
#  `address_id` smallint(5) unsigned NOT NULL AUTO_INCREMENT,
#  `address` varchar(50) NOT NULL,
#  `address2` varchar(50) DEFAULT NULL,
#  `district` varchar(20) NOT NULL,
#  `city_id` smallint(5) unsigned NOT NULL,
#  `postal_code` varchar(10) DEFAULT NULL,
#  `phone` varchar(20) NOT NULL,
#  `location` geometry NOT NULL,
#  `last_update` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
#  PRIMARY KEY (`address_id`),
#  KEY `idx_fk_city_id` (`city_id`),
#  SPATIAL KEY `idx_location` (`location`),
#  CONSTRAINT `fk_address_city` FOREIGN KEY (`city_id`) REFERENCES `city` (`city_id`) ON UPDATE CASCADE
#) ENGINE=InnoDB AUTO_INCREMENT=606 DEFAULT CHARSET=utf8'


#I believe I could use the RunSQL function below and insert the create table command
#-- except I'd remove the stuff after the ')' related to ENGINE

#sql_command = """
 
#"""
#RunSQL(sql_command)

#I chose not to run it since the table exists and I didn't want to mess up the database, but I believe
#I did the essence of the question by finding the schema for the table.  
```

##Question 6


```python
sql_query = """
select staff.first_name, staff.last_name, address.address
from staff
inner join address on
staff.address_id = address.address_id;
"""
staff = pd.read_sql_query(sql_query, engine)
staff
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>first_name</th>
      <th>last_name</th>
      <th>address</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Mike</td>
      <td>Hillyer</td>
      <td>23 Workhaven Lane</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Jon</td>
      <td>Stephens</td>
      <td>1411 Lillydale Drive</td>
    </tr>
  </tbody>
</table>
</div>




```python
sql_query = """
select staff.first_name, staff.last_name, sum(payment.amount) as total
from staff
join payment on
staff.staff_id = payment.staff_id
where payment.payment_date >= '2005-08-01'
and payment.payment_date <= '2005-08-31'
group by staff.first_name;
"""
staff = pd.read_sql_query(sql_query, engine)
staff
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>first_name</th>
      <th>last_name</th>
      <th>total</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Jon</td>
      <td>Stephens</td>
      <td>12218.48</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Mike</td>
      <td>Hillyer</td>
      <td>11853.65</td>
    </tr>
  </tbody>
</table>
</div>




```python
sql_query = """
select film.title, count(film_actor.actor_id) as actor_count
from film
inner join film_actor on
film.film_id = film_actor.film_id
group by film.title;
"""
film = pd.read_sql_query(sql_query, engine)
film.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>title</th>
      <th>actor_count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>ACADEMY DINOSAUR</td>
      <td>10</td>
    </tr>
    <tr>
      <th>1</th>
      <td>ACE GOLDFINGER</td>
      <td>4</td>
    </tr>
    <tr>
      <th>2</th>
      <td>ADAPTATION HOLES</td>
      <td>5</td>
    </tr>
    <tr>
      <th>3</th>
      <td>AFFAIR PREJUDICE</td>
      <td>5</td>
    </tr>
    <tr>
      <th>4</th>
      <td>AFRICAN EGG</td>
      <td>5</td>
    </tr>
  </tbody>
</table>
</div>




```python
sql_query = """
select film.title, count(inventory.inventory_id) as inventory_count
from film
inner join inventory on
film.film_id = inventory.film_id
where film.title = "Hunchback Impossible";
"""
inventory = pd.read_sql_query(sql_query, engine)
inventory
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>title</th>
      <th>inventory_count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>HUNCHBACK IMPOSSIBLE</td>
      <td>6</td>
    </tr>
  </tbody>
</table>
</div>




```python
sql_query = """
select customer.first_name, customer.last_name, sum(payment.amount) as Total_Amount_Paid
from customer
join payment on
customer.customer_id = payment.customer_id
group by customer.first_name
order by customer.last_name;
"""
customer = pd.read_sql_query(sql_query, engine)
customer.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>first_name</th>
      <th>last_name</th>
      <th>Total_Amount_Paid</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>RAFAEL</td>
      <td>ABNEY</td>
      <td>97.79</td>
    </tr>
    <tr>
      <th>1</th>
      <td>NATHANIEL</td>
      <td>ADAM</td>
      <td>133.72</td>
    </tr>
    <tr>
      <th>2</th>
      <td>KATHLEEN</td>
      <td>ADAMS</td>
      <td>92.73</td>
    </tr>
    <tr>
      <th>3</th>
      <td>DIANA</td>
      <td>ALEXANDER</td>
      <td>105.73</td>
    </tr>
    <tr>
      <th>4</th>
      <td>GORDON</td>
      <td>ALLARD</td>
      <td>160.68</td>
    </tr>
  </tbody>
</table>
</div>



##Question 7


```python
sql_query = """
select title
from film
where language_id in
 (
    select language_id
    from language 
    where language.name = 'english'
  )
AND
film.title like 'K%%'or film.title like 'Q%%';
"""
films = pd.read_sql_query(sql_query, engine)
films
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>title</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>KANE EXORCIST</td>
    </tr>
    <tr>
      <th>1</th>
      <td>KARATE MOON</td>
    </tr>
    <tr>
      <th>2</th>
      <td>KENTUCKIAN GIANT</td>
    </tr>
    <tr>
      <th>3</th>
      <td>KICK SAVANNAH</td>
    </tr>
    <tr>
      <th>4</th>
      <td>KILL BROTHERHOOD</td>
    </tr>
    <tr>
      <th>5</th>
      <td>KILLER INNOCENT</td>
    </tr>
    <tr>
      <th>6</th>
      <td>KING EVOLUTION</td>
    </tr>
    <tr>
      <th>7</th>
      <td>KISS GLORY</td>
    </tr>
    <tr>
      <th>8</th>
      <td>KISSING DOLLS</td>
    </tr>
    <tr>
      <th>9</th>
      <td>KNOCK WARLOCK</td>
    </tr>
    <tr>
      <th>10</th>
      <td>KRAMER CHOCOLATE</td>
    </tr>
    <tr>
      <th>11</th>
      <td>KWAI HOMEWARD</td>
    </tr>
    <tr>
      <th>12</th>
      <td>QUEEN LUKE</td>
    </tr>
    <tr>
      <th>13</th>
      <td>QUEST MUSSOLINI</td>
    </tr>
    <tr>
      <th>14</th>
      <td>QUILLS BULL</td>
    </tr>
  </tbody>
</table>
</div>




```python
sql_query = """
select actor.first_name, actor.last_name
from actor
where actor_id in
 (
  select actor_id
  from film_actor
  where film_id in
   (
    select film_id
    from film 
    where film.title = 'Alone Trip'
    )
  );
"""
actors = pd.read_sql_query(sql_query, engine)
actors
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>first_name</th>
      <th>last_name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>ED</td>
      <td>CHASE</td>
    </tr>
    <tr>
      <th>1</th>
      <td>KARL</td>
      <td>BERRY</td>
    </tr>
    <tr>
      <th>2</th>
      <td>UMA</td>
      <td>WOOD</td>
    </tr>
    <tr>
      <th>3</th>
      <td>WOODY</td>
      <td>JOLIE</td>
    </tr>
    <tr>
      <th>4</th>
      <td>SPENCER</td>
      <td>DEPP</td>
    </tr>
    <tr>
      <th>5</th>
      <td>CHRIS</td>
      <td>DEPP</td>
    </tr>
    <tr>
      <th>6</th>
      <td>LAURENCE</td>
      <td>BULLOCK</td>
    </tr>
    <tr>
      <th>7</th>
      <td>RENEE</td>
      <td>BALL</td>
    </tr>
  </tbody>
</table>
</div>




```python
sql_query = """
select customer.first_name, customer.last_name, customer.email, country.country
from customer
inner join address on
customer.address_id = address.address_id
inner join city on
address.city_id = city.city_id
inner join country on
city.country_id = country.country_id
where country.country = "Canada";
"""
canada = pd.read_sql_query(sql_query, engine)
canada
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>first_name</th>
      <th>last_name</th>
      <th>email</th>
      <th>country</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>DERRICK</td>
      <td>BOURQUE</td>
      <td>DERRICK.BOURQUE@sakilacustomer.org</td>
      <td>Canada</td>
    </tr>
    <tr>
      <th>1</th>
      <td>DARRELL</td>
      <td>POWER</td>
      <td>DARRELL.POWER@sakilacustomer.org</td>
      <td>Canada</td>
    </tr>
    <tr>
      <th>2</th>
      <td>LORETTA</td>
      <td>CARPENTER</td>
      <td>LORETTA.CARPENTER@sakilacustomer.org</td>
      <td>Canada</td>
    </tr>
    <tr>
      <th>3</th>
      <td>CURTIS</td>
      <td>IRBY</td>
      <td>CURTIS.IRBY@sakilacustomer.org</td>
      <td>Canada</td>
    </tr>
    <tr>
      <th>4</th>
      <td>TROY</td>
      <td>QUIGLEY</td>
      <td>TROY.QUIGLEY@sakilacustomer.org</td>
      <td>Canada</td>
    </tr>
  </tbody>
</table>
</div>




```python
sql_query = """
select film.title
from film
where film_id in
 (
  select film_id
  from film_category
  where category_id in
   (
    select category_id
    from category 
    where category.name = 'Family'
    )
  );
"""
family = pd.read_sql_query(sql_query, engine)
family
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>title</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>AFRICAN EGG</td>
    </tr>
    <tr>
      <th>1</th>
      <td>APACHE DIVINE</td>
    </tr>
    <tr>
      <th>2</th>
      <td>ATLANTIS CAUSE</td>
    </tr>
    <tr>
      <th>3</th>
      <td>BAKED CLEOPATRA</td>
    </tr>
    <tr>
      <th>4</th>
      <td>BANG KWAI</td>
    </tr>
    <tr>
      <th>5</th>
      <td>BEDAZZLED MARRIED</td>
    </tr>
    <tr>
      <th>6</th>
      <td>BILKO ANONYMOUS</td>
    </tr>
    <tr>
      <th>7</th>
      <td>BLANKET BEVERLY</td>
    </tr>
    <tr>
      <th>8</th>
      <td>BLOOD ARGONAUTS</td>
    </tr>
    <tr>
      <th>9</th>
      <td>BLUES INSTINCT</td>
    </tr>
    <tr>
      <th>10</th>
      <td>BRAVEHEART HUMAN</td>
    </tr>
    <tr>
      <th>11</th>
      <td>CHASING FIGHT</td>
    </tr>
    <tr>
      <th>12</th>
      <td>CHISUM BEHAVIOR</td>
    </tr>
    <tr>
      <th>13</th>
      <td>CHOCOLAT HARRY</td>
    </tr>
    <tr>
      <th>14</th>
      <td>CONFUSED CANDLES</td>
    </tr>
    <tr>
      <th>15</th>
      <td>CONVERSATION DOWNHILL</td>
    </tr>
    <tr>
      <th>16</th>
      <td>DATE SPEED</td>
    </tr>
    <tr>
      <th>17</th>
      <td>DINOSAUR SECRETARY</td>
    </tr>
    <tr>
      <th>18</th>
      <td>DUMBO LUST</td>
    </tr>
    <tr>
      <th>19</th>
      <td>EARRING INSTINCT</td>
    </tr>
    <tr>
      <th>20</th>
      <td>EFFECT GLADIATOR</td>
    </tr>
    <tr>
      <th>21</th>
      <td>FEUD FROGMEN</td>
    </tr>
    <tr>
      <th>22</th>
      <td>FINDING ANACONDA</td>
    </tr>
    <tr>
      <th>23</th>
      <td>GABLES METROPOLIS</td>
    </tr>
    <tr>
      <th>24</th>
      <td>GANDHI KWAI</td>
    </tr>
    <tr>
      <th>25</th>
      <td>GLADIATOR WESTWARD</td>
    </tr>
    <tr>
      <th>26</th>
      <td>GREASE YOUTH</td>
    </tr>
    <tr>
      <th>27</th>
      <td>HALF OUTFIELD</td>
    </tr>
    <tr>
      <th>28</th>
      <td>HOCUS FRIDA</td>
    </tr>
    <tr>
      <th>29</th>
      <td>HOMICIDE PEACH</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
    </tr>
    <tr>
      <th>39</th>
      <td>MAGUIRE APACHE</td>
    </tr>
    <tr>
      <th>40</th>
      <td>MANCHURIAN CURTAIN</td>
    </tr>
    <tr>
      <th>41</th>
      <td>MOVIE SHAKESPEARE</td>
    </tr>
    <tr>
      <th>42</th>
      <td>MUSIC BOONDOCK</td>
    </tr>
    <tr>
      <th>43</th>
      <td>NATURAL STOCK</td>
    </tr>
    <tr>
      <th>44</th>
      <td>NETWORK PEAK</td>
    </tr>
    <tr>
      <th>45</th>
      <td>ODDS BOOGIE</td>
    </tr>
    <tr>
      <th>46</th>
      <td>OPPOSITE NECKLACE</td>
    </tr>
    <tr>
      <th>47</th>
      <td>PILOT HOOSIERS</td>
    </tr>
    <tr>
      <th>48</th>
      <td>PITTSBURGH HUNCHBACK</td>
    </tr>
    <tr>
      <th>49</th>
      <td>PRESIDENT BANG</td>
    </tr>
    <tr>
      <th>50</th>
      <td>PRIX UNDEFEATED</td>
    </tr>
    <tr>
      <th>51</th>
      <td>RAGE GAMES</td>
    </tr>
    <tr>
      <th>52</th>
      <td>RANGE MOONWALKER</td>
    </tr>
    <tr>
      <th>53</th>
      <td>REMEMBER DIARY</td>
    </tr>
    <tr>
      <th>54</th>
      <td>RESURRECTION SILVERADO</td>
    </tr>
    <tr>
      <th>55</th>
      <td>ROBBERY BRIGHT</td>
    </tr>
    <tr>
      <th>56</th>
      <td>RUSH GOODFELLAS</td>
    </tr>
    <tr>
      <th>57</th>
      <td>SECRETS PARADISE</td>
    </tr>
    <tr>
      <th>58</th>
      <td>SENSIBILITY REAR</td>
    </tr>
    <tr>
      <th>59</th>
      <td>SIEGE MADRE</td>
    </tr>
    <tr>
      <th>60</th>
      <td>SLUMS DUCK</td>
    </tr>
    <tr>
      <th>61</th>
      <td>SOUP WISDOM</td>
    </tr>
    <tr>
      <th>62</th>
      <td>SPARTACUS CHEAPER</td>
    </tr>
    <tr>
      <th>63</th>
      <td>SPINAL ROCKY</td>
    </tr>
    <tr>
      <th>64</th>
      <td>SPLASH GUMP</td>
    </tr>
    <tr>
      <th>65</th>
      <td>SUNSET RACER</td>
    </tr>
    <tr>
      <th>66</th>
      <td>SUPER WYOMING</td>
    </tr>
    <tr>
      <th>67</th>
      <td>VIRTUAL SPOILERS</td>
    </tr>
    <tr>
      <th>68</th>
      <td>WILLOW TRACY</td>
    </tr>
  </tbody>
</table>
<p>69 rows × 1 columns</p>
</div>




```python
sql_query = """
select film.title, count(rental.rental_id) as Total_Rentals
from film
join inventory on
film.film_id = inventory.film_id
join rental on
inventory.inventory_id = rental.inventory_id
group by film.title
order by Total_Rentals desc;
"""
rentals = pd.read_sql_query(sql_query, engine)
rentals.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>title</th>
      <th>Total_Rentals</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>BUCKET BROTHERHOOD</td>
      <td>34</td>
    </tr>
    <tr>
      <th>1</th>
      <td>ROCKETEER MOTHER</td>
      <td>33</td>
    </tr>
    <tr>
      <th>2</th>
      <td>SCALAWAG DUCK</td>
      <td>32</td>
    </tr>
    <tr>
      <th>3</th>
      <td>FORWARD TEMPLE</td>
      <td>32</td>
    </tr>
    <tr>
      <th>4</th>
      <td>RIDGEMONT SUBMARINE</td>
      <td>32</td>
    </tr>
  </tbody>
</table>
</div>




```python
sql_query = """
select staff.store_id, address.address, sum(payment.amount) as Total_Revenue
from payment
join staff on
payment.staff_id = staff.staff_id
join store on
staff.store_id = store.store_id
join address on
store.address_id = address.address_id
group by staff.store_id;
"""
stores = pd.read_sql_query(sql_query, engine)
stores
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>store_id</th>
      <th>address</th>
      <th>Total_Revenue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>47 MySakila Drive</td>
      <td>33489.47</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>28 MySQL Boulevard</td>
      <td>33927.04</td>
    </tr>
  </tbody>
</table>
</div>




```python
sql_query = """
select store.store_id, city.city, country.country
from store
join address on
store.address_id = address.address_id
join city on
address.city_id=city.city_id
join country on
city.country_id = country.country_id;
"""
store = pd.read_sql_query(sql_query, engine)
store
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>store_id</th>
      <th>city</th>
      <th>country</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Lethbridge</td>
      <td>Canada</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Woodridge</td>
      <td>Australia</td>
    </tr>
  </tbody>
</table>
</div>




```python
sql_query = """
select category.name, sum(payment.amount) as Total_Rentals
from category
join film_category on
category.category_id = film_category.category_id
join inventory on
film_category.film_id = inventory.film_id
join rental on
inventory.inventory_id = rental.inventory_id
join payment on
rental.rental_id = payment.rental_id
group by category.name
order by Total_Rentals desc;
"""
genre = pd.read_sql_query(sql_query, engine)
genre.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>Total_Rentals</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Sports</td>
      <td>5314.21</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Sci-Fi</td>
      <td>4756.98</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Animation</td>
      <td>4656.30</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Drama</td>
      <td>4587.39</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Comedy</td>
      <td>4383.58</td>
    </tr>
  </tbody>
</table>
</div>



##Question 8


```python
sql_query = """
create view total_rentals_by_genre as
select category.name, sum(payment.amount) as Total_Rentals
from category
join film_category on
category.category_id = film_category.category_id
join inventory on
film_category.film_id = inventory.film_id
join rental on
inventory.inventory_id = rental.inventory_id
join payment on
rental.rental_id = payment.rental_id
group by category.name
order by Total_Rentals desc;
"""
RunSQL(sql_query)
```


```python
#I verified that total_rentals_by_genre is in my views by looking at MySQL workbench
```


```python
total_rentals = pd.read_sql_query('select * from total_rentals_by_genre', engine)
total_rentals.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>Total_Rentals</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Sports</td>
      <td>5314.21</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Sci-Fi</td>
      <td>4756.98</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Animation</td>
      <td>4656.30</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Drama</td>
      <td>4587.39</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Comedy</td>
      <td>4383.58</td>
    </tr>
  </tbody>
</table>
</div>




```python
RunSQL('drop view total_rentals_by_genre')
```


```python
#I verified that total_rentals_by_genre is no longer in my views by looking at MySQL workbench
```
