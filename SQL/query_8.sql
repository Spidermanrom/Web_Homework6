
-- 8. Знайти середній бал, який ставить певний викладач зі своїх предметів

SELECT t.fullname, ROUND(AVG(g.grade), 2) AS average_grade 
FROM grades g
JOIN disciplines d ON g.disciplines_id = d.id
JOIN teachers t ON d.teacher_id = t.id 
WHERE t.id = 3  -- Вказати id викладача
;