class Allergies:

    def __init__(self, score):
        self.allergens = []

        if score & 0b1:
            self.allergens.append("eggs")
        if score & 0b10:
            self.allergens.append("peanuts")
        if score & 0b100:
            self.allergens.append("shellfish")
        if score & 0b1000:
            self.allergens.append("strawberries")
        if score & 0b10000:
            self.allergens.append("tomatoes")
        if score & 0b100000:
            self.allergens.append("chocolate")
        if score & 0b1000000:
            self.allergens.append("pollen")
        if score & 0b10000000:
            self.allergens.append("cats")

    def allergic_to(self, item):
        return (item in self.allergens)

    @property
    def lst(self):
        return self.allergens
