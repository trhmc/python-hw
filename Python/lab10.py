#############
# Iterators #
#############

#RQ1
class Cheer:
    """
    >>> UC = Cheer("Bearcats")
    >>> for c in UC:
    ...     print(c)
    ...
    Give me an B
    Give me an e
    Give me an a
    Give me an r
    Give me an c
    Give me an a
    Give me an t
    Give me an s
    """
    "*** YOUR CODE HERE ***"
    def __init__(self, cheer):
      self.cheer = cheer
      self.current = 0

    def __next__(self):
      if self.current >= len(self.cheer):
        raise StopIteration
      result = "Give me an " + self.cheer[self.current]
      self.current += 1
      return result

    def __iter__(self):
      return self

#RQ2
class Countdown:
    """
    An iterator that counts down from N to 0.
    >>> for number in Countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    >>> for number in Countdown(2):
    ...     print(number)
    ...
    2
    1
    0
    """
    
    "*** YOUR CODE HERE ***"
    def __init__(self, N):
      self.current = N
    def __next__(self):
      if self.current < 0:
        raise StopIteration
      val = self.current
      self.current -= 1
      return val
    def __iter__(self):
      return self


##############
# Generators #
##############

# RQ3
def naturals():
    """A generator function that yields the infinite sequence of natural
    numbers, starting at 1.

    >>> m = naturals()
    >>> type(m)
    <class 'generator'>
    >>> [next(m) for _ in range(10)]
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """
    "*** YOUR CODE HERE ***"
    i = 1
    while True:
      yield i
      i += 1

#RQ4
def scale(s, k):
    """Yield elements of the iterable s scaled by a number k.

    >>> s = scale([1, 5, 2], 5)
    >>> type(s)
    <class 'generator'>
    >>> list(s)
    [5, 25, 10]

    >>> m = scale(naturals(), 2)
    >>> [next(m) for _ in range(5)]
    [2, 4, 6, 8, 10]
    """
    "*** YOUR CODE HERE ***"
    for a in s:
      yield a*k

# RQ5
def countdown(n):
    """
    A generator that counts down from N to 0.
    >>> for number in countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    >>> for number in countdown(2):
    ...     print(number)
    ...
    2
    1
    0
    """
    "*** YOUR CODE HERE ***"
    while n >= 0:
      yield n
      n -= 1


# RQ6
def hailstone(n):
    """
    >>> for num in hailstone(10):
    ...     print(num)
    ...
    10
    5
    16
    8
    4
    2
    1
    """
    "*** YOUR CODE HERE ***"
    while n != 1:
      yield n
      if n % 2 == 0:
        n = int(n / 2)
      else:
        n = int(n*3 + 1)
    yield n

    
