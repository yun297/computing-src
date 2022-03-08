#########################
### Introduction to R ###
#########################

# Treat R as a calculator
# Hint: Use Ctrl + R to run codes
# Hint: To check your command history (what you typed previously), Press the Up / Down button or Ctrl + Up.
123 + 456
123 / 456

# Construct: c() constructs a vector.
# <- or = assigns a value to a variable (named x in this case).
x <- c(1, 4, 9, 16)
x <- c(x, 25)

# Variable: You can use x whenever you want to know something about these numbers.
x
length(x)
sum(x)

# Indexing: You can also "call" specific values of the variable.
# E.g. If I want to find out the 2nd value of x :
x[2]

# Note: In R, indices start from 1 instead of 0 unlike most programming languages

# Indexing: What if we want to call multiple values in x?
x[c(3, 4, 5)]
3:5            # shortcut for c(3,4,5)
x[3:5]

# Manipulating Variables: What if we want to change x in some way?
x - 1
x - 1:5
x - mean(x)
sqrt(x)

# Comparisons: What if we want to compare x against some other value?
x > 10
x %% 2 == 0
# %% returns the remainder after division (by 2 in this case).
# ==  compares for equality.

# Comparisons always returns either TRUE or FALSE. Thus, they are useful for indexing.
x[x > 10]       # returns the values in x that are greater than 10
x[x %% 2 == 0]  # returns the even numbers in x


# AND/OR: What if we have more than one criteria?
(x > 10) & (x %% 2 == 0)
(x > 10) | (x %% 2 == 0)
# Use & for AND, | for OR
# This also works without the brackets

# Also try:
x[(x > 10) & (x %% 2 == 0)]
x[(x > 10) | (x %% 2 == 0)]



# Libraries: Libraries contain scripts to run more complex calculations.
# The "datasets" library is a dedicated library of example datasets.
library(datasets)
# If you can't load the library, you have to install it first.
# install.packages("datasets")

# Pick an interesting dataset. See complete list of datasets here:
library(help = "datasets")
# We pick the USArrests dataset (Violent Crime Rates by US State) and assign a short name to it for convenience.
d = USArrests

# Viewing the dataset
d           # View the full dataset
head(d)     # View just the first few rows of a dataset
?head       # For help on a function, type ? in front.
dim(d)      # Dimensions of a dataset
colnames(d) # Column names of a dataset
rownames(d) # Row names of a dataset

# Indexing datasets
d[1,]              # Returns first row
d[c(1, 3),]        # Returns first and third row
d[c(3, 1),]        # Returns third row first, then first row
d[,1]              # Returns first column
d["Alabama",]      # Returns row named Alabama
d[,"Murder"]       # Returns column named Murder
d$Murder           # Returns column named Murder (shortcut)
d$Murder >= 15     # Does the row has a value of "Murder" that is greater than or equal to 15?
d[d$Murder >= 15,] # Call the rows in which the values of "Murder" are greater than or equals to 15

#Sorting datasets
sort(d$Murder)       # Sort the "Murder" column only
order(d$Murder)      # Order the indices of the "Murder" column
d[order(d$Murder),]  # Sort entire dataset in increasing order of their "Murder" values

dord <- d[order(d$Assault, decreasing = TRUE),]

head(dord, 5)

# Summarising data
summary(d)           # Shows quantile and mean
summary(d$Murder)
