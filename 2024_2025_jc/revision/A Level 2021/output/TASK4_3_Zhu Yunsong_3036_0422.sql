SELECT c.name, ROUND(AVG(s.score), 2) AS average_score FROM scores AS s
INNER JOIN competitor AS c ON c.id = s.id
GROUP BY c.id