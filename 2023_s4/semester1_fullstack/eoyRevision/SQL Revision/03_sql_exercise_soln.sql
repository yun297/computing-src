SELECT Name, Class, IndexNo, Gender
FROM Student
WHERE Class="4A"
ORDER BY IndexNo DESC


SELECT Name, Class, IndexNo, Gender
FROM Student
INNER JOIN SCR USING (MatricNo)
INNER JOIN ClassGroup USING (ClassGroupID)
WHERE ClassGroup.ClassGroupName = 'Comp_4AB'

INSERT INTO Student
(MatricNo,Name,Class,IndexNo,Gender)
VALUES
("HS-2015-108", "Xiao Ming", "4A", "15", "M")

INSERT INTO SCR
(MatricNo,ClassGroupID)
VALUES
("HS-2015-108", "5")

UPDATE Student
SET Class = "4B"
WHERE MatricNo = "HS-2015-108"

DELETE FROM SCR
WHERE MatricNo = "HS-2015-108"

DELETE FROM Student
WHERE MatricNo = "HS-2015-108"