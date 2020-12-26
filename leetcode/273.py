#TAGS implem, recursive, string
#Trick is to see the recursive pattern and the type of f 
# Easier to return a list than a string


# pythonic: using split is faster than writing the full list
NINETEEN = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
HUNDRED = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()

def f(n) -> List[str]:
  if n >= 10 ** 9:
    a, b = divmod(n, 10 ** 9)
    return f(a) + ['Billion'] + f(b)
  elif n >= 10 ** 6:
    a, b = divmod(n, 10 ** 6)
    return f(a) + ['Million'] + f(b)
  elif n >= 10 ** 3:
    a, b = divmod(n, 10 ** 3)
    return f(a) + ['Thousand'] + f(b)
  elif n >= 10 ** 2:
    a, b = divmod(n, 10 ** 2)
    return f(a) + ['Hundred'] + f(b)
  elif n >= 20:
    a, b = divmod(n, 10)
    return [HUNDRED[a - 2]] + f(b)
  elif n > 0:
    return [NINETEEN[n-1]]
  else:
    return []

class Solution:
    def numberToWords(self, num: int) -> str:
      if num == 0:
        return "Zero"
      return ' '.join(f(num))


