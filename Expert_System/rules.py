from experta import Rule, KnowledgeEngine, P
from facts import Sun, Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune

class SunRules(KnowledgeEngine):
    """Rules specific to the Sun."""

    @Rule(Sun(type="G-type main-sequence star"))
    def identify_star_type(self):
        """Identify the type of star."""
        print("The Sun is a G-type main-sequence star, commonly called a yellow dwarf.")
    
    @Rule(Sun(core_temperature=P(lambda temp: temp > 10000000)))
    def performs_nuclear_fusion(self):
        """Identify the Sun's core temperature and nuclear fusion process."""
        print("The Sun performs nuclear fusion in its core, converting hydrogen into helium.")
    
    @Rule(Sun(surface_temperature=P(lambda temp: 5000 <= temp <= 6000)))
    def classify_as_yellow_dwarf(self):
        """Classify the Sun as a yellow dwarf based on surface temperature."""
        print("The Sun is classified as a yellow dwarf star based on its surface temperature.")
    
    @Rule(Sun(mass="99.8% of Solar System mass"))
    def describe_mass(self):
        """Describe the mass of the Sun."""
        print("The Sun holds 99.8% of the total mass of the Solar System.")

    @Rule(Sun(solar_cycle="11 years"))
    def explain_solar_activity(self):
        """Explain the Sun's solar activity cycle."""
        print("The Sun experiences an 11-year solar activity cycle with sunspots and flares.")

class MercuryRules(KnowledgeEngine):
    """Rules specific to Mercury."""

    @Rule(Mercury(type="Terrestrial planet"))
    def identify_planet_type(self):
        """Identify Mercury as a terrestrial planet."""
        print("Mercury is a terrestrial planet.")
    
    @Rule(Mercury(orbital_period="88 days"))
    def describe_orbital_period(self):
        """Describe Mercury's orbital period."""
        print("Mercury orbits the Sun in 88 days.")
    
    @Rule(Mercury(unique_features="Closest planet to the Sun"))
    def unique_features(self):
        """Highlight Mercury's unique features."""
        print("Mercury is the closest planet to the Sun.")

class VenusRules(KnowledgeEngine):
    """Rules specific to Venus."""

    @Rule(Venus(type="Terrestrial planet"))
    def identify_planet_type(self):
        """Identify Venus as a terrestrial planet."""
        print("Venus is a terrestrial planet.")
    
    @Rule(Venus(surface_temperature=P(lambda temp: temp > 400)))
    def extreme_heat(self):
        """Highlight Venus's extreme surface temperature."""
        print("Venus is the hottest planet in the Solar System, with surface temperatures around 465°C.")
    
    @Rule(Venus(atmosphere="Thick atmosphere composed mostly of carbon dioxide"))
    def thick_atmosphere(self):
        """Describe Venus's thick atmosphere."""
        print("Venus has a thick atmosphere composed mostly of carbon dioxide, creating intense greenhouse effects.")

class EarthRules(KnowledgeEngine):
    """Rules specific to Earth."""

    @Rule(Earth(type="Terrestrial planet"))
    def identify_planet_type(self):
        """Identify Earth as a terrestrial planet."""
        print("Earth is a terrestrial planet.")
    
    @Rule(Earth(surface_temperature=P(lambda temp: temp > 0)))
    def moderate_temperature(self):
        """Describe Earth's moderate surface temperature."""
        print("Earth has a moderate surface temperature, averaging around 15°C.")
    
    @Rule(Earth(atmosphere="Mostly nitrogen and oxygen"))
    def life_supporting_atmosphere(self):
        """Describe Earth's life-supporting atmosphere."""
        print("Earth has an atmosphere mostly composed of nitrogen and oxygen, supporting life.")
    
    @Rule(Earth(orbital_period="365.25 days"))
    def describe_orbital_period(self):
        """Describe Earth's orbital period."""
        print("Earth orbits the Sun in 365.25 days.")
    
    @Rule(Earth(unique_features="Contains liquid water, supports life"))
    def unique_features(self):
        """Highlight Earth's unique features."""
        print("Earth contains liquid water and supports life.")

class MarsRules(KnowledgeEngine):
    """Rules specific to Mars."""

    @Rule(Mars(type="Terrestrial planet"))
    def identify_planet_type(self):
        """Identify Mars as a terrestrial planet."""
        print("Mars is a terrestrial planet.")
    
    @Rule(Mars(surface_temperature=P(lambda temp: temp < 0)))
    def cold_temperature(self):
        """Describe Mars's cold surface temperature."""
        print("Mars has a cold surface temperature, ranging from −87 to −5°C.")
    
    @Rule(Mars(atmosphere="Thin atmosphere composed mostly of carbon dioxide"))
    def thin_atmosphere(self):
        """Describe Mars's thin atmosphere."""
        print("Mars has a thin atmosphere composed mostly of carbon dioxide.")
    
    @Rule(Mars(unique_features="Known as the Red Planet"))
    def unique_features(self):
        """Highlight Mars's unique features."""
        print("Mars is known as the Red Planet due to its reddish appearance caused by iron oxide on its surface.")

class JupiterRules(KnowledgeEngine):
    """Rules specific to Jupiter."""

    @Rule(Jupiter(type="Gas giant"))
    def identify_planet_type(self):
        """Identify Jupiter as a gas giant."""
        print("Jupiter is a gas giant.")
    
    @Rule(Jupiter(mass=P(lambda mass: mass > 1.8e27)))
    def massive_size(self):
        """Describe Jupiter's massive size."""
        print("Jupiter is the largest planet in the Solar System.")
    
    @Rule(Jupiter(atmosphere="Thick atmosphere composed mostly of hydrogen and helium"))
    def thick_atmosphere(self):
        """Describe Jupiter's thick atmosphere."""
        print("Jupiter has a thick atmosphere composed mostly of hydrogen and helium.")

class SaturnRules(KnowledgeEngine):
    """Rules specific to Saturn."""

    @Rule(Saturn(type="Gas giant"))
    def identify_planet_type(self):
        """Identify Saturn as a gas giant."""
        print("Saturn is a gas giant.")
    
    @Rule(Saturn(unique_features="Famous for its prominent ring system"))
    def ring_system(self):
        """Describe Saturn's ring system."""
        print("Saturn is famous for its prominent ring system, composed of ice and rock.")

class UranusRules(KnowledgeEngine):
    """Rules specific to Uranus."""

    @Rule(Uranus(type="Ice giant"))
    def identify_planet_type(self):
        """Identify Uranus as an ice giant."""
        print("Uranus is an ice giant.")
    
    @Rule(Uranus(unique_features="Rotates on its side"))
    def unique_rotation(self):
        """Highlight Uranus's unique rotation."""
        print("Uranus rotates on its side, making it unique among the planets in the Solar System.")

class NeptuneRules(KnowledgeEngine):
    """Rules specific to Neptune."""

    @Rule(Neptune(type="Ice giant"))
    def identify_planet_type(self):
        """Identify Neptune as an ice giant."""
        print("Neptune is an ice giant.")
    
    @Rule(Neptune(unique_features="Strongest winds in the Solar System"))
    def strong_winds(self):
        """Describe Neptune's strong winds."""
        print("Neptune has the strongest winds in the Solar System.")
