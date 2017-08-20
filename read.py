with open("csv/Kanji.csv", 'r', encoding='utf-8') as inFile:
	for line in inFile:
		if line.count(',') != 3:
			continue
		field1 = line.find(',')
		field2 = line.find(',', field1 + 1)
		field3 = line.find(',', field2 + 1)
		question = line[:field1]
		answer   = line[field1 + 1:field2]
		comment  = line[field2 + 1:field3]
		tag      = line[field3 + 1:]
