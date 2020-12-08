begin transaction
update breeds set breed_name = 'idk' where id_breed=13
waitfor delay '00:00:10'
update breeds set breed_name= 'idk2' where id_breed=12
commit transaction

