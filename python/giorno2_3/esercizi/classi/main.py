class Country:
    def __init__(self, name):
        self.name = name
        self.regions = []
    def add_region(self, region):
        if isinstance(region, Region):
            self.regions.append(region)
        else:
            raise TypeError("Only Region can be added to a Country.")

    @property
    def pop(self):
        return sum(region.pop for region in self.regions)

    @property
    def most_populuous_city(self):
        most_populous = None
        max_population = 0

        for region in self.regions:
            for city in region.cities:
                if city.pop > max_population:
                    most_populous = city
                    max_population = city.pop

        return most_populous

class Region:
    def __init__(self, name):
        self.name = name
        self.cities = []

    def add_city(self, city):
        if isinstance(city, City):
            self.cities.append(city)
        else:
            raise TypeError("Only instances of City can be added to a Region.")

    @property
    def pop(self):
        return sum(city.pop for city in self.cities)


class City:
    """A city"""

    def __init__(self, name, pop):
        self.name = name
        self.pop = pop
