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
from math import factorial, pi
from time import clock
############################################################
#						INITS
############################################################
decimal.getcontext().prec = 64
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
#					HALLEY'S METHOD
############################################################
err = D(1E-60)
n_lim = D(1E2)

def f(x,angle):
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
#					OPTION 1 - MAIN	
############################################################
if option == 1:
	while True:
		try:
			angle = D(float(input("Enter angle in radians: pi*"))*pi)
			break
		except:
			print("Invalid input, try again.")

	time_1sym = clock()
	result = Halley(angle)
	print("Result:", result, "in", (clock() - time_1sym), "seconds")
############################################################
#					OPTION 1 - MAIN	
############################################################