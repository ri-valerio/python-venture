eighties = ['', 'duran duran', 'B-52s', 'muse']
newwave = ['flock of seagulls', 'postal service']

remember = eighties[1]
print(eighties, remember)
eighties[1] = 'culture club'
print(eighties, remember)
band = newwave[0]
print(eighties, remember, band)
eighties[3] = band
print(eighties, remember, band)
eighties[0] = eighties[2]
print(eighties, remember, band)
eighties[2] = remember
print(eighties, remember, band)
print(eighties)
print(eighties[-1])
print(eighties[-2])
del eighties[0]
print(eighties)

more_eighties_stuff = ['Pink Floyd', 'U2', 'Buda']

# this extends the existing list without creating a new one
eighties.extend(more_eighties_stuff)
print(eighties)

# this creates a new list with the items in both lists
eighties = eighties + ["another band", "and another one"]
print(eighties)

eighties.insert(1, "Heeeeey")
print(eighties)
print(len(eighties))
