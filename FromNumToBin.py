#input positive integer and get the int in bin
import math

def ArrayToBin(arr, num):#פעולה שמקבלת מערך של מספרים מבסיס 2 ואת המספר הנקלט
    BinArr = []#מערך עבור המספר הבינארי שיוחזר
    i = len(arr)-1#נגדיר אינדקס ממנו נתחיל לסרוק במערך מהסוף להתחלה
    while(i!=-1):
        if(arr[i]<=num):#אם הספרה מבסיס 2 קטנה או שווה למספר הנקלט
            num -= arr[i]#פעלת חיסור מהמספר הנקלט
            BinArr += [1]#הביט דלוק לכן הוסף 1
            i -= 1#תוריד מערך האינדקס
        else:
            BinArr += [0]#הביט לא נדלק אז הוסף 0
            i -=1#תוריד מערך האינדקס
    return BinArr#תחזיר מערך המרכיב את המספר הבינארי של המספר הנקלט

def FindNegative(arr):#פעולת משלים ל 2
#פעולה המקבלת מערך בינארי המייצג מספר ומחזירה מערך בינארי המייצג את המערך כמספר שלילי
    for i in range(len(arr)):#not פעולת 
        if(arr[i]==0):
            arr[i] = 1
        else:
            arr[i] = 0
    TowInBin = []#הגדרת מערך בינארי עבור המספר 2
    for i in range(len(arr)-2):#בניית המערך
        TowInBin += [0]
    TowInBin += [0]
    TowInBin += [1]

    #not הוספת 1 למספר ה 
    flag = True#הגדרת דגל
    NegBinNum = []#הגדרת מערך למספר השלילי שיוחזר
    for j in range(len(arr)-1, -1, -1):#סריקת המערך של 2 והמערך של המספר הבינארי מהסוף להתחלה
        if(flag==False):#אם לא הועלה 1 למעלה
            if(arr[j]+TowInBin[j]+1==2):#אם עולה 1 למעלה
                NegBinNum += [0]#תוסיך 0
                flag = False#תסמן לטובת האיטרציה הבאה
            else:
                NegBinNum += [arr[j]+TowInBin[j]+1]#בצע פעולת חיבור רגילה
                flag = True#בטל את הסימון
        elif(arr[j]+TowInBin[j]==2):#אם עולה 1 למעלה
            NegBinNum += [0]#תוסיף 0
            flag = False#תסמן לטובת האיטרציה הבאה
        else:
            NegBinNum += [arr[j]+TowInBin[j]]#בצע פעולת חיבור רגילה

    return NegBinNum#תחזיר מערך המרכיב את המספר הבינארי השלילי של המספר הנקלט

num = int(input("Enter a number: "))#קלוט מספר
NumOfBits = int(input("Enter the number of bits (in base 2): "))#קלוט את כמות הביטים בהם המספר ייוצג
while(math.log(NumOfBits, 2).is_integer() is False):#בדיקה האם כמות הביטים היא בבסיס 2
    print("The num must be in base 2, try again...")
    NumOfBits = int(input("Enter the number of bits (in base 2): "))

BaseTowList = []#יצירת מערך המרכיב מספרים מבסיס 2
i = 0#הגדרת אינדקס
while(i!=NumOfBits):#בניית מערך ביטים כרצון המשתמש
    BaseTowList += [pow(2,i)]
    i = i+1
BinNumArr = ArrayToBin(BaseTowList, num)
for j in range(len(BinNumArr)):
    print(BinNumArr[j], end=' ')
    #הדפסת המספר הבינארי של המספר הנקלט בעזרת סריקת מערך בו נמצאים הביטים
NegativeBinNumArr = FindNegative(BinNumArr)
print("\nNegative number: ")
for k in range(len(NegativeBinNumArr)-1, -1, -1):
    print(NegativeBinNumArr[k], end=' ')
    #הדפסת המספר הבינארי השלילי של המספר הנקלט בעזרת סריקת המערך בו נמצאים הביטים