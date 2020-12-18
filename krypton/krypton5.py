# tries different key lenghts and print their supposed letter frequencies
# after running this try to examine the result and find the one that's most similar to the english letters distribution diagram, then use the right length in the script from the previous level 

files = ["/krypton/krypton5/found1", "/krypton/krypton5/found2", "/krypton/krypton5/found3", "/krypton/krypton5/krypton6"]

for num in range(2, 20):
    occurrences = {}
    for f in files:
        for line in open(f, "r"):
            chars = (c for n, c in enumerate(line) if n % num == 0 and c != " ")
            for char in chars:
                cnt = occurrences[char] if char in occurrences else 0
                occurrences[char] = cnt + 1

        print("Occurrences for try " + str(num))
        for el in sorted(occurrences, key=lambda el: occurrences[el], reverse=True):
            print(el + ": " + str(occurrences[el]))
