file = "adventdata.txt"
fh = open(file, 'r')
data = fh.readlines()
mydata = [map(int, x.split()) for x in data]

def isTriangle(a,b,c):
	'''contrapositive of triangle law (sum of any two sides is greater than the third then the triangle is impossible) -> (sum of ny 2 sides is less than the third, then the triangle is possible'''
	sumSides = a + b + c
	if (a >= sumSides - a):
		return False
	if (b >= sumSides - b):
		return False
	if (c >= sumSides - c):
		return False
	return True
	
def countTriangles(arr):
	'''arr is formatted with one triangle (sides a, b, c) as ints in a list on each line'''
	count = 0
	for tri in arr:
		if isTriangle(tri[0], tri[1], tri[2]):
			count = count + 1
			print tri
	return count
#There are 1902 arrs of length 3 in mydata.
#I go through each row
#Part 2
def transformData(arr):
	total_arr = [None] * len(arr)
	for i in range(0, len(arr), 3):
		arr0 = [arr[i][0], arr[i+1][0], arr[i+2][0]]
		arr1 = [arr[i][1], arr[i+1][1], arr[i+2][1]]
		arr2 = [arr[i][2], arr[i+1][2], arr[i+2][2]]
		print i
		total_arr[i] = arr0
		total_arr[i+1] = arr1
		total_arr[i+2] = arr2
	return total_arr
	 
	
if __name__ == "__main__":
	print countTriangles(transformData(mydata))
	
