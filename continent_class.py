from country_class import Country


class Continent:
    """A continent."""

    def __init__(self, name, countries):
        self.name = name
        self.countries = countries

    # Continent('NA', [Country('USA', 1, 2)])

    def total_population(self):
        ...
