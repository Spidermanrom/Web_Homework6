
-- 10. Список курсів, які певному студенту читає певний викладач

SELECT s.fullname AS Student, t.fullname AS Teacher, d.name AS Discipline 
FROM teachers t
JOIN disciplines d ON d.teacher_id = t.id 
JOIN grades g ON d.id = g.disciplines_id 
JOIN students s ON g.student_id = s.id 
WHERE s.id = 22 AND t.id = 3  -- Потрібно вказати s.id - студента та t.id - викладача
ORDER BY d.name
;