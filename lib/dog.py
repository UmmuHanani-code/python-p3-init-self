#!/usr/bin/env python3

class Dog:
    def __init__(self, name,  breed="Mutt"):
         self.name = name
         self.breed = breed



fido = Dog("Fido")
print(fido.name)
print(fido.breed)
snoopy =Dog("Snoopy", "Beagle")
print(snoopy.name)
print(snoopy.breed)