#!/usr/bin/env python3
# Proszę napisać funkcję, która jako argument przyjmuje liczbę całkowitą i wypisuje wszystkie co najmniej
# dwucyfrowe liczby pierwsze, powstałe poprzez wykreślenie z liczby pierwotnej co najmniej jednej cyfry.

def isprime(n: int) -> bool:
  if n < 2:
    return False
  if n == 2 or n == 3:
    return True
  if n % 2 == 0 or n % 3 == 0:
    return False
  i = 5
  while i * i <= n:
    if n % i == 0:
      return False
    i += 2
    if n % i == 0:
      return False
    i += 4
  return True

# 3    2    1    0 (i)
# ----------------
# 1    2    3    4 (n = 1234) (nsz = 3)
# ===
# 1    2    3    4 (csz = 0)
# ---
#     12   13   14 (csz = 1)
#          23   24
#               34
# ---
#         123  124 (csz = 2)
#              134
#              234
# ---
#             1234 (csz = 3)
def divide(n: int, nsz: int, i: int, c: int, csz: int) -> None:

  for j in range(nsz, i - 1, -1):
    t = (n // (10 ** j)) % 10
    t *= 10 ** csz
    t += c

    if t > 9 and isprime(t):
      print(t)

    if csz + 1 != nsz:
      divide(n, nsz, j + 1, t, csz + 1)

def main(n: int) -> None:
  sz = len(str(n))
  divide(n, sz - 1, 0, 0, 0)

if __name__ == "__main__":
  main(1234)

