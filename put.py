import happybase as hb


connection = hb.Connection("127.0.0.1", protocol='compact')

print(f"Host : {connection.host}")
print(f"Port: {connection.port}")

table = connection.table("notifications")

table.put(b'1', {b'attributes:type': b'Comment',
            b'attributes:for_user': b'Aritra',
            b'metrics:open': b'0'})

table.put(b'4', {b'attributes:type': b'Friend Request',
            b'attributes:for_user': b'Daniel',
            b'attributes:for_user': b'Ryan'})

table.put(b'5', {b'attributes:type': b'Comment',
            b'attributes:for_user': b'Rik',
            b'attributes:for_user': b'Alexa',
            b'attributes:for_thing':b'link',
            b'attributes:link': b'link'})


rows = table.rows([b'1', b'4',b'5'])

# rows_as_ordered_dict = OrderedDict(table.rows([b'1', b'4',b'5']))



for key, data in rows:
    for col_key in data:
        print(f"{str(key, 'utf-8')} : {str(col_key, 'utf-8')} ==> {str(data[col_key], 'utf-8')}")