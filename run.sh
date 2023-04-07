import mindsdb_sdk

# Connect to local server 
server = mindsdb_sdk.connect()
server = mindsdb_sdk.connect('http://127.0.0.1:47334')

# Connect to cloud server

server = mindsdb_sdk.connect(email='alissatroianonyc@gmail.com', password='password')
server = mindsdb_sdk.connect('https://cloud.mindsdb.com',email='alissatroianonyc@gmail.com', password='password')
