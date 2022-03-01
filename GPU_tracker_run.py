import GPU_tracker_argentina as GPU
from gpu_app import app
from multiprocessing import Process
from sqlalchemy import create_engine
#my situation
PATH = r'C:\Users\mossney\Documents\Selenium\chromedriver.exe'#This is my path, use yours
engine = create_engine('sqlite:///tracker.db', echo=False) #my engine

def rx580():
    GPU.price_tracker('rx 580', 80000, PATH, engine=engine, SQL= True, CSV=False, info=False, interval=3600*24, N=20)

def super_1660():
    GPU.price_tracker('gtx 1660 super', 80000, PATH, engine=engine, SQL= True, CSV=False, info=False, interval=3600*24, N=20)

def rtx3070():
    GPU.price_tracker('rtx 3070', 150000, PATH, engine=engine, SQL= True, CSV=False, info=False, interval=3600*24, N=20)

def rtx3060ti():
    GPU.price_tracker('rtx 3060 ti', 100000, PATH, engine=engine, SQL= True, CSV=False, info=False, interval=3600*24, N=20)

def rtx3080():
    GPU.price_tracker('rtx 3080', 180000, PATH, engine=engine, SQL= True, CSV=False, info=False, interval=3600*24, N=20)

def rx6700xt():
    GPU.price_tracker('rx 6700 xt', 150000, PATH, engine=engine, SQL= True, CSV=False, info=False, interval=3600*24, N=20)

def runapp():
    app.run(debug=True)

if __name__=='__main__':
     p1 = Process(target = rx580)
     p1.start()
     p2 = Process(target = super_1660)
     p2.start()
     p3 = Process(target = rtx3070)
     p3.start()
     p4 = Process(target = rtx3060ti)
     p4.start()
     p5 = Process(target = rtx3080)
     p5.start()
     p6 = Process(target = rx6700xt)
     p6.start()
     p7 = Process(target = runapp()) #connect website
     p7.start()


