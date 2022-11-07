class Rectangle:

    # Constructor

    def __init__(self, width = 0.0, height = 0.0):
        
        assert width >= 0, "The width cannot be a negative number."
        assert height >= 0, "The height cannot be a negative number."

        self.width = width
        self.height = height
    
    # Setters

    def set_width(self, value): # , width = 0.0

        self.width = value
    
    def set_height(self, value):
    
        self.height = value
    
    # Methods

    def get_area(self):

        return self.width * self.height
    
    def get_perimeter(self):

        return 2 * self.width + 2 * self.height
    
    def get_diagonal(self):

        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        
        return "\n".join(["*" * self.width for x in range(self.height)]) + "\n"
    
    def get_amount_inside(self, another):

        return int(self.get_area()/another.get_area())

    # If represented as a string

    def __str__(self):

        return f"Rectangle(width={self.width}, height={self.height})"

class Square(Rectangle):

    # Constructor

    def __init__(self, length):

        super().__init__(length, length)
        self.length = length
    
    # Setter

    def set_side(self, side):

        self.length = side
        self.width = side
        self.height = side

    def set_width(self, side):

        self.set_side(side)
    
    def set_height(self, side):
        
        self.set_side(side)

    # If represented as a string

    def __str__(self):
        return f"Square(side={self.length})"
    def get_amount_inside(self, another):

        return int(self.get_area()/another.get_area())

    # If represented as a string

    def __str__(self):

        return f"Rectangle(width={self.width}, heigth={self.height})"

class Square(Rectangle):

    # Constructor

    def __init__(self, length):

        super().__init__(length, length)
        self.length = length
    
    # Setter

    def set_side(self, side):

        self.length = side
        self.width = side
        self.height = side

    def set_width(self, side):

        self.set_side(side)
    
    def set_height(self, side):
        
        self.set_side(side)

    # If represented as a string

    def __str__(self):
        
        return f"Square(side={self.length})"