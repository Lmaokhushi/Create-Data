import numpy as np
import pandas as pd

def data(a):
  if (a==1):
    x = np.random.rand(5,5)
    dataframe1 = pd.DataFrame(x,columns=['A','B','C','D','E'])
  elif(a == 2):
        x = [0,0,0,0,0]
        r1= [0,0,0,0,0]
        r2= [0,0,0,0,0]
        r3= [0,0,0,0,0]
        r4= [0,0,0,0,0]
        print('Enter the values for columns: ')
        i=0
        for i in [0,1,2,3,4]:
            x[i] = input()
            i = i + 1
        print('Enter the values for first row: ')
        i=0
        for i in [0,1,2,3,4]:
            r1[i] = int(input())
            i = i + 1
        print('Enter the values for second row: ')
        i=0
        for i in [0,1,2,3,4]:
            r2[i] = int(input())
            i = i + 1
        print('Enter the values for third row: ')
        i=0
        for i in [0,1,2,3,4]:
            r3[i] = int(input())
            i = i + 1
        print('Enter the values for fourth row: ')
        i=0
        for i in [0,1,2,3,4]:
            r4[i] = int(input())
            i = i + 1
        dataframe1 = pd.DataFrame([r1,r2,r3,r4] , columns = x)
  else:
        print('DataFrame creation failed please enter 1 or 2 and try again')
  print(dataframe1)


print("Select the type of data that you want to plot \nChoose one of the three options given below")
print('1.Random data with 5 rows and 5 columns')
print('2.Customize dataframe with 5 columns and 4 rows')
a = int(input())
dataframe1 = data(a)
