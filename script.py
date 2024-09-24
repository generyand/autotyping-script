import pyautogui
import time
import random

# Greatly expanded lists of words
adjectives = [
    'Shiny', 'Swift', 'Colorful', 'Majestic', 'Tiny', 'Fierce', 'Graceful', 'Exotic', 'Playful', 'Mysterious',
    'Elegant', 'Vibrant', 'Gentle', 'Energetic', 'Sleek', 'Fluffy', 'Wise', 'Curious', 'Dazzling', 'Serene',
    'Mighty', 'Adorable', 'Clever', 'Radiant', 'Nimble', 'Charming', 'Spirited', 'Tranquil', 'Lively', 'Magnificent',
    'Whimsical', 'Robust', 'Delicate', 'Striking', 'Agile', 'Regal', 'Enchanting', 'Resilient', 'Ethereal', 'Luminous',
    'Jovial', 'Tenacious', 'Harmonious', 'Enigmatic', 'Vivacious', 'Alluring', 'Dapper', 'Effervescent', 'Gregarious', 'Intrepid',
    'Jubilant', 'Kaleidoscopic', 'Lustrous', 'Mellifluous', 'Nonchalant', 'Opulent', 'Pristine', 'Quixotic', 'Resplendent', 'Scintillating',
    'Tenebrous', 'Ubiquitous', 'Verdant', 'Wondrous', 'Xenial', 'Yielding', 'Zestful', 'Amiable', 'Beguiling', 'Capricious',
    'Diaphanous', 'Effulgent', 'Fecund', 'Gossamer', 'Halcyon', 'Ineffable', 'Jocund', 'Kindred', 'Lissome', 'Mellifluous'
]

creatures = [
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

habitats = [
    'Reef', 'River', 'Ocean', 'Lake', 'Pond', 'Lagoon', 'Stream', 'Bay', 'Estuary', 'Coral',
    'Forest', 'Jungle', 'Savanna', 'Desert', 'Tundra', 'Mountain', 'Valley', 'Meadow', 'Wetland', 'Grassland',
    'Cave', 'Cliff', 'Island', 'Volcano', 'Glacier', 'Canyon', 'Oasis', 'Plateau', 'Marsh', 'Swamp',
    'Rainforest', 'Arctic', 'Tropics', 'Coastline', 'Dune', 'Prairie', 'Fjord', 'Delta', 'Mangrove', 'Taiga',
    'Archipelago', 'Badlands', 'Chaparral', 'Deciduous', 'Everglades', 'Floodplain', 'Geothermal', 'Heath', 'Isthmus', 'Karst',
    'Lowland', 'Moor', 'Nubivagant', 'Outcrop', 'Permafrost', 'Quagmire', 'Ravine', 'Steppe', 'Thermokarst', 'Upland',
    'Veld', 'Woodland', 'Xeric', 'Yokul', 'Zanja', 'Atoll', 'Bayou', 'Crag', 'Drumlin', 'Escarpment'
]

def generate_phrase():
    # Randomly choose the number of words (1, 2, or 3)
    num_words = random.randint(1, 3)
    
    if num_words == 1:
        return random.choice(creatures)
    elif num_words == 2:
        return f"{random.choice(adjectives)} {random.choice(creatures)}"
    else:
        return f"{random.choice(adjectives)} {random.choice(creatures)} {random.choice(habitats)}"

# Time delay before the script starts typing (in seconds)
time.sleep(5)

# Generate and type 40 random phrases
for _ in range(40):
    phrase = generate_phrase()
    pyautogui.press('/')  # Press / to go to the search bar
    pyautogui.press('backspace')  # Press backspace to erase the /
    pyautogui.typewrite(phrase)  # Type the generated phrase
    pyautogui.press('enter')  # Press Enter after typing the phrase
    time.sleep(6)  # Wait for 6 seconds before typing the next phrase