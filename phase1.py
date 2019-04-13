from random import choice
from sys import exit, stdout
from time import sleep

a = range(1, 10)
o = []
i = []


def write(*args):
    args = [arg for arg in args if arg in a]
    o.append(choice(args))
    print("A: {}".format(o[-1]))


def read():
    try:
        i.append(int(input("B: ")))
    except (NameError, SyntaxError, TypeError, EOFError):
        exit()
    del a[a.index(o[-1])]
    if i[-1] in a:
        del a[a.index(i[-1])]
    else:
        exit()


write(1, 3, 5, 7)
read()
if i[-1] == 9:
    write((o[-1] + 3) % 8 + 1)
    read()
    write((i[-1] + 3) % 8 + 1)
    read()
    if not i[-2] % 2 and i[-1] in (o[-1] % 8 + 1, (o[-1] + 6) % 8 + 1):
        write((i[-1] + 3) % 8 + 1)
        read()
        if i[-1] in (o[-1] % 8 + 1, (o[-1] + 6) % 8 + 1):
            write(*a)
            m = "Congratulations. Did you figure it out?"
            for i in range(len(m)):
                stdout.write("\r{}".format(m[:i + 1]))
                stdout.flush()
                sleep(0.2)
        else:
            write(o[-1] % 8 + 1, (o[-1] + 6) % 8 + 1)
            exit()
    else:
        write(o[-1] % 8 + 1, (o[-1] + 6) % 8 + 1)
        exit()
elif i[-1] == (o[-1] + 3) % 8 + 1:
    write((o[-1] + 1) % 8 + 1, (o[-1] + 5) % 8 + 1)
    read()
    if i[-1] in {o[-1] % 8 + 1, (o[-1] + 6) % 8 + 1}.intersection((o[-2] % 8 + 1, (o[-2] + 6) % 8 + 1)):
        write((o[-1] + 3) % 8 + 1)
        read()
        if i[-1] in {o[-1] % 8 + 1, (o[-1] + 6) % 8 + 1}.intersection((o[-3] % 8 + 1, (o[-3] + 6) % 8 + 1)):
            write(9)
            exit()
        else:
            write(o[-3] % 8 + 1, (o[-3] + 6) % 8 + 1)
            exit()
    else:
        write(list({o[-1] % 8 + 1, (o[-1] + 6) % 8 + 1}.intersection((o[-2] % 8 + 1, (o[-2] + 6) % 8 + 1)))[0])
        exit()
elif i[-1] in ((o[-1] + 1) % 8 + 1, (o[-1] + 5) % 8 + 1):
    write((i[-1] + 3) % 8 + 1)
    read()
    if i[-1] in {o[-1] % 8 + 1, (o[-1] + 6) % 8 + 1}.intersection((o[-2] % 8 + 1, (o[-2] + 6) % 8 + 1)):
        write((o[-2] + 3) % 8 + 1)
        read()
        write(9, list({o[-1] % 8 + 1, (o[-1] + 6) % 8 + 1}.intersection((o[-2] % 8 + 1, (o[-2] + 6) % 8 + 1)))[0])
        exit()
    else:
        write(list({o[-1] % 8 + 1, (o[-1] + 6) % 8 + 1}.intersection((o[-2] % 8 + 1, (o[-2] + 6) % 8 + 1)))[0])
        exit()
else:
    write(9)
    read()
    if i[-1] == (o[-2] + 3) % 8 + 1:
        if i[-2] in (o[-2] % 8 + 1, (o[-2] + 6) % 8 + 1):
            write((i[-2] + 2) % 8 + 1, (i[-2] + 4) % 8 + 1)
        else:
            write(i[-2] % 8 + 1, (i[-2] + 6) % 8 + 1)
        read()
        write(list({o[-1] % 8 + 1, (o[-1] + 6) % 8 + 1}.intersection((o[-3] % 8 + 1, (o[-3] + 6) % 8 + 1)))[0],
              (o[-1] + 3) % 8 + 1)
        exit()
    else:
        write((o[-2] + 3) % 8 + 1)
        exit()
