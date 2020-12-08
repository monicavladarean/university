if exists (select * from dbo.sysobjects where id = object_id(N'[FK_TestRunTables_Tables]') and OBJECTPROPERTY(id, N'IsForeignKey') = 1)

ALTER TABLE [TestRunTables] DROP CONSTRAINT FK_TestRunTables_Tables

GO



if exists (select * from dbo.sysobjects where id = object_id(N'[FK_TestTables_Tables]') and OBJECTPROPERTY(id, N'IsForeignKey') = 1)

ALTER TABLE [TestTables] DROP CONSTRAINT FK_TestTables_Tables

GO



if exists (select * from dbo.sysobjects where id = object_id(N'[FK_TestRunTables_TestRuns]') and OBJECTPROPERTY(id, N'IsForeignKey') = 1)

ALTER TABLE [TestRunTables] DROP CONSTRAINT FK_TestRunTables_TestRuns

GO



if exists (select * from dbo.sysobjects where id = object_id(N'[FK_TestRunViews_TestRuns]') and OBJECTPROPERTY(id, N'IsForeignKey') = 1)

ALTER TABLE [TestRunViews] DROP CONSTRAINT FK_TestRunViews_TestRuns

GO



if exists (select * from dbo.sysobjects where id = object_id(N'[FK_TestTables_Tests]') and OBJECTPROPERTY(id, N'IsForeignKey') = 1)

ALTER TABLE [TestTables] DROP CONSTRAINT FK_TestTables_Tests

GO



if exists (select * from dbo.sysobjects where id = object_id(N'[FK_TestViews_Tests]') and OBJECTPROPERTY(id, N'IsForeignKey') = 1)

ALTER TABLE [TestViews] DROP CONSTRAINT FK_TestViews_Tests

GO



if exists (select * from dbo.sysobjects where id = object_id(N'[FK_TestRunViews_Views]') and OBJECTPROPERTY(id, N'IsForeignKey') = 1)

ALTER TABLE [TestRunViews] DROP CONSTRAINT FK_TestRunViews_Views

GO



if exists (select * from dbo.sysobjects where id = object_id(N'[FK_TestViews_Views]') and OBJECTPROPERTY(id, N'IsForeignKey') = 1)

ALTER TABLE [TestViews] DROP CONSTRAINT FK_TestViews_Views

GO



if exists (select * from dbo.sysobjects where id = object_id(N'[Tables]') and OBJECTPROPERTY(id, N'IsUserTable') = 1)

drop table [Tables]

GO



if exists (select * from dbo.sysobjects where id = object_id(N'[TestRunTables]') and OBJECTPROPERTY(id, N'IsUserTable') = 1)

drop table [TestRunTables]

GO



if exists (select * from dbo.sysobjects where id = object_id(N'[TestRunViews]') and OBJECTPROPERTY(id, N'IsUserTable') = 1)

drop table [TestRunViews]

GO



if exists (select * from dbo.sysobjects where id = object_id(N'[TestRuns]') and OBJECTPROPERTY(id, N'IsUserTable') = 1)

drop table [TestRuns]

GO



if exists (select * from dbo.sysobjects where id = object_id(N'[TestTables]') and OBJECTPROPERTY(id, N'IsUserTable') = 1)

drop table [TestTables]

GO



if exists (select * from dbo.sysobjects where id = object_id(N'[TestViews]') and OBJECTPROPERTY(id, N'IsUserTable') = 1)

drop table [TestViews]

GO



if exists (select * from dbo.sysobjects where id = object_id(N'[Tests]') and OBJECTPROPERTY(id, N'IsUserTable') = 1)

drop table [Tests]

GO



if exists (select * from dbo.sysobjects where id = object_id(N'[Views]') and OBJECTPROPERTY(id, N'IsUserTable') = 1)

drop table [Views]

GO



CREATE TABLE [Tables] (

	[TableID] [int] IDENTITY (1, 1) NOT NULL ,

	[Name] [nvarchar] (50) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL 

) ON [PRIMARY]

GO



CREATE TABLE [TestRunTables] (

	[TestRunID] [int] NOT NULL ,

	[TableID] [int] NOT NULL ,

	[StartAt] [datetime] NOT NULL ,

	[EndAt] [datetime] NOT NULL 

) ON [PRIMARY]

GO



CREATE TABLE [TestRunViews] (

	[TestRunID] [int] NOT NULL ,

	[ViewID] [int] NOT NULL ,

	[StartAt] [datetime] NOT NULL ,

	[EndAt] [datetime] NOT NULL 

) ON [PRIMARY]

GO



CREATE TABLE [TestRuns] (

	[TestRunID] [int] IDENTITY (1, 1) NOT NULL ,

	[Description] [nvarchar] (2000) COLLATE SQL_Latin1_General_CP1_CI_AS NULL ,

	[StartAt] [datetime] NULL ,

	[EndAt] [datetime] NULL 

) ON [PRIMARY]

GO



CREATE TABLE [TestTables] (

	[TestID] [int] NOT NULL ,

	[TableID] [int] NOT NULL ,

	[NoOfRows] [int] NOT NULL ,

	[Position] [int] NOT NULL 

) ON [PRIMARY]

GO



CREATE TABLE [TestViews] (

	[TestID] [int] NOT NULL ,

	[ViewID] [int] NOT NULL 

) ON [PRIMARY]

GO



CREATE TABLE [Tests] (

	[TestID] [int] IDENTITY (1, 1) NOT NULL ,

	[Name] [nvarchar] (50) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL 

) ON [PRIMARY]

GO



CREATE TABLE [Views] (

	[ViewID] [int] IDENTITY (1, 1) NOT NULL ,

	[Name] [nvarchar] (50) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL 

) ON [PRIMARY]

GO



ALTER TABLE [Tables] WITH NOCHECK ADD 

	CONSTRAINT [PK_Tables] PRIMARY KEY  CLUSTERED 

	(

		[TableID]

	)  ON [PRIMARY] 

GO



ALTER TABLE [TestRunTables] WITH NOCHECK ADD 

	CONSTRAINT [PK_TestRunTables] PRIMARY KEY  CLUSTERED 

	(

		[TestRunID],

		[TableID]

	)  ON [PRIMARY] 

GO



ALTER TABLE [TestRunViews] WITH NOCHECK ADD 

	CONSTRAINT [PK_TestRunViews] PRIMARY KEY  CLUSTERED 

	(

		[TestRunID],

		[ViewID]

	)  ON [PRIMARY] 

GO



ALTER TABLE [TestRuns] WITH NOCHECK ADD 

	CONSTRAINT [PK_TestRuns] PRIMARY KEY  CLUSTERED 

	(

		[TestRunID]

	)  ON [PRIMARY] 

GO



ALTER TABLE [TestTables] WITH NOCHECK ADD 

	CONSTRAINT [PK_TestTables] PRIMARY KEY  CLUSTERED 

	(

		[TestID],

		[TableID]

	)  ON [PRIMARY] 

GO



ALTER TABLE [TestViews] WITH NOCHECK ADD 

	CONSTRAINT [PK_TestViews] PRIMARY KEY  CLUSTERED 

	(

		[TestID],

		[ViewID]

	)  ON [PRIMARY] 

GO



ALTER TABLE [Tests] WITH NOCHECK ADD 

	CONSTRAINT [PK_Tests] PRIMARY KEY  CLUSTERED 

	(

		[TestID]

	)  ON [PRIMARY] 

GO



ALTER TABLE [Views] WITH NOCHECK ADD 

	CONSTRAINT [PK_Views] PRIMARY KEY  CLUSTERED 

	(

		[ViewID]

	)  ON [PRIMARY] 

GO



ALTER TABLE [TestRunTables] ADD 

	CONSTRAINT [FK_TestRunTables_Tables] FOREIGN KEY 

	(

		[TableID]

	) REFERENCES [Tables] (

		[TableID]

	) ON DELETE CASCADE  ON UPDATE CASCADE ,

	CONSTRAINT [FK_TestRunTables_TestRuns] FOREIGN KEY 

	(

		[TestRunID]

	) REFERENCES [TestRuns] (

		[TestRunID]

	) ON DELETE CASCADE  ON UPDATE CASCADE 

GO



ALTER TABLE [TestRunViews] ADD 

	CONSTRAINT [FK_TestRunViews_TestRuns] FOREIGN KEY 

	(

		[TestRunID]

	) REFERENCES [TestRuns] (

		[TestRunID]

	) ON DELETE CASCADE  ON UPDATE CASCADE ,

	CONSTRAINT [FK_TestRunViews_Views] FOREIGN KEY 

	(

		[ViewID]

	) REFERENCES [Views] (

		[ViewID]

	) ON DELETE CASCADE  ON UPDATE CASCADE 

GO



ALTER TABLE [TestTables] ADD 

	CONSTRAINT [FK_TestTables_Tables] FOREIGN KEY 

	(

		[TableID]

	) REFERENCES [Tables] (

		[TableID]

	) ON DELETE CASCADE  ON UPDATE CASCADE ,

	CONSTRAINT [FK_TestTables_Tests] FOREIGN KEY 

	(

		[TestID]

	) REFERENCES [Tests] (

		[TestID]

	) ON DELETE CASCADE  ON UPDATE CASCADE 

GO



ALTER TABLE [TestViews] ADD 

	CONSTRAINT [FK_TestViews_Tests] FOREIGN KEY 

	(

		[TestID]

	) REFERENCES [Tests] (

		[TestID]

	),

	CONSTRAINT [FK_TestViews_Views] FOREIGN KEY 

	(

		[ViewID]

	) REFERENCES [Views] (

		[ViewID]

	)

GO





CREATE TABLE activities
(
	week_day int NOT NULL,
	hourOfActivity int NOT NULL,
	activityName varchar(50),
	CONSTRAINT pk_activities PRIMARY KEY (week_day,hourOfActivity)
);

CREATE TABLE schools
(
	schoolId int NOT NULL,
	nrOfKids int,
	CONSTRAINT pk_schools PRIMARY KEY (schoolId)
);

CREATE TABLE kidsProgramme
(
	kidsProgrammeId int NOT NULL,
	schoolId int,
	week_day int NOT NULL,
	hourOfActivity int NOT NULL,
	duration int,
	CONSTRAINT fk_activities FOREIGN KEY (week_day,hourOfActivity) REFERENCES activities(week_day,hourOfActivity),
	CONSTRAINT pk_kidsProgramme PRIMARY KEY (kidsProgrammeId)
);

ALTER TABLE kidsProgramme
ADD CONSTRAINT fk_schools
FOREIGN KEY (schoolId) REFERENCES schools(schoolId);

GO

CREATE VIEW view_1
AS
SELECT * FROM activities

GO

CREATE VIEW view_2
AS
SELECT kp.week_day,kp.hourOfActivity FROM kidsProgramme AS kp
INNER JOIN activities AS a
ON kp.hourOfActivity = a.hourOfActivity AND a.week_day = kp.week_day

GO

CREATE VIEW view_3
AS
SELECT COUNT(kp.duration) as "nr", kp.duration FROM kidsProgramme as kp
INNER JOIN schools as s ON kp.schoolId = s.schoolId
INNER JOIN activities AS a ON kp.hourOfActivity = a.hourOfActivity AND a.week_day = kp.week_day
GROUP BY kp.duration

GO

CREATE PROCEDURE test_view_1
@id INT
AS
BEGIN
	DECLARE @start DATETIME = GETDATE()
	SELECT * FROM view_1
	DECLARE @stop DATETIME = GETDATE()
	INSERT INTO TestRunViews (TestRunID,ViewID,StartAt,EndAt) VALUES (@id,1,@start,@stop);
END;

GO
CREATE PROCEDURE test_view_2
@id INT
AS
BEGIN
	DECLARE @start DATETIME = GETDATE()
	SELECT * FROM view_2
	DECLARE @stop DATETIME = GETDATE()
	INSERT INTO TestRunViews (TestRunID,ViewID,StartAt,EndAt) VALUES (@id,2,@start,@stop);
END;

GO
CREATE PROCEDURE test_view_3
@id INT
AS
BEGIN
	DECLARE @start DATETIME = GETDATE()
	SELECT * FROM view_3
	DECLARE @stop DATETIME = GETDATE()
	INSERT INTO TestRunViews (TestRunID,ViewID,StartAt,EndAt) VALUES (@id,3,@start,@stop);
END;


INSERT INTO Views (Name) VALUES 
('view_1'),
('view_2'),
('view_3');

delete from Tests
delete from Views
delete from Tables

INSERT INTO Tables (Name) VALUES
('Activity'),
('School'),
('KidsProgramme');

INSERT INTO Tests (Name) VALUES
('test_1'),
('test_2'),
('test_3');

drop procedure insereaza
GO

CREATE PROCEDURE insereaza
@tableName VARCHAR(100), @noOfRows INT, @id INT
AS
BEGIN
	DELETE FROM TestTables
	DECLARE @start DATETIME
	DECLARE @end DATETIME
	IF @tableName = 'Activity'
		BEGIN
			SET @start = GETDATE();
			DECLARE @i1 INT = 1;
			WHILE (@i1 <= @noOfRows)
			BEGIN
				INSERT INTO activities(week_day,hourOfActivity,activityName) 
					VALUES(@i1, @i1, 'name');
				SET @i1 = @i1 + 1;
			END
			SET @end = GETDATE();
			INSERT INTO [TestRunTables] (TestRunID,TableID,StartAt,EndAt) 
				VALUES (@id,1,@start,@end);
		END
	IF @tableName = 'School'
		BEGIN
			SET @start = GETDATE();
			DECLARE @i INT = 1;
			WHILE (@i <= @noOfRows)
			BEGIN
				INSERT INTO schools(schoolId,nrOfKids) VALUES 
						(@i, @i*20);
				SET @i = @i + 1;
			END
			SET @end = GETDATE();
			INSERT INTO [TestRunTables] (TestRunID,TableID,StartAt,EndAt) 
				VALUES (@id,2,@start,@end);
		END
	IF @tableName = 'KidsProgramme'
		BEGIN
			SET @start = GETDATE();
			SET @i = 1;

			WHILE (@i <= @noOfRows)
			BEGIN
				INSERT INTO activities(week_day,hourOfActivity,activityName) 
					VALUES(@i, @i, 'name');
				INSERT INTO schools(schoolId,nrOfKids) VALUES 
						(@i, @i*20);
				INSERT INTO kidsProgramme(kidsProgrammeId,schoolId,week_day,hourOfActivity,duration) 
							VALUES (@i,@i,@i, @i,@i%3);
				SET @i = @i + 1;
			END
			SET @end = GETDATE();
			INSERT INTO [TestRunTables] (TestRunID,TableID,StartAt,EndAt) 
						VALUES (@id,3,@start,@end);
		END
END

INSERT INTO TestTables (TestID,TableID,NoOfRows,Position)
VALUES (1,1,1000,1),(1,2,1000,2),(1,3,1000,3);
 
GO

CREATE PROCEDURE test_schools
@id INT
AS
BEGIN
	DELETE FROM schools
	DECLARE @nrRanduri INT
	SET @nrRanduri = (SELECT NoOfRows FROM TestTables WHERE TableID = 2)
	EXEC insereaza 'School',@nrRanduri,@id; 
END

GO
CREATE PROCEDURE test_kidsProgrammes
@id INT
AS
BEGIN
	DELETE FROM schools
	DELETE FROM activities
	DELETE FROM kidsProgramme
	DECLARE @nrRanduri INT
	SET @nrRanduri = (SELECT NoOfRows FROM TestTables WHERE TableID = 3)
	EXEC insereaza 'KidsProgramme',@nrRanduri,@id; 
END

GO
CREATE PROCEDURE test_activities
@id INT
AS
BEGIN
	DELETE FROM activities
	DECLARE @nrRanduri INT
	SET @nrRanduri = (SELECT NoOfRows FROM TestTables WHERE TableID = 1)
	EXEC insereaza 'Activity',@nrRanduri,@id; 
END
GO

--DROP PROCEDURE test
GO
CREATE PROCEDURE test
AS
BEGIN
	DECLARE @start DATETIME = GETDATE();
	DECLARE @stop DATETIME;
	INSERT INTO TestRuns(Description,StartAt,EndAt) VALUES ('TEST',@start,@stop);
	DECLARE @id INT;
	SET @id = (SELECT MAX(TestRunID) FROM TestRuns);
	EXEC test_activities @id
	EXEC test_view_1 @id
	EXEC test_schools @id
	EXEC test_view_2 @id
	EXEC test_kidsProgrammes @id
	EXEC test_view_3 @id
	SET @stop = GETDATE();
	UPDATE TestRuns
	SET EndAt = @stop WHERE TestRunID = @id;
END;

EXEC test

SELECT * FROM [Tests]
SELECT * FROM [Tables]
SELECT * FROM [Views]
SELECT * FROM [TestRuns]
SELECT * FROM [TestRunTables] ORDER BY StartAt
SELECT * FROM [TestRunViews] ORDER BY StartAt

DELETE FROM TestRuns
DELETE FROM TestRunTables
DELETE FROM TestRunViews

DELETE FROM schools
DELETE FROM activities
DELETE FROM kidsProgramme

