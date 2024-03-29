import enum as Enum
from datetime import datetime

class ItemLocation(Enum):
    PERMANENT_GALLERIES = "Permanent Galleries"
    EXHIBITION_HALLS = "Exhibition Halls"
    OUTDOOR_SPACES = "Outdoor Spaces"
class TicketType(Enum):
    EXHIBITION = "Exhibition"
    TOUR = "Tour"
    SPECIAL_EVENT = "Special Event"

class TicketStatus(Enum):
    VALID = "Valid"
    INVALID = "Invalid"


class Item:
    """
    This class represents an item that belongs in the museum.

    Attributes:
    - item_id: The unique identifier for the item
    - item_title: The title of the item
    - item_artist: The artist/creator of the item
    - item_type: The type of the item
    - item_DOC: The date of creation of the item
    - historical_significance: The historical significance of the item
    - item_exhibition: The items that are presented in the exhibition.

    """
    def __init__(self, item_id, item_title, item_artist, item_type, item_DOC, historical_significance, item_exhibition):
        self._item_id = item_id
        self._item_title = item_title
        self._item_artist = item_artist
        self._item_type = item_type
        self._item_DOC = item_DOC
        self._historical_significance= historical_significance
        self._item_exhibition = None

    def setExhibition(self, item_exhibition):
        self._item_exhibition = item_exhibition


class Exhibition:
    """    
    This class represents an exhibition that exists in the museum.
    
    Attributes:
    - exhibition_title: The title of the exhibition
    - exhibition_location: The location of the exhibition (permanent galleries, exhibition halls, or outdoor spaces)
    - exhibition_location: The location of the exhibition
    
    """
    def __init__(self, exhibition_title, exhibition_location, exhibition_duration, Items):
        self._exhibition_title = exhibition_title
        self._exhibition_location = exhibition_location
        self._exhibition_duration = exhibition_duration
        self._Items = []

    def addItem(self, item):
        "This method adds an item to an existing exhibition."
        self._Items.append(item)


class Visitor:
    """
    This class represents .

    Attributes:
    -
    -
    -

    """


class Ticket:
    """
        This class represents a ticket that is used to enter the museum and its exhibitions.

        Attributes:
        -
        -
        -

        """






class GroupTour(Ticket):
    """
    This class represents .

    Attributes:
    -
    -
    -

    """

class SpecialEvent(Ticket):
    """
    This class represents .

    Attributes:
    -
    -
    -

    """