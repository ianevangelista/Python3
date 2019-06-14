str = "hei alle sammen"
str.split(" ")
fib1 = [1,1,2,3,5,8,13]
fib1[-1]
fib1[0:4] #går bare til 3
fib2 = [21, 34, 55]
fib = fib1 + fib2 #legger til i listen
fib.append(89) #legger til 89 sist
fib.pop() #fjerner default siste element, kan ha index
fib.append(89)
fib.append(89)
del(fib[0])

chars = ['mario', 'luigi', 'bowser', 5]
nums = [chars, fib1, [1,2,3,4]]
nums[0][0]
