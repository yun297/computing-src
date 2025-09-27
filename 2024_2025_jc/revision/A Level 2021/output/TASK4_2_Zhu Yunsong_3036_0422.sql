SELECT c.name, s.score FROM scores AS s
INNER JOIN competitor AS c ON c.id = s.id
WHERE s.round = 1
ORDER BY s.score DESC