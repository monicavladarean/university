set transaction isolation level repeatable read
begin transaction
select * from medSuplier
waitfor delay '00:00:05'
select * from medSuplier
commit transaction