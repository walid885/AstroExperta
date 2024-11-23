from experta import Fact

class Sun(Fact):
    """Fact: Represents properties of the Sun."""
    type = None
    age = None
    composition = None
    diameter = None
    mass = None
    core_temperature = None
    surface_temperature = None
    energy_source = None
    rotation_equator = None
    solar_cycle = None

class Mercury(Fact):
    """Fact: Represents properties of Mercury."""
    type = None 
    age = None
    composition = None
    diameter = None 
    mass = None 
    surface_temperature = None 
    atmosphere = None 
    orbital_period = None 
    rotation_period = None
    unique_features = None

class Venus(Fact):
    """Fact: Represents properties of Venus."""
    type = None 
    age = None
    composition = None
    diameter = None 
    mass = None 
    surface_temperature = None 
    atmosphere = None 
    orbital_period = None 
    rotation_period = None
    unique_features = None

class Earth(Fact):
    """Fact: Represents properties of Earth."""
    type = None 
    age = None
    composition = None
    diameter = None 
    mass = None 
    surface_temperature = None 
    atmosphere = None 
    orbital_period = None 
    rotation_period = None
    unique_features = None

class Mars(Fact):
    """Fact: Represents properties of Mars."""
    type = None 
    age = None
    composition = None
    diameter = None 
    mass = None 
    surface_temperature = None 
    atmosphere = None 
    orbital_period = None 
    rotation_period = None
    unique_features = None

class Jupiter(Fact):
    """Fact: Represents properties of Jupiter."""
    type = None 
    age = None
    composition = None
    diameter = None 
    mass = None 
    surface_temperature = None 
    atmosphere = None 
    orbital_period = None 
    rotation_period = None
    unique_features = None

class Saturn(Fact):
    """Fact: Represents properties of Saturn."""
    type = None 
    age = None
    composition = None
    diameter = None 
    mass = None 
    surface_temperature = None 
    atmosphere = None 
    orbital_period = None 
    rotation_period = None
    unique_features = None

class Uranus(Fact):
    """Fact: Represents properties of Uranus."""
    type = None 
    age = None
    composition = None
    diameter = None 
    mass = None 
    surface_temperature = None 
    atmosphere = None 
    orbital_period = None 
    rotation_period = None
    unique_features = None

class Neptune(Fact):
    """Fact: Represents properties of Neptune."""
    type = None 
    age = None
    composition = None
    diameter = None 
    mass = None 
    surface_temperature = None 
    atmosphere = None 
    orbital_period = None 
    rotation_period = None
    unique_features = None

from experta import KnowledgeEngine, Fact, Rule, AS, NOT, W, MATCH
from typing import Dict, List, Optional
import random

class PlanetQuestion(Fact):
    """Fact representing a user's answer to a question about a planet."""
    pass

class PlanetFeature(Fact):
    """Fact representing a specific feature of a planet."""
    pass

