class Complex :
	
	def __init__(self,r,i):
		self.real = r
		self.imaginary = i
	
	def __str__(self):
		return f"{self.real}+{self.imaginary}i"
	
	def __add__(self,other):
		return f"Sum of two Complex No. : {Complex(self.real+other.real, self.imaginary+other.imaginary)}"
	#(a+bi)(*)(c+di) = (ac-bd) + (ad+bc)i
	def __mul__(self,other):
		return f"Multiplication two Complex No. : {Complex(self.real*other.real - self.imaginary*other.imaginary, self.real*other.imaginary + self.imaginary*other.real)}"
		
	def __sub__(self,other):
		return f"Difference of two Complex No. : {Complex(self.real-other.real, self.imaginary-other.imaginary)}"

	def conjugate(self):
		return f"{Complex(self.real,({-self.imaginary}))}"
					
c1 = Complex(1,2)
print(c1)
c2 = Complex(2,3)
print(c2)
s = c1 + c2
m = c1 * c2
d = c1 - c2
print(s)
print(m)
print(d)
print(c1.conjugate())