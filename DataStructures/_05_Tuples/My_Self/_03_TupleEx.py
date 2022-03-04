
tuple1 = ('python', 'geek')
tuple2 = ('coder', 's')
t3 = tuple1 + tuple2

if t3!= 0:

    # t3 returns 0 if matched, 1 when not tuple1
    # is longer and -1 when tuple1 is shorter
    print('Not the same')
else:
    print('Same')
print('Maximum element in tuples 1,2: ' +
      str(max(tuple1)) + ',' +
      str(max(tuple2)))
print('Minimum element in tuples 1,2: ' +
      str(min(tuple1)) + ',' + str(min(tuple2)))
