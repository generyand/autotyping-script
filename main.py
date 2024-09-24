from src.phrase_generator import PhraseGenerator
from src.browser_controller import BrowserController
from src.typing_simulator import TypingSimulator
from config import INITIAL_DELAY, PHRASE_COUNT, TYPING_DELAY
import time

def main():
    phrase_generator = PhraseGenerator()
    browser_controller = BrowserController()
    typing_simulator = TypingSimulator()

    browser_controller.open_edge()
    time.sleep(INITIAL_DELAY)

    for _ in range(PHRASE_COUNT):
        phrase = phrase_generator.generate_phrase()
        typing_simulator.type_phrase(phrase)
        time.sleep(TYPING_DELAY)

if __name__ == "__main__":
    main()