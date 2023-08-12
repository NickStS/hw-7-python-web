SELECT subjects.name
FROM subjects
JOIN teachers USING (teacher_id)
WHERE teachers.name = 'GOIT';
