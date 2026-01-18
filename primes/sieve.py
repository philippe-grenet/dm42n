import math
import sys

def simple_sieve(limit):
  """Return all primes <= limit using the classic sieve."""
  is_prime = [True] * (limit + 1)
  is_prime[0:2] = [False, False]

  for p in range(2, int(math.isqrt(limit)) + 1):
    if is_prime[p]:
      for multiple in range(p * p, limit + 1, p):
        is_prime[multiple] = False

  return [p for p in range(2, limit + 1) if is_prime[p]]


def segmented_sieve(n):
  segment_size = int(math.isqrt(n)) + 1
  print("segment_size = ", segment_size)

  # Step 1: primes up to sqrt(n)
  base_primes = simple_sieve(segment_size)
  print("base_primes = ", base_primes)

  # Step 2: process segments [low, high)
  low = 2
  high = low + segment_size

  while low <= n:
    if high > n + 1:
      high = n + 1
    print("\nprocess segment: low = ", low, ", high = ", high)

    # Boolean array for current segment
    is_prime = [True] * (high - low)

    # ---- core segmented logic ----
    for p in base_primes:
      print("  p = ", p)

      # Find first multiple of p in [low, high)
      start = max(p * p, ((low + p - 1) // p) * p)
      print("  start = ", start)

      for multiple in range(start, high, p):
        is_prime[multiple - low] = False
        print("     multiple = ", multiple,", mark ", multiple - low)

    # --------------------------------
    # Output primes in this segment
    for i in range(low, high):
      if i >= 2 and is_prime[i - low]:
        print("  => ", i)

    low = high
    high += segment_size


segmented_sieve(int(sys.argv[1]))
