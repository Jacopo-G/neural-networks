def neuron_activation(inputs, weights, bias):
    n = 0
    output = []
    for weight_list in weights:
        output.append(sum([input * weight for input, weight in zip(inputs, weight_list)]) + bias[n])
        n += 1
    return output


inputs = [1, 2, 3, 4]
weights = [[0.2, 0.5, -0.3, 0.1], [-0.9, 0,4, 0.5, -0.2], [0.7, 0.2, 0.8, -0.8]]
bias = [1, 2, 0.5]

print(neuron_activation(inputs, weights, bias))