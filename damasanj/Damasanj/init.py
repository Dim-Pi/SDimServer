def main(**keys):


    Lesson      =     keys['Lesson']
    Massenger   =   keys ['Massenger']
    Admin       =     keys['Admin']
    Role        =      keys['Role']
    Option      =     keys['Option']    




    
    _lessons_list={      # Lessons_List
   #"example"    :       {'small_name':'xmp','name':'تست'   },
    "math"       :       {'small_name':'mth','name':'ریاضی' },
    "chemistry"  :       {'small_name':'chm','name':'شیمی'  },
    }


    _massenger_list={
        "soroush+"   :  {'sender':'_soroush+_driver'}
    }


    _admin_list=[
        "1UGgWYRWoxeafE2VPZTzUZ-YFgheBOWeypJSddLi5Fyo-_qUGl_eAKOF9Jc",
        "1uxTbAgywOEtM3SfU5YtuXA6Hf115TOPj9ku6p9vMlw5xfSLRpET16N8SnQ",
    ]


    _role_list=[
        {"name":'admin.math'      ,"Fname":'سرگروه ریاضی' ,"options":[Option._give('adm_mth'),Option._give('stu')]}  ,
        {"name":'admin.chemistry' ,"Fname":'سرگروه شیمی'  ,"options":[Option._give('adm_chm'),Option._give('stu')]}  ,
    ]














    for nm ,info in  list(_lessons_list.items()):
        Lesson.add(nm,**info)






    for nm ,info in  list(_massenger_list.items()):
        Massenger.add(nm,**info)






    for q in _admin_list :
        Admin._give(q)





    for info in _role_list:
        Role._give(**info)





