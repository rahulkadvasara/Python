dict={}

with open("nyc_weather.csv","r") as f:
    for line in f:
        tokens = line.split(',')
        day=tokens[0]
        try:
            temperature = int(tokens[1])
            dict[day]=temperature
        except:
            print("Invalid temperature.Ignore the row")

print(dict['Jan 6'])
