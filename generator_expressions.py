from filtering_comprehensions import is_prime
million_squres = (x*x for x in range(1000001))
# print(list(million_squres)[-10:])
print(sum(million_squres))

print(
    sum(x for x in range(1001)),
    sum(x for x in range(1001) if is_prime(x))
)
