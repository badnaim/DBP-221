# 1. Жагсаалтад 'python', 'php', 'java' гэсэн утгуудыг хадгал. Жагсаалт дахь байрлалыг ашиглан эдгээр утга бүрийг хэвлэ.
data = ['python', 'php', 'java']
for i in data:
    print(i)

# 2. 10 гишүүн бүхий тоон жагсаалт үүсгэ. Жагсаалтын нийлбэрийг давталт ашиглан хэвлэ.
data1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum = 0

for one in data1:
    sum += one

print("sum of numbers", sum)

# 3. 5 гишүүн бүхий тоон жагсаалт үүсгэ. Жагсаалтын гишүүдийн үржвэрийг хэвлэх функц бич. Үр дүнг хэвлэ.
data2 = [1, 2, 3, 4, 5]

def myFunctionOne(data):
    first = 1
    for one in data:
        first = first * one
    print(data[0],"ees", data[-1], "-iin", "urjwer =", first)


myFunctionOne(data2)

# 4. Өгөгдсөн тоон жагсаалтын 3 дахь элементийг сүүлийн сүүлийн элементтэй үржүүлэн үр дүнг буцаадаг функц бич.

def myFunctionTwo(data):
    one = data[2]
    two = data[-1]
    print(one * two)

myFunctionTwo([1, 2, 3, 4, 5])

#5.Өгөгдсөн тоон жагсаалтаас хамгийн их болон хамгийн бага утгуудыг буцаах функц бич. Үр дүнг хэвлэ.

def myFunctionThree(data):
    if len(data) == 0:
        print("0 number")
    else:
        maximum = max(data)
        minimum = min(data)
        return maximum, minimum

data3 = (1, 3, 5, 2, 8, 4)
max, min = myFunctionThree(data3)

print("max =", max, "min =", min)

#6. Өгөгдсөн жагсаалтаас хоёроос дээш оронтой, эхний болон төгсгөлийн тэмдэгтүүд нь
#хоорондоо адилхан гишүүн хэд байгааг тоолох функц бич.
#Жишээ: Оролт [abdba, abcd, 121 ], Гаралт 2

data4 = ["abdba", "abcd", 121 ]

def myFunctionFour(data):
    i = 0
    for one in data:
        if type(one) == str:
            if one[0] == one[-1]:
                i += 1
            else:
                i += 0
        if type(one) == int:
            oneStr = str(one)
            if oneStr[0] == oneStr[-1]:
                i += 1
            else:
                i += 0

    print("task 6:", i)

myFunctionFour(data4)

#7. Өгөгдсөн жагсаалтаас давхардсан утгуудыг арилгаж, хэвлэ.
#Жишээ: Оролт [abdba, abcd, 121, 121, abcd ], Гаралт [abdba, abcd, 121 ]
def myFunctionFive(data):
    arra = []
    for i in data:
       if i not in arra:
            arra.append(i)
    print("arra", arra)

data5 = ["abdba", "abcd", 121, 121, "abcd"]
myFunctionFive(data5)

#8. Жагсаалт хоосон эсэхийг шалгах функц бич. Үр дүнг хэвлэ.

def myFunctionSix(data):
    if len(data) == 0:
        print("ene list hooson bna")
    else:
        print("ene list hooson bish bna")

data6 = []
myFunctionSix(data6)

#9. 10 гишүүн бүхий жагсаалтын 4, 6, 8 дахь гишүүдийг устгаж, хэвлэ.

data7 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

del data7[7]
del data7[5]
del data7[3]

print("deleted 4 6 8 indexes ", data7)

#10. Тоон гишүүн бүхий tuple үүсгэ.

tuple = (1, 2, 3, 4, 5)

#11. Tuple –д гишүүн нэмэх програм бич.

new_tuple = tuple + (6,)
print("tuple", tuple)

#12. Tuple –ийн 2 дахь элемент болон араасаа 2 дахь элементийг хэвлэ.

print(tuple[1], tuple[-1])

#13. Tuple –д гараас оруулсан утга байгаа эсэхийг шалгах програм бич.

if tuple != new_tuple:
    print("garaar element nemegdeegui bn")
else:
    print("garaar too nemegdsen bn")

#14. Өгөгдсөн Tuple –ийн бүх гишүүдийг давталт ашиглан хэвлэ.

for i in tuple:
    print(i)

#15. 2 төрлийн set үүсгэн хооронд нь нэгтгэх програм бич

#set1 = set([1, 2, 3, 4, 5])
#set2 = set([4, 5, 6, 7, 8])

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

union_set = set1.union(set2)
print("Union set:", union_set)

#16. 2 төрлийн set үүсгэн аль алинд байгаа утгыг олох програм бич.

common_elements = set1.intersection(set2)

if common_elements:
    print("Common elements found:", common_elements)
else:
    print("No common elements found")

#17. Өгөгдсөн set-ийн уртыг ол

length = len(set1)
print("length = ", length)

#18. Өгөгдсөн set-ээс гараас оруулсан утгыг устга.

#new_numb = input("add a number: ")
#print(new_numb)

#removedSet = set1.discard(int(new_numb))
#print("removed: ", set1)

#19. Өгөгдсөн set-ийн бүх утгыг устга.

my_set = {1, 2, 3, 4, 5}

my_set.clear()

print("cleared:", my_set)

#20. Өгөгдсөн set-ийг устга.

del my_set

#21. Key, value нь тоон утга бүхий dictionary үүсгэж өсөх болон буурахаар эрэмбэл.

dictionary = {
    "firstVal": 1,
    "thirdVal": 3,
    "secondVal": 2
}

sorted_value = sorted(dictionary.values())
print("sorted", sorted_value)

#22. Өгөгдсөн key нь dictionary –д байгаа эсэхийг шалгах програм бич

if "firstVal" in dictionary:
    print("yes it is in")
else:
    print("no")

#23. Өгөгдсөн value нь dictionary –д байгаа эсэхийг шалгах програм бич.

if 1 in dictionary.values():
    print("yes it is in")
else:
    print("no")

#24. For давталт ашиглан dictionary –ийн key, value –г хэвлэх програм бич

for key, value in dictionary.items():
    print(f"Key: {key}, Value: {value}")

#25. Хоёр dictionary үүсгэж хооронд нь нэгтгэ.

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

merged_dict = {**dict1, **dict2}

print("merged_dict", merged_dict)

#26. Dictionary –д байгаа value хооронд нь нэмэх програм бич.

for value in dictionary.values():
    i = 0
    i += value
print("sum",i)