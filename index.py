from lib import set_timeout

def start():
    print('timeout function')

set_timeout(start, 3)

print('not timeouted')

set_timeout(start, 6)