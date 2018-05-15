#include <cstdio>
#include <set>
#include <stack>
#include <utility>
#include <vector>
#include <queue>
#include <map>
#include <iostream>
#include <cassert>
#include <cmath>
#include <algorithm>
#include <climits>

using namespace std;

// exponentiation 
// supposons n = p1^c1 .... pk^ck
// c1.lookup(first_prime) + c2.lookup(second_prime) ... + ck.lookup(last_prime)
void primefactors(int n) {
    assert(n >= 1);
    int div = 2;
    while (n > 1) {
        int coef = 0;
        while (n % div == 0) {
            n = n / div;
            coef++;
        }
        if (coef != 0) {
            cout << div << " " << coef << endl;
        }
        div++;
    }
}

// O(sqrt(n))
bool isPrime(int n) {
    assert(n >= 2);
    for (int div = 2; div * div <= n; div++) {
        if (n % div == 0) {
            return false;
        }
    }
    return true;
}

// compute primes lower than n
// O(n * ln(ln(n)))
// 1/2 + 1/3 + 1/5 + ... 1 / P_n ~ ln(ln(n))
// optimization:
// At each step in the main loop, 
// we cross numbers starting from div * div (and not div). All non-primes
// of the form p * div with p < div should be crossed already. 
void sieve(int n) {
    vector<bool> primes(n, true);
    primes[0] = false;
    primes[1] = false;
    primes[2] = true;

    for (int div = 2; div * div < n; div++) {
          if (primes[div]) {
              for (int i = div * div; i < n; i += div) {
                 primes[i] = false; 
             }
         }
    }
    for (int i = 0; i < n; i++) {
        if (primes[i]) cout << i << endl;
    }
}

int pgcd(int a, int b) {
    while (b != 0) {
        int tmp = a;
        a = b;
        b = tmp % b; 
    }
    return a;
}

int pgcd_rec(int a, int b) {
    if (b == 0) {
        return a;
    } else {
        return pgcd_rec(b, a % b);
    }
}

typedef tuple<int, int, int> tu;

// returns {u,v} such that u * a + v * b = pgcd(a,b) 
tu bezout(int a, int b) {
    assert(a > 0);
    int u = 0;
    int v = 0;
    int pgcd = 0;
    if (b == 0) {
        u = 1;
        v = 1;
        pgcd = a;
    } else {
        int u0, v0, pgcd0;
        tie(pgcd0, u0, v0) = bezout(b, a % b);
        u = v0;
        v = u0 - (a / b) * v0; 
        pgcd = pgcd0; 
    }
    assert(u * a + b * v == pgcd);
    cout << pgcd << " " << u << " " << v << endl;
    return {pgcd, u, v};
}

int main(int nargs, char **argv) {
    assert(pgcd_rec(13, 4) == 1);
    assert(pgcd_rec(60, 40) == 20);
    tu res1 = {1,-2,3};
    assert(bezout(10,3) == res1);
    tu res2 = {3,1,-2};
    assert(bezout(9,3) == res2);
    return 0;
}
