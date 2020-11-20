#!/usr/bin/env python3

# Dane są dwie tablice int t1[N], int t2[N] wypełnione liczbami naturalnymi. Proszę napisać
# funkcję, która sprawdzaczy czy każdej z tablic można wyciąć po jednym kawałku, tak aby suma
# elementów w obu kawałkach była: co najmniej drugą potęgą dowolnej liczby naturalnej.
# Łączna długości obu kawałków powinna wynosić 24.

CHUNKS_SIZE = 24

def is_at_sec_pow(n: int) -> bool:
  i, c = 2, 0
  while n % i != 0:
    if i * i > n:
      return False
    i += 1
  while n % i == 0:
    c += 1
    n //= i
  return n == 1 and c >= 2

