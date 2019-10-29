from importlib import import_module
is_prime = import_module("97_helpers").is_prime

num = int(input("\nIS IT PRIME? "))
yn = "YES" if is_prime(num) else "NO"
nt = "n't" if not is_prime(num) else ""
print(f"{yn}, {num} is{nt} prime\n")
