
from sklearn import tree

clf = tree.DecisionTreeClassifier()

# CHALLENGE - create 3 more classifiers...
# 1
# 2
# 3

# [height, weight, shoe_size]
X = [[181, 80, 10], [177, 70, 9], [160, 60, 6], [154, 54, 5], [166, 65, 8],
     [190, 90, 13], [175, 64, 6],
     [177, 70, 6], [159, 55, 5], [171, 75, 8], [181, 85, 9]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']
     
#Take input from the user
height = int(input("Please enter your height (in cms) : "))
weight = int(input("Please enter your weight (in Kgs) : "))
shoe_size = int(input("Please enter your shoe size (UK): "))


# CHALLENGE - ...and train them on our data
clf = clf.fit(X, Y)

prediction = clf.predict([[height, weight, shoe_size]])

# CHALLENGE compare their reusults and print the best one!

print(prediction)
