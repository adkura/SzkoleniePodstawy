import geom

print(geom.GiveGeomSeqElement(1, 2, 64))

a1=3
factory=2
maxindex=10

for i in range(1,maxindex):
    print(geom.GiveGeomSeqElement(a1, factory, i))

print('------------------------------------------------')
print('Factor is', geom.GiveFactorForGeomSeq(12,24))
print('------------------------------------------------')

print(geom.GiveSumOfNElementsGeomSeq(2, 3, 4))