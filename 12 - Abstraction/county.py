"""
Tanner Babcock
November 12, 2019
Module 12, topic 1: Gathering Data using Classes
"""
class County:
    def __init__(self, per_capita_income, median_household_income, median_family_income, population, num_households):
        self.per_capita_income = per_capita_income
        self.median_household_income = median_household_income
        self.median_family_income = median_family_income
        self.population = population
        self.num_households = num_households

    def population_per_household(self):
        return int(self.population.replace(',','')) / int(self.num_households.replace(',',''))

