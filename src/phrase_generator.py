import random
from data.word_lists import ADJECTIVES, CREATURES, HABITATS, PREPOSITIONS

class PhraseGenerator:
    def generate_phrase(self) -> str:
        """Generate a random phrase with 1-3 words."""
        num_words = random.randint(1, 3)
        
        if num_words == 1:
            return random.choice(CREATURES)
        elif num_words == 2:
            return f"{random.choice(ADJECTIVES)} {random.choice(CREATURES)}"
        else:
            return f"{random.choice(ADJECTIVES)} {random.choice(CREATURES)} {random.choice(PREPOSITIONS)} {random.choice(HABITATS)}"