import random

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

    return training_set, test_set, d

def get_output(w, x, bias):
    input_sum = bias # 1 * bias
    
    for i in range(len(w)):
        input_sum += (w[i] * float(x[i]))

    return 1 if input_sum > 0 else 0

def train_network(d, weights, train_set):
    for i in range(d):
        weights.append(random.random())
    bias = random.random()

    error_threshold = 0.5
    eta = 0.5
    itr_threshold = 1000

    itr_error = 1
    itr_num = 0
    while itr_error > error_threshold and itr_num < itr_threshold:
        itr_error = 0
        for x in train_set:
            y = float(x[d])
            actual_y = get_output(weights, x, bias)
            itr_error += pow(abs(actual_y - y), 2)

            for j in range(d + 1):
                if j == d:
                    bias += (eta * (y - actual_y))
                else:
                    weights[j] += (eta * (y - actual_y) * float(x[j]))
        itr_num += 1

    if itr_num == itr_threshold:
        return -1

    return weights, bias


sets = parse_input(); # Train set is 0, test set is 1 and d is 2

weights = []

new_weights = train_network(sets[2], weights, sets[0])

if new_weights == -1:
    print("no solution found")
else:
    for x in sets[1]:
        print(get_output(new_weights[0], x, new_weights[1]))
