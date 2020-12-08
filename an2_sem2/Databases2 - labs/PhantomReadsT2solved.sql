
set transaction isolation level serializable
begin transaction
select * from medSuplier
waitfor delay '00:00:05'
select * from medSuplier
commit transaction