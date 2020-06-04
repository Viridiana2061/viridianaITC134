

#make an array for the sorting of the selection 

array =[13,4,9,5,3,16,12]

def selectionSort(array):


	n = len(array)

	for i in range(n): #<--- Whatever the lenght of the array is how many times you are going to run the 

	#initially assume the first element of the unsorted part as the minimum 

	minimum = i 

	for j in range(i+1,n):

		if (array[j] < array[minimum]):

			minimum = j 



		temp = array[i]
		array[i] = array[minimum]
		array[minimum] = temp

	return array


print(selectionSort(array))
