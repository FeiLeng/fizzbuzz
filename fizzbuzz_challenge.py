x = input("what is your favorite number?")
number = int(x)
if (number%3==0) and (number%5==0):
    print ("Fizz Buzz")
elif number%3 == 0:
    print("Fizz")
elif number%5 == 0:
    print ("Buzz")
else: 
    print(f"{number}")