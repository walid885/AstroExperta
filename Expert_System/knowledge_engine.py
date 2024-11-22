from experta import KnowledgeEngine
from rules import SunRules
from facts import Sun

class SolarSystemExpert(SunRules, KnowledgeEngine):
    """Engine for Solar System rules and facts."""
    pass