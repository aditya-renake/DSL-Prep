table = [None] * 10

def insert(key):
    slot = key % 10

    while table[slot] is not None:
        slot = (slot + 1) % 10

    table[slot] = key

def search(key):
    for value in table:
        if value == key:
            return "Found"
    return "Not found"

def delete(key):
    for i in range(10):
        if table[i] == key:
            table[i] = None

insert(12)
insert(22)
insert(32)

print("Table:", table)
print("Search 22:", search(22))
delete(22)
print("After delete:", table)