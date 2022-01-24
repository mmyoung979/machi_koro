# Local imports
from .activate_landmark import API as ns_activate_landmark
from .game import API as ns_game
from .player import API as ns_player
from .purchase import API as ns_purchase
from .roll_dice import API as ns_roll

# Global variables
NAMESPACES = [
    ns_activate_landmark,
    ns_game,
    ns_player,
    ns_purchase,
    ns_roll,
]
