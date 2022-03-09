
# For this lab, we will use the dataset mtcars
d <- mtcars

# Understand your dataset
?mtcars
head(d)
str(d)

# We are going to start with single-variable regression
# x = am (Whether the car is automatic or manual)
# y = mpg (Miles per gallon, which represents the fuel efficiency of the car)

fit <- lm(mpg ~ am, data = d)
summary(fit)

# Now let's try adding a few more variables
# x1 = am (Whether the car is automatic or manual)
# x2 = wt (Weight of car)
# x3 = hp (Horsepower of car)
# y = mpg (Miles per gallon, which represents the fuel efficiency of the car)

fit2 <- lm(mpg ~ am + wt + hp, data = d)
summary(fit2)

plot(y = d$mpg, x = d$hp, pch = 19)
fit3 <- lm(mpg ~ hp, data = d)
fit3$coefficients
abline(a = fit3$coefficients[1], b = fit3$coefficients[2], col = "red")  #Adds a line to your plot. It takes two arguments.
# Use ?abline to find out what it does

#How to get best-fit line in ggplot
library(ggplot2)
qplot(y = d$mpg, x = d$hp) +
  geom_smooth(method = "lm", se = FALSE)

