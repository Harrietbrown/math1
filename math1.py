import math

def main():
        print("Hi, ask me to solve a problem \n")
        print("problem 1: Find the circumference of  circle")
        print("problem 2: What is the volume of water in a pool")
        print("problem 3: A plane travels 20km heading of 60 degrees, how far north and east does it go?.")
        print("problem 4: What is the final destination of a plane in terms of NS-EW from its starting position?.")

        prob=int(input())
        if prob == 1:
                problem1()
        elif prob == 2:
                problem2()
        elif prob == 3:
                problem3()
        elif prob == 4:
                problem4()
        else:
                print("not a valid problem")

def problem1():
        print("Enter the radius of a circle")
        N1=float(input())
        N2=math.pi*N1
        print("The circumference of that circle is %.2f" % (N2))

def problem2():
        print("what is the diamiter of the pool? in meters?")
        N1=float(input())
        print("how deep is the pool?")
        N2=float(input())
        print("The pool contains %.2f cubic meters of water." %(math.pi*N1*N2))

def problem3():
        print("A plane travels 20km on a course heading 60 degrees from north. \n")
        N1=20
        N2=60*math.pi/180
        N3=N1*math.cos(N2) #how far north or south does the plane land
        N4=N1*math.sin(N2) #how far east/west does the plane land

        print("Its final destination will be %.2fkm north and %.2fkm east" % (N3, N4))

def problem4():
        N1 = float(input("How har is the plane flying? "))
        N2 = float(input("what is the angle the plane is flying on? "))
        N2=N2*math.pi/180
        N3=N1*math.cos(N2) #how far north or south does the plane land
        N4=N1*math.sin(N2) #how far east/west does the plane land
        if N3 >= 0:
            NSstring= "%.2fkm north" % (N3) #make the output give information with the correct direction
        else:
            NSstring= "%.2fkm south" % (-N3)
        if N4 >= 0:
            EWstring= "%.2fkm east" % (N4)
        else:
            EWstring= "%.2fkm west" % (-N4)
        print("Its final destination will be ", NSstring, " and %.2fkm east" % (N4))

if __name__ == "__main__":
	main()
