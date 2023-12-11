class Rectangle:
  def __init__(self, width, height):
    self.width = width;
    self.height = height;

  def set_width(self, width):
    self.width = width;

  def set_height(self, height):
    self.height = height;

  def get_area(self):
    return self.width * self.height;
    
  def get_perimeter(self):
    return 2 * self.width + 2 * self.height;

  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** .5

  def get_picture(self):
    if self.height > 50 or self.width > 50:
      return "Too big for picture."
    else:
      picture = ""
      height = self.height
      #print(self.height)
      #print(self.width)
      while height > 0:
        picture += "*" * self.width + "\n"
        height -= 1
      return picture

  def get_amount_inside(self, shape):
    return int(self.get_area() / shape.get_area())

  def __str__(self):
    return "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"

class Square(Rectangle):
  def __init__(self, length):
    super().__init__(length, length)

  def set_side(self, length):
    self.width = length;
    self.height = length;

  def __str__(self):
    return "Square(side=" + str(self.width) + ")"

  def set_height(self, height):
    self.width = height
    self.height = height
    
  def set_width(self, width):
    self.width = width
    self.height = width