#Problem1 sum of multiples of 3 or 5 below 1000

#creates a program that finds out all multiples of 3 or 5 below 1000, and sums them all together  



total=0
for element in range(1,1000):
    if element%3==0 or element%5==0:
        total=total+element
        print (str(element) + "element")  
        print (total)
print(total)

