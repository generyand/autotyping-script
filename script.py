import pyautogui
import time

# List of 100 species of trees
tree_species = [
    'Alder', 'Ash', 'Aspen', 'Bald Cypress', 'Baobab', 'Beech', 'Birch', 'Black Walnut', 'Blackthorn', 'Box Elder',
    'Brazilwood', 'Buckeye', 'Butternut', 'Cedar', 'Cherry', 'Chestnut', 'Cottonwood', 'Cork Oak', 'Cucumber Tree',
    'Cypress', 'Douglas Fir', 'Dogwood', 'Elm', 'Eucalyptus', 'Fig', 'Fir', 'Ginkgo', 'Hemlock', 'Hickory', 'Holly',
    'Hornbeam', 'Jacaranda', 'Juniper', 'Katsura', 'Larch', 'Laurel', 'Lime', 'Linden', 'Locust', 'Mahogany', 'Magnolia',
    'Maple', 'Mulberry', 'Oak', 'Olive', 'Palm', 'Pine', 'Plane Tree', 'Poplar', 'Redbud', 'Redwood', 'Rowan',
    'Sassafras', 'Sequoia', 'Serviceberry', 'Silver Birch', 'Spruce', 'Sumac', 'Sweet Gum', 'Sycamore', 'Tamarack',
    'Teak', 'Tulip Tree', 'Walnut', 'Weeping Willow', 'White Cedar', 'White Oak', 'Willow', 'Yew', 'Yellow Birch',
    'Yellowwood', 'Zebrawood', 'Ailanthus', 'Amur Maple', 'Angel Oak', 'Banyan', 'Basswood', 'Bird Cherry', 'Bitter Cherry',
    'Blue Spruce', 'Boab Tree', 'Broadleaf', 'Calabash', 'Corkwood', 'Dragon Tree', 'Elder', 'English Oak', 'Fan Palm',
    'Fragrant Olive', 'Giant Sequoia', 'Honey Locust', 'Ironwood', 'Kapok Tree', 'Kentucky Coffee Tree', 'Lacebark Pine',
    'Lignum Vitae', 'Mango', 'Mountain Ash', 'Norway Spruce', 'Paper Birch', 'Pawpaw', 'Pecan', 'Red Maple', 'Scotch Pine',
    'Sourwood', 'Sweet Bay', 'Tupelo'
]

# Time delay before the script starts typing (in seconds)
time.sleep(5)

# Type each tree species, press / to go to the search bar, and backspace to erase the /
for species in tree_species:
    pyautogui.press('/')  # Press / to go to the search bar
    pyautogui.press('backspace')  # Press backspace to erase the /
    pyautogui.typewrite(species)  # Type the tree species
    pyautogui.press('enter')  # Press Enter after typing the species
    time.sleep(2)  # Wait for 2 seconds before typing the next species
