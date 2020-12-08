set transaction isolation level read committed
begin tran
select * from versions
SET TRANSACTION ISOLATION LEVEL SNAPSHOT
BEGIN TRAN
SELECT * FROM versions WHERE Vid = 1
WAITFOR DELAY '00:00:10'
UPDATE versions SET version_number = 8 WHERE Vid = 1
COMMIT TRAN