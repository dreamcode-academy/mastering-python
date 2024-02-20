data = [("Alice", [88, 92, 75]), ("Bob", [72, 85, 90]), ("Cara", [88, 92, 88])]

#Use a list comprehension to calculate the average score for each person.
averages = [(name, sum(scores)/len(scores)) for name, scores in data]
#print(averages)

#Create a set of unique scores from all students using an ensemble understanding.
unique_scores = {score for _, scores in data for score in scores}
#print(unique_scores)
#Use a dictionary comprehension to count the frequency of each score among all students.
score_frequency = {score:sum([scores.count(score) for _, scores in data]) for score in unique_scores}
print(score_frequency)