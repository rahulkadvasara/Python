def remote_control_next():
    yield 'cnn'
    yield 'espn'

# itr=remote_control_next()
# print(next(itr))
# print(next(itr))

for c in remote_control_next():
    print(c)