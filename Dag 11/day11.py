from aoc import read_input
from collections import Counter

# input
stones = map(int,read_input("inputdag11")[0].split())

# part 1
def convert_stone(stone):
    str_stone = str(stone)
    len_stone = len(str_stone)
    if stone == 0:
        return (1,)
    elif len_stone%2 == 0:
        return (int(str_stone[:len_stone//2]),int(str_stone[len_stone//2:]))
    else:
        return (stone*2024,)
    
for _ in range(25):
  stones = list(sum((convert_stone(stone) for stone in stones), ()))

print(len(stones))

# part 2
count_stones = Counter(stones)
for _ in range(50):
    for stone,amount in list(count_stones.items()):
        count_stones[stone] -= amount
        for new_stone in convert_stone(stone):
            count_stones[new_stone] += amount
    
print(sum(v for v in count_stones.values()))