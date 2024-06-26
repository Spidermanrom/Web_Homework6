
-- 1. Знайти 5 студентів із найбільшим середнім балом з усіх предметів

SELECT s.fullname, ROUND(AVG(g.grade), 2) AS average_grade 
FROM grades g
JOIN students s ON s.id = g.student_id
GROUP BY s.fullname 
ORDER BY average_grade DESC 
LIMIT 5
;