#input 取得使用者輸入練習
from operator import length_hint
from statistics import quantiles
from tabnanny import process_tokens

#name=input("請輸入名字:")
#print(f"你的名字是{name}")

#練習一:填詞遊戲
#adj_1 =input("請輸入第1個形容詞: ")
#noun =input("請輸入名詞:")
#adj_2 =input("請輸入第2個形容詞: ")     #input 是輸入
#verb =input("請輸入動詞:")
#adj_3 =input("請輸入第3個形容詞: ")

#print(f"今天我去了一個{adj_1}的動物園，在展覽中我看到了{noun}這個{noun}很{adj_2}，正在{verb}我感到很{adj_3} ")

#練習二:計算舉行面積
#length = float(input("請輸入矩形的長度"))
#width = float(input("請輸入矩形的寬度"))

#area = length* width
#print(f"面積為{area} 平方公分")

#練習三:購物車程式
item = input("你想買甚麼物品")  #input是輸入   #item是物品
price =float(input("價格多少?"))  #float浮點數  #price是價格
quantity =int (input("你需要多少件?"))   #quantity是數量的意思  #數量不會有半個所以使用int

total = price * quantity   #total 是總價格

print(f"你購買了{quantity} {item} ，總價為{total}")


