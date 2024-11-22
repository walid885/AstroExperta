from experta import Rule, KnowledgeEngine, P
from facts import Sun

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
