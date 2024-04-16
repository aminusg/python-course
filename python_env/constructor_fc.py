class Invoice:
    def __init__(self, client, total):
        self.client = client
        self.total = total

    def formatter(self):
        return f'{self.client} owes: ${self.total}'
    

google = Invoice('Google', 100)
snapchat = Invoice('SnapChat', 200)

print(google.formatter())
print(snapchat.formatter())



#Ejercicio
#Using our Garage class from the previous guide, add a constructor method



class Garage:
  def __init__(self, size):
        self.size = size
 
  def open_door(self):
    return f"The door opens a {self.size} car garage"
    
home = Garage(2) 
print(home.open_door())