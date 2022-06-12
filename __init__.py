import json

d = {}

d['1213'] = {
    'name': 'Me'
}

print(d['1213'])
a = eval('dict(' + str(d['1213']) + ')')

print(type(a))