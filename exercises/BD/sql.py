# Exsersises SQL

use sakila

select * from city 

select * from country

select city_id, country_id from city 

select country_id, city_id from city 

select c.country_id, c.city_id from city c #aliansy

select city_id as "id miasta", city as "miasto" from city

select city_id as "id miasta", city as "miasto" from city limit 5 #(top 5 rekordów)

select city_id as "id miasta", city as "miasto" from city order by city asc #(sort rosnąco)

select city_id as "id miasta", city as "miasto" from city order by city desc #(sort malejąco)

select * from city where city = "Bydgoszcz"

select * from city where city = "Bydgoszcz" or city = "Dallas"

select * from city where city = "Bydgoszcz" and city_id = 2 #(warunek nie użyteczny ponieważ ma być ID=2 a nazwa = Bydgoszcz)

select city as "nazwa_miasta", country_id as "ID_miasta" from city where city = "Bydgoszcz" or country_id = 2 limit 1

select city as "nazwa_miasta", country_id from city where city = "Bydgoszcz" or country_id = 2 order by city desc

select city_id, city from city where city_id  != 1

select * from city where city_id > 3 and city < 10

select * from city where city_id between 3 and 10 order by city desc 

select * from city where city like "Ad%" #(Miasta zaczynają się na "Ad")

select * from city where city like "%na"  #(Miasta kończą się na "na")

select * from city where (city like "%na" and country_id = 97) or (city  = "Bydgoszcz" or country_id = 20)
-- ------------------------------------------------------------------------------------------------------------------------

# Pobierz wszystkie rekordy z tabeli city
select * from city

# Pobierz rekord z tabeli city gdzie nazwa miast jest równa Moscow
select * from city where city = "Moscow"

# Pobierz wszystkie miasta zaczynające się na literę A
select city as "nazwa_miasta" from city where city like "A%" order by city asc 

# Pobierz wszystkie miasta kończące się na litery at, posortuj je malejąco po city_id
select city as "nazwa_miasta_end=at", city_id as "ID_miast" from city where city like "%at" order by city desc  

# Pobierz tylko nazwę miasta zamiast całego rekordy dla dowolnego warunku.
select city as "tylko_nazwa" from city c
-- ------------------------------------------------------------------------------------------------------------------------

select * from city where city = 'London'

select distinct * from city where city = 'London'

select distinct city from city where city = 'London' #(Usuwanie diplikatów)

select country_id, last_update from city where country_id = 103  

select country_id, last_update from city where country_id between 101 and 103

select distinct country_id, last_update from city where country_id between 101 and 103

select * from city where city = "London" or city = "Bydgoszcz" order by city desc, country_id asc #(sortowanie rosnąco a malejąco)
 
select * from city where city_id = 3 or city_id = 4 or city_id = 5 # --------------------> ALBO #------------------------->

select * from city where city_id in (3,4,5) #lepiej wygląda

select * from city where city_id not in (3,4,5)

#Grupowanie Danych

select country_id from city where country_id between 101 and 103 
group by country_id, last_update #(Grupowanie wg warunków)

#Obliczanie średniej

select * from film

select rating, replacement_cost from film

select rating, avg(replacement_cost) from film # ratingi a średni koszt filmów
where rating in ("PG", "G") # wg ratingów PG a G
group by rating # grupowanie na ratingi (podział na dwie kolumny)

select rating, min(replacement_cost) as "min_cost", max(replacement_cost) as "max_cost" from film  # minimalna a maksymalna cena
group by rating

select rating, avg(replacement_cost) from film 
group by rating
having avg(replacement_cost) < 20

select rating, count(replacement_cost) as "ilość_rekordów" from film  # count pokazule ilość rekordów
group by rating

select rating, sum(replacement_cost) as "suma" from film  # sum pokazule summę rekordów
group by rating
-- ------------------------------------------------------------------------------------------------------------------------

select city from city where city = "London"

select city from city where city = "London"
group by city

select distinct city from city where city = "London"
-- ------------------------------------------------------------------------------------------------------------------------

select * from film f 

select rating, avg(length) as "Długość" from film f where rating = "PG-13"
group by rating

select rating, min(`length`) as "Minimalna_długość", max(length) as "Maksymalna_długość" from film f where rating = "PG-13" or rating = "G"
group by rating

select sum(length) as "Suma_długości" from film f  

select count(title) as "Ilość_filmów" from film f 
-- ------------------------------------------------------------------------------------------------------------------------
-- Sakila Sample Database Schema
-- Version 1.5

-- Copyright (c) 2006, 2024, Oracle and/or its affiliates.

-- Redistribution and use in source and binary forms, with or without
-- modification, are permitted provided that the following conditions are
-- met:

-- * Redistributions of source code must retain the above copyright notice,
--   this list of conditions and the following disclaimer.
-- * Redistributions in binary form must reproduce the above copyright
--   notice, this list of conditions and the following disclaimer in the
--   documentation and/or other materials provided with the distribution.
-- * Neither the name of Oracle nor the names of its contributors may be used
--   to endorse or promote products derived from this software without
--   specific prior written permission.

-- THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
-- IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
-- THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
-- PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
-- CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
-- EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
-- PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
-- PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
-- LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
-- NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
-- SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

SET NAMES utf8mb4;
SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL';

DROP SCHEMA IF EXISTS sakila;
CREATE SCHEMA sakila;
USE sakila;

--
-- Table structure for table `actor`
--

CREATE TABLE actor (
  actor_id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
  first_name VARCHAR(45) NOT NULL,
  last_name VARCHAR(45) NOT NULL,
  last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY  (actor_id),
  KEY idx_actor_last_name (last_name)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Table structure for table `address`
--

CREATE TABLE address (
  address_id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
  address VARCHAR(50) NOT NULL,
  address2 VARCHAR(50) DEFAULT NULL,
  district VARCHAR(20) NOT NULL,
  city_id SMALLINT UNSIGNED NOT NULL,
  postal_code VARCHAR(10) DEFAULT NULL,
  phone VARCHAR(20) NOT NULL,
  -- Add GEOMETRY column for MySQL 5.7.5 and higher
  -- Also include SRID attribute for MySQL 8.0.3 and higher
  /*!50705 location GEOMETRY */ /*!80003 SRID 0 */ /*!50705 NOT NULL,*/
  last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY  (address_id),
  KEY idx_fk_city_id (city_id),
  /*!50705 SPATIAL KEY `idx_location` (location),*/
  CONSTRAINT `fk_address_city` FOREIGN KEY (city_id) REFERENCES city (city_id) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Table structure for table `category`
--

CREATE TABLE category (
  category_id TINYINT UNSIGNED NOT NULL AUTO_INCREMENT,
  name VARCHAR(25) NOT NULL,
  last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY  (category_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Table structure for table `city`
--

CREATE TABLE city (
  city_id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
  city VARCHAR(50) NOT NULL,
  country_id SMALLINT UNSIGNED NOT NULL,
  last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY  (city_id),
  KEY idx_fk_country_id (country_id),
  CONSTRAINT `fk_city_country` FOREIGN KEY (country_id) REFERENCES country (country_id) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Table structure for table `country`
--

CREATE TABLE country (
  country_id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
  country VARCHAR(50) NOT NULL,
  last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY  (country_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Table structure for table `customer`
--

CREATE TABLE customer (
  customer_id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
  store_id TINYINT UNSIGNED NOT NULL,
  first_name VARCHAR(45) NOT NULL,
  last_name VARCHAR(45) NOT NULL,
  email VARCHAR(50) DEFAULT NULL,
  address_id SMALLINT UNSIGNED NOT NULL,
  active BOOLEAN NOT NULL DEFAULT TRUE,
  create_date DATETIME NOT NULL,
  last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY  (customer_id),
  KEY idx_fk_store_id (store_id),
  KEY idx_fk_address_id (address_id),
  KEY idx_last_name (last_name),
  CONSTRAINT fk_customer_address FOREIGN KEY (address_id) REFERENCES address (address_id) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT fk_customer_store FOREIGN KEY (store_id) REFERENCES store (store_id) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Table structure for table `film`
--

CREATE TABLE film (
  film_id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
  title VARCHAR(128) NOT NULL,
  description TEXT DEFAULT NULL,
  release_year YEAR DEFAULT NULL,
  language_id TINYINT UNSIGNED NOT NULL,
  original_language_id TINYINT UNSIGNED DEFAULT NULL,
  rental_duration TINYINT UNSIGNED NOT NULL DEFAULT 3,
  rental_rate DECIMAL(4,2) NOT NULL DEFAULT 4.99,
  length SMALLINT UNSIGNED DEFAULT NULL,
  replacement_cost DECIMAL(5,2) NOT NULL DEFAULT 19.99,
  rating ENUM('G','PG','PG-13','R','NC-17') DEFAULT 'G',
  special_features SET('Trailers','Commentaries','Deleted Scenes','Behind the Scenes') DEFAULT NULL,
  last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY  (film_id),
  KEY idx_title (title),
  KEY idx_fk_language_id (language_id),
  KEY idx_fk_original_language_id (original_language_id),
  CONSTRAINT fk_film_language FOREIGN KEY (language_id) REFERENCES language (language_id) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT fk_film_language_original FOREIGN KEY (original_language_id) REFERENCES language (language_id) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Table structure for table `film_actor`
--

CREATE TABLE film_actor (
  actor_id SMALLINT UNSIGNED NOT NULL,
  film_id SMALLINT UNSIGNED NOT NULL,
  last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY  (actor_id,film_id),
  KEY idx_fk_film_id (`film_id`),
  CONSTRAINT fk_film_actor_actor FOREIGN KEY (actor_id) REFERENCES actor (actor_id) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT fk_film_actor_film FOREIGN KEY (film_id) REFERENCES film (film_id) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Table structure for table `film_category`
--

CREATE TABLE film_category (
  film_id SMALLINT UNSIGNED NOT NULL,
  category_id TINYINT UNSIGNED NOT NULL,
  last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (film_id, category_id),
  CONSTRAINT fk_film_category_film FOREIGN KEY (film_id) REFERENCES film (film_id) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT fk_film_category_category FOREIGN KEY (category_id) REFERENCES category (category_id) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Table structure for table `film_text`
-- 
-- InnoDB added FULLTEXT support in 5.6.10. If you use an
-- earlier version, then consider upgrading (recommended) or 
-- changing InnoDB to MyISAM as the film_text engine
--

-- Use InnoDB for film_text as of 5.6.10, MyISAM prior to 5.6.10.
SET @old_default_storage_engine = @@default_storage_engine;
SET @@default_storage_engine = 'MyISAM';
/*!50610 SET @@default_storage_engine = 'InnoDB'*/;

CREATE TABLE film_text (
  film_id SMALLINT UNSIGNED NOT NULL,
  title VARCHAR(255) NOT NULL,
  description TEXT,
  PRIMARY KEY  (film_id),
  FULLTEXT KEY idx_title_description (title,description)
) DEFAULT CHARSET=utf8mb4;

SET @@default_storage_engine = @old_default_storage_engine;

--
-- Triggers for loading film_text from film
--

DELIMITER ;;
CREATE TRIGGER `ins_film` AFTER INSERT ON `film` FOR EACH ROW BEGIN
    INSERT INTO film_text (film_id, title, description)
        VALUES (new.film_id, new.title, new.description);
  END;;


CREATE TRIGGER `upd_film` AFTER UPDATE ON `film` FOR EACH ROW BEGIN
    IF (old.title != new.title) OR (old.description != new.description) OR (old.film_id != new.film_id)
    THEN
        UPDATE film_text
            SET title=new.title,
                description=new.description,
                film_id=new.film_id
        WHERE film_id=old.film_id;
    END IF;
  END;;


CREATE TRIGGER `del_film` AFTER DELETE ON `film` FOR EACH ROW BEGIN
    DELETE FROM film_text WHERE film_id = old.film_id;
  END;;

DELIMITER ;

--
-- Table structure for table `inventory`
--

CREATE TABLE inventory (
  inventory_id MEDIUMINT UNSIGNED NOT NULL AUTO_INCREMENT,
  film_id SMALLINT UNSIGNED NOT NULL,
  store_id TINYINT UNSIGNED NOT NULL,
  last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY  (inventory_id),
  KEY idx_fk_film_id (film_id),
  KEY idx_store_id_film_id (store_id,film_id),
  CONSTRAINT fk_inventory_store FOREIGN KEY (store_id) REFERENCES store (store_id) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT fk_inventory_film FOREIGN KEY (film_id) REFERENCES film (film_id) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Table structure for table `language`
--

CREATE TABLE language (
  language_id TINYINT UNSIGNED NOT NULL AUTO_INCREMENT,
  name CHAR(20) NOT NULL,
  last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (language_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Table structure for table `payment`
--

CREATE TABLE payment (
  payment_id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
  customer_id SMALLINT UNSIGNED NOT NULL,
  staff_id TINYINT UNSIGNED NOT NULL,
  rental_id INT DEFAULT NULL,
  amount DECIMAL(5,2) NOT NULL,
  payment_date DATETIME NOT NULL,
  last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY  (payment_id),
  KEY idx_fk_staff_id (staff_id),
  KEY idx_fk_customer_id (customer_id),
  CONSTRAINT fk_payment_rental FOREIGN KEY (rental_id) REFERENCES rental (rental_id) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT fk_payment_customer FOREIGN KEY (customer_id) REFERENCES customer (customer_id) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT fk_payment_staff FOREIGN KEY (staff_id) REFERENCES staff (staff_id) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


--
-- Table structure for table `rental`
--

CREATE TABLE rental (
  rental_id INT NOT NULL AUTO_INCREMENT,
  rental_date DATETIME NOT NULL,
  inventory_id MEDIUMINT UNSIGNED NOT NULL,
  customer_id SMALLINT UNSIGNED NOT NULL,
  return_date DATETIME DEFAULT NULL,
  staff_id TINYINT UNSIGNED NOT NULL,
  last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (rental_id),
  UNIQUE KEY  (rental_date,inventory_id,customer_id),
  KEY idx_fk_inventory_id (inventory_id),
  KEY idx_fk_customer_id (customer_id),
  KEY idx_fk_staff_id (staff_id),
  CONSTRAINT fk_rental_staff FOREIGN KEY (staff_id) REFERENCES staff (staff_id) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT fk_rental_inventory FOREIGN KEY (inventory_id) REFERENCES inventory (inventory_id) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT fk_rental_customer FOREIGN KEY (customer_id) REFERENCES customer (customer_id) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Table structure for table `staff`
--

CREATE TABLE staff (
  staff_id TINYINT UNSIGNED NOT NULL AUTO_INCREMENT,
  first_name VARCHAR(45) NOT NULL,
  last_name VARCHAR(45) NOT NULL,
  address_id SMALLINT UNSIGNED NOT NULL,
  picture BLOB DEFAULT NULL,
  email VARCHAR(50) DEFAULT NULL,
  store_id TINYINT UNSIGNED NOT NULL,
  active BOOLEAN NOT NULL DEFAULT TRUE,
  username VARCHAR(16) NOT NULL,
  password VARCHAR(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL,
  last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY  (staff_id),
  KEY idx_fk_store_id (store_id),
  KEY idx_fk_address_id (address_id),
  CONSTRAINT fk_staff_store FOREIGN KEY (store_id) REFERENCES store (store_id) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT fk_staff_address FOREIGN KEY (address_id) REFERENCES address (address_id) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Table structure for table `store`
--

CREATE TABLE store (
  store_id TINYINT UNSIGNED NOT NULL AUTO_INCREMENT,
  manager_staff_id TINYINT UNSIGNED NOT NULL,
  address_id SMALLINT UNSIGNED NOT NULL,
  last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY  (store_id),
  UNIQUE KEY idx_unique_manager (manager_staff_id),
  KEY idx_fk_address_id (address_id),
  CONSTRAINT fk_store_staff FOREIGN KEY (manager_staff_id) REFERENCES staff (staff_id) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT fk_store_address FOREIGN KEY (address_id) REFERENCES address (address_id) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- View structure for view `customer_list`
--

CREATE VIEW customer_list
AS
SELECT cu.customer_id AS ID, CONCAT(cu.first_name, _utf8mb4' ', cu.last_name) AS name, a.address AS address, a.postal_code AS `zip code`,
	a.phone AS phone, city.city AS city, country.country AS country, IF(cu.active, _utf8mb4'active',_utf8mb4'') AS notes, cu.store_id AS SID
FROM customer AS cu JOIN address AS a ON cu.address_id = a.address_id JOIN city ON a.city_id = city.city_id
	JOIN country ON city.country_id = country.country_id;

--
-- View structure for view `film_list`
--

CREATE VIEW film_list
AS
SELECT film.film_id AS FID, film.title AS title, film.description AS description, category.name AS category, film.rental_rate AS price,
	film.length AS length, film.rating AS rating, GROUP_CONCAT(CONCAT(actor.first_name, _utf8mb4' ', actor.last_name) SEPARATOR ', ') AS actors
FROM film LEFT JOIN film_category ON film_category.film_id = film.film_id
LEFT JOIN category ON category.category_id = film_category.category_id LEFT
JOIN film_actor ON film.film_id = film_actor.film_id LEFT JOIN actor ON
  film_actor.actor_id = actor.actor_id
GROUP BY film.film_id, category.name;

--
-- View structure for view `nicer_but_slower_film_list`
--

CREATE VIEW nicer_but_slower_film_list
AS
SELECT film.film_id AS FID, film.title AS title, film.description AS description, category.name AS category, film.rental_rate AS price,
	film.length AS length, film.rating AS rating, GROUP_CONCAT(CONCAT(CONCAT(UCASE(SUBSTR(actor.first_name,1,1)),
	LCASE(SUBSTR(actor.first_name,2,LENGTH(actor.first_name))),_utf8mb4' ',CONCAT(UCASE(SUBSTR(actor.last_name,1,1)),
	LCASE(SUBSTR(actor.last_name,2,LENGTH(actor.last_name)))))) SEPARATOR ', ') AS actors
FROM film LEFT JOIN film_category ON film_category.film_id = film.film_id
LEFT JOIN category ON category.category_id = film_category.category_id LEFT
JOIN film_actor ON film.film_id = film_actor.film_id LEFT JOIN actor ON
  film_actor.actor_id = actor.actor_id
GROUP BY film.film_id, category.name;

--
-- View structure for view `staff_list`
--

CREATE VIEW staff_list
AS
SELECT s.staff_id AS ID, CONCAT(s.first_name, _utf8mb4' ', s.last_name) AS name, a.address AS address, a.postal_code AS `zip code`, a.phone AS phone,
	city.city AS city, country.country AS country, s.store_id AS SID
FROM staff AS s JOIN address AS a ON s.address_id = a.address_id JOIN city ON a.city_id = city.city_id
	JOIN country ON city.country_id = country.country_id;

--
-- View structure for view `sales_by_store`
--

CREATE VIEW sales_by_store
AS
SELECT
CONCAT(c.city, _utf8mb4',', cy.country) AS store
, CONCAT(m.first_name, _utf8mb4' ', m.last_name) AS manager
, SUM(p.amount) AS total_sales
FROM payment AS p
INNER JOIN rental AS r ON p.rental_id = r.rental_id
INNER JOIN inventory AS i ON r.inventory_id = i.inventory_id
INNER JOIN store AS s ON i.store_id = s.store_id
INNER JOIN address AS a ON s.address_id = a.address_id
INNER JOIN city AS c ON a.city_id = c.city_id
INNER JOIN country AS cy ON c.country_id = cy.country_id
INNER JOIN staff AS m ON s.manager_staff_id = m.staff_id
GROUP BY s.store_id
ORDER BY cy.country, c.city;

--
-- View structure for view `sales_by_film_category`
--
-- Note that total sales will add up to >100% because
-- some titles belong to more than 1 category
--

CREATE VIEW sales_by_film_category
AS
SELECT
c.name AS category
, SUM(p.amount) AS total_sales
FROM payment AS p
INNER JOIN rental AS r ON p.rental_id = r.rental_id
INNER JOIN inventory AS i ON r.inventory_id = i.inventory_id
INNER JOIN film AS f ON i.film_id = f.film_id
INNER JOIN film_category AS fc ON f.film_id = fc.film_id
INNER JOIN category AS c ON fc.category_id = c.category_id
GROUP BY c.name
ORDER BY total_sales DESC;

--
-- View structure for view `actor_info`
--

CREATE DEFINER=CURRENT_USER SQL SECURITY INVOKER VIEW actor_info
AS
SELECT
a.actor_id,
a.first_name,
a.last_name,
GROUP_CONCAT(DISTINCT CONCAT(c.name, ': ',
		(SELECT GROUP_CONCAT(f.title ORDER BY f.title SEPARATOR ', ')
                    FROM sakila.film f
                    INNER JOIN sakila.film_category fc
                      ON f.film_id = fc.film_id
                    INNER JOIN sakila.film_actor fa
                      ON f.film_id = fa.film_id
                    WHERE fc.category_id = c.category_id
                    AND fa.actor_id = a.actor_id
                 )
             )
             ORDER BY c.name SEPARATOR '; ')
AS film_info
FROM sakila.actor a
LEFT JOIN sakila.film_actor fa
  ON a.actor_id = fa.actor_id
LEFT JOIN sakila.film_category fc
  ON fa.film_id = fc.film_id
LEFT JOIN sakila.category c
  ON fc.category_id = c.category_id
GROUP BY a.actor_id, a.first_name, a.last_name;

--
-- Procedure structure for procedure `rewards_report`
--

DELIMITER //

CREATE PROCEDURE rewards_report (
    IN min_monthly_purchases TINYINT UNSIGNED
    , IN min_dollar_amount_purchased DECIMAL(10,2)
    , OUT count_rewardees INT
)
LANGUAGE SQL
NOT DETERMINISTIC
READS SQL DATA
SQL SECURITY DEFINER
COMMENT 'Provides a customizable report on best customers'
proc: BEGIN

    DECLARE last_month_start DATE;
    DECLARE last_month_end DATE;

    /* Some sanity checks... */
    IF min_monthly_purchases = 0 THEN
        SELECT 'Minimum monthly purchases parameter must be > 0';
        LEAVE proc;
    END IF;
    IF min_dollar_amount_purchased = 0.00 THEN
        SELECT 'Minimum monthly dollar amount purchased parameter must be > $0.00';
        LEAVE proc;
    END IF;

    /* Determine start and end time periods */
    SET last_month_start = DATE_SUB(CURRENT_DATE(), INTERVAL 1 MONTH);
    SET last_month_start = STR_TO_DATE(CONCAT(YEAR(last_month_start),'-',MONTH(last_month_start),'-01'),'%Y-%m-%d');
    SET last_month_end = LAST_DAY(last_month_start);

    /*
        Create a temporary storage area for
        Customer IDs.
    */
    CREATE TEMPORARY TABLE tmpCustomer (customer_id SMALLINT UNSIGNED NOT NULL PRIMARY KEY);

    /*
        Find all customers meeting the
        monthly purchase requirements
    */
    INSERT INTO tmpCustomer (customer_id)
    SELECT p.customer_id
    FROM payment AS p
    WHERE DATE(p.payment_date) BETWEEN last_month_start AND last_month_end
    GROUP BY customer_id
    HAVING SUM(p.amount) > min_dollar_amount_purchased
    AND COUNT(customer_id) > min_monthly_purchases;

    /* Populate OUT parameter with count of found customers */
    SELECT COUNT(*) FROM tmpCustomer INTO count_rewardees;

    /*
        Output ALL customer information of matching rewardees.
        Customize output as needed.
    */
    SELECT c.*
    FROM tmpCustomer AS t
    INNER JOIN customer AS c ON t.customer_id = c.customer_id;

    /* Clean up */
    DROP TABLE tmpCustomer;
END //

DELIMITER ;

DELIMITER $$

CREATE FUNCTION get_customer_balance(p_customer_id INT, p_effective_date DATETIME) RETURNS DECIMAL(5,2)
    DETERMINISTIC
    READS SQL DATA
BEGIN

       #OK, WE NEED TO CALCULATE THE CURRENT BALANCE GIVEN A CUSTOMER_ID AND A DATE
       #THAT WE WANT THE BALANCE TO BE EFFECTIVE FOR. THE BALANCE IS:
       #   1) RENTAL FEES FOR ALL PREVIOUS RENTALS
       #   2) ONE DOLLAR FOR EVERY DAY THE PREVIOUS RENTALS ARE OVERDUE
       #   3) IF A FILM IS MORE THAN RENTAL_DURATION * 2 OVERDUE, CHARGE THE REPLACEMENT_COST
       #   4) SUBTRACT ALL PAYMENTS MADE BEFORE THE DATE SPECIFIED

  DECLARE v_rentfees DECIMAL(5,2); #FEES PAID TO RENT THE VIDEOS INITIALLY
  DECLARE v_overfees INTEGER;      #LATE FEES FOR PRIOR RENTALS
  DECLARE v_payments DECIMAL(5,2); #SUM OF PAYMENTS MADE PREVIOUSLY

  SELECT IFNULL(SUM(film.rental_rate),0) INTO v_rentfees
    FROM film, inventory, rental
    WHERE film.film_id = inventory.film_id
      AND inventory.inventory_id = rental.inventory_id
      AND rental.rental_date <= p_effective_date
      AND rental.customer_id = p_customer_id;

  SELECT IFNULL(SUM(IF((TO_DAYS(rental.return_date) - TO_DAYS(rental.rental_date)) > film.rental_duration,
        ((TO_DAYS(rental.return_date) - TO_DAYS(rental.rental_date)) - film.rental_duration),0)),0) INTO v_overfees
    FROM rental, inventory, film
    WHERE film.film_id = inventory.film_id
      AND inventory.inventory_id = rental.inventory_id
      AND rental.rental_date <= p_effective_date
      AND rental.customer_id = p_customer_id;


  SELECT IFNULL(SUM(payment.amount),0) INTO v_payments
    FROM payment

    WHERE payment.payment_date <= p_effective_date
    AND payment.customer_id = p_customer_id;

  RETURN v_rentfees + v_overfees - v_payments;
END $$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE film_in_stock(IN p_film_id INT, IN p_store_id INT, OUT p_film_count INT)
READS SQL DATA
BEGIN
     SELECT inventory_id
     FROM inventory
     WHERE film_id = p_film_id
     AND store_id = p_store_id
     AND inventory_in_stock(inventory_id);

     SELECT COUNT(*)
     FROM inventory
     WHERE film_id = p_film_id
     AND store_id = p_store_id
     AND inventory_in_stock(inventory_id)
     INTO p_film_count;
END $$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE film_not_in_stock(IN p_film_id INT, IN p_store_id INT, OUT p_film_count INT)
READS SQL DATA
BEGIN
     SELECT inventory_id
     FROM inventory
     WHERE film_id = p_film_id
     AND store_id = p_store_id
     AND NOT inventory_in_stock(inventory_id);

     SELECT COUNT(*)
     FROM inventory
     WHERE film_id = p_film_id
     AND store_id = p_store_id
     AND NOT inventory_in_stock(inventory_id)
     INTO p_film_count;
END $$

DELIMITER ;

DELIMITER $$

CREATE FUNCTION inventory_held_by_customer(p_inventory_id INT) RETURNS INT
READS SQL DATA
BEGIN
  DECLARE v_customer_id INT;
  DECLARE EXIT HANDLER FOR NOT FOUND RETURN NULL;

  SELECT customer_id INTO v_customer_id
  FROM rental
  WHERE return_date IS NULL
  AND inventory_id = p_inventory_id;

  RETURN v_customer_id;
END $$

DELIMITER ;

DELIMITER $$

CREATE FUNCTION inventory_in_stock(p_inventory_id INT) RETURNS BOOLEAN
READS SQL DATA
BEGIN
    DECLARE v_rentals INT;
    DECLARE v_out     INT;

    #AN ITEM IS IN-STOCK IF THERE ARE EITHER NO ROWS IN THE rental TABLE
    #FOR THE ITEM OR ALL ROWS HAVE return_date POPULATED

    SELECT COUNT(*) INTO v_rentals
    FROM rental
    WHERE inventory_id = p_inventory_id;

    IF v_rentals = 0 THEN
      RETURN TRUE;
    END IF;

    SELECT COUNT(rental_id) INTO v_out
    FROM inventory LEFT JOIN rental USING(inventory_id)
    WHERE inventory.inventory_id = p_inventory_id
    AND rental.return_date IS NULL;

    IF v_out > 0 THEN
      RETURN FALSE;
    ELSE
      RETURN TRUE;
    END IF;
END $$

DELIMITER ;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;


---------------------------------------------------------------------
#16,03,2024
-- ------------------------------------------------------------------------------------------------------------------------

use sakila

select * from city 

select * from country

select city_id, country_id from city 

select country_id, city_id from city 

select c.country_id, c.city_id from city c #aliansy

select city_id as "id miasta", city as "miasto" from city

select city_id as "id miasta", city as "miasto" from city limit 5 #(top 5 rekordów)

select city_id as "id miasta", city as "miasto" from city order by city asc #(sort rosnąco)

select city_id as "id miasta", city as "miasto" from city order by city desc #(sort malejąco)

select * from city where city = "Bydgoszcz"

select * from city where city = "Bydgoszcz" or city = "Dallas"

select * from city where city = "Bydgoszcz" and city_id = 2 #(warunek nie użyteczny ponieważ ma być ID=2 a nazwa = Bydgoszcz)

select city as "nazwa_miasta", country_id as "ID_miasta" from city where city = "Bydgoszcz" or country_id = 2 limit 2,4

select city as "nazwa_miasta", country_id from city where city = "Bydgoszcz" or country_id = 2 order by city desc

select city_id, city from city where city_id  != 1

select * from city where city_id > 3 and city < 10

select * from city where city_id between 3 and 10 order by city desc 

select * from city where city like "Ad%" #(Miasta zaczynają się na "Ad")

select * from city where city like "%na"  #(Miasta kończą się na "na")

select * from city where (city like "%na" and country_id = 97) or (city  = "Bydgoszcz" or country_id = 20)
-- ------------------------------------------------------------------------------------------------------------------------

# Pobierz wszystkie rekordy z tabeli city
select * from city

# Pobierz rekord z tabeli city gdzie nazwa miast jest równa Moscow
select * from city where city = "Moscow"

# Pobierz wszystkie miasta zaczynające się na literę A
select city as "nazwa_miasta" from city where city like "A%" order by city asc 

# Pobierz wszystkie miasta kończące się na litery at, posortuj je malejąco po city_id
select city as "nazwa_miasta_end=at", city_id as "ID_miast" from city where city like "%at" order by city desc  

# Pobierz tylko nazwę miasta zamiast całego rekordy dla dowolnego warunku.
select city as "tylko_nazwa" from city c
-- ------------------------------------------------------------------------------------------------------------------------

select * from city where city = 'London'

select distinct * from city where city = 'London'

select distinct city from city where city = 'London' #(Usuwanie diplikatów)

select country_id, last_update from city where country_id = 103  

select country_id, last_update from city where country_id between 101 and 103

select distinct country_id, last_update from city where country_id between 101 and 103

select * from city where city = "London" or city = "Bydgoszcz" order by city desc, country_id asc #(sortowanie rosnąco a malejąco)
 
select * from city where city_id = 3 or city_id = 4 or city_id = 5 # --------------------> ALBO #------------------------->

select * from city where city_id in (3,4,5) #lepiej wygląda

select * from city where city_id not in (3,4,5)

#Grupowanie Danych
select country_id from city where country_id between 101 and 103 
group by country_id, last_update #(Grupowanie wg warunków)

#Obliczanie średniej

select * from film

select rating, replacement_cost from film

select rating, avg(replacement_cost) from film # ratingi a średni koszt filmów
where rating in ("PG", "G") # wg ratingów PG a G
group by rating # grupowanie na ratingi (podział na dwie kolumny)

select rating, min(replacement_cost) as "min_cost", max(replacement_cost) as "max_cost" from film  # minimalna a maksymalna cena
group by rating

select rating, avg(replacement_cost) from film 
group by rating
having avg(replacement_cost) < 20

select rating, count(replacement_cost) as "ilość_rekordów" from film  # count pokazule ilość rekordów
group by rating

select rating, sum(replacement_cost) as "suma" from film  # sum pokazule summę rekordów
group by rating
-- ------------------------------------------------------------------------------------------------------------------------

select city from city where city = "London"

select city from city where city = "London"
group by city

select distinct city from city where city = "London"
-- ------------------------------------------------------------------------------------------------------------------------

select * from film f 

select rating, avg(length) as "Długość" from film f where rating = "PG-13"
group by rating

select rating, min(`length`) as "Minimalna_długość", max(length) as "Maksymalna_długość" from film f where rating = "PG-13" or rating = "G"
group by rating

select sum(length) as "Suma_długości" from film f  

select count(title) as "Ilość_filmów" from film f 
-- ------------------------------------------------------------------------------------------------------------------------

select avg(length) as "Średnia" from film f 
where rating in ("PG", "PG-13")

select rating, avg(length) as "Średnia" from film f 
where rating in ("PG", "PG-13")
group by rating  
-- ------------------------------------------------------------------------------------------------------------------------

#NULL
select * from staff s 

select * from staff s where password != "test" or password is null

select * from staff s where password is not null 

select * from city c where country_id = 87

select city, country from city
inner join country on city.country_id = country.country_id  
order by city.city_id

select * from city
inner join country on city.city_id = country.country_id  #Zle!!!!!!!!!!!!!!
order by city.city_id

select city, country from city
inner join country on city.country_id = country.country_id
where country = "Poland"
order by city.city_id
-- ------------------------------------------------------------------------------------------------------------------------

select country_id from city # nie wiadomo, o którym ID chodzi
inner join country on city.country_id = country.country_id
where country = "Poland"
order by city.city_id

select city.country_id from city # wiadomo, o którym ID chodzi
inner join country on city.country_id = country.country_id
where country = "Poland"
order by city.city_id
-- ------------------------------------------------------------------------------------------------------------------------

select address.address 'ulica', 
address.postal_code 'kod_pocztowy', 
city.city 'nazwa_miasta', 
country.country 'nazwa_miast'
from address
join city ON city.city_id = address.city_id
join country on country.country_id = city.country_id
order by city.city

select * from city 

select * from country
-- ------------------------------------------------------------------------------------------------------------------------

select city 'Miasto', country 'Państwo' from city
join country on city.country_id = country.country_id
where country = "Poland" or country = "Australia" or country = "France"
order by city.city 
-- ------------------------------------------------------------------------------------------------------------------------

#????????????????????????????????
# * Zbuduj zapytanie łączące kategorie z filmami wyświetl tylko i wyłączeni film oraz nazwę kategorii

select * from film

select title 'Nazwa', name 'Kategoria' from film
join film_category on film.film_id  = film_category.film_id
join category on category.category_id = film_category.category_id  
order by category.name
-- ------------------------------------------------------------------------------------------------------------------------

use sakila

ALTER TABLE sakila.city MODIFY COLUMN country_id smallint unsigned NULL;
update city set country_id = null where city_id  in (4,5);

select * from city
-- ------------------------------------------------------------------------------------------------------------------------

#1
select city 'nazwa_miasta', country 'nazwa_kraju' from city
left join country on city.country_id = country.country_id 

select city 'nazwa_miasta', country 'nazwa_kraju' from city
right join country on city.country_id = country.country_id

#2
select film.title 'nazwa_filmu', actor.first_name 'imie_aktoru', actor.last_name 'nazwisko_aktoru' from film
join film_actor on film.film_id = film_actor.film_id
join actor on film_actor.actor_id = actor.actor_id

#3

select rating, 
min(length) 'min_długośc', 
max(length) 'max_długośc',
avg(length) 'średnia_długość',
sum(length) 'sum_długości' from film
group by rating
-- ------------------------------------------------------------------------------------------------------------------------

#1
create view 1_dane_stat_films as
select rating, 
min(length) 'min_długośc', 
max(length) 'max_długośc',
avg(length) 'średnia_długość',
sum(length) 'sum_długości' from film
group by rating

create view 1_aktory_w_filmach as
select film.title 'nazwa_filmu', actor.first_name 'imie_aktoru', actor.last_name 'nazwisko_aktoru' from film
join film_actor on film.film_id = film_actor.film_id
join actor on film_actor.actor_id = actor.actor_id

create view 1_miasta_i_kraje as
select city 'nazwa_miasta', country 'nazwa_kraju' from city
left join country on city.country_id = country.country_id 

#2
select * from `1_aktory_w_filmach`
where nazwa_filmu = 'ACADEMY DINOSAUR' or nazwisko_aktoru = "CHASE" limit 5

select * from `1_dane_stat_films`
where max_długośc >= 185 and rating != 'PG'
-- ------------------------------------------------------------------------------------------------------------------------


#17,03
-- ------------------------------------------------------------------------------------------------------------------------
create database hr_database

use hr_database

create table if not exists departments(
	id integer auto_increment primary key,
	name varchar(50) not null
);

create table if not exists employees (
	id integer auto_increment primary key,
	first_name varchar(50) not null,
	last_name varchar(50) not null,
	department_id int,
	foreign key (department_id) references departments (id)
);

select * from  employees e 

select * from departments d 
-- ------------------------------------------------------------------------------------------------------------------------

# Dodawanie danych do departments
insert into departments (name) values ('HR')

insert into departments (name) values ('Finanse')

select * from departments d 
-- ------------------------------------------------------------------------------------------------------------------------

# Dodawanie danych do employess
insert into employees (first_name, last_name, department_id) values ('Adam', 'Kowalski', 1)

insert into employees (first_name, last_name, department_id) values ('Jan', 'Nowak', 1)

insert into employees (first_name, last_name, department_id) values ('Anna', 'Kowal', NULL)

select * from  employees e 
-- ------------------------------------------------------------------------------------------------------------------------

select first_name as 'imie', last_name as 'nazwisko', name as 'dział'
from employees
left join departments on employees.department_id = departments.id # pokazuje wszystkich pracowników wraz z NULL departmentsami 

select first_name as 'imie', last_name as 'nazwisko', name as 'dział'
from employees
right join departments on employees.department_id = departments.id # pokazuje wszystkie departamenty wraz z NULL pracownikami
-- ------------------------------------------------------------------------------------------------------------------------

use hr_database

select * from employees

alter table employees add column age int not null after last_name

alter table employees drop column age

alter table employees add column nip varchar(20) not null 

alter table employees modify column nip varchar(50) null

alter table employees modify column first_name varchar(3) not null

alter table employees rename workers

alter table workers rename employees

alter table employees drop foreign key employees_ibfk_1

alter table employees add constraint FK_employees_departments foreign key (id_department) references departments (id)

create table customers(
	id int primary key auto_increment,
	name varchar(50) not null,
	employee_assigned_id int not null,
	constraint FK_customers_employees foreign key (employee_assigned_id) references employees(id)
)

drop table customers
-- ------------------------------------------------------------------------------------------------------------------------

select * from employees e 

insert into employees values (50,'Jan','Nowak',34, 2, '124142421')

insert into employees (first_name, last_name, age, id_department , nip) values ('Piotr','Nowak',34, 2, '124142421')

insert into employees (first_name, last_name, age, id_department , nip) values ('Piotr','Kowalski',34, 2, '124142421'), ('Anna','Kowalska',34, 56, '124142421')

insert into employees (first_name, last_name,  id_department , nip)  values ('Piotr','Nowak', 2, '124142421')

select * from departments d 

update departments set name = 'IT' where id =3

select * from employees e 

select * from employees e where last_name ='Kowalski'

update employees set last_name = 'Kowalczyk', age=36 where last_name ='Kowalski'

update employees set age = 20

select * from employees e where id = 53 or id = 52

delete from employees where id = 53 or id = 52

delete from employees 


create database Zadanie

use Zadanie

create table if not exists companies (
	id int auto_increment primary key,
	trade varchar(40) not null,
	number_of_employees integer default 0 not null 
)

# drop table companies

create table if not exists job_offers (
	id integer auto_increment primary key,
	offer_title varchar(40) not null,
	offer_min_salary decimal,
	offer_max_salary decimal
)

drop table job_offers

create table if not exists candidates (
	id integer auto_increment primary key,
	first_name varchar(40) not null,
	last_name varchar(40) not null,
	email varchar(30) not null,
	phone_number varchar(12),
	job_offer_id int,
	constraint FK_joboffers_candidates foreign key (job_offer_id) references job_offers (id),
	company_id int,
	constraint FK_companies_candidates foreign key (company_id) references companies (id)
)

# drop table candidates
-- ----------------------------------------------------------------------------------------------------------------

#1 DANE

insert into companies values 
(1, "Google", 135301), 
(2, "Apple", 161000), 
(3, "Amazon", 1500000), 
(4, "UPS", 500000), 
(5, "XBox", 10000)

insert into job_offers values 
(1, 'Test Automation Engineer', 500, 1000)
(2, 'IT Engineer', 2000, 10000), 
(3, 'Administrator ERP', 1500, 7000), 
(4, 'React Developer', 900, 8000), 
(5, 'Server Systems Administrator', 800, 5500),  
(6, 'Scrum Master', 1000, 15000), 
(7, 'DevOps', 5000, 50000)

insert into candidates values
(1,'Ivan', 'konopko', 'ivan.drop@gmail.com', '514698752', 7, 5),
(2,'Tatiana', 'Marinara', 'tatiana.Mari99@gmail.com',null, 3, 2),
(3,'Den', 'Sausa', 'ivDeNp99@gmail.com', '324696472', 4, 4),
(4,'Artem', 'Laula', 'Artem.zopa2343.upr@gmail.com', '564598756', 5, 2),
(5,'Ihor', 'Ruchk', 'ihor.ruchk@gmail.com', null, 7, 5),
(6,'Ranie', 'Lapuch', 'LochLap23@gmail.com', '489698654', 6, 5),
(7,'Iraque', 'Keps', 'Ir.Ke92@gmail.com', '514698365', 6, 4),
(8,'Soha', 'Davar', 'Soh.Ad@gmail.com', '485398732', 4, 3),
(9,'Vaha', 'Labada', 'KakashkaJa.Labada@gmail.com', '517695658', 3, 3),
(10,'Grigorij', 'Leps', 'grisha1@gmail.com', '524658556', 5, 5),
(11, 'Mateusz', 'Matejaszczuk', 'idr0pop@gmail.com', '415668765', 4, 2),
(12,'Paweł', 'Prosty', 'IchRa98@gmail.com', '454658232', 5, 1),
(13,'Ivan', 'Zarown', 'ivopar2@gmail.com', '145588648', 4, 1),
(14,'Artem', 'Kruk', 'artem.kruk@gmail.com', null, 2, 2),
(15,'Tatiana', 'Chushko', 'iv4Ola3@gmail.com', '515298558', 3, 2),
(16,'Taisiia', 'Huseih', 'mojapochta1@gmail.com', '144558762', 2, 4),
(17,'Oliwer', 'Ihotr', 'oliwer.ohotr20@gmail.com', null, 7, 3),
(18,'Artem', 'Mahet', 'Drozd123.fd@gmail.com', '525626736', 1, 5),
(19,'Ignat', 'Dobry', 'deRaca45@gmail.com', '534636736', 1, 5)
-- ----------------------------------------------------------------------------------------------------------------

#2 UPDATE

update candidates set first_name = 'Vasya' where id = 14

update job_offers set offer_min_salary = 6000 where offer_title = 'DevOps'

update job_offers set offer_max_salary = 8000 where id = 1
-- ----------------------------------------------------------------------------------------------------------------

#4 DELETE

delete from candidates where id = 14

delete from candidates where last_name = 'Dobry'

delete from candidates where first_name = 'Den'
-- ----------------------------------------------------------------------------------------------------------------

# 23,03,2024
# 5a

select concat(first_name, ' ' , last_name) as 'full_name' from employees e #separator trzeba dopisac

select concat_ws(' ', first_name, last_name) as 'full_name' from employees e #wraz z separatorem 

select concat_ws('_', 'imie: ', first_name, 'nazwisko: ', last_name) as 'full_name' from employees e # _ws

select last_name, substring(last_name, 2, 23) from employees e 


select last_name, substring(last_name,-5, 2) from employees e 

select first_name, last_name, name,
concat_ws(',',first_name, last_name, name)
from employees 
inner join departments  on employees.id_department = departments.id 
where name = 'HR'

FV 34212/03/24

select *, replace(name,'HR','Human resources' ) from departments d 

select nip,
case when nip = '' then 'brak nipu'
else 'nip wypelniony' end as 'nip_info'
from employees 


select first_name, last_name,
case when age < 20 then 'mlodszy specjalista'
when age >= 20 and age < 30 then 'specjalista'
else 'starszy specjalista' end as 'status'
from employees e 

update employees set age = 32 where id = 2

update employees set age = 19 where id = 5

update employees set last_name = 'Niwak' where id = 6

select id,first_name, last_name from employees where last_name  like 'N_w%'
-- ----------------------------------------------------------------------------------------------------------------

use hr_database

create table patients (
	id int auto_increment primary key,
	name varchar(50) not null,
	surname varchar(50) not null,
	tax_identifier varchar(20) unique 
)

create table libary (
	id int auto_increment primary key,
	lib_date_time datetime not null,
	lib_number varchar(20) not null,
	patients_id int not null,
	constraint FK_orders_patients foreign key (patients_id) references patients(id)
)

create table products(
	id int auto_increment primary key,
	name varchar(50) not null,
	description varchar(255)
)


create table order_items(
	id int auto_increment primary key,
	product_id int not null,
	net_price decimal not null,
	vat_rate int not null default 23,
	constraint FK_product_orderitems foreign key (product_id) references products(id)
)

create table warehouses(
	id int auto_increment primary key,
	name varchar(20) unique not null
)

create table product_stocks(
	product_id int not null,
	warehouse_id int not null,
	stock decimal,
	primary key(product_id, warehouse_id),
	constraint FK_product_productstocks foreign key (product_id) references products(id),
	constraint FK_warehouse_productstocks foreign key (warehouse_id) references warehouses(id)
)
-- ----------------------------------------------------------------------------------------------------------------

# 5b

insert into patients values 
(1,'Ivan', 'konopko', 'ue514698752'),
(2,'Tatiana', 'Marinara', 'ue154256985'),
(3,'Den', 'Sausa', 'ue324696472'),
(4,'Artem', 'Laula', 'ue564598756'),
(5,'Ihor', 'Ruchk', 'ue123569856'),
(6,'Ranie', 'Lapuch', 'ue489698654'),
(7,'Iraque', 'Keps', 'ue514698365'),
(8,'Soha', 'Davar', 'ue485398732'),
(9,'Vaha', 'Labada', 'ue517695658'),
(10,'Grigorij', 'Leps', 'by524658556'),
(11, 'Mateusz', 'Matejaszczuk','by415668765'),
(12,'Paweł', 'Prosty', 'ue454658232'),
(13,'Ivan', 'Zarown', 'jp145588648'),
(14,'Artem', 'Kruk', 'ue156956365'),
(15,'Tatiana', 'Chushko', 'ue515298558'),
(16,'Taisiia', 'Huseih', 'ju144558762'),
(17,'Oliwer', 'Ihotr', 'ue154856666'),
(18,'Artem', 'Mahet', 'ue525626736'),
(19,'Ignat', 'Dobry', 'ue534636736')

insert into libary values
(1, '2015-12-25 15:32:06.427', 'Str40_45', 4),
(2, '2016-02-20 10:00:06.000', 'Str41_40', 1),
(3, '2015-11-22 09:30:46.009', 'Str42_40', 19),
(4, '2014-12-10 06:00:23.055', 'Str44_40', 19),
(5, '2010-10-02 22:06:16.020', 'Str45_40', 14),
(6, '2010-04-06 23:00:08.000', 'Str44_40', 5),
(7, '2012-03-17 05:40:00.030', 'Str44_40', 6),
(8, '2016-05-24 12:08:54.450', 'Str48_40', 8),
(9, '2013-12-19 16:04:50.040', 'Str49_40', 18),
(10, '2020-10-08 18:20:08.050', 'Str41_40', 19)

insert into products values
(1, 'Product_1', 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. '),
(2, 'Product_2', 'Lorem Ipsum has been the industrys standard dummy text ever since the 1500s.'),
(3, 'produkt_3', 'When an unknown printer took a galley of type and scrambled it to make a type specimen book.')


insert into order_items values
(1, 3, 2500, 23),
(2, 2, 2000, 23),
(3, 1, 2050, 23),
(4, 1, 220, 23),
(5, 2, 200, 23),
(6, 3, 1500, 23)

insert into warehouses  values
(1, 'GoSpot'),
(2, 'Potar'),
(3, 'RatyRat'),
(4, 'Uert')

insert into product_stocks values
(1, 2, 9000),
(2, 2, 1000),
(3, 4, 500),
(3, 1, 1500)
-- ----------------------------------------------------------------------------------------------------------------

 select * from product_stocks ps 

truncate table product_stocks

select * from products 

select * from warehouses w 

insert into product_stocks (product_id, warehouse_id, stock) values (1,1, 10)

insert into product_stocks (product_id, warehouse_id, stock) values (1,2,5)


start transaction
update product_stocks set stock = stock - 10 where product_id =1 and warehouse_id  =1
update product_stocks set stock = stock + 10 where product_id = 1 and warehouse_id  = 2

select * from product_stocks ps 

commit

rollback

-- ----------------------------------------------------------------------------------------------------------------

select * from product_stocks ps 

select * from customers c 

DE213213321 = DE213213321
PL32132132 = 32132132


DELIMITER $$
create trigger clean_tax_identifier_before_insert
before insert on customers
for each row 
begin 
	if substring(new.tax_identifier, 1, 2) = 'PL' then
		set new.tax_identifier = replace(new.tax_identifier, 'PL', '');
	end if;
end
$$

DELIMITER ;

insert into customers (name, tax_identifier) values ('Firma test 1', 'DE213213321')

select * from customers c 

insert into customers (name, tax_identifier) values ('Firma test 2', 'PL213213321')

update customers set tax_identifier = 'PL213213321' where name = 'Firma test 2'

DELIMITER $$
create trigger clean_tax_identifier_before_update
before update on customers
for each row 
begin 
	if substring(new.tax_identifier, 1, 2) = 'PL' then
		set new.tax_identifier = replace(new.tax_identifier, 'PL', '');
	end if;
end
$$

DELIMITER ;

select * from orders

create table order_statuses(
 id int auto_increment primary key,
 name varchar(20) not null unique
)

alter table orders add order_status int 

alter table orders add constraint FK_order_order_status foreign key (order_status) references order_statuses(id)

insert into order_statuses(name) values ('Nowe'),('Realizowane'),('Zakonczone')

DELIMITER $$
create trigger set_new_order_status_before_insert
before insert on orders
for each row
begin 
	declare statusid INT;
	select id into statusid from order_statuses where name = 'Nowe';
	set new.order_status = statusid; 
end
$$
DELIMITER ;

select * from order_statuses

insert into orders(order_date_time, order_number, customer_id, order_status)
values ('2024-01-01 02:02', 'Order 123', 1, 3)

select * from orders

-- ----------------------------------------------------------------------------------------------------------
select * from customers c 

DELIMITER $$
create function VerifyTaxIdentifier (tax_identifier varchar(20))
returns varchar(150)
deterministic 
begin
	if substring(tax_identifier, 1, 2) = 'DE' then
		return 'Nip niemiecki';
	else 
		return 'Nip polski';
	end if;
end
$$

DELIMITER ;

select VerifyTaxIdentifier('DE21321')

select *, VerifyTaxIdentifier(c.tax_identifier) from customers c 

select * from product_stocks ps 

DELIMITER $$

create procedure UpdateOrInsertProductStock(
	in _product_id INT,
	in _warehouse_id int,
	in _stock decimal
)
begin
	if exists (select * from product_stocks where product_id = _product_id and warehouse_id = _warehouse_id) then	
		update product_stocks set stock = _stock where product_id = _product_id and warehouse_id = _warehouse_id;
	else
		insert into product_stocks (product_id, warehouse_id,stock) values (_product_id, _warehouse_id, _stock);	
	end if;
end
$$

DELIMITER ;


select * from product_stocks ps 

select * from warehouses w 

select * from products p 

call UpdateOrInsertProductStock(1,1,50)

