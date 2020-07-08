import custom_panda as pd
import numpy as np
import random as rd
data=pd.panda("iris.csv")
# pd.print_table(data)

layers=[]

# Function Definations
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
    for _ in range(column):
        temp=[]
        for _ in range(row):
            ten_pow=10**precision
            var=rd.randint(1,ten_pow-1)/ten_pow
            temp.append(var)
        temp_matrix.append(temp)
    return np.array(temp_matrix)

def sigmoid(x):
    return 1/1+np.exp(-1*x)

def activation_function(x):
    return sigmoid(x)

def weight_correction(weight):
    temp_weight=[]
    column_sum=weight.sum(axis=0)
    for row in range(len(weight)):
        temp_row=[]
        for item in range(len(weight[row])):
            temp_row.append(weight[row][item]/column_sum[item])
        temp_weight.append(temp_row)
    return np.array(temp_weight)

def error_matrix(weights,output_error):
    error_array=[]
    error_array.append(output_error)
    for i in range(len(weights)-1,0,-1):
        temp=weight_correction(weights[i]).dot(error_array[0])
        error_array.insert(0,temp)
    return error_array

def front_propogation(layers,weights):
    # print(layers)
    for i in range(len(layers)-1):
        temp=(layers[i].dot(weights[i]))
        # print(temp,np.array(list(map(sigmod,temp))))
        layers[i+1]=np.array(list(map(activation_function,temp)))

    print("\nlayers :- ",layers)

def back_propogation(layers,weights,expected_output):
    print("\nError matrix :- ",error_matrix(weights,layers[-1]-expected_output))
    

def X():
    pass

# Input Layer
# number_of_input=2
# first input 1 and second input 3 and so on...
input_layer=np.array([1,3,2])
layers.append(input_layer)

# Hidden Layer
# creating hidden layer of 3 nodes and 2 nodes and so on ....
# hidden_layer=create_hidden_layers(3,4)
hidden_layer=create_hidden_layers(4)
layers.extend(hidden_layer)

# Output Layer
# number_of_output=3
output_layer=np.array([0,0,0])
layers.append(output_layer)

#for training
expected_output=np.array([1,2,3])

# weight metrices
weights=[]
for i in range(len(layers)-1):
    weights.append(temp_weight_matrix(len(layers[i+1]),len(layers[i])))

# print(weights)
for i in weights:
    print(i)

# Forward Propogation
front_propogation(layers,weights)

# print("input ",layers[0])
# print("output ",layers[-1] )

# Back Propogation
back_propogation(layers,weights,expected_output)


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