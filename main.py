print('n школьников делят k яблок поровну, неделящийся остаток остается в корзинке. Сколько яблок достанется каждому школьнику? Сколько яблок останется в корзинке?')
n= int(input("Введите количество школьников: "))
k= int(input("Введите количество яблок: "))
a=k//n
b=k%n
print("Каждому школьнику досталось: ", a )
print("Яблок в корзине осталось: ",b)
    