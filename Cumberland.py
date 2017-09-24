############################################################
#
#	Author: Alexander Liptak
#	Date: 09 September 2017
#	E-Mail: Alexander.Liptak.2015@live.rhul.ac.uk
#	Phone: +44 7901 595107
#
############################################################
#
#	Option 1 - Calculate constant given angle swept out
#
#	Option 2 - Draw diagram given value of constant
#
#	Option 3 - Calcualte constant between two angles
#
############################################################
#						IMPORTS
############################################################
import decimal
from decimal import Decimal as D
from math import factorial, pi, sqrt
from time import clock
############################################################
#						INITS
############################################################
decimal.getcontext().prec = 32
############################################################
#					OPTION PICKER
############################################################
while True:
	try:
		option = int(input("Enter option [1,2,3]: "))
		if option not in [1,2,3]:
			raise ValueError()
		else:
			break
	except:
		print("Invalid option, try again.")
############################################################
#				HALLEY'S METHOD FOR SOLVING R
############################################################
def f(x,angle):
	n_lim = D(1E2)
	n = D(0)
	ans = D(0)
	while n<=n_lim:
		part1 = D(D(1)/((D(2)**(D(4)*n))*((D(2)*n)+D(1))))
		part2 = D(factorial(D(2)*n)/(factorial(n)*factorial(D(2)*n-n)))
		part3 = D(D(1)/(D(1)-(x**((D(2)*n)+D(1)))))
		ans = ans + (part1 * part2 * part3)
		n = n + 1
	ans = ans - angle
	return ans
	
def fd(x,angle):
	n_lim = D(1E2)
	n = D(0)
	ans = D(0)
	while n<=n_lim:
		part1 = D(D(1)/((D(2)**(D(4)*n))*((D(2)*n)+D(1))))
		part2 = D(factorial(D(2)*n)/(factorial(n)*factorial(D(2)*n-n)))
		part3 = ((D(2)*n)+D(1))/((D(1)-(x**((D(2)*n)+D(1))))**D(2))
		ans = ans + (part1 * part2 * part3)
		n = n + 1
	return ans
	
def fdd(x,angle):
	n_lim = D(1E2)
	n = D(0)
	ans = D(0)
	while n<=n_lim:
		part1 = D(D(1)/((D(2)**(D(4)*n))*((D(2)*n)+D(1))))
		part2 = D(factorial(D(2)*n)/(factorial(n)*factorial(D(2)*n-n)))
		part3 = ((D(2)*((D(2)*n)+D(1)))**D(2))/((D(1)-(x**((D(2)*n)+D(1))))**D(3))
		ans = ans + (part1 * part2 * part3)
		n = n + 1
	return ans

def Halley(angle):
	err = D(1E-30)
	guess = D(0.8)
	iter_lim = 1E4
	iter = 0
	while True:
		fx = f(guess,angle)
		fdx = fd(guess,angle)
		guess_new = guess - (D(2)*fx*fdx) / (D(2)*fdx*fdx-fx*fdd(guess,angle))
		iter = iter + 1
		if abs(guess_new-guess) <= err:
			break
		if iter == iter_lim:
			guess = "Unable to use Halley's method"
			break
		guess = guess_new
	return guess
############################################################
#						TOTAL AREA
############################################################
def TotalArea(angle):
	ans = angle/D(2)
	return ans
############################################################
#					TOTAL AREA OF TRIANGLES
############################################################
def TotalAreaofTrianlges(R):
	i_lim = D(1E2)
	i = D(0)
	ans = D(0)
	while i<=i_lim:
		part1 = D((D(R)**i)/D(2))
		part2 = D(sqrt(D(1)-((D(R)**(D(2)*i))/(D(4)))))
		ans = ans + (part1 * part2)
		i = i + 1
	return ans
############################################################
#		RATIO OF TOTAL AREA OF TRIANGLES TO TOTAL AREA
############################################################
def RatioTriangletoTotal(triangle, total):
	ans = D(triangle)/D(total)
	return ans
############################################################
#		RATIO OF TOTAL CORD LENGTH TO TOTAL ARC LENGTH
############################################################
def RatioCordtoArc(R, angle):
	i_lim = D(1E2)
	i = D(0)
	ans = D(0)
	while i<=i_lim:
		ans = ans + (D(R)**i)
		i = i + 1
	ans = ans/D(angle)
	return ans
############################################################
#					OPTION 1 - MAIN	
############################################################
if option == 1:
	while True:
		try:
			angle = D(float(input("Enter angle in radians: pi*"))*pi)
			break
		except:
			print("Invalid input, try again.")

	time_1R = clock()
	R = Halley(angle)
	print("R =", R, "; [", (clock() - time_1R), "seconds ]")
	
	time_1TotalArea = clock()
	totalArea = TotalArea(angle)
	print("Total area =", totalArea, "; [", (clock() - time_1TotalArea), "seconds ]")
	
	time_1TotalAreaofTriangles = clock()
	totalAreaofTriangles = TotalAreaofTrianlges(R)
	print("Total area of trianlges =", totalAreaofTriangles, "; [", (clock() - time_1TotalAreaofTriangles), "seconds ]")
	
	time_1RatioTriangletoTotal = clock()
	ratioTriangletoTotal = RatioTriangletoTotal(totalAreaofTriangles, totalArea)
	print("Ratio of total triangle area to total area =", ratioTriangletoTotal, "; [", (clock() - time_1RatioTriangletoTotal), "seconds ]")
	
	time_1RatioCordtoArc = clock()
	ratioCordtoArc = RatioCordtoArc(R, angle)
	print("Ratio of total cord length to total arc length =", ratioCordtoArc, "; [", (clock() - time_1RatioCordtoArc), "seconds ]")
############################################################
#					OPTION 3 - MAIN	
############################################################
if option == 3:
	