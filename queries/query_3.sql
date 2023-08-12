SELECT groups.name, AVG(grade) as avg_grade
FROM groups
JOIN students USING (group_id)
JOIN grades USING (student_id)
JOIN subjects USING (subject_id)
WHERE subjects.name = 'SQL'
GROUP BY groups.name;
