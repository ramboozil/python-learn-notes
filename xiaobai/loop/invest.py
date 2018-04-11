def invest(amount, rate, time):
    print('pricinple amount is {}'.format(amount))
    for i in range(1, time+1):
        total = amount * (1 + rate) ** i
        print('year {} :'.format(i) + '$' + str(total))


invest(100, 0.05, 10)
