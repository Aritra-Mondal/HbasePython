import happybase as hb


connection = hb.Connection("127.0.0.1", protocol='compact')

print(f"Host : {connection.host}")
print(f"Port: {connection.port}")

table = connection.table("notifications")

values = table.cells(b'1',b'metrics:open', include_timestamp=True)
for value in values:
    print("Cell data: {}".format(value))

cells = table.cells(b'5',b'attributes:link', include_timestamp=True)
for value, timestamp in cells:
    print("Cell data at {}: {}".format(timestamp, value))



# for key, data in rows:
#     for col_key in data:
#         print(f"{str(key, 'utf-8')} : {str(col_key, 'utf-8')} ==> {str(data[col_key], 'utf-8')}")