cities=['mumbai','new york','paris']
countries=['india','usa','france']
z=zip(cities,countries)
print(z)
for a in z:
    print(a)

d={city:country for city,country in zip(cities,countries)}
print(d)