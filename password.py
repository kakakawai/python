# -*- coding:utf-8 -*-
#######################################
#            密码验证程序             #
#   检验密码由大写，小写和数字组成    #
#######################################

def catch_psd(psd):
    flag = False
    is_up = False
    is_low = False
    is_digit = False
    no_alpha = False
    for i in psd:
        if i.isupper():
            is_up = True
        if i.islower():
            is_low = True
        if i.isdigit():
            is_digit = True
        if not i.isalpha():
            no_alpha = True
    if is_up and is_low and no_alpha:
        flag = True
    return flag

psd = raw_input('Enter your password:')
print catch_psd(psd)

#######################################   
#           checkPassword.py          #
#######################################
def has_lower_case(password):
    flag = False
    for i in password:
        if i.islower():
            flag = True
    return flag

def has_upper_case(password):
    flag = False
    for i in password:
        if i.isupper():
            flag = True
    return flag

def has_special(password):
    flag = False
    for i in password:
        if i.isdigit() and not i.isalpha():
            flag = True
    return flag
