SELECT Student.Class, Student.IndexNo, Student.Name, ClassGroup.ClassGroupName
FROM Student, ClassGroup, SCR
WHERE Student.MatricNo = SCR.MatricNo
AND ClassGroup.ClassGroupID = SCR.ClassGroupID
AND ClassGroup.ClassGroupName = 'Comp_4AB'
ORDER BY Student.Class ASC, Student.IndexNo ASC




SELECT Class, IndexNo, Name, ClassGroupName
FROM Student
INNER JOIN SCR USING (MatricNo)
INNER JOIN ClassGroup USING (ClassGroupID)
WHERE ClassGroup.ClassGroupName = 'Comp_4AB'
ORDER BY Student.Class ASC, Student.IndexNo ASC