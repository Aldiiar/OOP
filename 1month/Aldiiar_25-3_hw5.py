data = ("O!", "Megacom", "0705", "Beeline", "0550", "0770", "Katel", "0510", "Fonex", "0543")
data1 = list(data)

designations = []
codes = []


for i in data1:
      if i.isdigit():
            codes.append(i)
      else:
            designations.append(i)


operators = {}

i = 0
while i != len(designations):
    operators[designations[i]] = set([codes[i]])
    i += 1


operators.pop('Katel')
operators.pop('Fonex')


operators['O!'] = operators['O!'].union(['0700', '0500'])
operators['Megacom'] = operators['Megacom'].union(['0999', '0555'])
operators['Beeline'] = operators['Beeline'].union(['0222', '0777'])

for keys, values in operators.items():
    print(keys, '-', values)

