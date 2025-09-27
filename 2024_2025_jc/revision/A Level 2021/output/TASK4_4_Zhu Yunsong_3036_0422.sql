SELECT
	c.name,
	SUM(s.score) AS total,
	SUM(s.score) > 250
FROM scores AS s
INNER JOIN competitor AS c ON c.id = s.id
GROUP BY c.id
ORDER BY total DESC