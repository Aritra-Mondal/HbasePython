import happybase as hb
from utils import printRow

connection = hb.Connection("127.0.0.1", protocol='compact')

print(f"Host : {connection.host}")
print(f"Port: {connection.port}")

table = connection.table("notifications")

rows_forUser = table.row(b'1', columns=[b'attributes:for_user'], include_timestamp=True)

printRow(rows_forUser,1)

rows_forUser2 = table.row(b'5', columns=[b'attributes:for_user', b'attributes:link'], include_timestamp=True)

printRow(rows_forUser2, 5)

