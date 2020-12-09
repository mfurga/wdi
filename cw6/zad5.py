#!/usr/bin/env python3
#
# Dany jest ciąg zer i jedynek zapisany w tablicy T[N]. Proszę napisać funkcję, która odpowiadana pytanie
# czy jest możliwe pocięcie ciągu na kawałki z których każdy reprezentuje liczbę pierwszą. Długość każdego
# z kawałków nie może przekraczać 30. Na przykład dla ciągu 111011 jest to możliwe, a dla ciągu 110100
# nie jest możliwe.

import sys

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

def validate_chunks(p: list) -> bool:
  s = l[0]
  for i in range(1, len(p)):
    if p[i - 1] != p[i]:
      if not isprime(s):
        return False
      s = 0
    s = s * 2 + l[i]
  return isprime(s)

def generate(p: list, i: int = 0, c: int = 1, m: int = 0):
  p[i] = c
  if m == 30:
    return
  if i + 1 == len(p):
    if validate_chunks(p):
      print("TAK")
      sys.exit(0)
    return
  generate(p, i + 1, c, m + 1)
  generate(p, i + 1, c + 1, 0)

if __name__ == "__main__":
  l = [1, 1, 1, 0, 1, 1]
  sz = len(l)
  p = [0] * sz
  generate(p)
  print("NIE")

