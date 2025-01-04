#Gpt class solution#

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}')"


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        """Adds a book to the library."""
        self.books.append(book)

    def remove_book(self, book_to_remove):
        """Removes a book from the library. If there are duplicates, removes the first occurrence."""
        for book in self.books:
            if book.title == book_to_remove.title and book.author == book_to_remove.author:
                self.books.remove(book)
                return  # Exit after removing the first match
                
    def search_books(self, search_string):
        """Searches for books by title or author, case-insensitive."""
        matching_books = []
        search_string = search_string.lower()  # Convert search string to lowercase for case-insensitive comparison
        for book in self.books:
            if search_string in book.title.lower() or search_string in book.author.lower():
                matching_books.append(book)
        return matching_books
    
    ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,


    fireball_damage = 500
    potion_mana = 100



class Wizard:
    
    # The __init__ method is the constructor. It initializes the Wizard object.
    # It takes 'name', 'stamina', and 'intelligence' as arguments.
    def __init__(self, name, stamina, intelligence):
        
        # Private attribute '__stamina': Stores the stamina of the wizard.
        # The double underscore makes this attribute private (not directly accessible from outside the class).
        self.__stamina = stamina
        
        # Private attribute '__intelligence': Stores the intelligence of the wizard.
        # The double underscore makes this attribute private.
        self.__intelligence = intelligence
        
        # Public attribute 'name': Stores the name of the wizard.
        # This is accessible from outside the class.
        self.name = name
        
        # Public attribute 'mana': Stores the wizard's mana based on their intelligence.
        # We calculate mana as 10 times their intelligence.
        self.mana = self.__intelligence * 10
        
        # Public attribute 'health': Stores the wizard's health based on their stamina.
        # We calculate health as 100 times their stamina.
        self.health = self.__stamina * 100


class Wizard:
    def __init__(self, name, stamina, intelligence):
        self.name = name
        self.__stamina = stamina
        self.__intelligence = intelligence
        self.mana = self.__intelligence * 10
        self.health = self.__stamina * 100

    def get_fireballed(self):
        self.health -= fireball_damage
        

    def drink_mana_potion(self):
        self.mana -= potion_mana

        ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

fireball_damage = 500
potion_mana = 100
fireball_cost = 50


class Wizard:
    def __init__(self, name, stamina, intelligence):
        self.name = name
        self.__stamina = stamina
        self.__intelligence = intelligence
        self.mana = self.__intelligence * 10
        self.health = self.__stamina * 100

    def cast_fireball(self, target):
        if self.mana < fireball_cost:
            raise Exception(f"{self.name} cannot cast fireball")
        else:
            self.mana -= fireball_cost
            target.get_fireballed()
        

    def is_alive(self):
        return self.health > 0
       

    def get_fireballed(self):
        self.health -= fireball_damage


    def drink_mana_potion(self):
        self.mana += potion_mana
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.__account_number = account_number
        self.__balance = initial_balance

    def get_account_number(self):
        return self.__account_number

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Cannot deposit zero or negative funds")
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Cannot withdraw zero or negative funds")
        if self.__balance < amount:
            raise ValueError("Insufficient funds")
        self.__balance -= amount
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

class Student:
    def __init__(self, name):
        self.name = name
        self.__courses = {}

    def calculate_letter_grade(self, score):
        if score >= 90:
            return "A"
        elif 80 <= score < 90:
            return "B"
        elif 70 <= score < 80:
            return "C"
        elif 60 <= score < 70:
            return "D"
        else:
            return "F"


        
    def add_course(self, course_name, score):
        grade = self.calculate_letter_grade(score)
        self.__courses[course_name] = grade


    def get_courses(self):
        return self.__courses
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

class Human:
    def __init__(self, pos_x, pos_y, speed):
        self.__pos_x = pos_x
        self.__pos_y = pos_y
        self.__speed = speed

    def move_right(self):
        self.__pos_x += self.__speed
        return self.__pos_x
    
    def move_left(self):
        self.__pos_x -= self.__speed
        return self.__pos_x

    def move_up(self):
        self.__pos_y += self.__speed
        return self.__pos_y

    def move_down(self):
        self.__pos_y -= self.__speed
        return self.__pos_y

    def get_position(self):
        return (self.__pos_x, self.__pos_y)
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
class Human:
    def sprint_right(self):
        self.__raise_if_cannot_sprint()  # Check if there is enough stamina
        self.__pos_x += 2 * self.__speed  # Move position by twice the speed
        self.__use_sprint_stamina()  # Decrease stamina after sprint
        return self.__pos_x
        
    def sprint_left(self):
        self.__raise_if_cannot_sprint()  # Check if there is enough stamina
        self.__pos_x -= 2 * self.__speed  # Move position by twice the speed
        self.__use_sprint_stamina()  # Decrease stamina after sprint
        return self.__pos_x

    def sprint_up(self):
        self.__raise_if_cannot_sprint()  # Check if there is enough stamina
        self.__pos_y += 2 * self.__speed  # Move position by twice the speed
        self.__use_sprint_stamina()  # Decrease stamina after sprint
        return self.__pos_y

    def sprint_down(self):
        self.__raise_if_cannot_sprint()  # Check if there is enough stamina
        self.__pos_y -= 2 * self.__speed  # Move position by twice the speed
        self.__use_sprint_stamina()  # Decrease stamina after sprint
        return self.__pos_y

    def __raise_if_cannot_sprint(self):
        if self.__stamina <= 0:
            raise Exception("not enough stamina to sprint")
        

    def __use_sprint_stamina(self):
        self.__stamina -= 1


    def move_right(self):
        self.__pos_x += self.__speed

    def move_left(self):
        self.__pos_x -= self.__speed

    def move_up(self):
        self.__pos_y += self.__speed

    def move_down(self):
        self.__pos_y -= self.__speed

    def get_position(self):
        return self.__pos_x, self.__pos_y

    def __init__(self, pos_x, pos_y, speed, stamina):
        self.__pos_x = pos_x
        self.__pos_y = pos_y
        self.__speed = speed
        self.__stamina = stamina

,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

class Calculator:
    def __init__(self, initial_value=0):
        self.__result = initial_value

    def add(self, a):
        self.__result += a

    def subtract(self, a):
        self.__result -= a

    def multiply(self, a):
        self.__result *= a

    def divide(self, a):
        if a != 0:
            self.__result /= a
        else:
            raise ValueError("Cannot divide by zero")

    def modulo(self, a):
        if a == 0:
            raise ValueError("Cannot divide by zero")
        else:
            self.__result %= a

    def power(self, a):
        self.__result **= a

    def square_root(self):
        self.__result = self.__result ** 0.5

    def clear(self):
        self.__result = 0

    def get_result(self):
        return self.__result
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
import random  # Import the random module to shuffle the deck


class DeckOfCards:
    # Class-level constants for the suits and ranks
    SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]  # Four suits in a deck
    RANKS = [
        "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"
    ]  # Ranks from Ace to King

    def __init__(self):
        """Constructor initializes the deck of cards."""
        self.__cards = []  # Create an empty list to hold the cards
        self.create_deck()  # Call the method to populate the deck with cards

    def create_deck(self):
        """Creates a deck of 52 cards (Rank, Suit) in the correct order."""
        # Loop through all suits first, then all ranks
        for suit in self.SUITS:
            for rank in self.RANKS:
                # Append each card as a tuple (rank, suit) to the cards list
                self.__cards.append((rank, suit))

    def shuffle_deck(self):
        """Shuffles the deck randomly using random.shuffle."""
        random.shuffle(self.__cards)  # This shuffles the list of cards in place

    def deal_card(self):
        """Deals the top card from the deck (removes and returns it)."""
        if self.__cards:
            # Pop the last card off the deck and return it
            return self.__cards.pop()
        else:
            # If there are no cards left, return None
            return None


    def __str__(self):
        """Returns a string representation of the current number of cards in the deck."""
        # Return the number of cards left in the deck
        return f"The deck has {len(self.__cards)} cards"
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
class Human:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


class Archer(Human):
    def __init__(self, name, num_arrows):
        super().__init__(name)
        self.__num_arrows = num_arrows

    def get_num_arrows(self):
        return self.__num_arrows
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
class Human:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


class Archer(Human):
    def __init__(self, name, num_arrows):
        super().__init__(name)
        self.__num_arrows = num_arrows

    def get_num_arrows(self):
        return self.__num_arrows

    def use_arrows(self, num):
        if num > self.__num_arrows:
            raise Exception("not enough arrows")
        else:
            self.__num_arrows -= num
        
class Crossbowman(Archer):
    def __init__(self, name, num_arrows):
        super().__init__(name, num_arrows)

    def triple_shot(self, target):
        self.use_arrows(3)
        return f"{target.get_name()} was shot by 3 crossbow bolts"

class Wizard(Hero):
    def __init__(self, name, health, mana):
        super().__init__(name, health)
        self.__mana = mana

    def cast(self, target):
        if self.__mana < 25:
            raise Exception("not enough mana")
        self.__mana -= 25
        target.take_damage(25)

,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
class Unit:
    def __init__(self, name, pos_x, pos_y):
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y

    def in_area(self, x_1, y_1, x_2, y_2):
        return x_1 <= self.pos_x <= x_2 and y_1 <= self.pos_y <= y_2

        
class Dragon(Unit):
    def __init__(self, name, pos_x, pos_y, fire_range):
        super().__init__(name, pos_x, pos_y)
        self.__fire_range = fire_range

    def breathe_fire(self, x, y, units):
        hit_by_blast = []
        for unit in units:
            in_area = unit.in_area(
                x - self.__fire_range,
                y - self.__fire_range,
                x + self.__fire_range,
                y + self.__fire_range,
            )
            if in_area:
                hit_by_blast.append(unit)
        return hit_by_blast

,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
def main():
    dragons = [
        Dragon("Green Dragon", 0, 0, 1),
        Dragon("Red Dragon", 2, 2, 2),
        Dragon("Blue Dragon", 4, 3, 3),
        Dragon("Black Dragon", 5, -1, 4),
    ]

    # don't touch above this line

    for dragon in dragons:
        describe(dragon)

    for i in range(len(dragons)):
        dragon = dragons[i]
        dragons_copy = dragons.copy()
        del dragons_copy[i]
        dragon.breathe_fire(x=3, y=3, units=dragons_copy)


def describe(dragon):
    print(f"{dragon.name} is at {dragon.pos_x}/{dragon.pos_y}")


class Unit:
    def __init__(self, name, pos_x, pos_y):
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y

    def in_area(self, x_1, y_1, x_2, y_2):
        return (
            self.pos_x >= x_1
            and self.pos_x <= x_2
            and self.pos_y >= y_1
            and self.pos_y <= y_2
        )


class Dragon(Unit):
    def __init__(self, name, pos_x, pos_y, fire_range):
        super().__init__(name, pos_x, pos_y)
        self.__fire_range = fire_range

    def breathe_fire(self, x, y, units):
        print(f"{self.name} breathes fire at {x}/{y} with range {self.__fire_range}")
        print("====================================")
        for unit in units:
            in_area = unit.in_area(
                x - self.__fire_range,
                y - self.__fire_range,
                x + self.__fire_range,
                y + self.__fire_range,
            )
            if in_area:
                print(f"{unit.name} is hit by the fire")


main()
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width

    def get_perimeter(self):
        return 2 * (self.length + self.width)


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
class Siege:
    def __init__(self, max_speed, efficiency):
        self.max_speed = max_speed
        self.efficiency = efficiency

    def get_trip_cost(self, distance, food_price):
        return (distance / self.efficiency) * food_price

    def get_cargo_volume(self):
        pass


class BatteringRam(Siege):
    def __init__(
        self,
        max_speed,
        efficiency,
        load_weight,
        bed_area,
    ):
        super().__init__(max_speed, efficiency)
        self.load_weight = load_weight
        self.bed_area = bed_area

    def get_trip_cost(self, distance, food_price):
        base_cost = super().get_trip_cost(distance, food_price)
        base_cost += self.load_weight * 0.01
        return base_cost

    def get_cargo_volume(self):
        return self.bed_area * 2


class Catapult(Siege):
    def __init__(self, max_speed, efficiency, cargo_volume):
        super().__init__(max_speed, efficiency)
        self.cargo_volume = cargo_volume

    def get_cargo_volume(self):
        return self.cargo_volume
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def get_left_x(self):
        return min(self.__x1, self.__x2)
   
    def get_right_x(self):
        return max(self.__x1, self.__x2)

    def get_top_y(self):
        return max(self.__y1, self.__y2)
           
    def get_bottom_y(self):
        return min(self.__y1, self.__y2)

    def __repr__(self):
        return f"Rectangle({self.__x1}, {self.__y1}, {self.__x2}, {self.__y2})"
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
class Rectangle:
    def overlaps(self, rect):
        if (self.get_right_x() < rect.get_left_x() or
            self.get_left_x() > rect.get_right_x() or
            self.get_top_y() < rect.get_bottom_y() or
            self.get_bottom_y() > rect.get_top_y()):
            return False
        return True
    
    def __init__(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def get_left_x(self):
        if self.__x1 < self.__x2:
            return self.__x1
        return self.__x2

    def get_right_x(self):
        if self.__x1 > self.__x2:
            return self.__x1
        return self.__x2

    def get_top_y(self):
        if self.__y1 > self.__y2:
            return self.__y1
        return self.__y2

    def get_bottom_y(self):
        if self.__y1 < self.__y2:
            return self.__y1
        return self.__y2

    def __repr__(self):
        return f"Rectangle({self.__x1}, {self.__y1}, {self.__x2}, {self.__y2})"
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
class Unit:
    def __init__(self, name, pos_x, pos_y):
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y

    def in_area(self, x1, y1, x2, y2):
        pass


class Dragon(Unit):
    def __init__(self, name, pos_x, pos_y, height, width, fire_range):
        super().__init__(name, pos_x, pos_y)
        self.fire_range = fire_range
        self.height = height
        self.width = width
        x1 = pos_x - width / 2
        x2 = pos_x + width / 2
        y1 = pos_y + height / 2
        y2 = pos_y - height / 2
        self.__hit_box = Rectangle(x1, y2, x2, y1)

    def in_area(self, x1, y1, x2, y2):
        area_rect = Rectangle(x1, y1, x2, y2)
        return self.__hit_box.overlaps(area_rect)

class Rectangle:
    def overlaps(self, rect):
        return (
            self.get_left_x() <= rect.get_right_x()
            and self.get_right_x() >= rect.get_left_x()
            and self.get_top_y() >= rect.get_bottom_y()
            and self.get_bottom_y() <= rect.get_top_y()
        )

    def __init__(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def get_left_x(self):
        if self.__x1 < self.__x2:
            return self.__x1
        return self.__x2

    def get_right_x(self):
        if self.__x1 > self.__x2:
            return self.__x1
        return self.__x2

    def get_top_y(self):
        if self.__y1 > self.__y2:
            return self.__y1
        return self.__y2

    def get_bottom_y(self):
        if self.__y1 < self.__y2:
            return self.__y1
        return self.__y2
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
class Sword:
    def __init__(self, sword_type):
        self.sword_type = sword_type

    def __add__(self, other):
        if self.sword_type == "bronze" and other.sword_type == "bronze":
            return Sword("iron")
        if self.sword_type == "iron" and other.sword_type == "iron":
            return Sword("steel")
        else:
            raise Exception("can not craft")
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
Operation               Operator 	  Method
Addition 	                + 	      __add__
Subtraction 	            - 	      __sub__
Multiplication 	            * 	      __mul__
Power 	                    ** 	      __pow__
Division 	                / 	    __truediv__
Floor Division 	            // 	    __floordiv__
Remainder       (modulo) 	% 	      __mod__
Bitwise Left Shift 	        << 	    __lshift__
Bitwise Right Shift 	    >> 	    __rshift__
Bitwise AND 	            & 	     __and__
Bitwise OR 	                | 	     __or__
Bitwise XOR 	            ^ 	    __xor__
Bitwise NOT 	            ~ 	   __invert__

,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
class Dragon:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self):
        return f"I am {self.name}, the {self.color} dragon"
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
import random

SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]

RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]


class Card:
    def __init__(self, rank, suit):
        self.rank = rank 
        self.suit = suit
        self.rank_index = RANKS.index(rank)
        self.suit_index = SUITS.index(suit)

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

    def __lt__(self, other):
        if self.rank_index < other.rank_index:
            return True
        if self.rank_index == other.rank_index and self.suit_index < other.suit_index:
            return True
        return False
        

    def __gt__(self, other):
        if self.rank_index > other.rank_index:
            return True
        if self.rank_index == other.rank_index and self.suit_index > other.suit_index:
            return True
        return False
        
        

    # don't touch below this line

    def __str__(self):
        return f"{self.rank} of {self.suit}"
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
import random


class CardGame:
    def __init__(self,):
        self.deck = DeckOfCards()
        self.deck.shuffle_deck()

        
    def play(self):
        print("Nothing to play...")


class War(CardGame):
    def __init__(self,):
        super().__init__()
        self.player1_hand = []
        self.player2_hand = []
        
        

    def play(self):
        self.__deal_hand(self.player1_hand)
        self.__deal_hand(self.player2_hand)
        self.__battle()

    def __deal_hand(self, hand):
        for _ in range(5):
            hand.append(self.deck.deal_card())
        


    def __battle(self):
        player1_pile = []
        player2_pile = []
        player1_score = 0
        player2_score = 0
        ties = 0
        while len(self.player1_hand) > 0 or len(self.player2_hand) > 0:
            if len(self.player1_hand) == 0:
                random.shuffle(player1_pile)
                self.player1_hand = player1_pile.copy()
                player1_pile.clear()
            if len(self.player2_hand) == 0:
                random.shuffle(player2_pile)
                self.player2_hand = player2_pile.copy()
                player2_pile.clear()
            card1 = self.player1_hand.pop()
            card2 = self.player2_hand.pop()
            print(f"{card1} vs {card2}")
            if card1 > card2:
                player1_pile.append(card1)
                player1_pile.append(card2)
                player1_score += 1
                print(f"Player 1 wins with {card1}")
            elif card2 > card1:
                player2_pile.append(card1)
                player2_pile.append(card2)
                player2_score += 1
                print(f"Player 2 wins with {card2}")
            else:
                ties += 1
                print("Tie! Both players draw a card and play again")
        print("------------------------------------------")
        print("Game over!")
        print("------------------------------------------")
        print(f"Player 1: {player1_score}")
        print(f"Player 2: {player2_score}")
        print(f"Ties: {ties}")
        print("==========================================")


SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]

RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]


def index_of(lst, item):
    for i in range(len(lst)):
        if lst[i] == item:
            return i
    return None


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __cmp(self, other):
        self_suit_i = index_of(SUITS, self.suit)
        other_suit_i = index_of(SUITS, other.suit)
        self_rank_i = index_of(RANKS, self.rank)
        other_rank_i = index_of(RANKS, other.rank)
        if self_rank_i > other_rank_i:
            return "gt"
        if self_rank_i < other_rank_i:
            return "lt"
        if self_suit_i > other_suit_i:
            return "gt"
        if self_suit_i < other_suit_i:
            return "lt"
        return "eq"

    def __eq__(self, other):
        return self.__cmp(other) == "eq"

    def __gt__(self, other):
        return self.__cmp(other) == "gt"

    def __lt__(self, other):
        return self.__cmp(other) == "lt"

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class DeckOfCards:
    def __init__(self):
        self.__cards = []
        self.create_deck()

    def create_deck(self):
        for suit in SUITS:
            for rank in RANKS:
                self.__cards.append(Card(rank, suit))

    def shuffle_deck(self):
        random.shuffle(self.__cards)

    def deal_card(self):
        if len(self.__cards) == 0:
            return None
        return self.__cards.pop(0)


def test(seed):
    random.seed(seed)
    war = War()
    war.play()


def main():
    test(1)
    test(2)


main()
