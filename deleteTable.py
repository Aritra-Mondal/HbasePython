import happybase as hb

connection = hb.Connection("127.0.0.1", protocol='compact')

print(f"Host : {connection.host}")
print(f"Port: {connection.port}")


if b"notifications" not in connection.tables():
    print("Table not Exist!!!")
else:
    connection.disable_table("notifications")
    connection.delete_table("notifications")
    print("Table successfully deleted!!!")