# aoc2022 day3

total_priority = 0
with open('input.txt', 'r') as file:
    for line in file:
        items_list = line.strip()
        n = len(items_list) //2
        comp_1, comp_2 = items_list[:n], items_list[n:]

        # common_item = list(set(comp_1).intersection(comp_2))[0]
        common_item = [elem for elem in comp_1 if elem in comp_2][0]

        priority = (ord(common_item) - 96) if common_item.islower() else (ord(common_item) - 38)
        total_priority += priority
print(total_priority)
