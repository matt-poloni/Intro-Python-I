from importlib import import_module
is_prime = import_module("97_helpers").is_prime

num = int(input("\nIS IT PRIME? "))

prime = is_prime(num)
yn = "YES" if prime else "NO"
nt = "n't" if not prime else ""

print(f"{yn}, {num} is{nt} prime\n")
