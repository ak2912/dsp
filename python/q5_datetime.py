# Hint:  use Google to find python function

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'   

a = datetime.strptime(date_start, date_format)
b = datetime.strptime(date_stop, date_format)

delta = b-a
print delta.days

####b)  
date_start = '12312013'  
date_stop = '05282015'  

date_format2 = "%m%d%Y"
c = datetime.strptime(date_start, date_format2)
d = datetime.strptime(date_stop, date_format2)

delta = d-c
print delta.days

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  

date_format3 = "%d-%b-%Y"
e = datetime.strptime(date_start, date_format3)
f = datetime.strptime(date_stop, date_format3)

delta = f-e
print delta.days
