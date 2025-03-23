#型別轉換練習 type casting
name= "denny"
age = 20
gpa= 1.9
student=True

#顯示型別轉換

#student =str(student)   #str 是轉成字串
#print(student)
#print(type(student))   #注意type都是撿視型別

#gpa = int(gpa)    #int 是整數
#print(gpa)
#print(type(gpa) )   #注意type都是撿視型別

#age =float(age)  #float 是浮點數
#print(age)
#print(type (age))   #注意type都是撿視型別

#print(type(name))     #注意type都是撿視型別
#print(type(age))
#print(type(gpa))
#print(type(student))

#隱式型別轉換

x = 10
y = 2.0  #浮點數
x = x/y
print(x)
print(type(x))
