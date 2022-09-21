import happybase as hb


connection = hb.Connection("127.0.0.1", protocol='compact')

print(f"Host : {connection.host}")
print(f"Port: {connection.port}")

table = connection.table("notifications")

def deleteRowwithId(val):
    table.delete(f"{str(val).decode()}")

table.delete(b'1', columns=[b'attributes:for_user', b'metrics:open'])