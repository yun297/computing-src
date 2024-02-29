library(rvest) 
library(ggplot2)

getwd()
setwd("C:/Users/20248/OneDrive/Documents/School/Sch stuff/Infocumm")
temp <- read.csv("surface-air-temperature-monthly-mean.csv")
rainfall <-  read.csv("rainfall-monthly-total.csv")

weather <- merge(temp,rainfall)

weather$year <- substr(weather$month,1,4)
weather$month <- substr(weather$month,6,7)

weather$year <- as.numeric(weather$year)
weather$month <- as.numeric(weather$month)
head(weather)
yrTotalTemp <- NULL
yrTotalRain <- NULL
mnTotalTemp <- NULL
mnTotalRain <- NULL

# Part 1

for (i in unique(weather$month)) {
    mnTotalTemp <- append(mnTotalTemp, mean(weather[weather$month == i, 2]))
}
for (i in unique(weather$month)) {
    mnTotalRain <- append(mnTotalRain, mean(weather[weather$month == i, 3]))
}

plot(y = mnTotalTemp, x = 1:12, main = "Ave Temp / month", xlab = "Month", ylab = "Ave temp", type = "l")
plot(y = mnTotalRain, x = 1:12, main = "Ave Rainfall / month", xlab = "Month", ylab = "Ave Rainfall", type = "l")

# Part 2

for (i in unique(weather$year)) {
    yrTotalTemp <- append(yrTotalTemp, mean(weather[weather$year == i, 2]))
}
for (i in unique(weather$year)) {
    yrTotalRain <- append(yrTotalRain, mean(weather[weather$year == i, 3]))
}

plot(y = yrTotalTemp, x = 1982:2022, main = "Ave Temp / year", xlab = "Year", ylab = "Ave temp", type = "l")
plot(y = yrTotalRain, x = 1982:2022, main = "Ave Rainfall / year", xlab = "Year", ylab = "Ave Rainfall", type = "l")