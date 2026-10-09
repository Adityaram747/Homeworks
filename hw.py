n = 4

guess = input("Predict: how many total points for n = 4 laps? ")

points = list(range(1, n + 1))
total_points = sum(points)

print(f"Your guess: {guess}  Laps list: {points}  Total points: {total_points}")


input("\nPredict: what happens to the step count as n grows? Press Enter")

print("/n" + "=" * 70)
print(f"{'n':<8}  {'Formula Steps':<16}  {'Single Loop Steps':<20}  {'Nested Loop Steps':<20}")
print("=" * 70)

for size in [4, 10, 100, 1000]:
    formula_steps = 1
    
    single_steps = size
    
    nested_steps = size * (size + 1) // 2
    
    print(f"n = {size:<5}  {formula_steps:<16}  {single_steps:<20}  {nested_steps:<20}")

print("=" * 70)


def method_formula(n):
    return n * (n + 1) // 2

def method_single_loop(n):
    total = 0
    for lap in range(1, n + 1):
        total += lap
    return total

def method_nested_loop(n):
    total = 0
    for lap in range(1, n + 1):
        for point in range(1, lap + 1):
            total += 1
    return total