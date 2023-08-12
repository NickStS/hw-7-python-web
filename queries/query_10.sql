SELECT subjects.name AS course_name
FROM subjects
JOIN teachers ON subjects.teacher_id = teachers.id
JOIN grades ON subjects.id = grades.subject_id
WHERE grades.student_id = :student_id AND teachers.id = :teacher_id;
