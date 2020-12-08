CREATE DATABASE Horse_shelter
GO
USE Horse_shelter
GO

CREATE TABLE versions
(
	Vid INT PRIMARY KEY IDENTITY,
	version_number INT
);

INSERT INTO versions(version_number)
VALUES (0);

CREATE TABLE groomers
(
	id_groomer int,
	groomer_name varchar(255),
	age int,
	phone_number int
);

CREATE TABLE breeds
(
	id_breed int,
	breed_name varchar(255)
);

CREATE TABLE colors
(
	id_color int,
	color_name varchar(255)
);

CREATE TABLE paddocks
(
	id_paddock int,
	number_of_horses varchar(255)
);

CREATE TABLE medSuplier
(
	id_medSuplier int,
	medSuplier_name varchar(255),
);

CREATE TABLE medicine
(
	id_medicine int,
	medicine_name varchar(255),
	id_medSuplier int
);


CREATE TABLE adopters
(
	id_adopter int,
	adopter_name varchar(255),
	home_address int,
	phone_number int
);

CREATE TABLE adoptions
(
	id_horse int,
	id_adopter int,
	date_of_adootion int
);

CREATE TABLE disease
(
	id_disease int,
	disease_name varchar(255),
);

CREATE TABLE treatment
(
	id_medicine int,
	id_disease int,
	treatment_period int
);

CREATE TABLE horses 
(
	id_horse int,
	horse_name varchar(255),
	age int,
	id_breed int,
	id_color int,
	id_desease int,
	id_groomer int,
	is_adopted bit,
	id_paddock int
);

ALTER TABLE adopters ADD CONSTRAINT df_16 DEFAULT 16 FOR age;

ALTER TABLE horses
ALTER COLUMN id_horse INT NOT NULL;
ALTER TABLE horses
ADD PRIMARY KEY (id_horse);

ALTER TABLE groomers
ALTER COLUMN id_groomer INT NOT NULL;
ALTER TABLE groomers
ADD CONSTRAINT pk_groomer PRIMARY KEY (id_groomer);

ALTER TABLE breeds
ALTER COLUMN id_breed INT NOT NULL;
ALTER TABLE breeds
ADD PRIMARY KEY (id_breed);

ALTER TABLE colors
ALTER COLUMN id_color INT NOT NULL;
ALTER TABLE colors
ADD PRIMARY KEY (id_color);

ALTER TABLE paddocks
ALTER COLUMN id_paddock INT NOT NULL;
ALTER TABLE paddocks
ADD PRIMARY KEY (id_paddock);

ALTER TABLE medicine
ALTER COLUMN id_medicine INT NOT NULL;
ALTER TABLE medicine
ADD PRIMARY KEY (id_medicine);

ALTER TABLE medSuplier
ALTER COLUMN id_medSuplier INT NOT NULL;
ALTER TABLE medSuplier
ADD PRIMARY KEY (id_medSuplier);

ALTER TABLE adopters
ALTER COLUMN id_adopter INT NOT NULL;
ALTER TABLE adopters
ADD PRIMARY KEY (id_adopter);

ALTER TABLE adopters
ADD CONSTRAINT ct_adopter UNIQUE (home_address);

ALTER TABLE disease
ALTER COLUMN id_disease INT NOT NULL;
ALTER TABLE disease
ADD PRIMARY KEY (id_disease);

ALTER TABLE treatment
ALTER COLUMN treatment_period INT NOT NULL;
ALTER TABLE treatment
ADD CONSTRAINT pk_treatment PRIMARY KEY (treatment_period);

ALTER TABLE horses
ADD CONSTRAINT fk_paddock
FOREIGN KEY (id_paddock) REFERENCES paddocks(id_paddock);
ALTER TABLE horses
ADD FOREIGN KEY (id_groomer) REFERENCES groomers(id_groomer);
ALTER TABLE horses
ADD FOREIGN KEY (id_desease) REFERENCES disease(id_disease);
ALTER TABLE horses
ADD FOREIGN KEY (id_color) REFERENCES colors(id_color);
ALTER TABLE horses
ADD FOREIGN KEY (id_breed) REFERENCES breeds(id_breed);

ALTER TABLE medicine
ADD CONSTRAINT fk_sup
FOREIGN KEY (id_medSuplier) REFERENCES medSuplier(id_medSuplier);

ALTER TABLE treatment
ADD FOREIGN KEY (id_medicine) REFERENCES medicine(id_medicine);
ALTER TABLE treatment
ADD FOREIGN KEY (id_disease) REFERENCES disease(id_disease);

ALTER TABLE adoptions
ADD FOREIGN KEY (id_horse) REFERENCES horses(id_horse);
ALTER TABLE adoptions
ADD FOREIGN KEY (id_adopter) REFERENCES adopters(id_adopter);

INSERT INTO breeds
VALUES (12, 'pinto');

INSERT INTO breeds
VALUES (13, 'hafflinger');

INSERT INTO groomers
VALUES (2, 'Mara',20,121);

INSERT INTO horses
VALUES (6, 'Laika',3,13 ,15,3,1,'True',21);

INSERT INTO colors
VALUES (15,'green');

INSERT INTO medicine
VALUES (300,'syrop',21);

INSERT INTO paddocks
VALUES (100,'5');

UPDATE breeds
SET breed_name='pinto'
WHERE id_breed=12;

UPDATE colors
SET color_name='black'
WHERE id_color=15;

UPDATE groomers
SET age=21
WHERE age<21;

UPDATE groomers
SET groomer_name='Anne'
WHERE groomer_name LIKE 'Ana';

UPDATE paddocks
SET number_of_horses='2'
WHERE id_paddock=100 OR id_paddock=21;

DELETE FROM paddocks 
WHERE number_of_horses IS NULL;

DELETE FROM paddocks
WHERE number_of_horses BETWEEN 5 AND 6

DELETE FROM paddocks
WHERE number_of_horses IN (5,6);

SELECT horse_name
FROM horses
WHERE age=5 OR age=6;

SELECT phone_number FROM adopters
UNION 
SELECT phone_number FROM groomers;

SELECT id_horse
FROM horses
INTERSECT
SELECT id_horse
FROM adoptions;

SELECT groomer_name
FROM groomers
WHERE groomer_name IN ('Ana','Anuta','Ana-Maria','Anne');

SELECT groomer_name
FROM groomers
EXCEPT
SELECT adopter_name
FROM adopters;

SELECT groomer_name
FROM groomers
WHERE groomer_name NOT IN ('Ana','Maria','Ioana');

SELECT *
FROM horses
INNER JOIN paddocks ON horses.id_paddock=paddocks.id_paddock;

SELECT *
FROM horses
LEFT JOIN paddocks ON horses.id_paddock=paddocks.id_paddock;

SELECT *
FROM horses
RIGHT JOIN paddocks ON horses.id_paddock=paddocks.id_paddock
RIGHT JOIN colors ON horses.id_color=colors.id_color;

SELECT *
FROM adoptions
FULL JOIN adopters ON adoptions.id_adopter=adopters.id_adopter
FULL JOIN horses ON adoptions.id_horse=horses.id_horse;

SELECT adopter_name FROM adopters
WHERE phone_number IN (SELECT phone_number FROM groomers) AND phone_number>0728282634 ;

SELECT medSuplier_name FROM medSuplier
WHERE id_medSuplier IN (SELECT id_groomer FROM groomers WHERE id_groomer IN (SELECT id_adopter FROM adopters) );

SELECT TOP 3 id_adopter
FROM adoptions
WHERE EXISTS (SELECT horse_name FROM horses WHERE horses.id_horse = adoptions.id_horse AND age>4);

SELECT id_horse
FROM adoptions
WHERE EXISTS (SELECT horse_name FROM horses WHERE horses.id_horse = adoptions.id_horse AND age+1>5);

SELECT TOP 3*
FROM (SELECT disease_name  FROM disease WHERE id_disease<10) as diseases_names
WHERE disease_name LIKE 'f%';

SELECT TOP 3 *
FROM (SELECT horse_name FROM horses WHERE age+2<10) as horses_names
WHERE horse_name LIKE 'R%';

SELECT COUNT(id_horse) as Horses,id_breed
FROM horses
GROUP BY id_breed;

SELECT COUNT(id_horse) as Horses,id_breed
FROM horses
GROUP BY id_breed
HAVING id_breed<15
ORDER BY id_breed;

SELECT age
FROM horses
GROUP BY age
HAVING age < (SELECT AVG(age) FROM groomers)
ORDER BY age ;

SELECT age
FROM groomers
GROUP BY age
HAVING age < (SELECT AVG(age) FROM groomers)
ORDER BY age DESC; 

SELECT groomer_name
FROM groomers
WHERE age+1 > ALL (SELECT age FROM groomers);

SELECT id_horse
FROM adoptions
WHERE date_of_adootion > ANY (SELECT date_of_adootion FROM adoptions );

SELECT groomer_name
FROM groomers
WHERE phone_number != ANY (SELECT phone_number FROM adopters);

SELECT adopter_name
FROM adopters
WHERE phone_number != ANY (SELECT phone_number FROM groomers);

SELECT groomer_name
FROM groomers
WHERE age = (SELECT MAX(age) FROM groomers);

SELECT id_horse
FROM adoptions
WHERE date_of_adootion >(SELECT AVG(date_of_adootion) FROM adoptions );

SELECT groomer_name
FROM groomers
WHERE phone_number NOT IN (SELECT phone_number FROM adopters);

SELECT adopter_name
FROM adopters
WHERE phone_number NOT IN (SELECT phone_number FROM groomers);

GO
CREATE PROCEDURE proc1
AS
	ALTER TABLE horses
	ALTER COLUMN age FLOAT;
GO

CREATE PROCEDURE undoProc1
AS
	ALTER TABLE horses
	ALTER COLUMN age INT;
GO

CREATE PROCEDURE proc2
AS
	ALTER TABLE adopters
	ADD age INT;
	ALTER TABLE adopters ADD CONSTRAINT df_16 DEFAULT 16 FOR age;
GO


CREATE PROCEDURE undoProc2
AS
	ALTER TABLE adopters
	DROP CONSTRAINT df_16;
	ALTER TABLE adopters
	DROP COLUMN age;
GO


CREATE PROCEDURE proc3
AS
	ALTER TABLE horses
	DROP COLUMN horse_name;
GO



CREATE PROCEDURE undoProc3
AS
	ALTER TABLE horses
	ADD horse_name Varchar(50);
GO

CREATE PROCEDURE proc4
AS
	ALTER TABLE groomers
	ADD CONSTRAINT ct0 DEFAULT 0 FOR age;
GO

CREATE PROCEDURE undoProc4
AS
	ALTER TABLE groomers 
	DROP CONSTRAINT ct0;
GO

CREATE PROCEDURE proc5
AS
	ALTER TABLE adopters
	DROP CONSTRAINT df_16;
GO

CREATE PROCEDURE undoProc5
AS
	ALTER TABLE adopters 
	ADD CONSTRAINT df_16 DEFAULT 16 FOR age;
GO

ALTER TABLE adoptions
ALTER COLUMN date_of_adootion INT NOT NULL;

GO

CREATE PROCEDURE proc6
AS
	ALTER TABLE adoptions
	ADD CONSTRAINT pk_adoption PRIMARY KEY (date_of_adootion);
GO

CREATE PROCEDURE undoProc6
AS
	ALTER TABLE adoptions
	DROP CONSTRAINT pk_adoption;
GO

CREATE PROCEDURE proc7
AS
	ALTER TABLE treatment
	DROP CONSTRAINT pk_treatment;
GO

CREATE PROCEDURE undoProc7
AS
	ALTER TABLE treatment
	ADD CONSTRAINT pk_treatment PRIMARY KEY (treatment_period);
GO

CREATE PROCEDURE proc8
AS
	ALTER TABLE adopters
	DROP CONSTRAINT ct_adopter;
GO

CREATE PROCEDURE undoProc8
AS
	ALTER TABLE adopters
	ADD CONSTRAINT ct_adopter UNIQUE (home_address);
GO

CREATE PROCEDURE proc9
AS
	ALTER TABLE disease
	ADD CONSTRAINT ct_disease UNIQUE (disease_name);
GO

CREATE PROCEDURE undoProc9
AS
	ALTER TABLE disease
	DROP CONSTRAINT ct_disease;
GO

CREATE PROCEDURE proc10
AS
	ALTER TABLE horses
	DROP CONSTRAINT fk_paddock;
GO

CREATE PROCEDURE undoProc10
AS
	ALTER TABLE horses
	ADD CONSTRAINT fk_paddock UNIQUE (id_paddock);
GO

CREATE PROCEDURE proc11
AS
	ALTER TABLE horses
	ADD CONSTRAINT fk_color UNIQUE (id_color);
GO

CREATE PROCEDURE undoProc11
AS
	ALTER TABLE horses
	DROP CONSTRAINT fk_color;
GO

CREATE PROCEDURE proc12
AS
	CREATE TABLE interested_persons( 
	id_interested_person INT NOT NULL PRIMARY KEY, 
	person_name varchar(50) NOT NULL, 
	phone_number int
	);
GO

CREATE PROCEDURE undoProc12
AS
	DROP TABLE interested_persons;
GO

CREATE PROCEDURE proc13
AS
	DROP TABLE medSuplier;
GO

CREATE PROCEDURE undoProc13
AS
	CREATE TABLE medSuplier
	(
	id_medSuplier int,
	medSuplier_name varchar(255),
	);
GO

CREATE PROCEDURE change_version(@newVersion INT)
AS
	BEGIN
		DECLARE @oldVersion INT
		DECLARE @uspVersion VARCHAR(20)
		SELECT TOP  1 @oldVersion = version_number FROM versions
		IF @newVersion<0 OR @newVersion>13 
			BEGIN
				PRINT 'The version should be from 1 to 13'
			END
		ELSE
			BEGIN
				IF @oldVersion<@newVersion
					BEGIN
					SET @oldVersion=@oldVersion+1
					WHILE @oldVersion<=@newVersion
						BEGIN
							SET @uspVersion='proc'+CONVERT(VARCHAR(15),@oldVersion)
							EXEC @uspVersion
							PRINT 'Procedure executed: '+ @uspVersion
							SET @oldVersion = @oldVersion+1
						END
					END
				ELSE
					BEGIN
						WHILE	@oldVersion>@newVersion
							BEGIN
							SET @uspVersion='undoProc'+CONVERT(VARCHAR(15),@oldVersion)
							EXEC @uspVersion
							PRINT 'Procedure executed: '+ @uspVersion
							SET @oldVersion = @oldVersion-1								
							END
					END
			END
	END
	UPDATE versions
	SET version_number=@newVersion
GO

EXEC change_version 0;

UPDATE versions
SET version_number=0;




