data = "R4, R4, L1, R3, L5, R2, R5, R1, L4, R3, L5, R2, L3, L4, L3, R1, R5, R1, L3, L1, R3, L1, R2, R2, L2, R5, L3, L4, R4, R4, R2, L4, L1, R5, L1, L4, R4, L1, R1, L2, R5, L2, L3, R2, R1, L194, R2, L4, R49, R1, R3, L5, L4, L1, R4, R2, R1, L5, R3, L5, L4, R4, R4, L2, L3, R78, L5, R4, R191, R4, R3, R1, L2, R1, R3, L1, R3, R4, R2, L2, R1, R4, L5, R2, L2, L4, L2, R1, R2, L3, R5, R2, L3, L3, R3, L1, L1, R5, L4, L4, L2, R5, R1, R4, L3, L5, L4, R5, L4, R5, R4, L3, L2, L5, R4, R3, L3, R1, L5, R5, R1, L3, R2, L5, R5, L3, R1, R4, L5, R4, R2, R3, L4, L5, R3, R4, L5, L5, R4, L4, L4, R1, R5, R3, L1, L4, L3, L4, R1, L5, L1, R2, R2, R4, R4, L5, R4, R1, L1, L1, L3, L5, L2, R4, L3, L5, L4, L1, R3"
data = data.split(", ")

def walk2(data):
	xPos = 0
	yPos = 0
	headings = [[1,0],[0,-1],[-1,0],[0,1]]
	curr = 0
	visited = []
	for element in data:
		print xPos, yPos, headings[curr], element[0], int(element[1:])
		myData = element[0]
		displacement = int(element[1:])
		xMove = headings[curr][0]
		yMove = headings[curr][1]
		
		#Update position and heading
		if myData == "R":
			for i in range(1, displacement+1):
				visited.append([xPos, yPos])
				xPos += (xMove)
				yPos += (yMove)
				if ([xPos, yPos] in visited):
					return [xPos, yPos]
				
			curr = (curr + 1) % 4
		else:
			print xMove, displacement
			for i in range(1, displacement+1):
				visited.append([xPos, yPos])
				xPos += (-xMove)
				yPos += (-yMove)
				if ([xPos, yPos] in visited):
					return [xPos, yPos]
				
			curr = (curr - 1) % 4
	
	total_dist = abs(xPos) + abs(yPos)
	return total_dist
	
def walk(data):
	xPos = 0
	yPos = 0
	headings = [[1,0],[0,-1],[-1,0],[0,1]]
	curr = 0
	for element in data:
		print xPos, yPos, headings[curr], element[0], int(element[1:])
		myData = element[0]
		displacement = int(element[1:])
		xMove = headings[curr][0]
		yMove = headings[curr][1]
		
		#Update position and heading
		if myData == "R":
			xPos += (xMove * displacement)
			yPos += (yMove * displacement)
			curr = (curr + 1) % 4
		else:
			xPos += (-xMove * displacement)
			yPos += (-yMove * displacement)
			curr = (curr - 1) % 4
	
	total_dist = abs(xPos) + abs(yPos)
	return total_dist
			
	
print walk2(data)


			