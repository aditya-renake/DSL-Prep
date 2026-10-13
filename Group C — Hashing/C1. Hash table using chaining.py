table = [[] for i in range(10)]

def insert(key, value):
    slot = key % 10
    table[slot].append([key, value])

def search(key):
    slot = key % 10
    for pair in table[slot]:
        if pair[0] == key:
            return pair[1]
    return "Not found"

def delete(key):
    slot = key % 10
    for pair in table[slot]:
        if pair[0] == key:
            table[slot].remove(pair)
            return

insert(12, "Apple")
insert(22, "Banana")

print("Search 22:", search(22))
delete(12)
print("Table:", table)