class Movie():

    def __init__(self, name, year, category):
        self.name = name
        self.year = year
        self.category = category
    
    def __str__(self):
        return "{} - {}, launched on {}".format(self.name, self.category, self.year)
