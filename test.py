from nomenklatura import Dataset, NomenklaturaException

dataset = Dataset('iso-countries')
print [dataset.label]

#print list(dataset.entities())
#print repr(dataset.entity_by_name('cyprus'))

print repr(dataset.create_entity('Taka-tuka-land'))