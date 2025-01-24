

# 문제에 대해 출력만 하는 함수
def questionOnlyPrint(arg_question, arg_answer):
    for number, string in enumerate(arg_question):
        print(str(number+1)+'.', string)
        for ansnumber, ansstrstring in enumerate(arg_answer):
            print(str(ansnumber+1)+'.', ansstrstring, end='\t\t')
        print('\n----------')
    return

# 문제에 대해 입력을 받아 입력받은 숫자 문자 리스트를 리턴하는 함수
def questioninput(arg_question, arg_answer):
    resultStrList = []

    for number, string in enumerate(arg_question):
        print(str(number+1)+'.', string)
        for ansnumber, ansstrstring in enumerate(arg_answer):
            print(str(ansnumber+1)+'.', ansstrstring, end='\t\t')
        print()
        resultStrList.append(input(''))
        print('----------')

    return resultStrList

list_question = [
    "상품의 품질에 대해 어떻게 생각하시나요?",
    "상품의 가격에 대해 어떻게 생각하시나요?",
    "상품의 디자인에 대해 어떻게 생각하시나요?",
    "상품에 대한 전반적인 만족도는 어떠신가요?"
]

list_answer =  ["좋음", "중간", "좋아지길"]


questionOnlyPrint(list_question, list_answer)
inputStrList = questioninput(list_question, list_answer)

# 입력받은 리스트를 출력하는 함수
for strIndex in inputStrList:
    print(strIndex+'.', list_answer[(int(strIndex)-1)], end='\t\t')

print('\n----------')
