# from this page:
# https://stackoverflow.com/questions/18406165/creating-a-timer-in-python

# See Timer Objects from threading.
# https://docs.python.org/2/library/threading.html#timer-objects

from threading import Timer

def timeout():
    print("Game over")

# duration is in seconds
t = Timer(20 * 60, timeout)
t.start()

# wait for time completion
t.join()

##########

# Should you want pass arguments to the timeout function, you can give them in the timer constructor:
def timeout2(foo, bar=None):
    print('The arguments were: foo: {}, bar: {}'.format(foo, bar))

t2 = Timer(20 * 60, timeout2, args=['something'], kwargs={'bar': 'else'})

# Or you can use functools.partial to create a bound function, or you can pass in an instance-bound method.