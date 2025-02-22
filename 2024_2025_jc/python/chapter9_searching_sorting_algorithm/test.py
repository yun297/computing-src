with open("./A.txt", "r") as A_txt, open("./B.txt", "r") as B_txt:

C = []
record = {}

for line in A_txt:
  date_part, email = line[:10], line[10:].strip()
  day, month = int(date_part[:2]), int(date_part[3:5])
  
  record[email] = (day, month)
  C.append(line.strip())
  
for line in B_txt:
  date_part, email = line[:10], line[10:].strip()
  day, month = int(date_part[:2]), int(date_part[3:5])
  
  if email in record:
    existing_day, existing_month = record[email]
    
    if (month > existing_month) or (month == existing_month and day > existing_day):
      record[email] = (day, month)
      for i in range(len(C)):
        if C[i][10:] == email:
          C[i] == line.strip()
  else:
    C.append(line.strip())
    
print(record)
  
  
i = a = b = 0

# while a < len(A) and b < len(B):
#   if A[i] > B[i]:
#     C.append(A[i])
#     a += 1
#   elif A[i] < B[i]:
#     C.append(B[i])
#     b += 1
#   else if 