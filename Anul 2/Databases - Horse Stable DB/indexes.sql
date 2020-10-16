
CREATE TABLE employees
(
	employeeID int NOT NULL,
	employeeCNP int UNIQUE,
	employeeName varchar(50),
	CONSTRAINT pk_employees PRIMARY KEY (employeeID)
);

CREATE TABLE jobsToDo
(
	jobID int NOT NULL,
	hourOfJob int,
	jobName varchar(50),
	CONSTRAINT pk_jobs PRIMARY KEY (jobID)
);

CREATE TABLE programme
(
	programmeID int NOT NULL,
	employeeID int,
	jobID int,
	duration int,
	CONSTRAINT fk_employee FOREIGN KEY (employeeID) REFERENCES employees(employeeID),
	CONSTRAINT fk_jobs FOREIGN KEY (jobID) REFERENCES jobsToDo(jobID),
	CONSTRAINT pk_programme PRIMARY KEY (programmeID)
);

GO

CREATE VIEW view_c
AS

SELECT p.programmeID,p.duration, e.employeeName,j.jobName FROM programme p
INNER JOIN jobsToDo j ON j.jobID = p.jobID
INNER JOIN employees e ON p.employeeID=e.employeeID;

GO

--clustered index scan

SELECT employeeCNP
FROM employees
WHERE employeeName='Ana';

--clustered index seek

SELECT employeeName
FROM employees
WHERE employeeID=2;

--nonclustered index scan

SELECT employeeCNP
FROM employees;

--nonclustered index seek

SELECT employeeID
FROM employees
WHERE employeeCNP=1;

--key lookup

SELECT *
FROM employees
WHERE employeeCNP=1;

--b

DROP INDEX idx ON jobsToDo;

CREATE NONCLUSTERED INDEX idx ON jobsToDo(hourOfJob) 
SELECT jobID,hourOfJob
FROM jobsToDo
WHERE hourOfJob=1;

--c--
DROP INDEX idx2 ON programme

CREATE NONCLUSTERED INDEX idx2 ON programme(duration);

SELECT e.employeeName,j.jobName,j.hourOfJob FROM programme p
INNER JOIN jobsToDo j ON j.jobID = p.jobID
INNER JOIN employees e ON p.employeeID=e.employeeID
WHERE p.duration=1;

SELECT * FROM view_c;