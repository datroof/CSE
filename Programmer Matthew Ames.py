class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def work(self):
        print("%s goes to work." % self.name)


class Employee(Person):
    def __init__(self, name, age, job):
        super(Employee, self).__init__(name, age,)
        self.job = job

class Programmer(Employee):
    def __init__(self, name, age):
        super(Programmer, self).__init__(name, age, 'programmer')


steve = Programmer("Steve", 35)
print(steve.job)

print("Hello %s. You are %s and as of today you are a %s." % (steve.name, steve.age, steve.job) )