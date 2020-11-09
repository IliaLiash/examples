class Movie:
    def __init__(self, title, year, director):
        self.title = title
        self.year = year
        self.director = director


# objects of the class Movie
titanic = Movie("Титаник", 1997, "Джеймс Кэмерон")
star_wars = Movie("Звездные войны", 1977, "Джордж Лукас")
fight_club = Movie("Бойцовский клуб", 1999, "Дэвид Финчер")

# don't delete this code
# it is here to check your results
print(titanic.title)
print(star_wars.year)
print(fight_club.director)