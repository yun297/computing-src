SELECT 
    s.Gender,
    COUNT(*) AS TotalStudents,
    AVG(hr.Weight) AS AverageWeight,
    AVG(hr.Height) AS AverageHeight
FROM [Student] AS s
LEFT JOIN [StudentHealthRecord] AS hr
    ON s.StudentID = hr.StudentID
GROUP BY s.Gender;
