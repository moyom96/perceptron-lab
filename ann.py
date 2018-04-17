import random

def parse_input():
    d = int(input())
    m = int(input())
    n = int(input())

    training_set = []
    test_set = []
    weights = []

    for i in range(m):
        training_set.append(input().replace(' ','').split(','))
    for i in range(n):
        test_set.append(input().replace(' ','').split(','))

    print(training_set)
    print(test_set)

def get_output(w, x):
    threshold = 0
    input_sum = 0
    for i in range(len(w)):
        input_sum += (w[i] * x[i])

    return 1 if input_sum > threshold else return 0

def train_network(d, weights, train_set):
    for i in range(d):
        weights.append(random.random())
    threshold = random.random()

    for x in train_set:
        y = x[d]
        actual_y = get_output(weights, x)


parse_input();

