from random import randrange


def dice(numbers):
    print numbers
    a = lambda x, y: 'o' if x > y else ' '
    b = lambda x: 'o' if x % 2 else ' '
    st = ''
    print '----- ----- ----- ----- -----'
    for n in numbers:
        st += '|' + a(n, 1) + ' ' + a(n, 3) + '| '
    print st + '\n|   | |   | |   | |   | |   |'
    st = ''
    for n in numbers:
        st += '|' + a(n, 5) + b(n) + a(n, 5) + '| '
    print st + '\n|   | |   | |   | |   | |   |'
    st = ''
    for n in numbers:
        st += '|' + a(n, 3) + ' ' + a(n, 1) + '| '
    print st + '\n----- ----- ----- ----- -----\n'


def roll():
    d = []
    ans = 0
    for i in range(5):
        n = randrange(1, 7)
        ans += n-1 if n in [3, 5] else 0
        d.append(n)
    dice(d)
    return ans


def main():
    print 'The name of the game is Pedals Around the Rose'
    print 'All answers are either an even number or zero'
    while True:
        a = roll()
        while True:
            try:
                s = int(raw_input('What is the answer? '))
                break
            except ValueError:
                pass
            print 'Enter a number'
        if s == a:
            print 'You win!'
            exit()
        else:
            print 'Incorrect! The answer was', a


if __name__ == '__main__':
    main()
