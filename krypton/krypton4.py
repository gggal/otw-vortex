#print all letters and their frequencies

files = ["/krypton/krypton4/found1", "/krypton/krypton4/found2", "/krypton/krypton4/krypton5"]

occurrences = [{}, {}, {}, {}, {}, {}]
for f in files:
    for line in open(f, "r"):
        idx = 0
        for char in line:
            if char == ' ':
                continue
            cnt = occurrences[idx][char] if char in occurrences[idx] else 0
            occurrences[idx][char] = cnt + 1
            idx = idx + 1 if idx != 5 else 0
for idx, occur_map in enumerate(occurrences):
    print("Occurrences for index " + str(idx))
    for el in sorted(occur_map, key=lambda el: occur_map[el], reverse=True):
        print(el + ": " + str(occur_map[el]))
