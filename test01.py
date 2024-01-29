# Ex8: Cho một dãy ký tự được xem là một password. Kiểm tra password có hợp lệ hay không.
# Một password hợp lệ khi và chỉ khi thỏa mãn tất cả các điều kiện sau: 
# 1.Ít nhất 1 chữ cái nằm trong [a-z] 
# 2. Ít nhất 1 số nằm trong [0-9] 
# 3. Ít nhất 1 kí tự nằm trong [A-Z] 
# 4. Ít nhất 1 ký tự nằm trong [$ # @] 
# 5. Độ dài mật khẩu tối thiểu: 6 
# 6. Độ dài mật khẩu tối đa: 12

input_string = input("Nhap password: ")

cond_1 = False
for c in input_string:
    if c >= 'a' and c <= 'z':
        cond_1 = True
        break
    
cond_2 = False
for c in input_string:
    if c >= '0' and c <= '9':
        cond_2 = True
        break
    
cond_3 = False
for c in input_string:
    if c >= 'A' and c <= 'Z':
        cond_3 = True
        break
    
cond_4 = False
for c in input_string:
    if c in ['$', '#', '@']:
        cond_4 = True
        break
    
if len(input_string) >= 6:
    cond_5 = True
else:
    cond_5 = False
    
if len(input_string) <= 12:
    cond_6 = True
else:
    cond_6 = False
    
if cond_1 and cond_2 and cond_3 and cond_4 and cond_5 and cond_6:
    print("your password is valid")
else:
    print('your password is invalid')