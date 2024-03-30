from enum import Enum
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

class TourStatus(Enum):
    RESERVED = "Reserved"
    UNRESERVED = "Unreserved"




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
    - item_exhibition: The items that are displayed in the exhibition.

    """

    def __init__(self, item_id, item_title, item_artist, item_type, item_DOC, historical_significance, item_exhibition):
        self._item_id = item_id
        self._item_title = item_title
        self._item_artist = item_artist
        self._item_type = item_type
        self._item_DOC = item_DOC
        self._historical_significance = historical_significance
        self._item_exhibition = []

    def displayItem(self):
        "This method displays information of a specific item."
        print("ID: ", self._item_id)
        print("Title: ", self._item_title)
        print("Type: ", self._item_type)
        print("Artist: ", self._item_artist)
        print("Date of Creation: ", self._item_DOC)
        print("Historical Significance: ", self._historical_significance)
        print("")


class Exhibition:
    """    
    This class represents an exhibition that exists in the museum.
    
    Attributes:
    - exhibition_title: The title of the exhibition
    - exhibition_location: The location of the exhibition (permanent galleries, exhibition halls, or outdoor spaces)
    - exhibition_duration: The duration of the exhibition.
    
    """

    def __init__(self, exhibition_title, exhibition_location, exhibition_duration):
        self._exhibition_title = exhibition_title
        self._exhibition_location = exhibition_location
        self._exhibition_duration = exhibition_duration
        self._Items = []

    def add_item(self, item):
        "This method adds an item to an existing exhibition."
        self._Items.append(item)

    def remove_item(self, item):
        "This method removes an item from an existing exhibition."
        self._Items.remove(item)

    def display_exhibition(self):
        "This method displays information of the exhibition."
        print("Exhibition: ", self._exhibition_title)
        print("Location: ", self._exhibition_location)
        print("Duration: ", self._exhibition_duration)
        print("----" * 10)
        print("Items: ")
        for item in self._Items:
            item.displayItem()
            print("----" * 10)
        print("")


class Visitor:
    """
    This class represents a visitor that can visit the museum and its exhibitions.

    Attributes:
    - visitor_name: The name of the visitor
    - visitor_age: The age of the visitor
    - visitor_ID: The ID of the visitor (If they don't have a national ID, its value will be NONE.)

    """

    def __init__(self, visitor_name, visitor_age, vistor_ID, visitor_stud_teacher):
        self._visitor_name = visitor_name
        self._visitor_age = visitor_age
        self._visitor_ID = vistor_ID
        self._visitor_stud_teacher = visitor_stud_teacher
        self._visitor_tickets = []

    def purchase_ticket(self, ticket):
        self._visitor_tickets.append(ticket)


class Ticket:
    """
        This class represents a ticket that is used to enter the museum and its exhibitions.

        Attributes:
        - ticket_ID: The unique ID given to a ticket
        - ticket_type: The type of ticket (exhibitions, tours, or special events)
        - purchase_date: Date of purchase of the ticket
        - event_date: Date of event of the ticket
        - ticket_price: The price of the ticket
        - ticket_status: The status of the ticket (valid, invalid)

        """

    def __init__(self, ticket_ID, ticket_type, purchase_date, event_date, ticket_price, ticket_status):
        self._ticket_ID = ticket_ID
        self._ticket_type = ticket_type
        self._purchase_date = purchase_date
        self._event_date = event_date
        self._ticket_price = ticket_price
        self._ticket_status = ticket_status

    def display_receipt(self):
        print("====" * 10, "Recept", "====" * 10)
        print("Ticket ID:", self._ticket_ID)
        print("Price (AED): ", self._ticket_price)
        print("Ticket Type: ", self._ticket_type)
        print("Status: ", self._ticket_status)
        print("Purchase Date: ", self._purchase_date)
        print("Event Date: ", self._event_date)


class Tour(Ticket):
    """
    This class represents a tour ticket which is a type of ticket.

    Attributes:
    - tour_guide: The assigned tour guide.
    - tour_size: The size of the tour.
    - selected_date: The scheduled date of the tour

    """
    def __init__(self, tour_guide, tour_size, selected_date, tour_lang, tour_status):
        self._tour_guide = tour_guide
        self._tour_size = tour_size
        self._selected_date = selected_date
        self._tour_lang = tour_lang
        self._tour_status = tour_status

    def display_tour(self):
        print("Tour Guide: ", self._tour_guide)
        print("Tour Size: ", self._tour_size, "people")
        print("Scheduled Date: ", self._selected_date)
        print("Tour Language: ", self._tour_lang)
        print("Tour Status: ", self._tour_status.value)
        print("")


class Special(Ticket):
    """
    This class represents a special event ticket which is a type of ticket.

    Attributes:
    - special_title: The title of a special event
    - special_type: The type of special event (Fundraising, musical concerts, or light shows)
    - special_duration: The duration of the special event
    - special_location: The location of the special event (permanent galleries, exhibition halls, or outdoor spaces)
    - special_price: The price of a single regular special event ticket in AED.
    """
    def __init__(self, special_title, special_type, special_duration, special_from, special_to, special_location, special_price):
        self._special_title = special_title
        self._special_type = special_type
        self._special_duration = special_duration
        self._special_from = special_from
        self._special_to = special_to
        self._special_location = special_location
        self._special_price = special_price

    def display_special(self):
        "This method displays information of the exhibition."
        print("Title:", self._special_title)
        print("Event Type:", self._special_type)
        print("From:", self._special_from)
        print("To:", self._special_to)
        print("Duration:", self._special_duration, "Days")
        print("Location:", self._special_location)
        print("Price (AED):", self._special_price)
        print("")




def main():
    visitors = []
    exhibitions = []
    tours = [tour1, tour2]
    specials = [special1, special2]

    exhibition1.add_item(item1)
    exhibition1.add_item(item2)
    exhibition2.add_item(item3)
    exhibitions.extend([exhibition1, exhibition2])


    while True:
        # Potential Menu
        print("====" * 10, "Menu", "====" * 10)
        print("Press 1 to purchase a ticket")
        print("Press 2 to view exhibitions and their respective items")
        print("Press 3 to add a new exhibition")
        print("Press 4 to add a new item to an existing exhibition")
        print("Press 5 to end the program")
        userChoice = int(input(""))

        if userChoice == 1:
            print("")
            print("====" * 10, "Ticket Purchase", "====" * 10)
            print("Select Ticket Type:")
            print("1. Exhibition")
            print("2. Tour")
            print("3. Special Event")
            ticket_choice = int(input())
            if ticket_choice == 1:
                ticket_type = TicketType.EXHIBITION
                num_tickets = int(input("Enter how many tickets you would like to purchase: "))
                total_price = 0
                for i in range(num_tickets):
                    print("\nTicket", i + 1)
                    visitor_name = input("Enter the name of the visitor: ")
                    visitor_age = int(input("Enter the age of the visitor: "))
                    queID = input("Do you have a national ID? (Y / N)\n")
                    if queID.lower() == "y":
                        visitor_ID = (input("Enter the national ID: "))
                    else:
                        visitor_ID = None

                    queOcc = input("Are you a teacher or student of an institute? (Y / N)\n")
                    if queOcc.lower() == "y":
                        visitor_stud_teacher = True
                    else:
                        visitor_stud_teacher = False

                    visitor = Visitor(visitor_name, visitor_age, visitor_ID, visitor_stud_teacher)
                    visitors.append(visitor)

                    purchase_date = datetime.now()
                    event_date = input("Enter event date (YYYY-MM-DD): ")

                    ticket_price = calculate_price(ticket_type, visitor_age, visitor_ID, visitor_stud_teacher, None, None)
                    total_price = total_price + ticket_price
                    ticket = Ticket(len(visitors), ticket_type, purchase_date, event_date, ticket_price,
                                    TicketStatus.VALID)

                    visitor.purchase_ticket(ticket)
                    ticket.display_receipt()

                    print("\nTickets have been purchased successfully!")

                    print("Total Tickets Purchased: ", num_tickets)
                    print("Total: ", total_price, "AED")
                    print("")

            elif ticket_choice == 2:
                ticket_type = TicketType.TOUR
                print("====" * 10, "Available Tours", "====" * 10)
                unreserved_tours = [tour for tour in tours if tour._tour_status == TourStatus.UNRESERVED]
                count = 1
                if not unreserved_tours:
                    print("No tours available.")
                    break
                else:
                    for tour in unreserved_tours:
                        print("Tour", count)
                        count += 1
                        tour.display_tour()

                tour_choice = int(input("Select a tour: "))
                selected_tour = unreserved_tours[tour_choice - 1]
                ticket_price = calculate_price(ticket_type, None, None, None, selected_tour._tour_size, None)

                total_price = ticket_price

                selected_tour._tour_status = TourStatus.RESERVED

                print("\nTickets have been purchased successfully!")



                print("Total Tickets Purchased: ", selected_tour._tour_size)
                print("Total: ", total_price, "AED")
                print("")



            elif ticket_choice == 3:
                ticket_type = TicketType.SPECIAL_EVENT
                print("====" * 10, "Special Events", "====" * 10)
                count = 1
                for special in specials:
                    print("Special Event", count)
                    count += 1
                    special.display_special()
                special_choice = int(input("Select a special event: "))
                selected_special = specials[special_choice - 1]
                num_tickets = int(input("Enter how many tickets you would like to purchase: "))

                total_price = calculate_price(ticket_type, None, None, None, num_tickets, selected_special._special_price)
                print("\nTickets have been purchased successfully!")
                print("Total Tickets Purchased: ", num_tickets)
                print("Total: ", total_price, "AED")


        elif userChoice == 2:
            print("====" * 10, "Exhibitions", "====" * 10)
            for exhibition in exhibitions:
                exhibition.display_exhibition()

        elif userChoice == 3:
            "Creates a new exhibition"
            pass

        elif userChoice == 4:
            "Adds a new item to an existing exhibition"
            pass
        elif userChoice == 5:
            print("Exiting the program...")
            break
        else:
            print("Invalid response, please enter a valid input.")

def calculate_price(ticket_type, visitor_age, visitor_ID, visitor_stud_teacher, tour_size, special_price):
    "This method calculates the price of a ticket depending on the ticket type, the visitor age, and whether they have a visitor ID"
    ticket_price = 0
    if ticket_type == TicketType.EXHIBITION:
        if 18 <= visitor_age <= 60:
            if visitor_ID is None and not visitor_stud_teacher == True:
                ticket_price = 63
            else:
                ticket_price = 0

        else:
            if visitor_ID is not None or visitor_stud_teacher == False:
                ticket_price = 0
            else:
                ticket_price = 63

    elif ticket_type == TicketType.TOUR:
        ticket_price = (63 * 0.5) * tour_size

    elif ticket_type == TicketType.SPECIAL_EVENT:
        ticket_price = special_price * tour_size

    ticket_price *= 1.05 #Applying VAT
    return ticket_price


#Initial objects
exhibition1 = Exhibition("First Villages", ItemLocation.PERMANENT_GALLERIES, "Permanent")
exhibition2 = Exhibition("Towards A Modern World", ItemLocation.PERMANENT_GALLERIES, "Permanent")

item1 = Item("A001", "Female Figurine", "Unknown", "Sculpture", "3100-2800 BCE", "Very Significant", exhibition1)
item2 = Item("A002", "Hand Axe", "Unknown", "Arms, Military Equipment, Uniforms", "500000 BCE", "Significant", exhibition1)
item3 = Item("A003", "Portrait of William and Penelope Welby Playing Chess", "Francis Cotes", "Painting", "1769 AD", "Significant", exhibition2)

tour1 = Tour("Ahmed", 40, "2024-04-01", "EN/AR", TourStatus.RESERVED)
tour2 = Tour("Bob", 15, "2024-03-31", "EN", TourStatus.UNRESERVED)

special1 = Special("MASQUERAVE","Light Show and Dance", 1, "2024-04-27", "2024-04-27", "Exhibition Hall 1", 300.0)
special2 = Special("From Kalila wa Dimna to La Fontaine", "Art", 117, "2024-03-26", "2024-07-21","Exhibition Hall 1", 35)


main()