koex = "힣힣 한국어 테스트"
jpex = "こんにちは"
arex = "أحبك"
enex = "English test xoxo"
deex = "kaufen"

#ord는 char가 무슨 ascii 코드인지 알려줌
#python은 아스키 코드 베이스
def detectAscii(comment) :
    for i in range(len(comment)) :
       # print("{} : {}".format(comment[i],ord(comment[i])))
        print(comment[i])
        return ord(comment[i])

#utf-8로 encode
"""def detectutf(comment) :
    uni_no = comment.encode("utf-8")
    return uni_no
"""

#utf-8이 어떤 문자에 속하는지
#utf-8로 나온 숫자의 범위로?
def detectLang(uni_no) :
    if ((65 <= uni_no <= 90) or (97 <= uni_no <= 122)) :
        print("Latin 문자") 
    elif ((44032 <= uni_no <= 55203) or (12593 <= uni_no <= 12643)): 
        print("한글 문자")
    elif ((12353 <= uni_no <=12435) or (12448 <= uni_no <=12534)) :
        print("일본 문자")
    elif (1536 <= uni_no <= 1791) :
        print("아랍 문자") 
    #else :
        #태국어, 키릴문자"""

ko = detectAscii(koex)
en = detectAscii(enex)
de = detectAscii(deex)
jp = detectAscii(jpex)
ar = detectAscii(arex)


print("한국어 예시 : " + koex + "  한국어 첫 글자 " + str(ko),end="  ")
detectLang(ko)
print("영어 예시 : " + enex +"  영어 첫 글자 " + str(en), end="  ")
detectLang(en)
print("독일어 예시 : " + deex + "  독일어 첫 글자 " + str(de), end="  ")
detectLang(de)
print("일본어 예시 : " + jpex + "  일본어 첫 글자 " + str(jp), end="  ")
detectLang(jp)
print("아랍어 예시 : " + arex + "  아랍어 첫 글자 " + str(ar), end="  ")
detectLang(ar)