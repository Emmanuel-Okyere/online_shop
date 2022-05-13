class Any:
    def __init__(self, name):
        self._name = name


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new):
        self._name = new

def print_my_name(input_name): 
    my_name = Any(input_name)
    print(my_name.name)
    my_name.name = "Emma"
    print(my_name.name)

print_my_name("Gyateng")