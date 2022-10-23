import sys
sys.setrecursionlimit(5000)
def check(y, t, h):
    print('n = ' + str(y))
    if y > h:
        h = y

    if not y == 1:
        if (y % 2) == 0:
            even(y, t, h)
        else:
            odd(y, t, h)
    else:
        end(t, h)

def odd(x, t, h):
    new = x
    new *= 3
    new += 1
    t += 1
    check(new, t, h)

def even(z, t, h):
    newe = z
    newe = newe / 2
    t += 1
    check(newe, t, h)

def end(t, h):
    print('Process ended.')
    print('')
    print('---------------------')
    print('       Results       ')
    print('')
    print('Modifications - ' + str(t))
    print('Peak - ' + str(h))
    print('---------------------')
    sys.exit()
print('')
print('Madjik\'s 3n+1 Calculator')
print('')
print('-----Rules-----')
print('Even numbers get divided by 2.')
print('Odd numbers get multiplied by three and incremented by 1.')
print('')
print("\x1b]8;;https://madjikstuff.rf.gd/\aMore tools like this.\x1b]8;;\a")
print('')
start = int(input('Enter input (n): '))
check(start, 0, 0)
