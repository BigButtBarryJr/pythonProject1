#  defines the variable num as inputted integer
num = int(input("Input number: "))
count = 0

#  if num is less than or equal to 1, it's not a prime
if num <= 1:
    print("All primes are higher than 1")

#  it determines whether the number is prime or not
else:
    for i in range(num):
        if 1 < i < num:
            if num % i == 0:
                print(f"{num} / {i} = {int(num / i)}")
                count += 1

#  if the number is not a prime, it shows the calculations and tells you that it's not a prime
    if count > 0:
        print(f"\nThat is {count} even divisions")
        print(f"{num} is not prime")

#  if the number is a prime, it simply tells you so
    else:
        print(f"{num} is prime")