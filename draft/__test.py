class testClass:
  def __new__(cls, *args, **kwargs):
    return super().__new__(cls)

  def __init_(self, x):
    self.x = x

  def __repr__(self) -> string:
    return f"{type(self).__name__}(x={self.x})"

  def test():
    return