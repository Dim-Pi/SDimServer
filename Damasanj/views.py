
from typing import Type
from django.http import HttpResponse as Re 
from django.shortcuts import render

try:
    from SDimServer.Damasanj.library import mongo
except:
    from Damasanj.library import mongo


try:
    from SDimServer.Damasanj.models import *
except:
    from Damasanj.models import *



MSG.objects.filter(CFormat='in').delete()
Feedback.objects.filter(CFormat='in').delete()





def fr (re):
    return Re('Fr')





def keylessons (m,nmode=''):
    ls = Lesson.objects.all()
    ex0 = [[]]
    ex1 = {}
    r = 0
    num = 0
    for q in ls :
        num += 1
        ex0[r].append({'text':q.name,'command':'//%s'%q.Ename})
        ex1['/%s'%q.Ename] = nmode
        if len(ex0[r]) == 3 and num != len(ls) :
            r += 1
            ex0.append([])
    r = (ex0,ex1)

    return r[m]

    





class start:

    db = mongo()['Damasanj_msg']
    #db.drop()

    start0 = Feedback(
        
        name='start0',bmods={'main':'//jan','/True':'start01'}
        ,msg={
            0: MSG.new(body='سلام به دماسنج خوش اومدی\nبرای شروع آماده ای ؟',Type='TEXT'
                         ,keyb=[[{'text':'بزن بریم','command':'//True'}]] ,File=None ).Save()
        
        }
        
        ).Save()

    

    start01 = Feedback(
        name='start01',bmods={'main':'start02'},TYPE='static'
        ,msg={ 
            0: MSG.new( body='حالا اسمتم بگو متنّبه شیم  ( اسم غیر خانوادگی )',Type='TEXT').Save()
        }
    ).Save()

    start02 = Feedback(
        name='start02',bmods={'main':'start1'},TYPE='static'
        ,msg={
            0: MSG.new( body="به به حالا اون یکی اسمتم بگو که دیگه خیلی خیلی متّنبه بشیم( اسم خانوادگی )",Type='TEXT').Save()
        }
    ).Save()

    start1 = Feedback(
        name='start1',bmods={'main':'//again','/badmin':'sign1_0','/admin':'sign0_1','/student':'sign0_2'}
        ,msg={0:MSG.new(body="خیله خب حالا بگو ببینم چه کارا میکنی چه جور هست کارو بارت؟",Type='TEXT'
        ,keyb=[

        [{'text':'هیجی بابا یه غلطی کردم مدیر پایه یه عده خل و چل شدم'      ,'command':'//badmin'}]
        ,[{'text':'سرگروه شدم فقط اسمش باحاله'                               ,'command':'//admin'}]
        ,[{'text':'سرگروه و زیرگروه و سرور و برده خودمم با افتخار'         ,'command':'//student'}]
        ]).Save()
        }).Save()

    sign1_0 = Feedback(
        name='sign1_0',bmods={'main':'sign1_0'}
        ,msg={
            0: MSG.new( Type='TEXT'
            ,body='''بابا قربونت برم مدیرپایه عزیزم شما کجا اینجا کجا؟
            چه خبرا خوب هستین؟
            جسارت نشه خیلیا خودشونو جای شما جا میزنن زحمتتون به یکی از این شریعتا یه پیامی یه ندایی چیزی بدین کارتون رو اوکی میکنن
            @ali_04   @programmer.pro''').Save()
        }).Save()


    sign0_1 = Feedback(
        name='sign0_1',bmods={'main':'//jan'}
        ,msg={0:MSG.new(Type='TEXT' ,keyb=keylessons(0)
        ,body='''به به سرگروه عزیز چه خبرا؟
        راستی نگفتی کدوم درس لیاقت سرگروهی شما رو داشته؟ 
         '''
        ).Save()
        }
    ).Save()
    for q0 in keylessons(1,nmode='sign1_1'):

        sign0_1.bmods[q0] = 'sign1_1'

    sign0_1.Save()




    sign1_1 = Feedback(
        name ='sign1_1', bmods={'main':'sign2_1'},
        msg  =  {
            0: MSG.new(body='خب پس زحمتت به یکی از شریعتا یه پیامی بده کارت رو را میندازن \n @ali_04   @programmer.pro',Type='TEXT').Save()
        }
    ).Save()



    sign2_1 = Feedback(
        name = 'sign2_1' , bmods={'main':'//dont'},
        msg = {} ).Save()










def lsn(d):
    r = 0
    for a in d:
        if a > r:
            r = a
    
    return r



class Self :
    
    def Fadriver(it):
        li = {
            'stu'    :{'msg':None  ,'key':  {'text':'شرکت در فزاسنج','command':'//stu'}               ,'mod': {'key':'/stu'    ,'co':'frn_starter'}}
        }
        #                                                                                                                                _________________
        
        for q in Lesson.objects.all():
            li["adm_%s"%q.small_name] = {
                'msg': None,
                'key': {
                            'text':  'مدیریت بخش %s'%q.name ,
                            'command':   '//adm.%s'%q.small_name
                            },
                            'mod': {
                                'key':'/adm.%s'%q.small_name,
                                'co' :'adm_starter.%s'%q.small_name
                                }
                        }
        
        try:it.role.sync()       
        except:...

        md = it.role.optionsn
        mods = {'main':'//jan'}
        nm = {0:MSG.new(Type='TEXT',body='به به خب حالا چیکار کنیم؟').Save()}
        key0 = [[]]
        me = 0

        for q0 in md:
            
            q = li[q0]
            if q['msg']!=None:
                e0 = lsn(nm) + 1
                nm [e0] = q['msg']
            if q['key']!=None:
                key0[me].append(q['key'])
                if len(key0[me]) == 3 :
                    key0.append([])
                    me += 1
            if q['mod']!=None:
                mods[q['mod']['key']] = q['mod']['co']

        nm[lsn(nm)].keyb = key0
        nm[lsn(nm)].Save()

        return nm ,mods

    adriver = Feedback.newD(name='adriver',TYPE='dynamic' ,F='Fadriver').Save()
    
    




class admviews :

    adm_start0 = Feedback(name='adm_start0',TYPE='static',bmods={'main':'//jan','/staart':'adriver'}
    ,msg={
        0:MSG.new(Type='TEXT',body='به به میدونستم از اولم نباید بهت شک میکردم',keyb=[[{'text':'بریم به ادامه','command':'//staart'}]]).Save()
    }).Save()

    
    def Fadm_starter0 (it):
    
        mod = {'main':'//jan' ,'/add_Dor.%s'%it.mode2:'adm_add_dor0.%s'%it.mode2}
        if it.sign2 :
            ms = '''به پنل مدیریت خوش اومدی !!  حالا کجا بریم؟؟'''
        else:
            ms = '''معرفی میکنم اینجا پنل مدیریت دماسنجا..نه نه ببخشید فراسنجاست  خب حالا میتونی با یک خنده شیطانی هر کخی دلت بخواد بریزی!!! البته حواست باشه مدیر پایه ها نظارت میکنن!.......'''
            it.sign = True
        
        Msg = {0:MSG.new(Type='TEXT', body=ms,keyb=[[{'text':'ایجاد فراسنج','command':'//add_Dor.%s'%it.mode2}]]).Save()}
        
        
        return Msg , mod
    
    
    adm_starter = Feedback.newD( name='adm_starter',TYPE='dynamic' 
                                ,F='Fadm_starter0' ).Save()


    

    adm_add_dor0 = Feedback( name='adm_add_dor0'  ,bmods={'main':'adm_add_dor1'}
                        ,msg={
                            0:MSG.new(Type='TEXT'
                            ,body='''خب اولین وظیفه هر سرگره نسبت به فراسنجش انتخاب یک اسم نیکو برای اونه ببینم چه میکنی!'''
                            ,keyb=[[{'command':'[auto]','text':'وللش حوصله داریا خودت یه چیزی انتخاب کن'}],[{'command':'[back]','text':'وللش منصرف شدم'}]]
                            ).Save()
                        }).Save()
    



    adm_add_dor1 = Feedback( name='adm_add_dor1'  ,bmods={'main':'adm_add_dor2'}
                            ,msg={
                                0:MSG.new(Type='TEXT' ,body='''خب حالا مبحث فراسنجمون رو برام بفرست زحمتت!(اگه چندتا مبحثه بینشون "و" بزار)'''
                                ,keyb=[[{'command':'[auto]','text':'فعلا عجله ای نیست باشه بعدا'}],[{'command':'[back]','text':' ولش کن کلا '}]]).Save()
                            }).Save()




    adm_add_dor2 = Feedback( name='adm_add_dor2'  ,bmods={'main':'//jan','/True':'adm_learn_add_question0','/False':'adm_add_question0'}
                            ,msg = {
                                0: MSG(Type='TEXT' ,body="خیله خب حالا رسیدیم به بخش اصلی کار یعنی اضافه کردن سوال به <farasanj.name>"  ).Save() , #last_end_______________________________
                                1: MSG(Type='TEXT' ,body=" خب اگه اینکارو بلدی که هیچی اگرنه از گزینه [بلد نیستم] استفاده کن!"
                                ,keyb=[[{'command':'//False','text':'نه بابا بلدم!'}],[{'command':'//True','text':'[بلد نیستم]'}]] ).Save()
                                 }).Save()








def keyv (key,fname,e):
    return Feedback( name='register',
        msg={
        0: MSG.new(body='''سلام اینم از آقای %s ادعای %s کرده'''%(fname,e),Type='TEXT').Save(),
        1: MSG.new(body='به ربات ریپلای کن',Type='TEXT').Save(),
        2: MSG.new(body=str(key),Type='TEXT').Save()
        }
    ).Save()



funs = {
    'Fadriver':       Self.Fadriver                      ,
    'Fadm_starter0':  admviews.Fadm_starter0             ,
}

givefun(funs)
