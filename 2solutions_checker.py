with open(r'C:\Users\newma\OneDrive\Desktop\PCS_II\Assignment2\my_output.txt','r') as file:

    A = file.readlines()

with open(r'C:\Users\newma\OneDrive\Desktop\PCS_II\Assignment2\sample_output.txt','r') as file:

    B = file.readlines()

if A==B:
    print("YAY")
else:
    print("nope,try again you can do it!!!!")