# function name_of_function(p1, p2) {
#     ...;
#     return ...;
# }

def name_of_function(p1, p2):
    return p1 + p2

# this is a dictionary
d = { 'key'            : 'value',
       'lambda'        : lambda(x, y): x + y,
       'some_function' : name_of_function,
       0               : 1,
    }
# print d[0]
# print d['key']
# print d['some_function'](2, 3) #name_of_function(2, 3)
# print d['lambda']((2,3))
d['color'] = 'red'
print d
del d['color']
print d
