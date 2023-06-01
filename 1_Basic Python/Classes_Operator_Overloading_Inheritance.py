class demo:
    def message(self):
        print("Demo Message")
class demo1(demo):
    def __init__(self, name, age): #constructor 
        private: self.name=name #access specifier OOP concept
        self.age=age
    def function(self): #python method
        print("Hello")

call=demo1("Sapthak", 19)

print(call.age) 
call.function()
call.message()