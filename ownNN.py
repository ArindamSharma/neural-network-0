import numpy as np
import custom_panda as pd
import random as rd
import pickle
data=pd.panda("iris.csv")
# pd.print_table(data)
layers=[]
# Function Definations
def sigmoid(x):
    # if(x>0):
    #     return x
    # return 0
    return 1/1+np.exp(-1*x)

def sigmoid_derivative(x):
    # if(x>0):
    #     return 1
    # return 0
    return sigmoid(x)*(1-sigmoid(x))

def activation_function(x):
    return sigmoid(x)

def printweights(weights):
    print("weights :-")
    for i in weights:
        print(i)

def create_hidden_layers(*number_of_nodes):
    array=[]
    for i in number_of_nodes:
        temp=[]
        for _ in range(i):
            temp.append(0)
        array.append(np.array(temp))
    return array

def temp_weight_matrix(row,column):
    precision=1
    temp_matrix=[]
    for _ in range(row):
        temp=[]
        for _ in range(column):
            ten_pow=10**precision
            var=rd.randint(1,ten_pow-1)/ten_pow
            temp.append(var)
        temp_matrix.append(temp)
    return np.array(temp_matrix)

def random_weights_generator(layers):
    # weight metrices
    weights=[]
    for i in range(len(layers)-1):
        weights.append(temp_weight_matrix(len(layers[i+1]),len(layers[i])))
    return weights

def front_propogation(layers,weights):
    for i in range(len(weights)):
        temp=np.matmul(weights[i],layers[i])
        # print(temp,np.array(list(map(sigmod,temp))))
        layers[i+1]=np.array(list(map(activation_function,temp)))

def weight_change(weight):
    temp_weight=[]
    # print(weight)
    row_sum=weight.sum(axis=1)
    # print(row_sum)
    for row in range(len(weight)):
        temp_row=[]
        for item in range(len(weight[row])):
            x=weight[row][item]/row_sum[row]
            temp_row.append(x)
        temp_weight.append(temp_row)
    return np.array(temp_weight)

def create_error_matrix(weights,output_error):
    error_array=[]
    error_array.append(output_error)
    for i in range(len(weights)-1,0,-1):
        temp=np.matmul(weight_change(weights[i]).transpose(),(error_array[0]))
        error_array.insert(0,temp)
    return error_array

def error_weight_differential(error,prev_output,linked_weights):
    # print(error,"---",linked_weights,"----",prev_output)
    temp_sum=0
    for i,j in zip(prev_output,linked_weights):
        temp_sum+=i*j 
        # print(i,",",j,",",temp_sum)
    # print(temp_sum,",",-1 * sigmoid_derivative(temp_sum) )
    return ( -1 *error* sigmoid_derivative(temp_sum) ) *( prev_output)

def back_propogation(layers,weights,target_output,learning_rate):
    actual_output=layers[-1]
    error_matrix=create_error_matrix(weights,target_output-actual_output)
    # print("error:- ",error_matrix)

    for layer_index in range( (len(error_matrix)-1),-1,-1  ):
        for node in range(len(error_matrix[layer_index])):
            # print(weights[layer_index])
            x=error_weight_differential(
                    error_matrix[layer_index][node],
                    layers[layer_index],
                    weights[layer_index][node]
                    )
            weight_old=weights[layer_index][node]
            weight_new=weight_old-(learning_rate*x )
            # print(weight_old,learning_rate,x,weight_new)
            weights[layer_index][node]=weight_new

def Test(layers,weights):
    front_propogation(layers,weights)

def Train(layers,weights,expected_output,learning_rate):
    Test(layers,weights)
    back_propogation(layers,weights,expected_output,learning_rate)


# Input Layer
# number_of_input=2
# first input 1 and second input 3 and so on...
input_layer=np.array([1,2,3])
layers.append(input_layer)
# Hidden Layer
# creating hidden layer of 3 nodes and 2 nodes and so on ....
# hidden_layer=create_hidden_layers(3,4)
hidden_layer=create_hidden_layers(4,5,6,7,8,9,8,5,4)
layers.extend(hidden_layer)
# Output Layer
# number_of_output=3
output_layer=np.array([0,0,0])
layers.append(output_layer)
#for training
expected_output=np.array([2,4,6])
#learining rate
learning_rate=0.0008
#getting random weights

weights=random_weights_generator(layers)

printweights(weights)
print(layers)
for _ in range(100):
    Train(layers,weights,expected_output,learning_rate)
    print("layers :-",layers)

printweights(weights)

Test(layers,weights)
layers[0]=np.array([1,5,8])
print("layers :-",layers)


# import tkinter as tk
# root=tk.Tk()
# root.title("Neural Networking")
# root.geometry('1024x768')
# lbl=tk.Label(root,text="Number of input Node ")
# lbl.pack()
# txt = tk.Entry(root, width=10) 
# txt.pack() 
  
  
# # function to display user text when 
# # button is clicked 
# def clicked(): 
  
#     res = "You wrote" + txt.get() 
#     lbl.configure(text = res) 
  
# # button widget with red color text inside 
# btn = tk.Button(root, text = "Click me" , 
#              fg = "red", command=clicked) 
  
# btn.pack() 
# root.mainloop()