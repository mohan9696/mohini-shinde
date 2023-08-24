def f1(mark):
    total = sum(mark)
    average = total / len(mark)
    return average
physics_score = 80
chemistry_score = 79
maths_score = 70
english_score = 84
mark = [physics_score, chemistry_score, maths_score, english_score]
s1 = f1(mark)
print( s1, "%")