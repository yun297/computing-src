#########################
### Data Preparation  ###
#########################

# Combine Data
d1 = cbind(rownames(d), d[,1:2]) # Use cbind to combine columns
d2 = cbind(rownames(d), d[,3:4])

# Change Names
rownames(d)
rownames(d) <- NULL
colnames(d1)[1] <- "State"
colnames(d2)[1] <- "State"

# Randomize
set.seed(1)  # Fix a seed for reproducibility
rand <- sample(nrow(d2))
rand
d2 <- d2[rand,]
d2half <- d2[rand[1:25], ]

# Merge
merge(d1, d2) # The merge function uses the common column to merge two datasets.
merge(d1, d2half, all.x = FALSE)

# Recoding Data / Create new columns
d$MurderCat[d$Murder >= 10] <- "Slaughter House"
d$MurderCat[d$Murder < 10]  <- "Animal Shelter"
head(d)

# Reading Data from your computer
getwd() # Gets current working directory
setwd("D:/School/Computing Module/computing-private/2022_sec3/data_science_sabbatical") # Sets new working directory

# Download data from https://github.com/hxchua/datakueh/blob/master/datasets/mrtsg.csv
mrt <- read.csv("mrtsg.csv") # Reads data

### QUIZ TIME ###
mrt[order(mrt$STN_NAME),]
mrt$STN_NAME[duplicated(mrt$STN_NAME)]



# Reading Data from the Internet
library(rvest) # May need to install a new library using install.packages('rvest')

# The package has a function that reads the html
page <- read_html("https://en.wikipedia.org/wiki/Men%27s_100_metres_world_record_progression") 

page_tables <- html_table(page, fill = T) # The package also has a function that extracts tables from html
records <- page_tables[[5]] # Let's extract the 5th table
head(records)               #View dataset
str(records)                #View information about dataset

# Mini Quiz
records$Date <- as.Date(records$Date, format = " ") # key in the correct date format