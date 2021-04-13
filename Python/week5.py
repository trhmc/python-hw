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
  result = ' '
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
