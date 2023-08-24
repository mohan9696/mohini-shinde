def decor_result(result_function):
    def distinction(marks):
        for m  in marks:
            if m>=74:
                print("Distinction")
        result_function(marks)
    return distinction
#@decor_result
def result(marks):
    for m in marks:
        if m>=35:
            pass
        else:
            print("FAIL")
            break
    else:
        print("PASS");
result([50,60,32,34,45,75,76,79,84])