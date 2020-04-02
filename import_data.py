import csv

# import the relevant model
from app.models import Creature

for filename in ["bugs.csv", "fish.csv"]:
  print ("* Opening " + filename)
  with open(filename, encoding='utf-8') as csvfile:
    print ("- Opened " + filename)
    reader = csv.reader(csvfile)
    print ("- Created reader object")
    for line in reader:
      print ("-- Attempting to parse " + line[0])
      _, c = Creature.objects.get_or_create(
        name=line[0],
        #seasonality=line[1], # Calculated during save
        location=line[2],
        time=line[3],
        price=line[4],
        creature_type=line[5],
        january=(True if line[6] == 'Y' else False),
        february=(True if line[7] == 'Y' else False),
        march=(True if line[8] == 'Y' else False),
        april=(True if line[9] == 'Y' else False),
        may=(True if line[10] == 'Y' else False),
        june=(True if line[11] == 'Y' else False),
        july=(True if line[12] == 'Y' else False),
        august=(True if line[13] == 'Y' else False),
        september=(True if line[14] == 'Y' else False),
        october=(True if line[15] == 'Y' else False),
        november=(True if line[16] == 'Y' else False),
        december=(True if line[17] == 'Y' else False)
      )
      print ("Imported: " + line[0])
