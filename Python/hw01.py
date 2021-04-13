_author_ = "Chau Tran"
_email_ = "tranc2@mail.uc.edu"

from math import ceil
def egypt(n,d):
    """
    >>> egypt(3,4)
    1/2 + 1/4 = 3/4
    >>> egypt(11,12)
    1/2 + 1/3 + 1/12 = 11/12
    >>> egypt(123,124)
    1/2 + 1/3 + 1/7 + 1/64 + 1/8333 + 1/347186112 = 123/124
    >>> egypt(103,104)
    1/2 + 1/3 + 1/7 + 1/71 + 1/9122 + 1/141449381 + 1/100039636784966432 + 1/1250991116008501010708121870401536 + 1/1157928441835091937304760466661018606167497415589888 + 1/96147502125227830816714882832524060301989191378522711849551704096768 = 103/104
    """
    Num = n
    Den = d
    ans = ''
    k = 1
    while Num != 0:
      #round up to find the next denominator
      i = ceil(Den/Num)
      #break when i <= 1 to avoid infinite loop
      if (i <= 1):
        break
      if (Num >= 0):
          if (Den % Num == 0):
              ans = ans + '1/' + str(i) + ' + '
        Num = (Num * i) - Den
        Den = Den * i
    ans = ans[:-3]
    print(ans,"= {0}/{1}".format(n,d))

import doctest
if __name__ == "__main__":
    doctest.testmod(verbose=True)

## Partial credit will be given for code that passes the two given doctests. 
## For full credit on HW1 you should test your solutions to egypt(103,104) and  egypt(123,124)
## These are more difficult and may require you to develop faster, more efficient code.
