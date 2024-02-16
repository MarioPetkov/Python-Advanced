def softuni_students(*args, **kwargs):
    students = {}

    for course_id, username in args:
        if username in students:
            students[username].append(course_id)
        else:
            students[username] = [course_id]

    for course_id, username in kwargs:
        if username in students:
            students[username].append(course_id)
        else:
            students[username] = [course_id]



print(softuni_students(    ('id_7', 'Silvester1'),    ('id_32', 'Katq21'),    ('id_7', 'The programmer'),    id_76='Spring Fundamentals',    id_7='Spring Advanced',))