
#defining the functions for rectangle and circle
def rectangle():
    #taking the length and width input from the user
    
    length=float(input("Enter the length of the rectangle:"))
    width=float(input("Enter the width of the rectangle:"))
    
    #to calculate area and perimeter of the rectangle
    area=length*width
    perimeter =2*(length+width)
    return area, perimeter

def circle():
    #taking the radius of the circle as input from the user
    radius = float(input("enter the radius of the circle: "))
    
    #for calculating the area and perimeter
    area=(3.142)*(radius**2)
    perimeter = 2*(3.142)*radius
    return area, perimeter

def triangle():
    base=float((input("enter the height of the rectangle:")))
    height=float(input("enter the height of the rectangle: "))
    side1=float((input("enter the side1:")))
    side2=float(input("enter the side2:"))
    area=(.5)*base*height
    perimeter=2*side1+base+side2
    return area, perimeter

#defining the main function
def main():
    shape=input("Enter shape(rectangle/circle/triangle):")
    
    if shape =="rectangle":
        area, perimeter= rectangle()
    
    elif shape=="circle":
        area, perimeter=circle()
    
    elif shape=="triangle":
        area,perimeter=triangle()
        
    else:
        print("Invalid Inputs:")
        return
    print(f"area of {shape} is {area}")
    print(f"perimeter of {shape} is {perimeter}")
    
    
if __name__=="__main__":
    main()
