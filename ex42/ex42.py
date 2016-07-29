#!/usr/bin/env python
## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
	pass

## is
class Dog(Animal):
	
	def __init__(self, name):
		## has
		self.name = name

## is
class Cat(Animal):
	
	def __init__(self, name):
		## has
		self.name = name

class Person(object):
	
	def __init__(self, name):
		## has
		self.name = name

		## Person has-a pet of some kind
		self.pet = None

## is
class Employee(Person):
	
	def __init__(self, name, salary):
		## has hmm what is this strange magic?
		super(Employee, self).__init__(name)
		## has
		self.salary = salary

## is
class Fish(object):
	pass

## is
class Salmon(Fish):
	pass

## is
class Halibut(Fish):
	pass

## rover is-a Dog
rover = Dog("Rover")

## is
satan = Cat("Satan")

## is
mary = Person("Mary")

## has
mary.pet = satan

## is
frank = Employee("Frank", 120000)

## has
frank.pet = rover

## is
flipper = Fish()

## is
crouse = Salmon()

## is
harry = Halibut()
