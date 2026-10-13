routes = [
    (2, "A", "B"),
    (5, "A", "C"),
    (1, "B", "C"),
    (4, "B", "D"),
    (3, "C", "D")
]

routes.sort()
chosen = []
total_time = 0

for time, start, end in routes:
    # Add a route if it connects two different groups
    start_group = [r[0] for r in chosen if r[1] == start or r[2] == start]
    end_group = [r[0] for r in chosen if r[1] == end or r[2] == end]

    if not start_group or not end_group or start_group[0] != end_group[0]:
        chosen.append((time, start, end))
        total_time += time

print("Chosen routes:", chosen)
print("Total time:", total_time)