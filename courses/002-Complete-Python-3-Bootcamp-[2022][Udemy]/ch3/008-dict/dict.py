# dict
prices_lookup = {'apple': 2.99, 'orange': 1.88, 'milk': 5.99}
print(prices_lookup['milk'])
# nested
d = {'k1':123,'k2':[0, 1, 2],'k3':{'insideKey': 100}}
print(d['k1'], d['k2'][2], d['k3']['insideKey'])
# get all keys or values
keys = d.keys()
print(keys)
values = d.values()
print(values)
items = d.items()
print(items)
