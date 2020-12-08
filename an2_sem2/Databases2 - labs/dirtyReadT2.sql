set transaction isolation level read uncommitted
begin tran
select * from medSuplier
waitfor delay '00:00:15'
select * from medSuplier
commit tran
