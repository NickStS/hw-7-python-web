SELECT students.name, grade, date
FROM students
JOIN groups USING (group_id)
JOIN grades USING (student_id)
JOIN subjects USING (subject_id)
WHERE groups.name = 'CORE' AND subjects.name = 'Python';
