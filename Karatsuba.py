
def getHalfSize(x,y):
	iMax = max(len(str(x)),len(str(y)))
	return (iMax/2 + iMax%2)

def karatsuba(x, y):
	iHalf = getHalfSize(x,y)
	x1 = x / pow(10,iHalf)
	x2 = x - (x1 * pow(10,iHalf))
	y1 = y / pow(10, iHalf)
	y2 = y - (y1 * pow(10,iHalf))
	print "Val1 %s => %s - %s " %(x,x1,x2) 
	print "Val2 %s => %s - %s " %(y,y1,y2)
	#x1 = getHalf(x)
	#x2 = x - x1
	

	#y1 = getHalf(y)
	#y2 = y - y1
	

def main():
	print "Calculare Karatsuba"
	karatsuba(12345,6789)


if __name__ == '__main__': 
	main() 