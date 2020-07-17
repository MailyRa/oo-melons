"""Classes for melon orders."""

import random 
import datetime

class AbstractMelonOrder():
    """An abstract base class that other Melon Orders inherit from."""

    def __init__(self, species, qty, order_type, tax):

        self.species = species
        self.qty = qty
        self.order_type = order_type
        self.tax = tax
        self.shipped = False


    def base_price(self):
    
        base_price = random.randit(5,9)  
        return base_price 

        #datetime.datetime.now() to get current time 
        current_time = datetime.datetime.now()

        if current_time.hour >= 8 and current_time.hour <= 11 and current_time.weekday() <5:
            base_price += 4

        #https://www.geeksforgeeks.org/python-now-function/ 
        return base_price

    
    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5

        if self.species == "Christmas melons":

            base_price = base_price * 1.5

        total = (1 + self.tax) * self.qty * base_price

        if self.order_type == "international" and self.qty < 10:
            total += 3 

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

class GovernmentMelonOrder(AbstractMelonOrder):
 
    def __init__(self, species, qty):
        super().__init__(species, qty, 'government', 0.0)
        
        self.passed_inspection = False 

    def mark_inspection(self, passed):

        self.passed_inspection = passed 


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    def __init__(self, species, qty):
        super().__init__(species, qty, 'domestic', 0.08)



class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        super().__init__(species, qty, "international", 0.17)


    def get_country_code(self):
        """Return the country code."""

        return self.country_code

order0 = InternationalMelonOrder("watermelon", 6, "AUS")
order1 = DomesticMelonOrder("cantaloupe", 8)
order2 = GovernmentMelonOrder("watermelon", 6,)

print(order2.get_total())
