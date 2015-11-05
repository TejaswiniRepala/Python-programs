def num_of_cities():
  num = raw_input("Please enter the no of cities:")
  return num

def city_names():
  cities = []
  for i in range(0,int(num_of_cities())):
    city = raw_input("Please enter the city name that you would like to visit:")
    if not city in cities:
      cities.append(city)
  return cities

def first_sentence(cities):
  sentence = "You would like to visit "
  for i, city in enumerate(cities):
    if (i < len(cities)-1):
      sentence += "%s as city %d and " % (city, i+1)
    else:
      sentence += "%s as city %d ." % (city, i+1)
  return sentence

def new_sentence(sentence):
  items = sentence.split()
  for i, item in enumerate(items):
    if item.isdigit():
      items[i] = str(int(item) + 1)
  return " ".join(items)

def main():
  sentence1 = first_sentence(city_names())
  print "sentence1:", sentence1
  sentence2 = new_sentence(sentence1)
  print "sentence2:", sentence2
  
if __name__ == '__main__':
  main()
