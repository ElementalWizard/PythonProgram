#part 1
print ("")
print("This is the 1st part")
def right_justify(name):
    x = len(name)
    y = 70-x
    name = (" " * y) + name
    print name
    print ("The lenght of this text is " + str(len(name)) + " and it starts at space number " + str(y))

right_justify("lol")


#part 2
print ("")
print("This is the 2nd part")
def do_twice(f, n):
    f(n)
    f(n)


def print_twice(n):
    print (str(n))
    print (str(n))

print ("")
do_twice(print_twice, 'spam')


def do_fourtimes(f, n):
    do_twice(f, n)
    do_twice(f, n)


do_fourtimes(print_twice, "spam")


#part 03
print ("")
print("This is the 3rd part")
def top_mid_bot(w):
    x = '+'
    y = '- '
    print x, y*w, x, y*w, x


def wall(n):
    z = 0
    while z < n:
        s = '  '
        w = '|'
        print w, s*n, w, s*n, w
        z = z + 1


def do_2x2(w):
    top_mid_bot(w)
    wall(w)
    top_mid_bot(w)
    wall(w)
    top_mid_bot(w)


print ("")
print("This is a 2x2 square.")
do_2x2(4)


def do_two(f):
    f()
    f()


def do_four(f):
    do_two(f)
    do_two(f)


def one_four_one(f, g, h):
    f()
    do_four(g)
    h()


def print_start():
    print '+',


def print_dash():
    print '-',


def print_wall():
    print '|',


def print_space():
    print ' ',


def print_end():
    print


def nothing():
    "do nothing"


def print1beam():
    one_four_one(nothing, print_dash, print_start)


def print1post():
    one_four_one(nothing, print_space, print_wall)


def print4beams():
    one_four_one(print_start, print1beam, print_end)


def print4posts():
    one_four_one(print_wall, print1post, print_end)


def print_row():
    one_four_one(nothing, print4posts, print4beams)


def print_grid():
    one_four_one(print4beams, print_row, nothing)

print ("")
print("This is a 4x4 square.")
print_grid()



