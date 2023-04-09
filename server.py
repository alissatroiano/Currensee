import mindsdb_sdk

server = mindsdb_sdk.connect()
server = mindsdb_sdk.connect('http://127.0.0.1:47334')

server = mindsdb_sdk.connect(email='alissatroianonyc@gmail.com', password='B@nana$5900')
server = mindsdb_sdk.connect('https://cloud.mindsdb.com', email='alissatroianonyc@gmail.com', password='B@nana$5900')

# databases = server.list_databases()

# database = databases[1] # Database type object

# query = database.query('select * from files.test_data')
# print(query.fetch())
# print(database)

project = server.list_projects()
print(project)

project = server.get_project('mindsdb')
models = project.list_models()

print(models)
# model = models[0]
model = project.get_model('crypto4')

print(model)