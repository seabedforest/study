alphabet={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':1,
          'k':2,'l':3,'m':4,'n':5,'o':6,'p':7,'q':8,'r':9,'s':1,'t':2,
          'u':3,'v':4,'w':5,'x':6,'y':7,'z':8,}
str01='dsagr3525eu21422'
list_01=list(str01)
odd_number_totle=0
even_number_totle=0
number=0
for i in range(len(list_01)-1,-1,-1):
    if i % 2 == 0:
        if list_01[i].isdigit():
            number=int(list_01[i])*2
            if number // 10:
                number -= 9
            even_number_totle +=number
    else:
        if list_01[i].isdigit():
            odd_number_totle +=int(list_01[i])
        else:
            odd_number_totle +=alphabet[list_01[i]]

if (odd_number_totle+even_number_totle) % 10 == 0:
    print('ok')
else:
    print('error')