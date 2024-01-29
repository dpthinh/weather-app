# # Ex1. Cho hai số nguyên dương bất kỳ a và b, kiểm tra xem a có chia hết cho b hoặc b có chia hết cho a không.
# # Nếu a chia hết cho b, in ra màn hình: "a chi hết cho b", nếu b chia hết cho a thì in ra màn hình: "b chia hết cho a",
# # những trường hợp còn lại thì in ra: "a và b không có mối liên hệ với nhau thông qua phép chia"

# a = int(input("Nhập số a: "))
# b = int(input("Nhập số b: "))

# if a % b == 0:
#     print("a chia hết cho b")
# elif b % a == 0:
#     print("b chia hết cho a")
# else:
#     print("a và b không có mối liên hệ với nhau thông qua phép chia")

# # Ex2. Cho ba số a, b, c. Kiểm tra xem ba số a, b, c có phải là độ dài của một tam giác vuông hay không?
# # Nếu đúng thì in ra màn hình: 'độ dài ba cạnh a, b, c có thể tạo thành 1 tam giác vuông', nếu sai in ra màn hình
# # 'độ dài ba cạnh a, b, c không thể tạo thành 1 tam giác vuông'

# a = int(input("Nhập số a: "))
# b = int(input("Nhập số b: "))
# c = int(input("Nhập số c: "))

# cond_1 = (a**2 + b**2 == c**2)
# cond_2 = (a**2 + c**2 == b**2)
# cond_3 = (b**2 + c**2 == a**2)
# if cond_1 or cond_2 or cond_3:
#     print('a, b, c có thể tạo thành 1 tam giác vuông')
# else:
#     print('độ dài ba cạnh a, b, c không thể tạo thành 1 tam giác vuông')

# a = int(input('Nhap so a: '))
# b = int(input('Nhap so b: '))
# a, b = b, a
# print('So a:', a)
# print('So b:', b)        

# tmp_li = [0, 4, 5, 10, 20, 30, 60]
# d = 10
# result = 0
# for v in tmp_li:
#     if v % d == 0 and v != 0:
#         result += 1
# print(result)

# tmp_li = [4, 5, 2, 10]
# tmp_li.sort()
# print('So nho nhat:', tmp_li[0])
# print('So lon nhat:', tmp_li[-1])

# s = 'Toi di hoc lap trinh tai MindX'
# capital_letters = 0
# non_capital_letters = 0
# for v in s:
#     if v >= 'a' and v <= 'z':
#         non_capital_letters += 1
#     elif v >= 'A' and v <= 'Z':
#         capital_letters += 1
        
# print('So ky tu in hoa trong chuoi:', capital_letters)
# print('So ky tu in thuong trong chuoi:', non_capital_letters)

# s = input('Nhap password: ')
# valid_password = 1

# # Kiem tra dieu kien it nhat 1 chu cai nam trong [a-z]
# flag_cond_1 = 0
# for c in s:
#     if c >= 'a' and c <= 'z':
#         flag_cond_1 = 1
#         break
    
# # Kiem tra dieu kien it nhat 1 so nam trong [0-9]
# flag_cond_2 = 0
# for c in s:
#     if c >= '0' and c <= '9':
#         flag_cond_2 = 1
#         break
    
# # Kiem tra dieu kien it nhat 1 ky tu nam trong [A-Z]
# flag_cond_3 = 0
# for c in s:
#     if c >= 'A' and c <= 'Z':
#         flag_cond_3 = 1
#         break
    
# # It nhat 1 ky tu nam trong [$ # @]
# flag_cond_4 = 0
# for c in s:
#     if c in ['$', '#', '@']:
#         flag_cond_4 = 1
#         break
    
# flag_cond_5 = 0
# if len(s) >= 6:
#     flag_cond_5 = 1
    
# flag_cond_6 = 0
# if len(s) <= 12:
#     flag_cond_6 = 1
    
# if flag_cond_1 and flag_cond_2 and flag_cond_3 and flag_cond_4 and flag_cond_5 and flag_cond_6:
#     print('valid password')
# else:
#     print('invalid password')

# a = 12
# b = 16

# belongs_to_a = [c for c in range(1,a+1) if a % c == 0]
# belongs_to_b = [c for c in range(1,b+1) if b % c == 0]
# belongs_to_a_and_b = [c for c in belongs_to_a if c in belongs_to_b]
# print(belongs_to_a_and_b)

# def check_prime(a):
#     for v in range(2, a//2 + 1):
#         if a % v == 0:
#             return False
        
#     return True

# tmp_li = [2, 4, 5, 6, 7, 9, 10]
# result_li = [c for c in tmp_li if check_prime(c)]
# print(result_li)

# def fibo(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
    
#     result = fibo(n-1) + fibo(n-2)
#     return result

# print(fibo(100))

# fibo_li = [0, 1]
# n = 100
# for v in range(2,n+1):
#     new_v = fibo_li[-1] + fibo_li[-2]
#     fibo_li.append(new_v)
    
# print(fibo_li[-1])

# input_li = [100, 10, 5, 6, 3, 7, 2, 3, 4, 5]
# my_dict = {}
# for v in input_li:
#     if my_dict.get(v) == None:
#         my_dict[v] = 1
#     else:
#         my_dict[v] += 1
        
# my_set = list(set(input_li))
# my_set.sort()
# for v in my_set:
#     print(v, my_dict[v])

# tho + ga = 35
# 2*tho + 4*ga = 94

# for tho in range(36):
#     num_tho = tho
#     num_ga = 35 - num_tho
    
#     if 2 * num_tho + 4 * num_ga == 94:
#         print('Tho: ', num_tho)
#         print('Ga: ', num_ga)

def is_character_string(s):
    for v in s:
        if (v >= 'a' and v <= 'z') or (v >= 'A' and v <= 'Z'):
            continue
        else:
            return False
    return True

def is_number_string(s):
    for v in s:
        if v >= '0' and v <= '9':
            continue
        else:
            return False
    return True
            

s = '  NGUYEN  LE    CHI BAO    123   456'
my_li = s.split(' ')
new_li = [v for v in my_li if v != '']

character_string, number_string = 0, 0
for v in new_li:
    if is_character_string(v):
        character_string += 1
    elif is_number_string(v):
        number_string += 1


print(character_string, number_string)