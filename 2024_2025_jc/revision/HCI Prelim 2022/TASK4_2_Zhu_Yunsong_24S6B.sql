SELECT s.Name, s.Gender, hr.Weight, hr.Height
FROM [Student] AS s
LEFT JOIN [StudentHealthRecord] AS hr
	ON s.StudentID = hr.StudentID
ORDER BY s.Gender ASC, s.Name DESC;