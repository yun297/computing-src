drug <- NULL
for (i in 1:length(records$Athlete)){
  if (records$Athlete[i] == "Ben Johnson" |
      records$Athlete[i] == "Tim Montgomery" |
      records$Athlete[i] == "Justin Gatlin" ){
    drug <- c(drug, i)
  }
}

records_clean <- records[-drug,] #Removes records

# Alternative, faster way
disqualified <- c("Ben Johnson", "Tim Montgomery", "Justin Gatlin")
drug <- which(records$Athlete %in% disqualified)
records_clean <- records_clean <- records[-drug,]


qplot(x = records_clean$Date, y = records_clean$Time, 
      main = "100m Sprint World Records Progression", 
      xlab = "Year", ylab = "100m Sprint Times", 
      geom = c("point", "line")
)
