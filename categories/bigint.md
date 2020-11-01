# Big integers

## Addition

```
def sum(num1, num2):
    n = max(len(num1), len(num2))
    num1 = num1.zfill(n)
    num2 = num2.zfill(n)
    carry = 0
    res = []
    for d1, d2 in zip(reversed(num1), reversed(num2)):
        x = int(d1) + int(d2) + carry
        d = x % 10
        carry = x // 10
        res.append(str(d))
    if carry:
        res.append(str(carry))
    return "".join(reversed(res))
```

## Multiplication

### digit mult

```
def mult(num, digit):
    res = []
    carry = 0
    for d in reversed(num):
        r = d * digit + carry
        a = r % 10
        carry = (r - a) // 10
        res.append(a)
    if carry:
        res.append(carry)
   return list(reversed(res))
```

We know an upper bound on the length of the product:

  `len(prod(a,b)) < len(a) + len(b)`





