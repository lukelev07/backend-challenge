# Written by Luke Levis

"""
1.) Edge cases that I have accounted for include a list that was completely rotated, or a list of length one.

2.) The expected running time of this algorithm (assuming distinct entries) is O(log n). 
However, if the list were made up of non-distinct integers (say a list of all 2's and one 4), 
then the running time would become inneficient since we would need to look individually at n elements--extending the runtime to O(n).

3.) If the initial list contained a large amount of elements, parallelizing the process would benefit greatly. 
One option is to use the multithreading enhancements that something like OpenMP provides. If we split up the list into equal sized sections, 
and gave each thread the job of finding the max element in its section, when we combined the results, finding the max element in the much smaller list would become more efficient.

Another option is to take advantage of the Map Reduce paradigm with Spark or Hadoop. 
Something like the Amazon EC2 servers would  serve as our "threads" and the work could be split among the servers to handle their respective sections of the list, then the results could be joined.

Of course, one would have to decide if the costs of multiple fork-and-join operations was worth it. 

"""

def shiftSearch(nums, low, high):
	# list rotated all the way
	if nums[low] < nums[high]:
		return nums[high]
	# list of length 1
	elif low == high:
		return nums[high]
	# middle of current section
	middle = (low + high)/2	
	# check middle and prevent out of bounds error
	if middle < high and nums[middle] > nums[middle+1]:
		return nums[middle]
	# decide which side to recurse on
	elif nums[low] > nums[high]:
		return shiftSearch(nums, low, middle-1)
	else:
		return shiftSearch(nums, middle+1, high)

def main():
	l1 = [8, 9, 10, 11, 1, 3, 7]
	r1 = shiftSearch(l1, 0, len(l1)-1)
	print "The result should be 11 and it is {0}.".format(r1)

	l2 = [6, 8, 10, 2, 4]
	r2 = shiftSearch(l2, 0, len(l2)-1)
	print "The result should be 10 and it is {0}.".format(r2)

	l3 = [2, 4, 6, 8, 10]
	r3 = shiftSearch(l3, 0, len(l3)-1)
	print "The result should be 10 and it is {0}.".format(r3)

	# look away! It runs in O(n), ahh!
	l4 = [2, 2, 2, 2, 2, 2, 2, 2, 2, 4, 2, 2, 2, 2, 2, 2, 2, 2, 2]
	r4 = shiftSearch(l4, 0, len(l4)-1)
	print "The result should be 4 and it is {0}.".format(r4)

main()
