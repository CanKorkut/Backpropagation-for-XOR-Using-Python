"""
	Can Korkut
	24.04.2019
"""

import math
import random

def sigmoid(x):
    return 1 / (1 + math.exp(-x))
   
def sigmoid_derivative(x):
    return x*(1-x)

class input_neuron:
    def neuron_calculate(self,i0,i1,W0,W1,bias):
       f1=(W0*i0) +(i1*W1)+bias
       f_net=sigmoid(f1)
       return f_net
      
class output_neuron:
    def neuron_calculate(self,i0,i1,W0,W1,bias):
       f1=(W0*i0) +(i1*W1)+bias
       f_net=sigmoid(f1)
       return f_net

def predict():
   # create input and output neuron
   ineuron0 =  input_neuron()
   ineuron1 =  input_neuron()
   oneuron = output_neuron()
   
   fark=0
   sd=0
   global_error=0
   n = 5 # Learning rate
   
   X= [0,0,1,1]
   Y= [0,1,0,1]
   Z= [0,1,1,0]
   indis = 0
   # set weight random values
   W0=random.random()
   W1=random.random()
   W2=random.random()
   W3=random.random()
   W4=random.random()
   W5=random.random()
   
   W1_bias=random.random()
   W2_bias=random.random()
   W3_bias=random.random()
   counter=0
   #prediction
   while True:
      counter=counter+1
      if(counter==20000): # 20000 epoch
         break
      i0=X[indis]
      i1=Y[indis]
      in_0=ineuron0.neuron_calculate(i0,i1,W0,W1,W1_bias)
      in_1=ineuron1.neuron_calculate(i0,i1,W2,W3,W2_bias)
      out= oneuron.neuron_calculate(in_0,in_1,W4,W5,W3_bias)
	  
      print ( str(X[indis]) + " xor "+ str(Y[indis])+"= "+str(out))
      if counter % 4 == 0:
      	print ("---------------------- epoch: "+ str(counter)+" ----------------------------")
	  
      sd=sigmoid_derivative(out)
      fark=Z[indis]-out
      global_error=fark * sd * n
      hidden_error0=sigmoid_derivative(in_0) * global_error * W4 * n
      hidden_error1=sigmoid_derivative(in_1) * global_error * W5 * n
	  
      W0=W0 + (hidden_error0 * i0)
      W1=W1 + (hidden_error0 * i1)
      W2=W2 + (hidden_error1 * i0)
      W3=W3 + (hidden_error1 * i1)
      W4=W4 + (global_error * in_0)
      W5=W5 + (global_error * in_1)
      W1_bias=hidden_error0 + W1_bias;
      W2_bias=hidden_error1 + W2_bias;
      W3_bias=W3_bias + global_error
	  
      if(indis==3):
         indis=0
      else:
         indis=indis+1
         
      
      

if __name__=="__main__":
	predict()
    
    
    
