from time import sleep

def com (dos,ch):

    if dos > 1:
        dos = dos/100

    do = dos * 100

    nbox = ch * 2

    coms = nbox*do // 100

    dobs = coms // 2

    one  = coms % 2

    nons = ch - one - dobs

    retn = "[%s%s%s]"%('='*int(dobs),'-'*int(one),' '*int(nons))

    return retn
\


oo = 200
for a in range(0,201):
    print (com(a/200,oo)  ,end='\r')
    sleep(0.05)
print (com(a/200,oo))