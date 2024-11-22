from knowledge_engine import SolarSystemExpert
from facts import Sun

def main():
    # Initialize the expert system
    engine = SolarSystemExpert()
    engine.reset()  # Prepare the engine
    
    # Add Sun facts
    engine.declare(Sun(temperature=5778, size='1.4 million km', composition='hydrogen'))
    
    # Run the engine to evaluate rules
    engine.run()

if __name__ == "__main__":
    main()