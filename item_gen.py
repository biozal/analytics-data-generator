# Python item generator based on silly rules
# Author:  Aaron LaBeau
# Date:  06/27/2022
#
# DEPENDENCIES:
# pip3 install -U jsonpickle 
#
# item schema
#	{
#		"itemId": "",
#		"name": "",
#		"price": "",
#		"data": ""
#	}

import json
import random
import uuid
import jsonpickle

from decimal import Decimal

#open seed file
with open('item_data_seed.json') as json_file:

	#define beer class to use for serialization
	class BeerItem:
		def __init__(self, name, description):
			self.itemId = str(uuid.uuid4()) 
			self.name = name
			self.price = round(random.uniform(4.00, 25.00), 2)
			self.description = description
			self.documentType = "item"
		def printItem(self):
			print (self.name + " " + str(self.price.quantize(Decimal('0.01'))) + " " + str(self.itemId) + " " + self.description)

	#set encoding options to allow for unicode characters
	jsonpickle.set_preferred_backend('json')
	jsonpickle.set_encoder_options('json', ensure_ascii=False)

	#start by loading the file into a dictionary
	data = json.load(json_file)

	#how many random items to create
	howManyItems = 100001

	#flavors to put with name
	keyFlavors = "flavors"
	keyHerbs = "herbs"
	keySpices = "spices"

	#beer name
	keyPrefix = "prefix"
	keyName = "name"
	keySuffix = "suffix"
	beerName = []
	beerItems = []

	for index in range(howManyItems):
		isRepeat = True 
		while isRepeat == True :
			flavor = ""
			#business rule is we want to pick flavors instead of herb or spice most of the time
			whichFlavor = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
			if whichFlavor <= 6:
				flavor = random.choice(data[keyFlavors])
			elif whichFlavor == 7 or whichFlavor == 8:
				flavor = random.choice(data[keyHerbs])
			else :
				flavor = random.choice(data[keySpices])

			prefix = random.choice(data[keyPrefix])	
			name = random.choice (data[keyName])	
			suffix = random.choice(data[keySuffix])
			genItemName = flavor + " " + name + " " + suffix
			genItemDescription = prefix + " " + suffix + " with " + flavor + " flavors" 
			if genItemName not in beerName:
				beerName.append(genItemName)
				beerItems.append(BeerItem(genItemName, genItemDescription))
				isRepeat = False

	#serialize to json
	json_objects = jsonpickle.encode(beerItems, unpicklable=False) 

	#writing items to disk
	with open("beer_items.json", "w") as outfile:
		outfile.write(json_objects)

