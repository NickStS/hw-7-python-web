SELECT subjects.name
FROM subjects
JOIN grades USING (subject_id)
JOIN students USING (student_id)
JOIN teachers ON subjects.teacher_id = teachers.teacher_id
WHERE students.name = 'Nick' AND teachers.name = 'GOIT';
