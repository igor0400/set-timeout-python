from lib import set_timeout

set_timeout(lambda: print('timeout 1'), 1)

print('not timeouted')

set_timeout(lambda: print('timeout 2'), 6)