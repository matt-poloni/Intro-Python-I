from importlib import import_module
sieve = import_module("97_helpers").sieve

lim = int(input("\nINPUT LIMIT: "))
print(f"PRIMES: {sieve(lim)}\n")
