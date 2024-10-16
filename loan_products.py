

def run(questions = None):
    print()
    print()

    correct_num = 0
    for num, q in enumerate(questions, start=1): 
        print("Question " + str(num) + ": " + q["question"])
        for o in q["options"]:
            print(o)
        respond = input("Your answer (A, B, C, or D):").upper()  
        if respond == q["answer"] :
            print("Correct!")
            correct_num+=1
        else:
            print("Wrong. The correct answer is "+q["answer"])
        print()
        print()

    print("Quiz Completed! Your total score is: "+str(correct_num)+"/"+str(len(questions)))
    return 



def main():
    # 금융 상품 관련 문제 리스트
    questions = [
        {
            "question": "What is the main feature of a fixed deposit?",
            "options": ["A. High liquidity", "B. Fixed interest rate", "C. No maturity period", "D. High risk"],
            "answer": "B"
        },
        {
            "question": "Which of the following is a type of government security?",
            "options": ["A. Treasury bonds", "B. Corporate bonds", "C. Mutual funds", "D. Fixed deposits"],
            "answer": "A"
        },
        {
            "question": "What does APR stand for in loans?",
            "options": ["A. Annual Percentage Rate", "B. Average Payment Rate", "C. Accumulated Payment Ratio", "D. Annual Payment Ratio"],
            "answer": "A"
        },
        {
            "question": "Which investment option is considered the safest?",
            "options": ["A. Stocks", "B. Bonds", "C. Savings account", "D. Real estate"],
            "answer": "C"
        },
        {
            "question": "What is the primary benefit of compound interest?",
            "options": ["A. Lower taxes", "B. Faster wealth accumulation", "C. Increased liquidity", "D. Fixed interest rates"],
            "answer": "B"
        }
    ]

    run(questions)
    return 

if __name__ == "__main__":
    main()
