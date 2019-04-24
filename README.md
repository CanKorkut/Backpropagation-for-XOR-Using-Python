# Backpropagation-for-XOR-Using-Python

Application performs backpropagation algorithm for xor problem


# Variables

X = [ 0, 0, 1, 1] Y = [ 0, 1, 0, 1] are inputs

Z = [ 0,1,1,0] is label array

n is learning rate 

W's are weights and and initially gets a random value
# Formula

W_new = W_old + ß

ß = n * (input) * (error)

global_error = label(Z) - output 

hidden_error=sigmoid_derivative(input) * global_error * W_hidden * n

