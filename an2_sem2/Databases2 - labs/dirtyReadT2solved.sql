set transaction isolation level read committed 
begin transaction
select * from medSuplier
waitfor delay '00:00:15'
select * from medSuplier
commit transaction