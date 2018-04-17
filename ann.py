def parse_input():
    d = int(input())
    m = int(input())
    n = int(input())

    training_set = []
    test_set = []

    for i in range(m):
        training_set.append(input().replace(' ','').split(','))
    for i in range(n):
        test_set.append(input().replace(' ','').split(','))

    print(training_set)
    print(test_set)

parse_input();
