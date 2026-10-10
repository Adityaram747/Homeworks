quiz_scores = [45, 78, 92, 60, 85, 99, 73, 50]

print("Original Quiz Scores:", quiz_scores)
print("-" * 45)

def get_score_by_index(scores, index):
    return scores[index]


print("\n1. Direct Access O(1):")
print(f"Score at index 2 is: {get_score_by_index(quiz_scores, 2)}")


def search_score(scores, target):
    steps = 0
    for i in range(len(scores)):
        steps += 1
        if scores[i] == target:
            return f"Found {target}! Total steps taken: {steps}"
    return f"{target} not found. Total steps: {steps}"


print("\n2. Linear Search O(N):")
print(search_score(quiz_scores, 85)) 


def compare_all_pairs(scores):
    steps = 0
    for i in range(len(scores)):
        for j in range(len(scores)):
            steps += 1
    return f"Total comparisons made for {len(scores)} students: {steps}"


print("\n3. Pair Comparison O(N^2):")
print(compare_all_pairs(quiz_scores))