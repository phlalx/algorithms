# Big integers

We scan the inputs in reverse order, and produce the result in reverse order
as well. Think of corner cases.

## Addition

Everything is simpler if both nums have the same size.
Trick: We use `zfill`.

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

We use the "school" algorithms. We multiply digit by digit.

    1 1 1
      4 5
    -----
    5 5 5
  4 4 4 .
  -------
  4 9 9 5

The difference is that we perform the addition on the fly. For that, we
need to know the size of the result.

We know an upper bound on the length of the product is `len(prod(a,b)) <= len(a) + len(b)`

Proof: `a = 9 * 10 ** (len(a) - 1)`

```
def multiply(self, num1: str, num2: str) -> str:
    if num1 == "0" or num2 == "0":
        return "0"

    a = [int(d) for d in reversed(num1)]
    b = [int(d) for d in reversed(num2)]
    p = len(num1)
    q = len(num2)
    res = [ 0 ] * (p + q)
    for i in range(p):
        carry = 0
        for j in range(q):
            carry, d = divmod(a[i] * b[j] + res[i+j] + carry, 10)
            res[i + j] = d
        res[i+q] = carry
    return (''.join(str(i) for i in reversed(res))).lstrip('0')
```





