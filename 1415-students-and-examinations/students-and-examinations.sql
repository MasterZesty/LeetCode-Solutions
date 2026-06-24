SELECT
    s.student_id,
    s.student_name,
    t.subject_name,
    COUNT(e.subject_name) AS attended_exams
FROM students s
CROSS JOIN subjects t
LEFT JOIN examinations e
    ON e.student_id = s.student_id
   AND e.subject_name = t.subject_name
GROUP BY
    s.student_id,
    s.student_name,
    t.subject_name
ORDER BY
    s.student_id,
    t.subject_name;