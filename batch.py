import happybase as hb


connection = hb.Connection("127.0.0.1", protocol='compact')

print(f"Host : {connection.host}")
print(f"Port: {connection.port}")

table = connection.table("notifications")

with table.batch() as b:
    b.put(b'2', {b'attributes:type': b'Comment', 
                b'attributes:for_user': b'Sweta',
                b'metrics:open':b'0'})
    b.delete(b'2', columns=['attributes:type'])
    b.send()