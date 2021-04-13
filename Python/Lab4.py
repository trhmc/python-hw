##Lab04 Required Questions ##

#########
# Lists #
#########

# RQ1
def cascade(lst):
    """Returns the cascade of the given list using recursion.

    >>> cascade([1, 2, 3, 4])
    [1, 2, 3, 4, 4, 3, 2, 1]
    """
    if not lst:
        return []
    else:
        return [lst[0]] + cascade(lst[1:]) + [lst[0]]

# RQ2
def maptwice(fn, seq):
    """Applies fn twice onto each element in seq and returns the resulting list.

    >>> maptwice(lambda x: x*x, [1, 2, 3])
    [1, 16, 81]
    """
##    new = []
##    for item in seq:
##        new += [fn(fn(item))]
##    return new
    if not seq:
        return []
    else:
        return maptwice(fn,seq[:-1]) + [fn(fn(seq[-1]))]
        
#RQ3
def filterout(pred, seq):
    """Keeps elements in seq only if they do not satisfy pred.

    >>> filterout(lambda x: x % 2 == 0, [1, 2, 3, 4])
    [1, 3]
    """
    if not seq:
        return []
    else:
        if pred(seq[0]):
            return filterout(pred,seq[1:])
        else:
            return [seq[0]] + filterout(pred,seq[1:])

#RQ4
def comp(n, pred):
    """ Uses a one line list comprehension to return list of the first n integers (0...n-1) which satisfy the predicate pred.
    >>> comp(7, lambda x: x%2 ==0)
    [0, 2, 4, 6]
    """
    return [x for x in range(n) if pred(x)]

#RQ5
def flatten(lst):
    """ Takes a nested list and "flattens" it.
    
    >>> flatten([1, 2, 3]) 
    [1, 2, 3]
    >>> x = [1, [2, 3], 4]      
    >>> flatten(x)
    [1, 2, 3, 4]
    >>> x = [[1, [1, 1]], 1, [1, 1]] 
    >>> flatten(x)
    [1, 1, 1, 1, 1, 1]
    >>> lst = [1, [[2], 3], 4, [5, 6]]
    >>> flatten(lst)
    [1, 2, 3, 4, 5, 6]
    """
    if not lst:
        return lst
    else:
        if type(lst[-1]) == list:
          return flatten(flatten(lst[:-1]) + lst[-1])
        return flatten(lst[:-1]) + lst[-1:]

    
import doctest
if __name__ == "__main__":
  doctest.testmod(verbose=True)
