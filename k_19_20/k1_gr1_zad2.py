#!/usr/bin/env python3

# Dana jest tablica int t[N][N] zawierająca liczby naturalne. Proszę napisać funkcję, która sprawdza
# czy z tablicy można usunąć jeden wiersz i dwie kolumny, tak aby każdy z pozostałych elementów tablicy
# w zapisie dwójkowym posiadał nieparzystą liczbę jedynek.

def count_ones(n: int) -> int:
  c = 0
  while n > 0:
    if n % 2 == 1:
      c += 1
    n //= 2
  return c

def check(t: list, r: int, c1: int, c2: int) -> bool:
  sz = len(t)
  for i in range(sz):
    if i == r:
      continue
    for j in range(sz):
      if j == c1 or j == c2:
        continue
      if t[i][j] == 0:
        return False
  return True

def main(t):
  sz = len(t)

  for i in range(sz):
    for j in range(sz):
      if count_ones(t[i][j]) % 2 == 1:
        t[i][j] = 1
      else:
        t[i][j] = 0
 
  for r in range(sz):
    for c1 in range(sz - 1):
      for c2 in range(c1 + 1, sz):
        if check(t, r, c1, c2):
          return True

  return False

if __name__ == "__main__":
  t = [
    [1, 1, 3, 3],
    [3, 1, 1, 1],
    [1, 1, 1, 1],
    [3, 1, 3, 3]
  ]
  print(main(t))

