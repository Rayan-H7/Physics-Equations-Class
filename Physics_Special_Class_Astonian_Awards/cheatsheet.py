
from time import time


class CheatSheet:
    
    voltage = 6
    
    def __init__(self):
        pass
    
    def speed(self,velocity, time):
        speed = velocity * time
        print("The speed is "+str(speed)+" mph.")
        
    def velocity(self,speed, time):
        velocity = speed / time
        print("The velocity is "+str(velocity)+" mph.")
        
    def time(self,speed, velocity):
        time = speed / velocity
        print("The amount of time is "+str(velocity)+" seconds.")
        
    def weight_earth(mass):
        gravitational_field = 9.8
        weight = mass * gravitational_field
        print("The weight is "+str(weight)+" kg.")
        print("Do you want to know the weight if you were on the moon? ")
        answer = input()
        if answer == "Yes":
            gravitational_field = 9.6
            weight = mass * gravitational_field
            print("The weight is "+str(weight)+" kg.")
        else:
            print("Nevermind then.")
            
        
    def force(mass, acceleration):
        force = mass * acceleration
        print("The force is "+str(force)+"N.")
        print("Do you want to know the acceleration? ")
        answer = input()
        if answer == "Yes":
            acceleration = force / mass
            print("The acceleration is "+str(acceleration)+" seconds.")
        
    
        
        