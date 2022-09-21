import happybase as hb

connection = hb.Connection("127.0.0.1", protocol='compact')

print(f"Host : {connection.host}")
print(f"Port: {connection.port}")


if b"notifications" not in connection.tables():
    connection.create_table('notifications',
                            {'attributes':dict(),
                            'metrics':dict()})
    print("Table Created!!")
else:
    print("Table already exists!!!")
