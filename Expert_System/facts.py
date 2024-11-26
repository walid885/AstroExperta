from experta import Fact
from typing import Dict, Any, Optional

class CelestialBody(Fact):
    """Base class for celestial objects."""
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

class Sun(CelestialBody):
    """Properties of the Sun."""
    core_temperature = None
    energy_source = None
    rotation_equator = None
    solar_cycle = None

class Planet(CelestialBody):
    """Base class for planets."""
    pass

class Mercury(Planet):
    """Properties of Mercury."""
    pass

class Venus(Planet):
    """Properties of Venus."""
    pass

class Earth(Planet):
    """Properties of Earth."""
    pass

class Mars(Planet):
    """Properties of Mars."""
    pass

class Jupiter(Planet):
    """Properties of Jupiter."""
    pass

class Saturn(Planet):
    """Properties of Saturn."""
    pass

class Uranus(Planet):
    """Properties of Uranus."""
    pass

class Neptune(Planet):
    """Properties of Neptune."""
    pass

class BlackHole(Fact):
    """Properties of a Black Hole."""
    type = None  # Stellar, Supermassive, etc.
    mass = None
    size = None
    location = None
    formation_method = None
    unique_features = None
    discovery_year = None
    associated_phenomena = None  # Jets, accretion disk, etc.
class PlanetQuestion(Fact):
    """
    Represents a question about planets in the expert system.
    """
    def __init__(self, 
                 question_id: str = None, 
                 question_text: str = None, 
                 feature_map: Dict[str, bool] = None,
                 **kwargs):
        super().__init__(**kwargs)
        self.question_id = question_id
        self.question_text = question_text
        self.feature_map = feature_map or {}

class PlanetFeature(Fact):
    """
    Represents a feature of a planet in the expert system.
    """
    def __init__(self, 
                 planet_name: str = None, 
                 features: Dict[str, Any] = None,
                 **kwargs):
        super().__init__(**kwargs)
        self.planet_name = planet_name
        self.features = features or {}
