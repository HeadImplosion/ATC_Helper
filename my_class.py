class myClass:

  def __new__(cls, *args, **kwargs):
    print("1. Create a new instance of myClass.")
    return super().__new__(cls)
  
  def __init__(self, hold_no):
    self.hold_no = hold_no

# Return string representations of class name and variables
  def __repr__(self) -> str:
    return f"{type(self).__name__}(hold_no={self.hold_no})"

  def method():
    print("This is myClass")
    return
  
  def set_hold_no(self, i):
    self.hold_no = i
  
  def get_hold_no(self):
    return self.hold_no