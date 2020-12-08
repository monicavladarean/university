set deadlock_priority low
begin transaction
update breeds set breed_name = 'idkT2' where id_breed=12
waitfor delay '00:00:10'
update breeds set breed_name= 'idk2T2' where id_breed=13
commit transaction

