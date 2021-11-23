# chapter 3.6
# Subject: associacy arrays
# Time: 5 minutes
# GO!

marvel = {
    'name': 'imei',
    "nazwisko":'siema',
    'volume': 1


}
for key in marvel:
    print(key+'='+str(marvel[key]))
print('\r\nMarvel keys')
print(marvel.items())

print('\r\nMarvel keys')
for key,val in marvel.items():
    print(key+'='+str(val))

dc = dict()
dc['name'] = "siema"
dc["nazwisko"] = 'marek'
print('\r\nDc Keys/values')
print(dc.items())
print(dc.values())

print('\r\nDc Keys()')
for key in dc.keys():
    print('K'+key)
for val in dc.values():
    print('K'+val)