def current_time(*time) :
    import datetime
    wel = datetime.datetime.now()
    return wel.hour ,(wel.minute+2)


    #whatsapp messages
import pywhatkit
time=current_time()
pywhatkit.sendwhatmsg('+918669040343',"This message came from python programming , don't be afraid of it . ",time[0],time[1])
