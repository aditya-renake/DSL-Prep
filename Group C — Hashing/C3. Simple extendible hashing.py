buckets = [[], []]
limit = 2

def insert(key):
    global buckets

    slot = key % len(buckets)

    if len(buckets[slot]) == limit:
        # Make twice as many buckets
        old_keys = []
        for bucket in buckets:
            old_keys += bucket

        buckets = [[] for i in range(len(buckets) * 2)]

        # Put old keys into the new buckets
        for old_key in old_keys:
            new_slot = old_key % len(buckets)
            buckets[new_slot].append(old_key)

        slot = key % len(buckets)

    buckets[slot].append(key)

def search(key):
    slot = key % len(buckets)
    return key in buckets[slot]

def delete(key):
    slot = key % len(buckets)
    if key in buckets[slot]:
        buckets[slot].remove(key)

insert(1)
insert(3)
insert(5)

print("Buckets:", buckets)
print("Search 5:", search(5))
delete(3)
print("After delete:", buckets)