# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

class Vehicle:
    """Vehicle base class."""
    def __init__(self):
        pass


# Subclasses GroundVehicle
class GroundVehicle(Vehicle):
    """ Base Vehicles on the ground."""
    def __init__(self):
        pass


class Car(GroundVehicle):
    """A standard car."""
    def __init__(self):
        pass


class Motorcycle(GroundVehicle):
    """A standard motorcycle."""
    def __init__(self):
        pass


# Subclasses FlightVehicle
class FlightVehicle(Vehicle):
    """A flying type vehicle."""
    def __init__(self):
        pass


class Starship(FlightVehicle):
    """It's a starship, woo!"""
    def __init__(self):
        pass


class Airplane(FlightVehicle):
    """Using lift to defy gravity on terrestrial surfaces."""
    def __init__(self):
        pass
