from array import array

scores = array("i")

print("ITEM 1 - Create and Populate The Array")
print("")

count = int(input("How many scores do you want to enter? "))
print("")

# loop to get each score
for i in range(count):
    value = int(input("Enter a score: " + str(i + 1) + ": "))
    scores.append(value)

# displaying
print("Scores:", scores)
print("Number of scores:", len(scores))
print("")

print("ITEM 2 – Analyze and Manipulate the Array")
print("")

highest_score = scores[0]
lowest_score = scores[0]
total_score = 0
passed_count = 0
failed_count = 0

for s in scores:
    if s > highest_score:
        highest_score = s
    if s < lowest_score:
        lowest_score = s
    total_score += s

    if s >= 75:
        passed_count += 1
    else:
        failed_count += 1

average_score = total_score / len(scores)

# displaying the results
print("Highest Score:", highest_score)
print("Lowest Score:", lowest_score)
print("Total Score:", total_score)
print(f"Average Score: {average_score:.2f}")
print("Passed:", passed_count)
print("Failed:", failed_count)
print("")

print("ITEM 3 – Convert and Manipulate Using a List")
print("")

# converting array to list
scores_list = scores.tolist()
print("Array converted to List:")
print(scores_list)

# addition of a new score
new_score = int(input("Enter an additional score: "))
scores_list.append(new_score)
print("")

# score to remove
remove_score = int(input("Enter a score to remove: "))
print("")


# checking score
if remove_score in scores_list:
    scores_list.remove(remove_score)
    print(remove_score, "was removed.")
    print("")
else:
    print(remove_score, "was not found in the list.")
    print("")

# Display final list
print("Updated List:")
print(scores_list)
print("")

print("ITEM 4 – Use a Tuple and Set for Data Analysis")
print("")

print("Part A – Tuple")
scores_tuple = tuple(scores_list)
print("Tuple:")
print(scores_tuple)
print("First Score:", scores_tuple[0])
print("Last Score:", scores_tuple[-1])
print("Number of Scores: ", len(scores_tuple))
print("")

print("Part B – Set")
scores_set = set(scores_list)
print("Set of Unique Scores:")
print(scores_set)
print("Number of Unique Scores:", len(scores_set))
print("")

# asking for a score to check
search = int(input("Enter a score to search: "))
if search in scores_set:
    print(search, "already exists in the set")
    print("")
else:
    print(search, "does not exist in the set")
    print("")

print("ITEM 5 – Final Data Report")
print("")

print("========== FINAL SCORE REPORT ==========")
print("Original Array:")
print(scores)
print("Final List:")
print(scores_list)
print("Tuple:")
print(scores_tuple)
print("Unique Scores:")
print(scores_set)
print("")
print("Total Number of Scores:", len(scores_list))

# recalculating
final_total = 0
final_pass = 0
final_fail = 0

for s in scores_list:
    final_total += s
    if s >= 75:
        final_pass += 1
    else:
        final_fail += 1

print("Highest Score:", max(scores_list))
print("Lowest Score:", min(scores_list))
print(f"Average Score: {final_total / len(scores_list):.2f}")
print("Passing Scores:", final_pass)
print("Failing Scores:", final_fail)
print("")

print("========== SCORE CLASSIFICATION ==========")
for s in scores_list:
    if s >= 90:
        grade = "Excellent"
    elif s >= 80:
        grade = "Very Good"
    elif s >= 75:
        grade = "Passed"
    else:
        grade = "Failed"
    print(s, "-", grade)
