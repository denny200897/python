#變速和資料型別練習

#數字變速
age=28  #數字
print("我的年紀是" + str(age)) #因為這是數字所以需要轉型才能相加  輸入str就能將數字轉成字串，這樣列應字串出來就是數字

#inteager 整數(不會有小數點)  例如:年齡
age=30

#float 浮點數(有小數點)
gpa=3.3
print(f"我的gpa {gpa} 分")
print(type(gpa))#加入這個是告訴我們資料型別  這樣可以驗證我們帶的type都是正確的

#string 字串
name= 'Denny'
print(f"我的名字是 {name}" )
print(type(name))#加入這個是告訴我們資料型別 這樣可以驗證我們帶的type都是正確的

#boolaean布林值    (是 或 不是 ture and false)
is_online= True
print(f"在線上嗎? {is_online}")
print(type(is_online))#加入這個是告訴我們資料型別 這樣可以驗證我們帶的type都是正確的
