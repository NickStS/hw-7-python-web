SELECT student_id, name
FROM students
JOIN groups USING (group_id)
WHERE groups.name = 'CORE';
