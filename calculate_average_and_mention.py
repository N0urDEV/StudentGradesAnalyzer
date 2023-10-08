note1 = float(input("Please enter the first grade (out of 20): "))
note2 = float(input("Please enter the second grade (out of 20): "))
note3 = float(input("Please enter the third grade (out of 20): "))
moyenne = (note1 + note2 + note3) / 3
if moyenne >= 16:
        mention = "Excellent"
elif 14 <= moyenne < 16:
        mention = "Very Good"
elif 12 <= moyenne < 14:
        mention = "Good"
elif 10 <= moyenne < 12:
        mention = "Passable"
else:
        mention = "Insufficient"
print("The student's average is:", moyenne)
print("Mention:", mention)
