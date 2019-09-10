class Rectangle():
    def __init__(room,length,breadth,unitcost):
        room.length=length
        room.breadth=breadth
        room.unitcost=unitcost
    def get_perimeter(room):
        return 2*(room.length+room.breadth)
    def get_area(room):
        return (room.length*room.breadth)
    def get_cost(room):
        return ((room.get_area())*room.unitcost)
    def output(room):
        print("Perimeter of the room=",room.get_perimeter())
        print("Area of the room=",room.get_area())
        print("Cost of the room=",room.get_cost())
    
    
r= Rectangle(160,120,2000)
r.output()
s= Rectangle(10,10,10)
s.output()
print(r.get_perimeter())
print(s.get_cost())

class Square(Rectangle):
    pass

t= Square(30,30,10)
t.output()