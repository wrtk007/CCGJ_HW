koex = "한국어 테스트"
enex = "English test xoxo"
deex = "Deutsch test äÖ"

#ord는 char가 무슨 ascii 코드인지 알려줌
#python은 아스키 코드 베이스
"""def detectLang(comment) :
    for i in range(len(comment)) :
        print("{} : {}".format(comment[i],ord(comment[i])))
"""

#utf-8로 encode
def detectutf(comment) :
    unicode_string = comment.encode("utf-8")
    return unicode_string

#utf-8이 어떤 문자에 속하는지
#utf-8로 나온 숫자의 범위로?
"""def detectLang(unicode_string) :
    if Latin : 
    elif Hangeul :
    elif ChineseChar :
    elif JapaneseChar :
    elif Arab : 
    else :
        #태국어, 키릴문자 등
"""