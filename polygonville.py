import turtle

def main():
    # set up the name of the window
    turtle.title("Polygonville")
    # setup the screen size through (425, 425)
    # setup the initial location through (0,0)
    turtle.setup(1000,650,0,0)
    print("Welcome to Polygonville!")
    totalSides = input("Input number of sides in the polygon: ")
    while totalSides != 0:
        if totalSides < 3:
            print("Sorry, " + str(totalSides) + " is not "
            + "valid, click window to exit")
        elif totalSides == 3:
            totalAngles = 180 * (totalSides - 2)
            sideLength = input("Put polygon sidelength: ")
            angle = totalAngles/totalSides
            func1(totalSides, sideLength, angle, totalAngles)
        else:
            totalAngles = 180 * (totalSides - 2)
            sideLength = input("Put polygon side length: ")
            angle = totalAngles/totalSides
            func2(totalSides, sideLength, angle, totalAngles)
        print("Polygon Summary: \n" + 
            "Sides: " + str(totalSides) + "| Anterior Angle: " + 
            str(angle) + "| Sum of Angles: " + str(totalAngles))
        totalSides = input("\nInput number of sides in the polygon: ")
    if totalSides == 0:
        print("Thank you for using Polygonville!")

def func1(totalSides, sideLength, angle, totalAngles):
    #make turtle move forward(pixels) to draw triangle 
    for i in range(0, totalSides):
        turtle.forward(sideLength)
        turtle.right(90)
        turtle.right(30)
            
def func2(totalSides, sideLength, angle, totalAngles):
    #make turtle move forward(pixels) 
    for i in range(0, totalSides):
        turtle.forward(sideLength)
        if angle <= 90:
            turtle.right(angle)
        else:
            turtle.right(180 - angle)
main()
turtle.exitonclick()   