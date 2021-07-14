from gevent import monkey
from gevent.pool import Pool







def main():
    from sys import path
    from S_ports import bots

    monkey.patch_all(GEVENT_SUPPORT=True)

    pool = Pool(len(bots))

    for bot in bots :
        pool.spawn(bot.run)
    
    pool.join()


    









if __name__ == "__main__":
    main()