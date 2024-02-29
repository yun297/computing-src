
# Reading Data from your computer
getwd() # Gets current working directory
setwd("C:/Users/kenne/OneDrive/Desktop/Data Science/BDS2022") # Sets new working directory
d <- read.csv('titanic.csv')

# View some information about the dataset
head(d)
str(d)

# Randomize the order of the dataset
set.seed(16)
d <- d[sample(nrow(d)),]

# Split the dataset into two
train <- d[1:514,]
test <- d[515:714,]

######################
### Decision Trees ###
######################

# We need the rpart library. Use install.packages("rpart") if needed.
install.packages("rpart")
library(rpart)
# Use ?rpart to know more about the library.

# Run the Decision Trees algorithm on the Train dataset
my_tree <- rpart(Survived ~ Pclass + Sex + Age + SibSp + Parch + Fare + Embarked,
                 data = train, method="class")

# The following functions plot the tree
plot(my_tree)
text(my_tree)

# Use your tree to make a prediction for each data point in the test dataset
tr_prediction <- predict(my_tree, test, type="class")

# Check accuracy of test dataset
# We compare tr_prediction against test$Survived (the actual answer) to see how many we got correct
tr_prediction == test$Survived                # TRUE means correct, FALSE means wrong
score = sum(tr_prediction == test$Survived)   # Sum everything up to tally your score
print(paste("Number of correct predictions =", score, "/ 200"))

######################
### Random Forests ###
######################

# We need the randomForest library. Use install.packages("randomForest") if needed.
install.packages("randomForest")
library(randomForest)
# Use ?randomForest to know more about the library.

# Run the randomForest algorithm on the Train dataset
my_forest <- randomForest(as.factor(Survived) ~ Pclass + Sex + Age + SibSp + Parch + Fare + Embarked, # Specify which variables we want
                          data = train,       # Specifies data
                          importance = TRUE,  # Allows us to view which variable is important
                          ntree = 10           # Number of trees in the forest. More tree takes longer to run, but gives a better forest.
                          )

# Use the following function to plot a chart that tells you the importance of the variables. 
# Most important variable will be at the top.
varImpPlot(my_forest)

# Use your forest to make a prediction for each data point in the test dataset
rf_prediction <- predict(my_forest, test)

# Check accuracy of test dataset
# We compare rf_prediction against test$Survived (the actual answer) to see how many we got correct
rf_prediction == test$Survived                # TRUE means correct, FALSE means wrong
score = sum(rf_prediction == test$Survived)   # Sum everything up to tally your score
print(paste("Number of correct predictions =", score, "/ 200"))

# Try the following to see whether your prediction accuracy improves:
# - Increase the number of trees (ntree) to 100 and 1000.
# - Select fewer variables to use

##########################
### Nearest Neighbours ###
##########################

# We need the class library. Use install.packages("class") if needed.
library(class)
# Use ?class to know more about the library.

# We do some data processing to remove columns that do not work well with Nearest Neighbours
train_knn <- train[,-c(1,3,8,10,11)]
test_knn <- test[,-c(1,3,8,10,11)]
train_knn$Sex <- sapply(as.character(train_knn$Sex), switch, 'male' = 0, 'female' = 1)
test_knn$Sex <- sapply(as.character(test_knn$Sex), switch, 'male' = 0, 'female' = 1)

# Scale the dataset. This is needed because knn uses Euclidean distance to calculate similiarity of data points.
# As such, variables with larger scales distort the calculations. Scaling makes all variables have mean 0 and standard deviation 1.
train_knn <- scale(train_knn)
test_knn <- scale(test_knn)

# Run the Nearest Neighbours algorithm on the dataset
knn_prediction <- knn(train = train_knn,    # Train dataset
                      test = test_knn,      # Test dataset
                      cl = train$Survived,  # True answers
                      k = 29)               # Number of nearest neighbours to consider

# Check accuracy of test dataset
# We compare knn_prediction against test$Survived (the actual answer) to see how many we got correct
knn_prediction == test$Survived                # TRUE means correct, FALSE means wrong
score = sum(knn_prediction == test$Survived)   # Sum everything up to tally your score
print(paste("Number of correct predictions =", score, "/ 200"))

# Try the following to see whether your prediction accuracy improves:
# - Changing the values of k (Use odd numbers)

####################
###   Plotting   ###
####################

# Since we know that Age and Sex are important variables, we can make a plot out of it.
# This is a histogram plot, where x-axis is Age, and y-axis is number of passengers in
# the age group. It is split into female and male, and color coded by whether they survived.
library(ggplot2)
ggplot(data = d, aes(Age, fill = factor(Survived))) + 
  geom_histogram() + 
  facet_grid(.~Sex) 
