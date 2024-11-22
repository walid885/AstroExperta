from experta import Rule, KnowledgeEngine, P
from facts import Sun, Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune

class SunRules(KnowledgeEngine):
    @Rule(Sun(type="G-type main-sequence star"))
    def identify_star_type(self):
        print("The Sun is a G-type main-sequence star, commonly called a yellow dwarf.")
    
    @Rule(Sun(core_temperature=P(lambda temp: temp > 10000000)))
    def performs_nuclear_fusion(self):
        print("The Sun performs nuclear fusion in its core, converting hydrogen into helium.")
    
    @Rule(Sun(surface_temperature=P(lambda temp: 5000 <= temp <= 6000)))
    def classify_as_yellow_dwarf(self):
        print("The Sun is classified as a yellow dwarf star based on its surface temperature.")
    
    @Rule(Sun(mass="99.8% of Solar System mass"))
    def describe_mass(self):
        print("The Sun holds 99.8% of the total mass of the Solar System.")

    @Rule(Sun(solar_cycle="11 years"))
    def explain_solar_activity(self):
        print("The Sun experiences an 11-year solar activity cycle with sunspots and flares.")

class MercuryRules(KnowledgeEngine):
    @Rule(Mercury(type="Terrestrial planet"))
    def identify_planet_type(self):
        print("Mercury is a terrestrial planet.")
    
    @Rule(Mercury(orbital_period="88 days"))
    def describe_orbital_period(self):
        print("Mercury orbits the Sun in 88 days.")
    
    @Rule(Mercury(unique_features="Closest planet to the Sun"))
    def unique_features(self):
        print("Mercury is the closest planet to the Sun.")

class VenusRules(KnowledgeEngine):
    @Rule(Venus(type="Terrestrial planet"))
    def identify_planet_type(self):
        print("Venus is a terrestrial planet.")
    
    @Rule(Venus(surface_temperature=P(lambda temp: temp > 400)))
    def extreme_heat(self):
        print("Venus is the hottest planet in the Solar System, with surface temperatures around 465°C.")
    
    @Rule(Venus(atmosphere="Thick atmosphere composed mostly of carbon dioxide"))
    def thick_atmosphere(self):
        print("Venus has a thick atmosphere composed mostly of carbon dioxide, creating intense greenhouse effects.")

class EarthRules(KnowledgeEngine):
    @Rule(Earth(type="Terrestrial planet"))
    def identify_planet_type(self):
        print("Earth is a terrestrial planet.")
    
    @Rule(Earth(surface_temperature=P(lambda temp: temp > 0)))
    def moderate_temperature(self):
        print("Earth has a moderate surface temperature, averaging around 15°C.")
    
    @Rule(Earth(atmosphere="Mostly nitrogen and oxygen"))
    def life_supporting_atmosphere(self):
        print("Earth has an atmosphere mostly composed of nitrogen and oxygen, supporting life.")
    
    @Rule(Earth(orbital_period="365.25 days"))
    def describe_orbital_period(self):
        print("Earth orbits the Sun in 365.25 days.")
    
    @Rule(Earth(unique_features="Contains liquid water, supports life"))
    def unique_features(self):
        print("Earth contains liquid water and supports life.")

class MarsRules(KnowledgeEngine):
    @Rule(Mars(type="Terrestrial planet"))
    def identify_planet_type(self):
        print("Mars is a terrestrial planet.")
    
    @Rule(Mars(surface_temperature=P(lambda temp: temp < 0)))
    def cold_temperature(self):
        print("Mars has a cold surface temperature, ranging from −87 to −5°C.")
    
    @Rule(Mars(atmosphere="Thin atmosphere composed mostly of carbon dioxide"))
    def thin_atmosphere(self):
        print("Mars has a thin atmosphere composed mostly of carbon dioxide.")
    
    @Rule(Mars(unique_features="Known as the Red Planet"))
    def unique_features(self):
        print("Mars is known as the Red Planet due to its reddish appearance caused by iron oxide on its surface.")

class JupiterRules(KnowledgeEngine):
    @Rule(Jupiter(type="Gas giant"))
    def identify_planet_type(self):
        print("Jupiter is a gas giant.")
    
    @Rule(Jupiter(mass=P(lambda mass: mass > 1.8e27)))
    def massive_size(self):
        print("Jupiter is the largest planet in the Solar System.")
    
    @Rule(Jupiter(atmosphere="Thick atmosphere composed mostly of hydrogen and helium"))
    def thick_atmosphere(self):
        print("Jupiter has a thick atmosphere composed mostly of hydrogen and helium.")

class SaturnRules(KnowledgeEngine):
    @Rule(Saturn(type="Gas giant"))
    def identify_planet_type(self):
        print("Saturn is a gas giant.")
    
    @Rule(Saturn(unique_features="Famous for its prominent ring system"))
    def ring_system(self):
        print("Saturn is famous for its prominent ring system, composed of ice and rock.")

class UranusRules(KnowledgeEngine):
    @Rule(Uranus(type="Ice giant"))
    def identify_planet_type(self):
        print("Uranus is an ice giant.")
    
    @Rule(Uranus(unique_features="Rotates on its side"))
    def unique_rotation(self):
        print("Uranus rotates on its side, making it unique among the planets in the Solar System.")

class NeptuneRules(KnowledgeEngine):
    @Rule(Neptune(type="Ice giant"))
    def identify_planet_type(self):
        print("Neptune is an ice giant.")
    
    @Rule(Neptune(unique_features="Strongest winds in the Solar System"))
    def strong_winds(self):
        print("Neptune has the strongest winds in the Solar System.")
