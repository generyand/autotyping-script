import pyautogui
import time
import random
import webbrowser
from typing import List, Callable

# Constants
EDGE_PATH = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"
BING_URL = "https://www.bing.com"
INITIAL_DELAY = 2
PHRASE_COUNT = 40
TYPING_DELAY = 6

# Word lists
ADJECTIVES: List[str] = [
    'Shiny', 'Swift', 'Colorful', 'Majestic', 'Tiny', 'Fierce', 'Graceful', 'Exotic', 'Playful', 'Mysterious',
    'Elegant', 'Vibrant', 'Gentle', 'Energetic', 'Sleek', 'Fluffy', 'Wise', 'Curious', 'Dazzling', 'Serene',
    'Mighty', 'Adorable', 'Clever', 'Radiant', 'Nimble', 'Charming', 'Spirited', 'Tranquil', 'Lively', 'Magnificent',
    'Whimsical', 'Robust', 'Delicate', 'Striking', 'Agile', 'Regal', 'Enchanting', 'Resilient', 'Ethereal', 'Luminous',
    'Jovial', 'Tenacious', 'Harmonious', 'Enigmatic', 'Vivacious', 'Alluring', 'Dapper', 'Effervescent', 'Gregarious', 'Intrepid',
    'Jubilant', 'Kaleidoscopic', 'Lustrous', 'Mellifluous', 'Nonchalant', 'Opulent', 'Pristine', 'Quixotic', 'Resplendent', 'Scintillating',
    'Tenebrous', 'Ubiquitous', 'Verdant', 'Wondrous', 'Xenial', 'Yielding', 'Zestful', 'Amiable', 'Beguiling', 'Capricious',
    'Diaphanous', 'Effulgent', 'Fecund', 'Gossamer', 'Halcyon', 'Ineffable', 'Jocund', 'Kindred', 'Lissome', 'Mellifluous'
]

CREATURES: List[str] = [
    # Fish
    'Angelfish', 'Bass', 'Clownfish', 'Dorado', 'Eel', 'Flounder', 'Guppy', 'Halibut', 'Koi', 'Lionfish',
    'Marlin', 'Neon Tetra', 'Octopus', 'Pufferfish', 'Quillfish', 'Rainbowfish', 'Salmon', 'Tuna', 'Unicornfish', 'Viperfish',
    'Wrasse', 'Yellowtail', 'Zebrafish', 'Barracuda', 'Carp', 'Discus', 'Goldfish', 'Haddock', 'Icefish', 'Jellyfish',
    # Dogs
    'Labrador', 'Poodle', 'Bulldog', 'Shepherd', 'Beagle', 'Husky', 'Chihuahua', 'Rottweiler', 'Dachshund', 'Corgi',
    'Dalmatian', 'Greyhound', 'Mastiff', 'Pug', 'Retriever', 'Schnauzer', 'Terrier', 'Whippet', 'Yorkie', 'Zuchon',
    # Cats
    'Siamese', 'Persian', 'Maine Coon', 'Sphynx', 'Bengal', 'Ragdoll', 'Abyssinian', 'Scottish Fold', 'Burmese', 'Russian Blue',
    'Bombay', 'Chartreux', 'Exotic', 'Himalayan', 'Javanese', 'Korat', 'Manx', 'Nebelung', 'Ocicat', 'Pixiebob',
    # Birds
    'Eagle', 'Hummingbird', 'Owl', 'Parrot', 'Penguin', 'Flamingo', 'Peacock', 'Toucan', 'Falcon', 'Sparrow',
    'Albatross', 'Bluejay', 'Cockatoo', 'Dove', 'Egret', 'Finch', 'Gull', 'Heron', 'Ibis', 'Jackdaw',
    # Other Animals
    'Elephant', 'Lion', 'Giraffe', 'Kangaroo', 'Panda', 'Koala', 'Dolphin', 'Tiger', 'Gorilla', 'Cheetah',
    'Aardvark', 'Bison', 'Camel', 'Deer', 'Echidna', 'Frog', 'Gazelle', 'Hippo', 'Iguana', 'Jaguar',
    # Trees and Plants
    'Oak', 'Maple', 'Pine', 'Willow', 'Birch', 'Redwood', 'Baobab', 'Eucalyptus', 'Sequoia', 'Bonsai',
    'Acacia', 'Bamboo', 'Cedar', 'Dogwood', 'Elm', 'Fir', 'Ginkgo', 'Hazel', 'Ironwood', 'Juniper'
]

HABITATS: List[str] = [
    'Reef', 'River', 'Ocean', 'Lake', 'Pond', 'Lagoon', 'Stream', 'Bay', 'Estuary', 'Coral',
    'Forest', 'Jungle', 'Savanna', 'Desert', 'Tundra', 'Mountain', 'Valley', 'Meadow', 'Wetland', 'Grassland',
    'Cave', 'Cliff', 'Island', 'Volcano', 'Glacier', 'Canyon', 'Oasis', 'Plateau', 'Marsh', 'Swamp',
    'Rainforest', 'Arctic', 'Tropics', 'Coastline', 'Dune', 'Prairie', 'Fjord', 'Delta', 'Mangrove', 'Taiga',
    'Archipelago', 'Badlands', 'Chaparral', 'Deciduous', 'Everglades', 'Floodplain', 'Geothermal', 'Heath', 'Isthmus', 'Karst',
    'Lowland', 'Moor', 'Nubivagant', 'Outcrop', 'Permafrost', 'Quagmire', 'Ravine', 'Steppe', 'Thermokarst', 'Upland',
    'Veld', 'Woodland', 'Xeric', 'Yokul', 'Zanja', 'Atoll', 'Bayou', 'Crag', 'Drumlin', 'Escarpment'
]

def generate_phrase() -> str:
    """Generate a random phrase with 1-3 words."""
    num_words = random.randint(1, 3)
    
    if num_words == 1:
        return random.choice(CREATURES)
    elif num_words == 2:
        return f"{random.choice(ADJECTIVES)} {random.choice(CREATURES)}"
    else:
        return f"{random.choice(ADJECTIVES)} {random.choice(CREATURES)} {random.choice(HABITATS)}"

def open_edge() -> None:
    """Open Microsoft Edge browser."""
    webbrowser.register('edge', None, webbrowser.BackgroundBrowser(EDGE_PATH))
    webbrowser.get('edge').open(BING_URL)

def type_phrase(phrase: str) -> None:
    """Type a phrase into the search bar."""
    pyautogui.press('/')
    pyautogui.press('backspace')
    pyautogui.typewrite(phrase)
    pyautogui.press('enter')

def main() -> None:
    """Main function to run the script."""
    open_edge()
    time.sleep(INITIAL_DELAY)

    for _ in range(PHRASE_COUNT):
        phrase = generate_phrase()
        type_phrase(phrase)
        time.sleep(TYPING_DELAY)

if __name__ == "__main__":
    main()