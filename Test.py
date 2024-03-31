from Museum import *
import unittest


class TestMuseum(unittest.TestCase):
    def setUp(self):
        # Create some sample exhibitions, items, tours, and special events for testing
        self.exhibition1 = Exhibition("First Villages", ItemLocation.PERMANENT_GALLERIES, "Permanent")
        self.exhibition2 = Exhibition("Towards A Modern World", ItemLocation.PERMANENT_GALLERIES, "Permanent")

        self.item1 = Item("A001", "Female Figurine", "Unknown", "Sculpture", "3100-2800 BCE", "Very Significant",
                          self.exhibition1)
        self.item2 = Item("A002", "Hand Axe", "Unknown", "Arms, Military Equipment, Uniforms", "500000 BCE",
                          "Significant", self.exhibition1)
        self.item3 = Item("A003", "Portrait of William and Penelope Welby Playing Chess", "Francis Cotes", "Painting",
                          "1769 AD", "Significant", self.exhibition2)

        self.tour1 = Tour("Ahmed", 40, "2024-04-01", "EN/AR", TourStatus.RESERVED)
        self.tour2 = Tour("Bob", 15, "2024-03-31", "EN", TourStatus.UNRESERVED)

        self.special1 = Special("MASQUERAVE", "Light Show and Dance", 1, "2024-04-27", "2024-04-27",
                                "Exhibition Hall 2", 300.0)
        self.special2 = Special("From Kalila wa Dimna to La Fontaine", "Art", 117, "2024-03-26", "2024-07-21",
                                "Exhibition Hall 1", 35.0)

main()


#Test Case 1: Purchasing an exhibition ticket
'''
======================================== Menu ========================================
Press 1 to purchase a ticket
Press 2 to view exhibitions and their respective items
Press 3 to add a new exhibition
Press 4 to remove an existing exhibition
Press 5 to add a new item to an existing exhibition
Press 6 to add a new tour
Press 7 to add a new special event
Press 8 to end the program
1

======================================== Ticket Purchase ========================================
Select Ticket Type:
1. Exhibition
2. Tour
3. Special Event
1
======================================== Exhibitions ========================================
1. First Villages
2. Towards A Modern World
Select an exhibition: 1
Enter how many tickets you would like to purchase: 1

Ticket 1
Enter the name of the visitor: Rashed Alhosani
Enter the age of the visitor: 19
Do you have a national ID? (Y / N)
Y
Enter the national ID: 202208228
Are you a teacher or student of an institute? (Y / N)
Y
Enter event date (YYYY-MM-DD): 2024-04-01
======================================== Receipt ========================================
Ticket ID: 5e806e48-ef8c-4
Price (AED):  66.15
Ticket Type:  Exhibition
Status:  Valid
Purchase Date:  2024-03-31 15:47:55.723074
Event Date:  2024-04-01
Exhibition: First Villages

Tickets have been purchased successfully!
Total Tickets Purchased:  1
Total:  66.15 AED

======================================== Menu ========================================
Press 1 to purchase a ticket
Press 2 to view exhibitions and their respective items
Press 3 to add a new exhibition
Press 4 to remove an existing exhibition
Press 5 to add a new item to an existing exhibition
Press 6 to add a new tour
Press 7 to add a new special event
Press 8 to end the program
8

Exiting the program...
'''

#Test Case 2: Purchasing a tour ticket then trying to book another
'''

======================================== Menu ========================================
Press 1 to purchase a ticket
Press 2 to view exhibitions and their respective items
Press 3 to add a new exhibition
Press 4 to remove an existing exhibition
Press 5 to add a new item to an existing exhibition
Press 6 to add a new tour
Press 7 to add a new special event
Press 8 to end the program
1

======================================== Ticket Purchase ========================================
Select Ticket Type:
1. Exhibition
2. Tour
3. Special Event
2
======================================== Available Tours ========================================
Tour 1
Tour Guide: Bob
Tour Size: 15 people
Scheduled Date: 2024-03-31
Tour Language: EN
Tour Status: Unreserved

Select a tour: 1

Tickets have been purchased successfully!
======================================== Receipt ========================================
Ticket ID: 973d0860-84c5-4
Price (AED):  0.0
Ticket Type:  Tour
Status:  Valid
Purchase Date:  2024-03-31 15:49:38.184286
Event Date:  2024-03-31
----------------------------------------
Tour Information:
Tour Guide: Bob
Tour Size: 15 people
Scheduled Date: 2024-03-31
Tour Language: EN
Tour Status: Reserved

Total Tickets Purchased:  15
Total:  496.125 AED

======================================== Menu ========================================
Press 1 to purchase a ticket
Press 2 to view exhibitions and their respective items
Press 3 to add a new exhibition
Press 4 to remove an existing exhibition
Press 5 to add a new item to an existing exhibition
Press 6 to add a new tour
Press 7 to add a new special event
Press 8 to end the program
1

======================================== Ticket Purchase ========================================
Select Ticket Type:
1. Exhibition
2. Tour
3. Special Event
2
======================================== Available Tours ========================================
No tours available.
======================================== Menu ========================================
Press 1 to purchase a ticket
Press 2 to view exhibitions and their respective items
Press 3 to add a new exhibition
Press 4 to remove an existing exhibition
Press 5 to add a new item to an existing exhibition
Press 6 to add a new tour
Press 7 to add a new special event
Press 8 to end the program
8
Exiting the program...
'''

#Test Case 3: Purchasing a special event ticket
'''

======================================== Menu ========================================
Press 1 to purchase a ticket
Press 2 to view exhibitions and their respective items
Press 3 to add a new exhibition
Press 4 to remove an existing exhibition
Press 5 to add a new item to an existing exhibition
Press 6 to add a new tour
Press 7 to add a new special event
Press 8 to end the program
1

======================================== Ticket Purchase ========================================
Select Ticket Type:
1. Exhibition
2. Tour
3. Special Event
3
======================================== Special Events ========================================
Special Event 1
Title: MASQUERAVE
Event Type: Light Show and Dance
From: 2024-04-27
To: 2024-04-27
Duration: 1 Days
Location: Exhibition Hall 2
Price (AED): 300.0

Special Event 2
Title: From Kalila wa Dimna to La Fontaine
Event Type: Art
From: 2024-03-26
To: 2024-07-21
Duration: 117 Days
Location: Exhibition Hall 1
Price (AED): 35.0

Select a special event: 1
Enter how many tickets you would like to purchase: 2

Tickets have been purchased successfully!
======================================== Receipt ========================================
Ticket ID: 758a0a2b-a05b-4
Price (AED):  0.0
Ticket Type:  Special Event
Status:  Valid
Purchase Date:  2024-03-31 15:50:54.121812
Event Date:  2024-04-27
----------------------------------------
Special Event Information:
Title: MASQUERAVE
Event Type: Light Show and Dance
From: 2024-04-27
To: 2024-04-27
Duration: 1 Days
Location: Exhibition Hall 2
Price (AED): 300.0

Total Tickets Purchased:  2
Total:  630.0 AED
======================================== Menu ========================================
Press 1 to purchase a ticket
Press 2 to view exhibitions and their respective items
Press 3 to add a new exhibition
Press 4 to remove an existing exhibition
Press 5 to add a new item to an existing exhibition
Press 6 to add a new tour
Press 7 to add a new special event
Press 8 to end the program
8
Exiting the program...
'''

#Test Case 4: Adding a new exhibition that has the Mona Lisa
'''
======================================== Menu ========================================
Press 1 to purchase a ticket
Press 2 to view exhibitions and their respective items
Press 3 to add a new exhibition
Press 4 to remove an existing exhibition
Press 5 to add a new item to an existing exhibition
Press 6 to add a new tour
Press 7 to add a new special event
Press 8 to end the program
3
======================================== Adding an exhibition ========================================
Enter the title of the new exhibition: Masterpiece Revealed: The Mona Lisa Unveiled
Enter the location of the new exhibition (Permanent_Galleries, Exhibition_Halls, or Outdoor_Spaces): Exhibition_Halls
Enter the duration of the new exhibition (days): 30
New exhibition added successfully!
======================================== Menu ========================================
Press 1 to purchase a ticket
Press 2 to view exhibitions and their respective items
Press 3 to add a new exhibition
Press 4 to remove an existing exhibition
Press 5 to add a new item to an existing exhibition
Press 6 to add a new tour
Press 7 to add a new special event
Press 8 to end the program
5
======================================== Adding a new item ========================================
Available exhibitions:
1. First Villages
2. Towards A Modern World
3. Masterpiece Revealed: The Mona Lisa Unveiled
Select an existing exhibition to add an item to: 3
Enter the ID of the item: M001
Enter the title of the new item: Mona Lisa
Enter the artist/creator of the new item: Leonardo da Vinci
Enter the type of the new item: Painting
Enter the date of creation of the new item (YYYY-MM-DD): 1503 AD
Enter the historical significance of the new item: Highly Significant
New item has been added successfully!
======================================== Menu ========================================
Press 1 to purchase a ticket
Press 2 to view exhibitions and their respective items
Press 3 to add a new exhibition
Press 4 to remove an existing exhibition
Press 5 to add a new item to an existing exhibition
Press 6 to add a new tour
Press 7 to add a new special event
Press 8 to end the program
2
======================================== Exhibitions ========================================
========================================
Exhibition:  First Villages
Location:  Permanent Galleries
Duration:  Permanent
----------------------------------------
Items: 
ID:  A001
Title:  Female Figurine
Type:  Sculpture
Artist:  Unknown
Date of Creation:  3100-2800 BCE
Historical Significance:  Very Significant


ID:  A002
Title:  Hand Axe
Type:  Arms, Military Equipment, Uniforms
Artist:  Unknown
Date of Creation:  500000 BCE
Historical Significance:  Significant


========================================
Exhibition:  Towards A Modern World
Location:  Permanent Galleries
Duration:  Permanent
----------------------------------------
Items: 
ID:  A003
Title:  Portrait of William and Penelope Welby Playing Chess
Type:  Painting
Artist:  Francis Cotes
Date of Creation:  1769 AD
Historical Significance:  Significant


========================================
Exhibition:  Masterpiece Revealed: The Mona Lisa Unveiled
Location:  Exhibition Halls
Duration:  30
----------------------------------------
Items: 
ID:  M001
Title:  Mona Lisa
Type:  Painting
Artist:  Leonardo da Vinci
Date of Creation:  1503 AD
Historical Significance:  Highly Significant


======================================== Menu ========================================
Press 1 to purchase a ticket
Press 2 to view exhibitions and their respective items
Press 3 to add a new exhibition
Press 4 to remove an existing exhibition
Press 5 to add a new item to an existing exhibition
Press 6 to add a new tour
Press 7 to add a new special event
Press 8 to end the program
8

Exiting the program...

'''

#Test Case 5 Removing an exhibition then checking on it
'''
======================================== Menu ========================================
Press 1 to purchase a ticket
Press 2 to view exhibitions and their respective items
Press 3 to add a new exhibition
Press 4 to remove an existing exhibition
Press 5 to add a new item to an existing exhibition
Press 6 to add a new tour
Press 7 to add a new special event
Press 8 to end the program
4
======================================== Removing an exhibition ========================================
Available exhibitions:
1. First Villages
2. Towards A Modern World
Select the exhibition you want to remove: 2
Exhibition 'Towards A Modern World' and its items has been removed successfully!
======================================== Menu ========================================
Press 1 to purchase a ticket
Press 2 to view exhibitions and their respective items
Press 3 to add a new exhibition
Press 4 to remove an existing exhibition
Press 5 to add a new item to an existing exhibition
Press 6 to add a new tour
Press 7 to add a new special event
Press 8 to end the program
2
======================================== Exhibitions ========================================
========================================
Exhibition:  First Villages
Location:  Permanent Galleries
Duration:  Permanent
----------------------------------------
Items: 
ID:  A001
Title:  Female Figurine
Type:  Sculpture
Artist:  Unknown
Date of Creation:  3100-2800 BCE
Historical Significance:  Very Significant


ID:  A002
Title:  Hand Axe
Type:  Arms, Military Equipment, Uniforms
Artist:  Unknown
Date of Creation:  500000 BCE
Historical Significance:  Significant


======================================== Menu ========================================
Press 1 to purchase a ticket
Press 2 to view exhibitions and their respective items
Press 3 to add a new exhibition
Press 4 to remove an existing exhibition
Press 5 to add a new item to an existing exhibition
Press 6 to add a new tour
Press 7 to add a new special event
Press 8 to end the program
8

Exiting the program...
'''

#Test Case 6: Creating a new tour and purchasing it
'''
======================================== Menu ========================================
Press 1 to purchase a ticket
Press 2 to view exhibitions and their respective items
Press 3 to add a new exhibition
Press 4 to remove an existing exhibition
Press 5 to add a new item to an existing exhibition
Press 6 to add a new tour
Press 7 to add a new special event
Press 8 to end the program
6
======================================== Adding a new tour ========================================
Enter the name of the tour guide: Rashed
Enter the size of the tour: 30
Enter the scheduled date of the tour (YYYY-MM-DD): 2024-04-10
Enter the language of the tour: EN/AR
A tour has been added successfully!
======================================== Menu ========================================
Press 1 to purchase a ticket
Press 2 to view exhibitions and their respective items
Press 3 to add a new exhibition
Press 4 to remove an existing exhibition
Press 5 to add a new item to an existing exhibition
Press 6 to add a new tour
Press 7 to add a new special event
Press 8 to end the program
1

======================================== Ticket Purchase ========================================
Select Ticket Type:
1. Exhibition
2. Tour
3. Special Event
2
======================================== Available Tours ========================================
Tour 1
Tour Guide: Bob
Tour Size: 15 people
Scheduled Date: 2024-03-31
Tour Language: EN
Tour Status: Unreserved

Tour 2
Tour Guide: Rashed
Tour Size: 30 people
Scheduled Date: 2024-04-10
Tour Language: EN/AR
Tour Status: Unreserved

Select a tour: 2

Tickets have been purchased successfully!
======================================== Receipt ========================================
Ticket ID: 94b4a4cc-d3e1-4
Price (AED):  0.0
Ticket Type:  Tour
Status:  Valid
Purchase Date:  2024-03-31 15:57:49.210870
Event Date:  2024-04-10
----------------------------------------
Tour Information:
Tour Guide: Rashed
Tour Size: 30 people
Scheduled Date: 2024-04-10
Tour Language: EN/AR
Tour Status: Reserved

Total Tickets Purchased:  30
Total:  992.25 AED

======================================== Menu ========================================
Press 1 to purchase a ticket
Press 2 to view exhibitions and their respective items
Press 3 to add a new exhibition
Press 4 to remove an existing exhibition
Press 5 to add a new item to an existing exhibition
Press 6 to add a new tour
Press 7 to add a new special event
Press 8 to end the program
8
Exiting the program...

'''

#Test Case 7: Adding a special event and purchasing a ticket
'''

======================================== Menu ========================================
Press 1 to purchase a ticket
Press 2 to view exhibitions and their respective items
Press 3 to add a new exhibition
Press 4 to remove an existing exhibition
Press 5 to add a new item to an existing exhibition
Press 6 to add a new tour
Press 7 to add a new special event
Press 8 to end the program
7
======================================== Adding a new special event ========================================
Enter the title of the special event: FIFA World Cup Final Fan Festival
Enter the type of the special event: Fan Screening
Enter the duration of the special event (days): 1
Enter the start date of the special event (YYYY-MM-DD): 2022-12-18
Enter the end date of the special event (YYYY-MM-DD): 2022-12-18
Enter the location of the special event: Outdoor Spaces
Enter the price of a single regular ticket for the special event (AED): 45.0
New special event has been added successfully!
======================================== Menu ========================================
Press 1 to purchase a ticket
Press 2 to view exhibitions and their respective items
Press 3 to add a new exhibition
Press 4 to remove an existing exhibition
Press 5 to add a new item to an existing exhibition
Press 6 to add a new tour
Press 7 to add a new special event
Press 8 to end the program
1

======================================== Ticket Purchase ========================================
Select Ticket Type:
1. Exhibition
2. Tour
3. Special Event
3
======================================== Special Events ========================================
Special Event 1
Title: MASQUERAVE
Event Type: Light Show and Dance
From: 2024-04-27
To: 2024-04-27
Duration: 1 Days
Location: Exhibition Hall 2
Price (AED): 300.0

Special Event 2
Title: From Kalila wa Dimna to La Fontaine
Event Type: Art
From: 2024-03-26
To: 2024-07-21
Duration: 117 Days
Location: Exhibition Hall 1
Price (AED): 35.0

Special Event 3
Title: FIFA World Cup Final Fan Festival
Event Type: Fan Screening
From: 2022-12-18
To: 2022-12-18
Duration: 1 Days
Location: Outdoor Spaces
Price (AED): 45.0

Select a special event: 3
Enter how many tickets you would like to purchase: 5

Tickets have been purchased successfully!
======================================== Receipt ========================================
Ticket ID: 11dfe951-8bc0-4
Price (AED):  0.0
Ticket Type:  Special Event
Status:  Valid
Purchase Date:  2024-03-31 16:00:40.177539
Event Date:  2022-12-18
----------------------------------------
Special Event Information:
Title: FIFA World Cup Final Fan Festival
Event Type: Fan Screening
From: 2022-12-18
To: 2022-12-18
Duration: 1 Days
Location: Outdoor Spaces
Price (AED): 45.0

Total Tickets Purchased:  5
Total:  236.25 AED
======================================== Menu ========================================
Press 1 to purchase a ticket
Press 2 to view exhibitions and their respective items
Press 3 to add a new exhibition
Press 4 to remove an existing exhibition
Press 5 to add a new item to an existing exhibition
Press 6 to add a new tour
Press 7 to add a new special event
Press 8 to end the program
8

Exiting the program...

'''