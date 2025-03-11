import os
#this is done so as, when in production i can set the environment variables to
#something diff for that srvr and then will still be able to use the code without changing values
db_config={
    'user':os.getenv('DB_USER','root'),
    'password':os.getenv('DB_PASSWORD','sidh2017'),
    'host':os.getenv('DB_HOST','localhost'),
    'database':os.getenv('DB_NAME','passwordmanager')
}

master_key = os.getenv('MASTER_KEY','root123').encode()
