koex = "한국어 테스트"
chex = "我愛你"
jpex = "こんにちは"
arex = "مرحبًا"
enex = "English test xoxo"
deex = "Deutsch test äÖ"

#ord는 char가 무슨 ascii 코드인지 알려줌
#python은 아스키 코드 베이스
def detectAscii(comment) :
    for i in range(len(comment)) :
       # print("{} : {}".format(comment[i],ord(comment[i])))
        return ord(comment[i])

#utf-8로 encode
"""def detectutf(comment) :
    uni_no = comment.encode("utf-8")
    return uni_no
"""

#utf-8이 어떤 문자에 속하는지
#utf-8로 나온 숫자의 범위로?
def detectLang(uni_no) :
    if ((uni_no>65 and uni_no<90) or (uni_no>97 and uni_no<122)) :
        print("Latin문자") 
""" elif Hangeul :
    elif ChineseChar :
    elif JapaneseChar :
    elif Arab : 
    else :
        #태국어, 키릴문자"""

ko = detectAscii(koex)
en = detectAscii(enex)
de = detectAscii(deex)

print("한국어 예시 : " + koex + "  한국어 첫 글자 " + str(ko))
detectLang(ko)
print("영어 예시 : " + enex +"  영어 첫 글자 " + str(en), end="  ")
detectLang(en)
print("독일어 예시 : " + deex + "  독일어 첫 글자 " + str(de), end="  ")
detectLang(de)