### بخش کاتبخانه ها moudles و تابع ها ###
import math as m
import json as j
import os
def addition ( x1 ,x2 ) :
    """ تابع برای مجموع گرفتن دو عدد است """
    result = float ( x1 ) + float ( x2 )
    return result 
def subtraction ( x1 , x2 ) :
    """ تابع برای منها کردن """
    result = float ( x1 ) - float ( x2 )
    return result 
def multiplication ( x1 , x2 ) :
    """ تابع برای ضرب کردن """
    result = float ( x1 ) * float ( x2 )
    return result
def division ( x1 , x2 ) :
    """ تابع برای تقسم کردن """
    try  :
        result = float ( x1 ) / float ( x2 )
        return result
    except ZeroDivisionError :
        return str ( "Error: Division by zero" ) 
def power ( x1 , x2 ) :
    """ تابع برای به توان رساندن یعنی هم عدد و هم توان را میتوان مشخص کرد """
    result = float ( x1 ) ** float ( x2 )
    return result
def square_root ( x1 ) :
    """ این تابع برای گرفتن رادیکال است """
    result = m.sqrt ( float ( x1 ) )
    return result
def absolute_value ( x1 ) :
    """ این تابع برای گرفتن قدر مطلق است """
    result = abs ( float ( x1 ) ) 
    return result
def remaining ( x1 , x2 ) :
    """ این تابع برای گرفتن باقی مانده یک تقسیم است """
    result = float ( x1 ) % float ( x2 ) 
    return result
def percentage (x1 , per ) :
    """ این تابع برای گرفتن x درصد از یک عدد است (x یعنی به عدد دلخواه) """
    result = ( float ( x1 ) * float ( per ) ) / 100
    return result 
def save ( x1 , x2 , operation , result ) :
    """ برای ذخیره کردن اطلاعات تاریخچه در فایل و این تابع 4 آرماگون دارد json استفاده می شود """
    with open ( "history.json" , "a" ) as file :
            history = {
                "num1" : x1 ,
                "operation" : operation ,
                "num2" : x2 ,
                "result" : result
                      }
            j.dump ( history , file )
            file.write ( "\n" )
def load ( ) :
    """ این تابع برای برگرداندن مقادیر تابع save () است """
    try :
        with open ( "history.json" , "r" ) as file :
            data =[]
            for line in file :
                line = line.strip (  )
                data.append ( line )
        if data == list ( [] ) :
            print ( "Thre's no history yet." )
        else :
            data.reverse ( )
            for item in range ( len ( data ) ) :
                show_data = j.loads ( data [ item ] )
                if show_data [ "operation" ] == "||" :
                    print ("|" + show_data [ "num1" ] + "|" , "=" , show_data [ "result" ] )
                elif show_data [ "operation" ] == "**" :
                    print ( "sqart" , show_data [ "num1" ] , "=" , show_data [ "result" ] )
                elif show_data != None :
                    print ( show_data [ "num1" ] , show_data [ "operation" ] , show_data [ "num2" ], "=" , show_data [ "result" ] ) 
    except FileNotFoundError :
        with open ( "history.json" , "x" ) :
            print ( "Thre's no history yet." )
### بخش اصلی و مربوط به قسمت های اجرایی توابع ###
load ()
while True :
    choice = input ( "please choice the operation you wish to perform and Enter help to display operations: " )
    if choice == "help":
        print ( "+ for Addition \n - for  subtraction \n * for multiplication \n / for division and // for remaining division \n ^ for power \n ** for square root \n || for absolute value \n % for percentage  \n exit for to close app \n clear history for clear history" )
    elif choice == "clear history" :
        with open ( "history.json" , "w" ) :
            pass
        print ( "clear history successful" )
    elif choice == "exit" :
        print ( " exit successful" )
        break
    elif choice == "+" :
        x1 = input ( "enter number 1: " )
        x2 = input ( "enter number 2: " )
        print ( x1 , "+" , x2 , "=" , addition ( x1 , x2 ) )
        save ( x1 , x2 , "+" , addition ( x1 , x2 ) )
    elif choice == "-" :
        x1 = input ( "enter number 1: " )
        x2 = input ( "enter number 2: " )
        print ( x1 , "-" , x2 , "=" , subtraction ( x1 , x2 ) )
        save ( x1 , x2 , "-" , subtraction ( x1 , x2 ) )
    elif choice == "*" :
        x1 = input ( "enter number 1: " )
        x2 = input ( "enter number 2: " )
        print ( x1 , "*" , x2 , "=" , multiplication ( x1 , x2 ) )
        save ( x1 , x2 , "*" , multiplication ( x1 , x2 ) )
    elif choice == "/" :
        x1 = input ( "enter number 1: " )
        x2 = input ( "enter number 2: " )
        print ( x1 , "/" , x2 , "=" , division ( x1 , x2 ) )
        save ( x1 , x2 , "/" , division ( x1 , x2 ) )
    elif choice == "//" :
        x1 = input ( "enter number 1: " )
        x2 = input ( "enter number 2: " )
        print ( x1 , "//" , x2 , "=" , remaining ( x1 , x2 ) )
        save ( x1 ,x2 , "//" , remaining ( x1 , x2 ) )
    elif choice == "^" :
        x1 = input ( "enter number 1: " )
        x2 = input ( "enter number 2: " )
        print ( x1 , "^" , x2 , "=" , power ( x1 , x2 ) )
        save ( x1 , x2 , "^" , power ( x1 , x2 ) )
    elif choice == "**" : 
        x1 = input ( "enter number for sqart: " )
        print ( "sqart" , x1 , "=" , square_root ( x1 ) )
        save ( x1 , None , "**" , square_root ( x1 ) )
    elif choice == "||" :
        x1 = input ( "enter number for absolute: " )
        print ("|" + x1 + "|" , "=" , absolute_value ( x1 ) )
        save ( x1 , None , "||" , absolute_value ( x1 ) )
    elif choice == "%" :
        x1 = input ( "enter number: " )
        per = input ( "enter percentage number: %" )
        print ( x1 , "%" , per , "=" , percentage ( x1 , per ) )
        save ( x1 , per , "%" , percentage ( x1 , per ) )