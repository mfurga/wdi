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

def subset(n: int, d: int, t: int = 0, i: int = 0) -> None:
  if d == 0:
    if t != n and t > 9 and isprime(t):
      print(t)
    return
  subset(n, d // 10, (d % 10) * 10 ** i + t, i + 1)
  subset(n, d // 10, t, i)

def main(n: int) -> None:
  subset(n, n)

if __name__ == "__main__":
  main(1234)

