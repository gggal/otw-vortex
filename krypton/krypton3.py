#print all letters and their frequencies

files = ["/krypton/krypton3/found1", "/krypton/krypton3/found2", "/krypton/krypton3/found3", "/krypton/krypton3/krypton4"]

occurrences  = {}
for f in files:
    for line in open(f, "r"):
        for char in line:
            cnt = occurrences[char] if char in occurrences else 0
            occurrences[char] = cnt + 1

for el in sorted(occurrences, key=lambda el: occurrences[el], reverse=True):
    print(el + ": " + str(occurrences[el]))
