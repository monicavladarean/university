USE [Horse_shelter]
GO

-- Functions to verify input --

CREATE FUNCTION uf_ValidateTreatPackRecomandation (@recomandation varchar(255)) RETURNS INT AS
BEGIN
DECLARE @return INT
SET @return = 0
IF(@recomandation IN ('after training','before training','anytime','after competition','before competition'))
SET @return = 1
RETURN @return
END

GO

CREATE FUNCTION uf_ValidateName (@name varchar(255)) RETURNS INT AS
BEGIN
DECLARE @return INT
SET @return = 0
IF(@name IS NOT NULL)
SET @return = 1
RETURN @return
END

GO

-- pb. 1 (rollback) --

ALTER PROCEDURE AddTreatPack  
	@sweetName varchar(255), 
	@vegetableName varchar(255),
	@recomandation varchar(255)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

BEGIN TRAN
BEGIN TRY
	IF(dbo.uf_ValidateName(@sweetName)<>1)
	BEGIN
		RAISERROR('Sweet name can not be null',14,1)
	END
	IF(dbo.uf_ValidateName(@vegetableName)<>1)
	BEGIN
		RAISERROR('Vegetable name can not be null',14,1)
	END
	IF(dbo.uf_ValidateTreatPackRecomandation(@recomandation)<>1)
	BEGIN
		RAISERROR('Invalid recomandation',14,1)
	END
INSERT INTO sweets VALUES(@sweetName)
print 'Insert sweet complete'
INSERT INTO vegetables VALUES(@vegetableName)
print 'Insert vegetable complete'
declare @sid int
set @sid = (select IDENT_CURRENT('sweets'))
declare @vid int
set @vid = (select IDENT_CURRENT('vegetables'))
INSERT INTO treatPacks values(@vid, @sid, @recomandation)
print 'Insert treat pack complete'
COMMIT TRAN
print 'Transaction committed'
END TRY
BEGIN CATCH
ROLLBACK TRAN
print 'Transaction rollbacked'
print ERROR_MESSAGE()
END CATCH
END
 
EXEC AddTreatPack 'sugar',NULL,'anytime';
EXEC AddTreatPack NULL,'carrot','after training';
EXEC AddTreatPack 'sugar','carrot','now';
EXEC AddTreatPack 'surprise','surprise','after training';

select * from sweets;
select * from vegetables;
select * from treatPacks;

GO

-- pb. 2 (recover) --

CREATE PROCEDURE AddSweet
	@sweetName varchar(255)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

-- Insert statements for procedure here
BEGIN TRAN
BEGIN TRY
	IF dbo.uf_ValidateName(@sweetName)<>1
	BEGIN
		RAISERROR('Sweet name can not be null', 14, 1)				
	END
	INSERT INTO sweets VALUES(@sweetName)
	print 'Insert sweet complete'
	COMMIT TRAN
	print 'Transaction committed'
END TRY
BEGIN CATCH
	ROLLBACK TRAN
	print 'Sweet transaction rollbacked'
	RETURN 1
END CATCH
RETURN 0
END

GO

CREATE PROCEDURE AddVegetable
	@vegetableName varchar(255)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

-- Insert statements for procedure here
BEGIN TRAN
BEGIN TRY
	IF dbo.uf_ValidateName(@vegetableName)<>1
	BEGIN
		RAISERROR('Vegetable name can not be null', 14, 1)				
	END
	INSERT INTO vegetables VALUES(@vegetableName)
	print 'Insert vegetable complete'
	COMMIT TRAN
	print 'Transaction committed'
END TRY
BEGIN CATCH
	ROLLBACK TRAN
	print 'Vegetable transaction rollbacked'
	RETURN 1
END CATCH
RETURN 0
END

GO

CREATE PROCEDURE AddOneTreatPack
	@recomandation varchar(max)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

BEGIN TRAN
BEGIN TRY
	IF dbo.uf_ValidateTreatPackRecomandation(@recomandation)<>1
	BEGIN
		RAISERROR('Recomandation is invalid', 14, 1)				
	END

	DECLARE @sid int
	SET @sid = (select IDENT_CURRENT('sweets'))
	DECLARE @vid int
	SET @vid = (select IDENT_CURRENT('vegetables'))
	INSERT INTO treatPacks VALUES(@vid, @sid, @recomandation)
	print 'Insert pack complete'
	COMMIT TRAN
	print 'Transaction committed'
END TRY
	BEGIN CATCH
	ROLLBACK TRAN
	print 'One reat pack transaction rollbacked'
END CATCH
END

GO

CREATE PROCEDURE AddTreatPack2  
	@sweetName varchar(255), 
	@vegetableName varchar(255),
	@recomandation varchar(255)
AS
BEGIN
-- SET NOCOUNT ON added to prevent extra result sets from
-- interfering with SELECT statements.
SET NOCOUNT ON;

DECLARE @sweet INT
EXECUTE @sweet = AddSweet @sweetName
IF (@sweet <> 1)
	BEGIN
	DECLARE @vegetable int
	EXECUTE @vegetable = AddVegetable @vegetableName
	if (@vegetable <> 1)
		EXECUTE AddOneTreatPack @recomandation
	END
END

EXEC AddTreatPack2 'cookie','hay','now';
EXEC AddTreatPack2 'candy','corn','before training';

select * from sweets;
select * from vegetables;
select * from treatPacks;

-- pb. 3 in separate sql files --
-- dirty reads --
-- non-repeatable reads --
-- phantom reads --
-- deadlock --

-- pb. 4 in separate sql files --
-- update conflict --

select * from programme;
select * from employees;
select * from instructors;
select * from equestrians;