# Python Program to Swap First & Last Letters of a String
def swapchar(string):
	start = string[0]
	end   = string[-1]
	newstr = ''
	for char in string:
		if char == start: #Appending a Last Letter in First Position
			newstr = end
			continue
		elif char == end:
			newstr += start #Appending a First Letter in Last Position
			break
		newstr += char
	return newstr.lower()
# Driver Code
if __name__ == '__main__':
	swap = swapchar("Google")
	print(swap)