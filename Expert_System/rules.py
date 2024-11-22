from experta import Rule, KnowledgeEngine

class SunRules(KnowledgeEngine):
    @Rule(Sun(temperature=P(lambda t: t > 4000), composition='hydrogen'))
    def is_main_sequence_star(self):
        print("The Sun is a main-sequence star, suitable for sustaining a planetary system.")