insert into medSuplier values(10,'America')
begin transaction
waitfor delay '00:00:05'
update medSuplier set medSuplier_name = 'Nederlands'
where medSuplier_name = 'America'
commit transaction