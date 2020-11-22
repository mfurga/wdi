#!/usr/bin/env python3
# Proszę napisać program wypisujący elementy ciągu Fibonacciego mniejsze od miliona.

a, b = 1, 1
while a < 1_000_000:
  print(a)
  a, b = b, a + b

