from nomenklatura import Dataset, NomenklaturaException

dataset = Dataset('iso-countries')
print [dataset.label]

#print list(dataset.entities())

#cyp = dataset.entity_by_name('cyprus') 
#print cyp.__data__
#cyp.reviewed = False
#print cyp.__data__
#cyp.update()

e = dataset.entity_by_name('christmas island') 
print repr(e)
print repr(e.dereference())