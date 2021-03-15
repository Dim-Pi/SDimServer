def main(**keys):
    Lesson = keys['Lesson']


    # lessons
    _lessons_list={
    "math":{'small_name':'mth','name':'ریاضی'}
    }
    for nm ,info in  list(_lessons_list.items()):
        Lesson.add(nm,**info)




