class Country:
    """A country with a name, populaton, and area."""

    def __init__(self, name, pop, area):
        self.name = name
        self.population = pop
        self.area = area

    def is_larger(x, y):
        return x.area > y.area

    def population_density(x):
        return x.population / x.area

    def __str__(self):
        return (str(self.name) + ' has a population of ' +
                (str(self.population)) + ' and is ' + str(self.area) +
                ' square km.')

    def __repr__(self):
        return 'Country({0}, {1}, {2})'.format(self.name, self.population,
                                               self.area)
