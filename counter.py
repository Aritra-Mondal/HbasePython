import happybase as hb


connection = hb.Connection("127.0.0.1", protocol='compact')

print(f"Host : {connection.host}")
print(f"Port: {connection.port}")

table = connection.table("notifications")

print(table.counter_inc(b'1', b'metrics:counter')) 
print(table.counter_inc(b'2', b'metrics:counter', value=3))  
print(table.counter_inc(b'1', b'metrics:counter')) 
print(table.counter_inc(b'1', b'metrics:counter', value=4))     

print(table.counter_inc(b'3', b'metrics:counter2')) 

print(table.counter_dec(b'1', b'metrics:counter')) 


print(table.counter_get(b'1', b'metrics:counter')) 

table.counter_set(b'3', b'metrics:counter', 12)