import json 

country_list = []

for i in range(5):
    country_name = input("Enter a country: ")
    country_pop = int(input("Enter a country population (Millions): "))

    country_dict = {}
    country_dict[country_name] = country_pop

    country_list.append(country_dict)

outfile = open("countries.json", "w")

json.dump(country_list, outfile, indent=4)

outfile.close()
