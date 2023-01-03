def time_fun():
    global ti
    ti=time.localtime()
    cur_date=time.strftime("%d/%m/%Y",ti)
    cti=time.strftime("%H:%M:%S %p",ti)
    print(cur_date)
    print(cti)
    second=time.strftime("%S",ti)
    second=6
    print("Please Wait , Your Quiz Will Start Soon: ",end=" ")
    for i in range(6):
        if second==6:
            pass
        elif second==1:
            print('-'*15)
            print("Get Ready")
            print('-'*15)
        else:
            print(second)
            time.sleep(1)
        second=second-1
    
    print("----------------------")
    print(" "*10+"start"+" "*10)
    print("----------------------")