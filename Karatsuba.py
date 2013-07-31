# Sample script to use Karatsuba Algorithm
# Author: Laercio Simoes

def getHalfSize(x,y):
	iMax = max(len(str(x)),len(str(y)))
	return (iMax/2 + iMax%2)

def karatsuba(x, y):
	iHalf = getHalfSize(x,y)
	x1 = x / pow(10,iHalf)
	x2 = x - (x1 * pow(10,iHalf))
	y1 = y / pow(10, iHalf)
	y2 = y - (y1 * pow(10,iHalf))

	z0 = x2 * y2
	z1 = (x2 * y1) + (x1 * y2)
	z2 = x1 * y1

	result = (z2 *  pow(pow(10, iHalf),2)) + (z1 * pow(10, iHalf)) + z0

	print "Val X %s => %s - %s " %(x,x1,x2) 
	print "Val Y %s => %s - %s " %(y,y1,y2)
	print "Val Z0  = %s Z1 = %s Z2 = %s " %(z0,z1,z2)
	print "Result %s " %(result)
	

def main():
	print "Calculare Karatsuba"
	karatsuba(12345,6789)


if __name__ == '__main__': 
	main() 