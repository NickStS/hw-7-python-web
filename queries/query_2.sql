SELECT student_id, name, AVG(grade) as avg_grade
FROM students
JOIN grades USING (student_id)
JOIN subjects USING (subject_id)
WHERE subjects.name = 'Python'
GROUP BY student_id, name
ORDER BY avg_grade DESC
LIMIT 1;
