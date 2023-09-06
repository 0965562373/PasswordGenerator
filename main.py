import random
letters = ['A','B', 'C' , 'D','E','F' , 'G' ,'H' , 'J' ,'K' , 'L' , 'M' , 'N' , 'O' , 'P' ,'Q','R' ,'S','T'
           ,'S','T','U' ,'V' ,'W' ,'X' ,'Y' ,'Z' ,'a' , 'b' ,'c' , 'd' ,'e' ,'f' ,'g','h','i','j' ,'k' ,'l'
           ,'m' ,'n' ,'o' ,'p' ,'q' ,'r','s' ,'t' ,'u' ,'v' ,'w' ,'x' ,'y','z']
symbols = ['!', '@' ,'#' ,'$' ,'%' ,'^' ,'&' ,'*' ,'(' ,')' ,'+']
number = ['1','2' ,'3' ,'4' ,'5' ,'6','7','8','9','0']
print("Welcome to password generator!")
n_letters = int(input("How many letters you want in your password?\n"))
n_symbols = int(input("How many symbols you want in your sybmols?\n"))
n_number = int(input("How many numbers you want in your numbers?\n"))
password = []
for i in range(1,n_letters + 1):
    r = random.choice(letters)
    password += r
for i in range(1,n_symbols +1):
    s = random.choice(symbols)
    password += s
for i in range(1,n_number + 1):
    k = random.choice(number)
    password +=k
random.shuffle(password)
password_list = ""
for char in password:
    password_list += char
print(password_list)


