# 1.
# ““671111101031149711611710897116105111110115” This is a “ASCII numbers”
# string. Please try to convert the string to TEXT. The text matches a regular
# expression, "[a-zA-Z]+"gm.
import math
as_numbers=671111101031149711611710897116105111110115

def transfer(ascii_numbers):
    ascii_code={"a":97, "z":122, "A":65, "Z":90}
    arr=[]
    for i in range(int(math.log10(ascii_numbers)//1), -1, -1):
        if ascii_numbers//10**i >= ascii_code["A"] and ascii_numbers//10**i <= ascii_code["Z"]:
            arr.append(chr(ascii_numbers//10**i))
            ascii_numbers=ascii_numbers%10**i
        if ascii_numbers//10**i >= ascii_code["a"] and ascii_numbers//10**i <= ascii_code["z"]:
            arr.append(chr(ascii_numbers//10**i))
            ascii_numbers=ascii_numbers%10**i
    txt=""
    for i in arr:
        txt+=i
    return txt

print(transfer(as_numbers))  

# 2.
class Singleton: # Design pattern的單例模式
    _instance = None # 建立一個實例
    def __new__(cls, *args, **kwargs): 
        if cls._instance is None: # 如果實例不存在
            cls._instance = super().__new__(cls) # 建立一個實例
        return cls._instance # 實例存在，返回該實例
         
    def __init__(self): 
        pass
    def sayHello(self, name, message):
        print(f"Hi, {name}. Your message: {message}.")

person1=Singleton() 
person2=Singleton()
person1.sayHello("Tom", "how are you?")
person2.sayHello("Lin", "I'm fine.")
print(id(person1))
print(id(person2))