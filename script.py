import pyautogui
import time

# List of 100 species of fish
fish_species = [
    'Angelfish', 'Archerfish', 'Arowana', 'Barracuda', 'Bass', 'Betta', 'Bluegill', 'Bonito', 'Bullhead', 'Carp',
    'Catfish', 'Clownfish', 'Cod', 'Corydoras', 'Crappie', 'Damselfish', 'Discus', 'Dorado', 'Dragonfish', 'Drum',
    'Eel', 'Emperor', 'Flatfish', 'Flounder', 'Flying Fish', 'Gars', 'Goby', 'Gourami', 'Grouper', 'Grunt', 'Guppy',
    'Haddock', 'Hake', 'Halibut', 'Herring', 'Jackfish', 'John Dory', 'Koi', 'Lionfish', 'Mackerel', 'Marlin',
    'Minnow', 'Molly', 'Monkfish', 'Moray Eel', 'Mullet', 'Napoleonfish', 'Oscar', 'Paddlefish', 'Parrotfish', 'Peacock Bass',
    'Perch', 'Pike', 'Piranha', 'Pollock', 'Pomfret', 'Pompano', 'Pufferfish', 'Rainbow Trout', 'Rasbora', 'Ray',
    'Red Snapper', 'Roach', 'Rockfish', 'Sailfish', 'Salmon', 'Sardine', 'Scat', 'Scorpionfish', 'Sea Bass', 'Seahorse',
    'Shark', 'Sheepshead', 'Skate', 'Smelt', 'Snakehead', 'Snapper', 'Sockeye Salmon', 'Sole', 'Stargazer', 'Stickleback',
    'Sturgeon', 'Sunfish', 'Swordfish', 'Tarpon', 'Tilapia', 'Triggerfish', 'Tuna', 'Turbot', 'Walleye', 'Wahoo',
    'Wrasse', 'Yellowfin Tuna', 'Zebra Danio', 'Zebrafish', 'Zander', 'Whale Shark', 'Whitefish', 'Weeverfish', 'Yellowtail',
    'Yellow Perch', 'Zander', 'Zebrafish'
]

# Time delay before the script starts typing (in seconds)
time.sleep(5)

# Type each fish species, press / to go to the search bar, and backspace to erase the /
for species in fish_species:
    pyautogui.press('/')  # Press / to go to the search bar
    pyautogui.press('backspace')  # Press backspace to erase the /
    pyautogui.typewrite(species)  # Type the fish species
    pyautogui.press('enter')  # Press Enter after typing the species
    time.sleep(2)  # Wait for 2 seconds before typing the next species
