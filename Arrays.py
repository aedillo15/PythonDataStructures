#Array of numbers
numbers = [10,20,300,40.5,50]
#Random indexing --> 0(1) we can get the items if we know the index
#print(numbers[2])
#We can also change the value of an index in the array, only in Python can we change the value regardless of the datatype
numbers[1] = 'Adam'
#Printing out the new assigned value of the second index in the numbers array
print('The new assigned value to the second index ' + numbers[1])
#Printing out all the values in the numbers array by using a for loop
#for num in numbers:
#    print(num)
#Prints out the numbers array for the same length as the amount of indices in numbers
for i in range(len(numbers)):
    print(numbers[i])
#Prints the end of the array minus 2, so splices the end of the array by 2
print(numbers[:-2])


