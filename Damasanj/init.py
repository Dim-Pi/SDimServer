def main(**keys):
    Lesson      =     keys['Lesson']
    Massenger   =   keys ['Massenger']
    




    
    _lessons_list={      # Lessons_List
   #"example"    :       {'small_name':'xmp','name':'تست'   },
    "math"       :       {'small_name':'mth','name':'ریاضی' },
    "chemistry"  :       {'small_name':'chm','name':'شیمی'  },
    }


    for nm ,info in  list(_lessons_list.items()):
        Lesson.add(nm,**info)








    _massenger_list={
        "soroush+"   :  {'sender':'_soroush+_sender'}
    }

    for nm ,info in  list(_massenger_list.items()):
        Massenger.add(nm,**info)
