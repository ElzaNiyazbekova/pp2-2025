import random
def r():
    b = input("Hello! What is your name? ")
    print("Well, " + b + ", I am thinking of a number between 1 and 20.")

    a = random.randint(1, 20)
    d = 0
    while True:
        c = int(input("Take a guess. "))
        if c == 0:
            break
        if c<a:
            print("Your guess is too low")
            d+=1
        elif c>a:
            print("Your guess is too high.")
            d+=1
        else:
            print("Good job," +b+"!"+"You guessed my number in", d, "guesses!")
            d = 0
r()
    

