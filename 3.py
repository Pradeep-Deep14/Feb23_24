def is_prime(number):
    if number <2:
        return False
    
    for i in range(2,number):
        if number % i == 0:
            return False
    return True

#Print Prime Numbers

print("Prime Numbers between 1 and 100:")
for number in range(1,101):
    if is_prime(number):
        print(number,end=" ")