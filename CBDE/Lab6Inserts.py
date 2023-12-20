import random
import string


def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase + string.ascii_uppercase + string.digits
    length = random.randint(1, length)
    result_str = ''
    return result_str

#FUNCIONA pero me falta comprobar que los fixed sean fixed texts
#Y tal vez comprobar que las dates no se hagan overlap
#Ahora falta mirar como hacer los inserts


def enviaParts(v): 
    for parte in v: 
        print("xd")
    part = []


def randomDate(): 
    letters = string.digits
    result_str = str(random.randint(1,30))
    result_str = result_str + "/"
    result_str = result_str + str(random.randint(0,12))
    result_str = result_str + "/"
    result_str = result_str + str(random.randint(22, 99))
    return result_str

def getRandomPK(v, i): 
    a = random.randint(0, v.__len__()-1)
    return v[a][i]

part = []
for i in range(200000): 
    #part.append((i+1, get_random_string(55), get_random_string(25), get_random_string(10), get_random_string(25), random.randint(1,1000), get_random_string(10), random.uniform(1.0,1000.9), get_random_string(25)))
    j = i+1
    session.run("CREATE (part" + j + ": Part{p_partkey: " + j + ", p_name: ' "+get_random_string(55)+
                    "', p_mfgr: '" + get_random_string(25) + "', p_brand: '" + get_random_string(10) + "', p_type: '"+get_random_string(25)+
                    "', p_size: " + random.randint(1,1000) + ", p_container: 'Containter" + get_random_string(10) + "'"
                    ", p_retailprice: " + random.uniform(1.0,1000.9) +
                    ", p_comment: '"+get_random_string(25)+"'})")
print("part creada")

region = []
region.append((1, "NORTH", "NOCOMMENT"))
region.append((2, "CENTER", "NOCOMMENT"))
region.append((3, "SOUTH", "NOCOMMENT"))
    


nation = []
nation.append((1, "SWEDEN", 1, get_random_string(50)))
nation.append((2, "FRANCE", 2, get_random_string(50)))
nation.append((3, "GERMANY", 2,get_random_string(50)))
nation.append((4, "SPAIN", 2, get_random_string(50)))
nation.append((5, "PORTUGAL", 3, get_random_string(50)))
    

customer = []
for i in range(150000): 
    customer.append((i+1, get_random_string(25), get_random_string(40), getRandomPK(nation, 0), get_random_string(15), random.randint(0,10000), get_random_string(10), get_random_string(117)))

supplier = []
for i in range(10000): 
    supplier.append((i+1, get_random_string(25), get_random_string(40), getRandomPK(nation, 0), get_random_string(15), random.randint(0,10000), get_random_string(101)))

partsupp = []
for j in range(supplier.__len__()):
        partsupp.append((j+random.randint(0,100), j+1, random.randint(0,10), random.uniform(1.0, 100.0), get_random_string(199)))



orders = []
for i in range(1500000):
    orders.append((i+1, random.randint(0, customer.__len__(),), get_random_string(1), random.uniform(1.0, 10000.0), randomDate(), get_random_string(15), get_random_string(15), random.randint(0, 10), get_random_string(79)))
print("orders creadas")

lineItem = []
for i in range(100000): 
    j = random.randint(0, partsupp.__len__()-1)
    lineItem.append((random.randint(0, orders.__len__()), partsupp[j][0], partsupp[j][1], random.randint(0, 100), random.uniform(1.0, 100.0), random.uniform(1.0, 100.0), random.uniform(0.0, 75.0), random.uniform(0.0, 25.0), get_random_string(1), get_random_string(1), randomDate(), randomDate(), randomDate(), get_random_string(25), get_random_string(10), get_random_string(44)))
print("lineitem creada")


print("tablas acabadas de crear")
a = part.__len__() + nation.__len__() + region.__len__() + customer.__len__() + partsupp.__len__() + lineItem.__len__() + orders.__len__()
print(a)


