file1 = open('felfedezesek.csv','r',encoding='ISO-8859-1')
Felfedez = list(file1)
Kemia = []
for i in Felfedez:
    Kemia.append(i.rstrip().split(';'))
length = len(Kemia)

#3.feladat
print('3.feladat: Elemek szama:',length-1)

#4.feladat
Okor_szam = 0
for i in range(1,length):
    if Kemia[i][0] == 'Ókor':
        Okor_szam += 1
    else:
        break
print('4.fekladat: Felfedezesek szama az okorban:',Okor_szam)

#5.feladat
while True:
    temp = input('5.feladat: Kerek egy vegyjelet:')
    if temp.isalpha():
        if 1 <= len(temp) <= 2:
            break
    else:
        continue
    
#6.feladat
temp = temp.title()
flag = 0
for i in Kemia:
    if temp == i[2]:
        owo = i
        flag = 1
        break
if flag:
    print('6.feladat:Kereses')
    print('\tAz elem vegyjele:',temp)
    print('\tAz elem neve:',owo[1])
    print('\tRendszam:',owo[3])
    print('\tFelfedezes eve:',owo[0])
    print('\tFelfedezo:',owo[4])
else:
    print('6.feladat:Kereses')
    print('\tNincs ilyen elem az adatforrasban')

#7.feladat

maxev = 0
NoOkor = 0
for i in range(1,length):
    if Kemia[i][0] != 'Ókor':
        NoOkor = i
        break
for i in range(NoOkor,length-1):
    if int(Kemia[i+1][0])-int(Kemia[i][0]) > maxev:
        maxev = int(Kemia[i+1][0])-int(Kemia[i][0])
print('7.feladat:',maxev,'ev volt a leghosszab idoszak ket elem felfedezes kozott.')
     
#8.feladat
evszamok = []
for i in range(NoOkor,length):
    evszamok.append(Kemia[i][0]) 
evszam = sorted((set(evszamok)))
print('8.feladat:Statisztika')
for i in evszam:
    db = evszamok.count(i)
    if db > 3:
        print(i+':',db,'db')

    
    
    
    
    