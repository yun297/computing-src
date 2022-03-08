#########################
###       Plots       ###
#########################

# Let's plot the data which we collected from Wikipedia earlier
plot(x = records$Date, y = records$Time, 
     main = "100m Sprint World Records Progression", 
     xlab = "Year", ylab = "100m Sprint Times"
)

# R also has libraries that help make better plots
library(ggplot2) # May need to install a new library using install.packages('ggplot2')
qplot(x = records$Date, y = records$Time, 
      main = "100m Sprint World Records Progression", 
      xlab = "Year", ylab = "100m Sprint Times"
)

# Line and Point plot
qplot(x = records$Date, y = records$Time, 
      main = "100m Sprint World Records Progression", 
      xlab = "Year", ylab = "100m Sprint Times", 
      geom = c("point", "line")
)


#########################
###     IF / FOR      ###
#########################

x <- c(1, 4, 9, 16, 25)

# Guess what happens?
if (sum(x) > 50){
  x[1] <- x[1] + 1
} else {
  x[2] <- x[2] + 1
}
x

# Guess what happens?
for (i in 1:length(x)){
  x[i] <- x[i] * 2
  print(i)
  print(x)
}


# Quiz starter code (REPLACE ## WITH YOUR CODE)
drug <- NULL
for (i in 1:length( ## )){
  if ( ## ){
    drug <- c(drug, ## )
              }
}

records_clean <- records[-drug,] #Removes records
