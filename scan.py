from base64 import encode
from importlib.abc import Traversable
import happybase as hb


connection = hb.Connection("127.0.0.1", protocol='compact')

print(f"Host : {connection.host}")
print(f"Port: {connection.port}")

table = connection.table("notifications")

def getAllValues(table):
    for key, data in table.scan():
        print(key, data)

def getValuesRangedStart(table, start):
    for key, data in table.scan(row_start=str(start).encode()):
        print(key, data)

def getValuesRangedStop(table, stop):
    for key, data in table.scan(row_stop=str(stop).encode()):
        print(key, data)

def getAllValuesInRange(table, start, stop):
    for key, data in table.scan(row_start=str(start).encode(), row_stop=str(stop).encode()):
        print(key, data)

def getAllValuesWithPrefexRow(table, prefix):
    for key, data in table.scan(row_prefix=prefix.encode()):
        print(key, data)


getAllValues(table)

# getValuesRangedStart(table, 1)
# getValuesRangedStop(table, 5)
# getAllValues(table, 1,5)
# getAllValuesWithPrefexRow(table,"1")



