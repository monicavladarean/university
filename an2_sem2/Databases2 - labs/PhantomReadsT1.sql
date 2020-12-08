
begin transaction
waitfor delay '00:00:04'
insert into medSuplier values (134,'Russia')
commit transaction