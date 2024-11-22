from knowledge_engine import SolarSystemExpert
from facts import Sun, Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune

def main():
    # Initialize the expert system
    engine = SolarSystemExpert()
    engine.reset()  # Prepare the engine
    
    # Declare Sun facts
    engine.declare(Sun(type="G-type main-sequence star"))
    engine.declare(Sun(age="4.6 billion years"))
    engine.declare(Sun(composition="hydrogen and helium"))
    engine.declare(Sun(diameter="1.4 million km"))
    engine.declare(Sun(mass="99.8% of Solar System mass"))
    engine.declare(Sun(core_temperature=15000000))  # in Celsius
    engine.declare(Sun(surface_temperature=5500))  # in Celsius
    engine.declare(Sun(energy_source="nuclear fusion"))
    engine.declare(Sun(rotation_equator="24 days"))
    engine.declare(Sun(solar_cycle="11 years"))

    # Declare Mercury facts
    engine.declare(Mercury(type="Terrestrial planet"))
    engine.declare(Mercury(age="4.5 billion years"))
    engine.declare(Mercury(composition="Silicate rocks and metals"))
    engine.declare(Mercury(diameter="4,880 km"))
    engine.declare(Mercury(mass="3.30 x 10^23 kg"))
    engine.declare(Mercury(surface_temperature="−173 to 427°C"))
    engine.declare(Mercury(atmosphere="Exosphere composed mostly of oxygen, sodium, hydrogen, helium, and potassium"))
    engine.declare(Mercury(orbital_period="88 days"))
    engine.declare(Mercury(rotation_period="59 days"))
    engine.declare(Mercury(unique_features="Closest planet to the Sun"))

    # Declare Venus facts
    engine.declare(Venus(type="Terrestrial planet"))
    engine.declare(Venus(age="4.5 billion years"))
    engine.declare(Venus(composition="Silicate rocks and metals"))
    engine.declare(Venus(diameter="12,104 km"))
    engine.declare(Venus(mass="4.87 x 10^24 kg"))
    engine.declare(Venus(surface_temperature="465°C"))
    engine.declare(Venus(atmosphere="Thick atmosphere composed mostly of carbon dioxide"))
    engine.declare(Venus(orbital_period="225 days"))
    engine.declare(Venus(rotation_period="243 days (retrograde)"))
    engine.declare(Venus(unique_features="Hottest planet in the Solar System"))

    # Declare Earth facts
    engine.declare(Earth(type="Terrestrial planet"))
    engine.declare(Earth(age="4.5 billion years"))
    engine.declare(Earth(composition="Silicate rocks and metals"))
    engine.declare(Earth(diameter="12,742 km"))
    engine.declare(Earth(mass="5.97 x 10^24 kg"))
    engine.declare(Earth(surface_temperature=15))  # Average temperature in Celsius
    engine.declare(Earth(atmosphere="Mostly nitrogen and oxygen"))
    engine.declare(Earth(orbital_period="365.25 days"))
    engine.declare(Earth(rotation_period="24 hours"))
    engine.declare(Earth(unique_features="Contains liquid water, supports life"))

    # Declare Mars facts
    engine.declare(Mars(type="Terrestrial planet"))
    engine.declare(Mars(age="4.6 billion years"))
    engine.declare(Mars(composition="Silicate rocks and metals"))
    engine.declare(Mars(diameter="6,779 km"))
    engine.declare(Mars(mass="6.39 x 10^23 kg"))
    engine.declare(Mars(surface_temperature="−87 to −5°C"))
    engine.declare(Mars(atmosphere="Thin atmosphere composed mostly of carbon dioxide"))
    engine.declare(Mars(orbital_period="687 days"))
    engine.declare(Mars(rotation_period="24.6 hours"))
    engine.declare(Mars(unique_features="Known as the Red Planet"))

    # Declare Jupiter facts
    engine.declare(Jupiter(type="Gas giant"))
    engine.declare(Jupiter(age="4.5 billion years"))
    engine.declare(Jupiter(composition="Hydrogen and helium"))
    engine.declare(Jupiter(diameter="139,820 km"))
    engine.declare(Jupiter(mass="1.90 x 10^27 kg"))
    engine.declare(Jupiter(surface_temperature="−108°C"))
    engine.declare(Jupiter(atmosphere="Thick atmosphere composed mostly of hydrogen and helium"))
    engine.declare(Jupiter(orbital_period="12 years"))
    engine.declare(Jupiter(rotation_period="9.9 hours"))
    engine.declare(Jupiter(unique_features="Largest planet in the Solar System"))

    # Declare Saturn facts
    engine.declare(Saturn(type="Gas giant"))
    engine.declare(Saturn(age="4.5 billion years"))
    engine.declare(Saturn(composition="Hydrogen and helium"))
    engine.declare(Saturn(diameter="116,460 km"))
    engine.declare(Saturn(mass="5.68 x 10^26 kg"))
    engine.declare(Saturn(surface_temperature="−139°C"))
    engine.declare(Saturn(atmosphere="Thick atmosphere composed mostly of hydrogen and helium"))
    engine.declare(Saturn(orbital_period="29 years"))
    engine.declare(Saturn(rotation_period="10.7 hours"))
    engine.declare(Saturn(unique_features="Famous for its prominent ring system"))

    # Declare Uranus facts
    engine.declare(Uranus(type="Ice giant"))
    engine.declare(Uranus(age="4.5 billion years"))
    engine.declare(Uranus(composition="Water, methane, and ammonia ices"))
    engine.declare(Uranus(diameter="50,724 km"))
    engine.declare(Uranus(mass="8.68 x 10^25 kg"))
    engine.declare(Uranus(surface_temperature="−195°C"))
    engine.declare(Uranus(atmosphere="Thick atmosphere composed mostly of hydrogen and helium"))
    engine.declare(Uranus(orbital_period="84 years"))
    engine.declare(Uranus(rotation_period="17.2 hours"))
    engine.declare(Uranus(unique_features="Rotates on its side"))

    # Declare Neptune facts
    engine.declare(Neptune(type="Ice giant"))
    engine.declare(Neptune(age="4.5 billion years"))
    engine.declare(Neptune(composition="Water, methane, and ammonia ices"))
    engine.declare(Neptune(diameter="49,244 km"))
    engine.declare(Neptune(mass="1.02 x 10^26 kg"))
    engine.declare(Neptune(surface_temperature="−200°C"))
    engine.declare(Neptune(atmosphere="Thick atmosphere composed mostly of hydrogen and helium"))
    engine.declare(Neptune(orbital_period="165 years"))
    engine.declare(Neptune(rotation_period="16.1 hours"))
    engine.declare(Neptune(unique_features="Strongest winds in the Solar System"))

    # Run the engine to evaluate rules
    engine.run()

if __name__ == "__main__":
    main()
