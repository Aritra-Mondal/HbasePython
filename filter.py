from base64 import encode
from importlib.abc import Traversable
import happybase as hb


connection = hb.Connection("127.0.0.1", protocol='compact')

print(f"Host : {connection.host}")
print(f"Port: {connection.port}")

table = connection.table("notifications")

def getRowFilteredValues(table):
    for key, data in table.scan(filter="RowFilter(=,'substring:1')"):
        print(key, data)

def getColumnFilteredValues(table):
    for key, data in table.scan(filter="SingleColumnValueFilter('attributes','for_user',=,'substring:Sweta')"):
        print(key, data)

def getColumnExcludeFilteredValues(table):
    for key, data in table.scan(filter="SingleColumnValueExcludeFilter('attributes','for_user',=,'substring:Alexa')"):
        print(key, data)

def getKeyOnlyfilteredValues(table):
    for key, data in table.scan(filter="KeyOnlyFilter()"):
        print(key, data)

def getFirstKeyOnlyfilteredValues(table):
    for key, data in table.scan(filter="FirstKeyOnlyFilter()"):
        print(key, data)



getColumnExcludeFilteredValues(table)