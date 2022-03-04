class Movie:
    def __init__(self,title,hero,heroin):
        self.title = title
        self.hero = hero
        self.heroin = heroin

    def info(self):
        print("Movie Name:",self.title)
        print("Hero Name:",self.hero)
        print("Heroin Name:",self.heroin)

m = Movie('Aarya-2','Allu Arjun','Kajal')
m.info()
m1 = Movie('INDRA','MEGA STAR Chiranjeevi','Sonalibindray')
m1.info()
m2 = Movie('Tagore','MEGA STAR Chiranjeevi','Shriya saran')
m2.info()

'''list_of_movies = []
while True:
    title = input("Enter movie name:")
    hero = input("Enter hero name:")
    heroin = input("Enter heroin name:")
     m = Movie(title,hero,heroin)
    list_of_movies.append(m)
    print("Movie added to the list sucessfully")
    option = input('DO you want to add one more movie [Yes/No]:')
    if option.lower()=='No':
        break
print("All Movies Information")
print('#'*40)
for movie in list_of_movies:
    movie.info()'''