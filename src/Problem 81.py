# https://projecteuler.net/problem=81
#Path sum: two ways
#Using only translations of 1 right and 1 down, find the value of theshortest path from the top left to the bottom right of problem81matrix.txt

#imports the txt matrix file
f=open('problem81 matrix.txt','r')
content=f.read()
print(content)
f.close()


#or i in content:
    #print (i)

#read each line of the txt file and add it to a line on an array of an array
#print (super_matrix)