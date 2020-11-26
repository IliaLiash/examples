class Hotel:
        
        def __init__(self, name, stars, price):
                self.name = name
                self.price = price
                self.stars = stars
                
hotels = []

Atlantic = Hotel('Atlantic Castle Hotel', 3, 45000)
hotels.append(Atlantic)
Oriental = Hotel('Oriental Tide Hotel & Spa', 5, 92000)
hotels.append(Oriental)
Bronze = Hotel('Bronze Mansion Resort', 4, 84000)
hotels.append(Bronze)
Parallel = Hotel('Parallel Harbor Hotel', 4, 80000)
hotels.append(Parallel)
Obsidian = Hotel('Obsidian Vertex Hotel', 5, 120000)
hotels.append(Obsidian)
Noble = Hotel('Noble Memorial Hotel', 4, 59000)
hotels.append(Noble)
Mirth = Hotel('Mirth Hotel', 4, 64000)
hotels.append(Mirth)
Felicity = Hotel('Felicity Motel', 3, 29000)
hotels.append(Felicity)
Renaissance = Hotel('Renaissance Hotel', 3, 49000)
hotels.append(Renaissance)
Rainbow = Hotel('Rainbow Hotel & Spa', 5, 154000)
hotels.append(Rainbow)
   
input_sum = int(input())
count = 0

hotels = sorted(hotels, key=lambda x:x.price)[::-1]

for element in hotels:
        if element.price <= input_sum:
                print(element.name, element.stars, element.price)
                count += 1
                if count == 3:
                        break
        else:
                continue

if count == 0:
        print('No such options')
        
