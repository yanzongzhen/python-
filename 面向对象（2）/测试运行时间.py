import time
def run_time(func):
    def new_fun(*args,**kwargs):
        t0 = time.time()
        print('star time: %s'%(time.strftime('%x',time.localtime())) )
        back = func(*args)
        print('end time: %s'%(time.strftime('%x',time.localtime())) )
        print('run time: %s'%(time.time() - t0))
        return back
    return new_fun
