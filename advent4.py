file = "adventdata4.txt"
fh = open(file, 'r')
data = fh.readlines()

# import re
# import string

# def freqTable(string):
	# myTable = {}
	# for char in string:
		# if char in myTable:
			# myTable[char] += 1
		# else:
			# myTable[char] = 1
	# return myTable
	
# def makeCode(roomName):
	# myTable = freqTable(roomName)
	# list_key_values = [[k,v] for k,v in myTable.items()]
	# #key function is called on each element prior to making comparisons
	# #lambda function is simply x (i.e. element) maps to x[1] (i.e. second element)
	# list_key_values.sort(key = lambda x: (-x[1], x[0]))
	# top5 = list_key_values[0:5]
	# return [x[0] for x in top5]

# def isRoom(arr):
	# '''lists in arr are room ids. They follow the form ([a-z]*\-)*[1-9]*-[a-z]{5} where the first part is the room name, the second is the section id, and the third is the code.
	# Codes are legit if they are the top 5 most frequent letters in the room name, with ties broken in the code by alphabetic order.'''
	
	# #This is all chunking the room codes and stuff into chunks.
	# roomRegex = re.compile('.+?(?=[1-9])')
	# roomName = roomRegex.match(arr)
	# remainingString = arr[roomName.end():]
	
	# stationRegex = re.compile('[0-9]*')
	# stationId = stationRegex.match(remainingString)
	# remainingString = remainingString[stationId.end():]
	
	# codeRegex = re.compile('\[.*$')
	# code = codeRegex.match(remainingString)
	
	# roomName = roomName.group().replace('-','')
	# stationId = stationId.group()
	# code = code.group().replace('[','').replace(']','')
	
	# #frequency table of the roomname
	# trueCode = makeCode(roomName)

	# if trueCode == list(code):
		# return int(stationId)
	# else:
		# return 0
	
# if __name__ == "__main__":
	# count = 0
	# for room in data:
		# count += isRoom(room)
	# print count


#PART 2:
import re
import string

def freqTable(string):
	myTable = {}
	for char in string:
		if char in myTable:
			myTable[char] += 1
		else:
			myTable[char] = 1
	return myTable
	
def makeCode(roomName):
	myTable = freqTable(roomName)
	list_key_values = [[k,v] for k,v in myTable.items()]
	#key function is called on each element prior to making comparisons
	#lambda function is simply x (i.e. element) maps to x[1] (i.e. second element)
	list_key_values.sort(key = lambda x: (-x[1], x[0]))
	top5 = list_key_values[0:5]
	return [x[0] for x in top5]

def isRoom(arr):
	'''lists in arr are room ids. They follow the form ([a-z]*\-)*[1-9]*-[a-z]{5} where the first part is the room name, the second is the section id, and the third is the code.
	Codes are legit if they are the top 5 most frequent letters in the room name, with ties broken in the code by alphabetic order.'''
	
	#This is all chunking the room codes and stuff into chunks.
	roomRegex = re.compile('.+?(?=[1-9])')
	roomName = roomRegex.match(arr)
	remainingString = arr[roomName.end():]
	
	stationRegex = re.compile('[0-9]*')
	stationId = stationRegex.match(remainingString)
	remainingString = remainingString[stationId.end():]
	
	codeRegex = re.compile('\[.*$')
	code = codeRegex.match(remainingString)
	
	roomName = roomName.group().replace('-','')
	stationId = stationId.group()
	code = code.group().replace('[','').replace(']','')
	
	#frequency table of the roomname
	trueCode = makeCode(roomName)

	if trueCode == list(code):
		return True
	else:
		return False
		
def decrypt(arr):
	roomRegex = re.compile('.+?(?=[1-9])')
	roomName = roomRegex.match(arr)
	remainingString = arr[roomName.end():]
	
	stationRegex = re.compile('[0-9]*')
	stationId = stationRegex.match(remainingString)
	
	roomName = roomName.group()
	stationId = int(stationId.group())
	
	#frequency table of the roomname
	alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	decrypted = ''
	for char in roomName:
		if char == '-':
			decrypted += ' '
		elif char in alphabet:
			decrypted += alphabet[(alphabet.index(char) + stationId) % len(alphabet)]
	return decrypted
	
def getStationId(arr):
	roomRegex = re.compile('.+?(?=[1-9])')
	roomName = roomRegex.match(arr)
	remainingString = arr[roomName.end():]
	
	stationRegex = re.compile('[0-9]*')
	stationId = stationRegex.match(remainingString)
	
	roomName = roomName.group()
	stationId = int(stationId.group())
	return stationId
		
if __name__ == "__main__":
	for index, room in enumerate(data):
		if isRoom(room):
			decrypted = decrypt(room)
			if 'north' in decrypted:
				print getStationId(room)
		else:
			data[index] = 0


		