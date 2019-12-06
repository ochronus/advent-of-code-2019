def part1(pairs):
    total = 0
    # strategy: trace each node back to the common ancestor in the graph.
    # each step is a direct orbit, we just need to add them up.
    # each indirect orbit is a series of direct orbits, so we just need to add them up
    for space_object in pairs:
        while space_object != "COM":
            space_object = pairs[space_object]
            total += 1
    return(total)

def part2(pairs):
    start = pairs['YOU']
    end = pairs['SAN']
    
    # strategy: track back both to COM as the common ancestor in the graph
    
    path_of_start = [start]
    while path_of_start[-1] != "COM":
        path_of_start.append(pairs[path_of_start[-1]])      # just follow the graph edges

    path_of_end = [end]
    while path_of_end[-1] != "COM":
        path_of_end.append(pairs[path_of_end[-1]])

    # strategy: eliminate the common path to COM as the common ancestor which leaves us with
    #           the two sub-paths to the last common node in the graph
    while path_of_start[-1] == path_of_end[-1]:
        path_of_start.pop(-1)
        path_of_end.pop(-1)

    return(len(path_of_start) + len(path_of_end))


with open('../input.txt', 'r') as file:
    data = [l.strip().split(')') for l in file.readlines()]

pairs = {b:a for a, b in data}  # b orbits a

print(part1(pairs))
print(part2(pairs))

