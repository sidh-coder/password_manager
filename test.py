# test_db.py
import modules.database as db

db.create_user_table()

#db.add_user('sidh',b'sidh2017','sidh@gmail.com')
dict  = db.list_user_data('sidh')
print(dict['email'])