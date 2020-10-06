def migratory_birds():
    n = int(input())
    birds = list(map(int, input().split()))
    bird_sightings = {x: 0 for x in set(birds)}
    all_keys = list(bird_sightings.keys())
    for i in range(len(all_keys)):
        bird_sightings[all_keys[i]] = birds.count(all_keys[i])

    duplicate_values_dict = {}
    for key,value in bird_sightings.items():
        duplicate_values_dict.setdefault(value, set()).add(key)
    print(bird_sightings)


migratory_birds()