## Lab 5: Required Questions - Dictionaries  ##

# RQ1
def merge(dict1, dict2):
    """Merges two Dictionaries. Returns a new dictionary that combines both. You may assume all keys are unique.

    >>> new =  merge({1: 'one', 3:'three', 5:'five'}, {2: 'two', 4: 'four'})
    >>> new == {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
    True
    """
    newdict = {}
    for item in dict1:
        newdict[item] = dict1[item]
    for item in dict2:
        newdict[item] = dict2[item]
    return newdict
    


# RQ2
def counter(message):
    """ Returns a dictionary where the keys are the words in the message, and each
    key is mapped (has associated value) equal 
    to the number of times the word appears in the message.
    >>> x = counter('to be or not to be')
    >>> x['to']
    2
    >>> x['be']
    2
    >>> x['not']
    1
    >>> y = counter('run forrest run')
    >>> y['run']
    2
    >>> y['forrest']
    1
    """
    count = {}
    for word in message.split():
        if word not in count:
            count[word] = 1
        else:
            count[word] += 1
    return count


# RQ3
def replace_all(d, x, y):
    """ Returns a dictionary where the key/value pairs are the same as d, 
    except when a value is equal to x, then it should be replaced by y.
    >>> d = {'foo': 2, 'bar': 3, 'garply': 3, 'xyzzy': 99}
    >>> replace_all(d, 3, 'poof')
    >>> d == {'foo': 2, 'bar': 'poof', 'garply': 'poof', 'xyzzy': 99}
    True
    """
    for item in d:
        if d[item] == x:
            d[item] = y
    #return d

# RQ4
def sumdicts(lst):
   """ 
   Takes a list of dictionaries and returns a single dictionary which contains all the keys/value pairs found in list. And 
   if the same key appears in more than one dictionary, then the sum of values in list of dictionaries is returned 
   as the value mapped for that key
   >>> d = sumdicts ([{'a': 5, 'b': 10, 'c': 90, 'd': 19}, {'a': 45, 'b': 78}, {'a': 90, 'c': 10}] )
   >>> d == {'b': 88, 'c': 100, 'a': 140, 'd': 19}
   True
   """
   newd = {}
   for dict in lst:
       for item in dict:
           if item not in newd:
               newd[item] = dict[item]
           else:
               newd[item] += dict[item]
   return newd

#RQ5
def build_successors_table(tokens):
  table = {}
  prev = '.'
  for word in tokens:
    if prev not in table:
      table[prev] = []
    table[prev] += [word]
    prev = word
  return table

def construct_tweet(word, table):
  import random
  result = ''
  while word not in ['.', '!', '?']:
    result += word + ' '
    word = random.choice(table[word])
  return result + word
def random_tweet(table):
  import random
  return construct_tweet(random.choice(table['.']), table)
def shakespeare_tokens(path='shakespeare.txt', url='http://composingprograms.com/shakespeare.txt'):
    """Return the words of Shakespeare's plays as a list."""
    import os
    from urllib.request import urlopen
    if os.path.exists(path):
        return open('shakespeare.txt', encoding='ascii').read().split()
    else:
        shakespeare = urlopen(url)
        return shakespeare.read().decode(encoding='ascii').split()
    
shakestokens = shakespeare_tokens()
shakestable = build_successors_table(shakestokens)

def middle_tweet(table):
    """ Calls the function random_tweet() 5 times (see Interactive Worksheet) and 
    returns the one string which has length in middle value of the 5.
    Returns a string that is a random sentence of average length starting with word, and choosing successors from table.
    """
    import random
    sent = []
    for n in range(5):
        sent.append(random_tweet(table))
    sent = sorted(sent, key = len)
    sentence = sent[2]
    print('middle_value tweet: ',sentence)
    print()
    word = sentence.split()
    return construct_tweet(random.choice(word), table)


import doctest
if __name__ == "__main__":
  doctest.testmod(verbose=True)
