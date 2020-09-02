import string
from sys import argv
import traceback
import logging

chars = string.ascii_uppercase
allowed_chars = '[]()_$";+.'


def code_splitter():
    code = argv[1]
    code = code.replace(" ","")
    splitted = code.rstrip(';').split(';')
    functions = [func[:func.find("(")] for func in splitted] 
    arguments = [arg[arg.find("(")+1:arg.find(")")] for arg in splitted]
    return functions , arguments


def static_variables():
    uppercase_a =  '$_=[];'
    uppercase_a += '$_="$_";'
    uppercase_a += '$_=$_["_"=="="];'
    temp_uppercase_a = '$__=$_;'
    strtolower = encoder_helper('STRTOLOWER', '$____')
    lowercase_a =  '$___=$_;'
    lowercase_a += strtolower
    lowercase_a += '$___=$____($___);'
    temp_lowercase_a = '$____=$___;'
    return uppercase_a + temp_uppercase_a + lowercase_a + temp_lowercase_a


def encoder():
    encoded = ""
    functions , arguments = code_splitter()
    funcs_vars = ['$____'+('_'*(i+1)) for i in range(len(functions))]
    for i in range(len(functions)):
        encoded_funcs = encoder_helper(functions[i],funcs_vars[i])
        encoded += encoded_funcs
    args_vars =  ['$____'+('_'*(i+1+len(functions))) for i in range(len(arguments))]
    for i in range(len(arguments)):
        encoded_args = encoder_helper(arguments[i],args_vars[i])
        encoded += encoded_args
    for func_var,arg_var in zip(funcs_vars,args_vars):
        encoded += execute_code(func_var,arg_var);
    return encoded


def encoder_helper(plaintext,var):
    local_encoded = ""
    try:
        for char in plaintext:
            if char in chars and char.isupper():
                local_encoded +=  '$__++;' * chars.find(char)
                local_encoded += var + '.=$__;'
                local_encoded += '$__=$_;'
            elif char.upper() in chars and char.islower():
                local_encoded += '$____++;' * chars.find(char.upper())
                local_encoded += var + '.=$____;'
                local_encoded += '$____=$___;'
            elif char in allowed_chars and char != "'" and char != '"':
                local_encoded += var + '.="' + char + '";'
    except Exception as e:
        logging.error(traceback.format_exc())
    return local_encoded


def execute_code(func, arg):
    return func + '(' + arg + ')' + ';'

if __name__ == "__main__":
    if len(argv) == 2:
        encoded =  static_variables()
        encoded += encoder()
        print(f"Encoded Code: {encoded}")
    else:
        print("Usage: python3 " + argv[0] + " \"<PHP CODE>\"")
        print("Example: python3 " + argv[0] + " \"system('id');\"")

