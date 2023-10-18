##Functional Prompt
def flatten_and_sort(array):
    arr = []
    for item in array:
        for i in item:
            arr.append(i)
    return sorted(arr)


##Object Oriented Prompt
class Podracer:
  def __init__(self, max_speed, condition, price):
    self.max_speed = max_speed
    self.condition = condition
    self.price = price

  # Define repair() method that will update the condition of the podracer to "repaired"
  def repair(self):
    self.condition = "repaired"
    
# Define AnakinsPod that inherits the Podracer class, containing a boost that will double max_speed
class AnakinsPod(Podracer):
  def __init__(self, max_speed, condition, price):
    super.init(max_speed, condition, price):
  
  def boost(self):
    self.max_speed *= 2
    
# Define SebulbasPod class that inherits Podracer 
# This class should have a flame_jet that will update the condition of a podracer to "trashed"
class SebulbasPod(Podracer):
  def __init__(self, max_speed, condition, price):
    super.init(max_speed, condition, price):
  
  def flame_jet(self,other):
    other.condition = "trashed"