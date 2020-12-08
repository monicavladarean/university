begin transaction
update medSuplier set medSuplier_name = 'England'
where id_medSuplier = 2
waitfor delay '00:00:5'
rollback transaction
