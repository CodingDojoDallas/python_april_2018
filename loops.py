arr = [1,2,3,4,4,5,6,6]
# JAVASCRIPT
# for (start, stop, step) {
#     ...
# }
# for (var i = 0; i < ...; i++) {
#
# }
for i in range(len(arr)):
    print 'i: {}'.format(i)
    print 'arr[' + str(i) + ']', arr[i]
    print 'arr[{}] - {}'.format(i, arr[i])

print '*'*20
for i in arr:
    print i

# if (arr.length > 5 && arr.length < 20) { ... }
if len(arr) <> 5 and len(arr) < 20:
    print 'compound and'

# if (arr.length > 5 || arr.length < 20) { ... }
if len(arr) > 5 or len(arr) < 20:
    print 'compound and'


# >>> arr
# [1, 2, 3]
# >>> len(arr)
# 3
# >>> arr.sort()
# >>> arr
# [1, 2, 3]
# >>> arr = [3,2,1]
# >>> arr.sort()
# >>> arr
# [1, 2, 3]
# >>> arr = [3,2,1]
# >>> sorted(arr)
# [1, 2, 3]
# >>> arr
# [3, 2, 1]
# >>> arr.reverse()
# >>> arr
# [1, 2, 3]
# >>> reverse(arr)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'reverse' is not defined
# >>> arr.find(1)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'list' object has no attribute 'find'
# >>> arr[1]
# 2
# >>> s = 'hello there everyone!'
# >>> s.find('there')
# 6
# >>> s[6:]
# 'there everyone!'
# >>> s.replace('there', 'red')
# 'hello red everyone!'
# >>> s
# 'hello there everyone!'
# >>> s = 'hello there everyone! there'
# >>> s.replace('there', 'red')
# 'hello red everyone! red'
# >>>
# >>> s.replace('there', 'red', 1)
# 'hello red everyone! there'
# >>> s
# 'hello there everyone! there'
# >>> s = s.replace('there', 'red', 1)
# >>> s
# 'hello red everyone! there'
# >>> help(min)
#
# >>> help(max)
#
# >>> help(sort)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'sort' is not defined
# >>> help(sorted)
#
# >>> sorted(s)
# [' ', ' ', ' ', '!', 'd', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'h', 'h', 'l', 'l', 'n', 'o', 'o', 'r', 'r', 'r', 't', 'v', 'y']
# >>> sorted(s, reverse=True)
# ['y', 'v', 't', 'r', 'r', 'r', 'o', 'o', 'n', 'l', 'l', 'h', 'h', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'd', '!', ' ', ' ', ' ']
# >>>




# >>> help(range)
#
# >>> range(10)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# >>> range(-10)
# []
# >>> range(0,-10)
# []
# >>> range(0,-10,-1)
# [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
# >>> range(-10,-1)
# [-10, -9, -8, -7, -6, -5, -4, -3, -2]
# >>>

# >>> s
# 'hello red everyone! there'
# >>> help(count)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'count' is not defined
# >>> import string
# >>> help(string.count)
#
# >>> help(string.count)
#
# >>> 'elephant'.count('e')
# 2
# >>> s
# 'hello red everyone! there'
# >>> s.split()
# ['hello', 'red', 'everyone!', 'there']
# >>> s.split('!')
# ['hello red everyone', ' there']
# >>> my_list
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'my_list' is not defined
# >>> my_list = ['hello red everyone', ' there']
# >>> my_list
# ['hello red everyone', ' there']
# >>> my_list.join()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'list' object has no attribute 'join'
# >>> ''.join(my_list)
# 'hello red everyone there'
# >>> '!!!!!!'.join(my_list)
# 'hello red everyone!!!!!! there'
# >>> ','.join(my_list)
# 'hello red everyone, there'
# >>> '\t'.join(my_list)
# 'hello red everyone\t there'
# >>> s
# 'hello red everyone! there'
# >>> s.endswith('e')
# True
# >>> s.endswith('r')
# False
# >>> i = 0
# >>> i++
#   File "<stdin>", line 1
#     i++
#       ^
# SyntaxError: invalid syntax
# >>> push
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'push' is not defined
# >>> arr
# [1, 2, 3]
# >>> arr.push(4)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'list' object has no attribute 'push'
# >>> arr.append(4)
# >>> arr
# [1, 2, 3, 4]
# >>> arr += 5
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'int' object is not iterable
# >>> arr += [5]
# >>> arr
# [1, 2, 3, 4, 5]
# >>> arr.append('stick to the end!!')
# >>> arr
# [1, 2, 3, 4, 5, 'stick to the end!!']
# >>> arr2 = ['another', 'list']
# >>> arr
# [1, 2, 3, 4, 5, 'stick to the end!!']
# >>> arr2
# ['another', 'list']
# >>> arr.append(arr2)
# >>> arr
# [1, 2, 3, 4, 5, 'stick to the end!!', ['another', 'list']]
# >>> arr.extend(arr2)
# >>> arr
# [1, 2, 3, 4, 5, 'stick to the end!!', ['another', 'list'], 'another', 'list']
