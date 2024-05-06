class Usuario:
    def __init__(self, name, password):
        self.name = name
        self.password = password
user1 = Usuario('Jaime', "R2D2") 

print(f"User Name: {user1.name}")
print(f"Password: {user1.password}")