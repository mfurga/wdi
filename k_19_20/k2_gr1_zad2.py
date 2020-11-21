#!/usr/bin/env python3

# Na zbiorze liczb całkowitych określono trzy operacje: A,B,C przekształcające liczby:
#  A: zwiększa liczbę o 3;
#  B: podwaja liczbę;
#  C: wszystkie parzyste cyfry w liczbie zwiększa o 1, np. 2356->3357, 1999->1999.
#
# Proszę napisać funkcję która sprawdza czy można przekształcić liczbę X na liczbę Y 
# w nie więcej niż N krokach. Do funkcji należy przekazać wartości X, Y, N, funkcja
# powinna zwrócić liczbę możliwych ciągów operacji przekształcających liczbę X w Y
# (lub wartość 0 jeżeli takie przekształcenie nie istnieje). Uwaga: zabronione jest
# używanie kolejno dwóch tych samych operacji.
#
# Na przykład:
#  Dla X=11,Y=31,N=4 funkcja powinna zwrócić 3 bo są 3 możliwe ciągi operacji: ABA, ACBC, CABA
#  Dla X=11,Y=32,N=4 funkcja powinna zwrócić 0.

from typing import Callable

def A(n: int):
  return n + 3

def B(n: int):
  return 2 * n

def C(n: int):
  s, i = 0, 1
  while n > 0:
    l = n % 10
    l += 1 - l % 2
    s += i * l
    n //= 10
    i *= 10
  return s

def count(x: int, y: int, n: int, op: Callable) -> int:
  if n == 0:
    return 0
  x = op(x)
  n -= 1
  if x == y:
    return 1
  if op == A:
    return count(x, y, n, B) + count(x, y, n, C)
  if op == B:
    return count(x, y, n, A) + count(x, y, n, C)
  if op == C:
    return count(x, y, n, A) + count(x, y, n, B)

def main(x: int, y: int, n: int) -> int:
  return count(x, y, n, A) + count(x, y, n, B) + count(x, y, n, C)

