#!/usr/bin/env python3

# Dwie liczby są zgodne piątkowo, jeżeli posiadają tyle samo cyfr parzystych w ich reprezentacjach w systemie
# pozycyjnym o podstawie 5. Dane są dwie tablice int tab1[MAX1][MAX1], tab2[MAX2][MAX2](MAX2 > MAX1> 1).
# Proszę napisać funkcję, która sprawdzi, czy możliwe jest takie przyłożenie tab1 do tab2, aby w pokrywającym się
# obszarze co najmniej 33% odpowiadających sobie elementów z tab1 i tab2 było zgodnych piątkowo.
# Uwaga: należy uwzględnić, że tab1 może tylko częściowo przykrywać tab2 (patrz rysunek), a wsprawdzanym obszarze
# musi znaleźć się co najmniej jeden element.

def compatible5(n1: int, n2: int) -> bool:
  c1, c2 = 0, 0
  while n1 > 0:
    if (n1 % 5) % 2 == 0:
      c1 += 1
    n1 //= 5
  while n2 > 0:
    if (n2 % 5) % 2 == 0:
      c2 += 1
    n2 //= 5
  return c1 == c2

def compare(t1: list, t2: list, k: int, l: int) -> bool:
  sz1, sz2 = len(t1), len(t2)
  c, g = 0, 0
  for i in range(sz1):
    if i + k < 0 or i + k >= sz2:
      continue
    for j in range(sz1):
      if j + l < 0 or j + l >= sz2:
        continue
      if compatible5(t1[i][j], t2[i + k][j + l]):
        g += 1
      c += 1
  return g / c >= 0.33

def main(t1: list, t2: list) -> bool:
  sz1, sz2 = len(t1), len(t2)
  assert sz2 > sz1 > 1

  for i in range(-1 * sz1 + 1, sz2):
    for j in range(-1 * sz1 + 1, sz2):
      if compare(t1, t2, i, j):
        return True
  return False

if __name__ == "__main__":
  t2 = [
    [1, 2, 3, 4],
    [4, 5, 6, 5],
    [7, 8, 9, 6],
    [7, 8, 9, 6]
  ]
  t1 = [
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3]
  ]
  print(main(t1, t2))

