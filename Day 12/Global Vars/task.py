# # Modifying Global Scope
#
# enemies = 1
#
#
# def increase_enemies():
#     global enemies
#     enemies += 1
#     print(f"enemies inside function: {enemies}")
#
#
# increase_enemies()
# print(f"enemies outside function: {enemies}")


#            prime no

def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True

print(is_prime(2))
print(is_prime(3))
print(is_prime(5))
print(is_prime(75))
