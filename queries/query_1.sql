SELECT student_id, name, AVG(grade) as avg_grade
FROM students
JOIN grades USING (student_id)
GROUP BY student_id, name
ORDER BY avg_grade DESC
LIMIT 5;
