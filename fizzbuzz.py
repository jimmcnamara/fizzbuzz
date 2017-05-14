def fizzbuzz():
    limit=int(input("select an upper limit:  "))
    for n in range(1,limit):
        if n%5==0 and n%3==0:
            print("buzz")
        elif n%5==0:
            print("fizz")
        elif n%3==0:
            print("buzzfizz")
        else:
            print(n)


fizzbuzz()
