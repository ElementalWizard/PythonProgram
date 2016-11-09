global xn
global yn


def ask():
    global xn
    global yn
    x = input("Enter first number: ")
    y = input("Enter second number: ")
    xn = x
    yn = y


def div():

    print("")
    print("Let\'s divide!")
    ask()
    z = float(xn)/yn
    print "El resultado es ", z


def sums():
    print("")
    print("Let\'s sum!")
    ask()
    e = xn+yn
    print "El resultado es ", str(e)


def minus():
    print("")
    print("Let\'s minus!")
    ask()
    e = xn-yn
    print "El resultado es ", str(e)


def divm(x, y):

    print("")
    print("Let\'s divide manually!")

    z = float(x)/y
    print "El resultado es ", z


def sumsm(x, y):
    print("")
    print("Let\'s sum manually!")
    e = x+y
    print "El resultado es ", str(e)


def op(x, y):
    divm(x, y)
    sumsm(x, y)


div()
sums()
minus()
op(6, 3)

