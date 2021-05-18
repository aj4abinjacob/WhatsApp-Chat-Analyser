import sys
import re
from datetime import datetime
from datetime import timedelta


#Functions

def get_link(msg):
    link = re.findall(url_extract,msg)
    if len(link) >= 1:
        for i in link:
            return i+" "

def proper_date(dt):
    dat_for = dt.split('/')
    pr_dat = []
    for x in dat_for:
        if x.startswith('0'):
            x = x.replace('0','')
            pr_dat.append(x)
        else:
            pr_dat.append(x)        
    dt = '/'.join(pr_dat)
    dt = datetime.datetime.strptime(dt, "%d/%m/%y").strftime("%Y-%m-%d")
    return dt

def time_bins(tim):
    tim = datetime.datetime.strptime(tim, "%I:%M %p")
    stim = tim+timedelta(hours=1)
    fir = tim.strftime("%I %p")
    sec = stim.strftime("%I %p")
    tim = f"{fir} - {sec}"
    return tim    

def readable_date(dt):
    dt = datetime.datetime.strptime(dt, "%y-%m-%d").strftime("%Y-%B-%d")
    return dt




args = sys.argv
if len(args) == 1:
    print("No chat found")
    exit()
else:
    print('Analysing',args[1])
    chat_file = args[1]
    chat = chat_file.split('WhatsApp Chat with ')[1].rstrip('.txt')
    print(args[1])
    file = open(chat_file,'r',encoding='utf8')
    file = file.read()
    file = file.split('\n')

    form_data = []
    for line in file:
        if len(line) > 2 and line[2] == '/' and line[5] == '/' and line[8] ==',':
            form_data.append(line)
        else:
            form_data[-1] = form_data[-1]+' '+line

    url_extract = r"""(?i)\b((?:https?:(?:/{1,3}|[a-z0-9%])|[a-z0-9.\-]+[.](?:com|net|org|edu|gov|mil|aero|asia|biz|cat|coop|info|int|jobs|mobi|museum|name|post|pro|tel|travel|xxx|ac|ad|ae|af|ag|ai|al|am|an|ao|aq|ar|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|bv|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|cr|cs|cu|cv|cx|cy|cz|dd|de|dj|dk|dm|do|dz|ec|ee|eg|eh|er|es|et|eu|fi|fj|fk|fm|fo|fr|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|il|im|in|io|iq|ir|is|it|je|jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mk|ml|mm|mn|mo|mp|mq|mr|ms|mt|mu|mv|mw|mx|my|mz|na|nc|ne|nf|ng|ni|nl|no|np|nr|nu|nz|om|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt|pw|py|qa|re|ro|rs|ru|rw|sa|sb|sc|sd|se|sg|sh|si|sj|Ja|sk|sl|sm|sn|so|sr|ss|st|su|sv|sx|sy|sz|tc|td|tf|tg|th|tj|tk|tl|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug|uk|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|yu|za|zm|zw)/)(?:[^\s()<>{}\[\]]+|\([^\s()]*?\([^\s()]+\)[^\s()]*?\)|\([^\s]+?\))+(?:\([^\s()]*?\([^\s()]+\)[^\s()]*?\)|\([^\s]+?\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’])|(?:(?<!@)[a-z0-9]+(?:[.\-][a-z0-9]+)*[.](?:com|net|org|edu|gov|mil|aero|asia|biz|cat|coop|info|int|jobs|mobi|museum|name|post|pro|tel|travel|xxx|ac|ad|ae|af|ag|ai|al|am|an|ao|aq|ar|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|bv|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|cr|cs|cu|cv|cx|cy|cz|dd|de|dj|dk|dm|do|dz|ec|ee|eg|eh|er|es|et|eu|fi|fj|fk|fm|fo|fr|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|il|im|in|io|iq|ir|is|it|je|jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mk|ml|mm|mn|mo|mp|mq|mr|ms|mt|mu|mv|mw|mx|my|mz|na|nc|ne|nf|ng|ni|nl|no|np|nr|nu|nz|om|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt|pw|py|qa|re|ro|rs|ru|rw|sa|sb|sc|sd|se|sg|sh|si|sj|Ja|sk|sl|sm|sn|so|sr|ss|st|su|sv|sx|sy|sz|tc|td|tf|tg|th|tj|tk|tl|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug|uk|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|yu|za|zm|zw)\b/?(?!@)))"""

    links = []
    links_pos = []
    for nu,line in enumerate(form_data):
        link = re.findall(url_extract,line)
        if len(link) >= 1:
            links_pos.append(nu)
            for i in link:
                links.append(i)
    
   

    #Getting Dates
    date = []
    for line in form_data:
        line = line.split(',')[0]
        line = line.rstrip().lstrip()
        date.append(line)


    #Getting Time
    time =[]
    for line in form_data:
        line = line[10:18]
        line = line.rstrip().lstrip()
        time.append(line)
    

    #Getting Sender & Events
    sender = []
    events_po = []
    for nu,line in enumerate(form_data):
        line = line.split('-')[1]
        po = line.find(':')
        line = line.rstrip().lstrip()
        if po == -1:
            events_po.append(nu)
            sender.append(line)
        else:
            line = line[0:po-1]
            sender.append(line) 
  
    #Getting Message
    message = []
    for line in form_data:
        line = line.split('-')[1:]
        line = '-'.join(line)
        line = line[line.find(':')+1:]
        line = line.rstrip().lstrip()
        message.append(line)  

    link_file = open(f'Links shared with {chat}.txt','w',encoding="utf-8")
    detailed_link_file = open(f'Detailed info on links shared with {chat}.txt','w',encoding="utf-8")
    for i in links_pos:
        lmsg = message[i]
        lsen = sender[i]
        ltime = time[i]
        ldate = datetime.strptime(date[i], '%d/%m/%y').strftime('%d-%b-%Y')
        link = get_link(lmsg)
        detailed_link_file.writelines(f"{ldate},{ltime},{lsen},{link}\n")
        link_file.writelines(f"{link}\n")
    print('Done extracting links') 
    
