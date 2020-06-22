class Animal:
    def eat(self):
        print("吃")


class Dog(Animal):
    def running(self):
        print("跑")
        super().eat()


class Brid(Animal):
    def flying(self):
        print("飞")
        super().eat()


a = Animal()
d = Dog()
b = Brid()

print(isinstance(a, Animal))
print(isinstance(d, Animal))
print(isinstance(d, Brid))
print(isinstance(b, Dog))


print(issubclass(Animal,Animal))
print(issubclass(Animal,Dog))
print(issubclass(Dog,Animal))

print(type(a) == Animal)
print(type(d) == Animal)
print(type(b) == Animal)
print(type(d) == Dog)