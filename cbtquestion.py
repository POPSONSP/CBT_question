"""
PROJECT:
Write a cbt theory programme for a school whereby the students will be requested to sit for an exam,
respond to 10 random cbt  questions and at the end of the exams the score will be printed
"""
import time
questions=["1. Where is Sqi situated ?", "2.Who is the founder of twitter ?", "3.What is the full meaning of ECOWAS ?", 
           "4.SQI is what type of School ?", "5. Who is the president of Nigeria ?",
             "6. Who is the elected president in the 2023 election ?",
           "7.Nigeria National flag has how many colours ?", "8. Water refered to as tasteful,colourful and enzymes filled is said to be ?", 
           "9. Python can be refered to as ?", "10.Charges regarded as been positievely charged is know as ?"]
options= ["a. ABUJA \n b.KANO \n c. LAGOS \n d. IBADAN", "a. Anthony Taylor \n b.Mark Zugerberg \n c.Mike Oliver \n d. Elon Musk", 
          "a.ECONOMIC COMMUNITY OF WEST AFRICA STATES  /n b. ECONOMIC COMMON WEALTH AND STATES \n c. ECONOMIC Uninion of west African state \n d. Economic State of West Africa State.",
          "a.Buisness \n b. Marketing \n c. Coding \n d.Agency", "a. Olusegun Obasanjo \n b. Oluyemi Osinbanjo \n C. Muhammed Buhari \n d.Bola Hammed Tinubu",
          "a. Peter Obi \n b. Atiku Abubakar \n c. Bola Tinubu d. Kola Oladeju", "a.3 \n b. 2 \n c. 4 \n d. none", 
          "a. Good \n b. Juice \n c. bad \n d. fair", "a. Calculating tool \n b. Writing tool \n c. Mind Expressing channel \n d. Programming Language", 
          "a.Neutron \n b. Electron \n c. potron \n d. proton"]
answers= ["d", "b", "a", "c", "c", "c", "b", "c","d", "d"]
score = 0
for p in range(10):
    print(questions[p])
    time.sleep(1)
    print(options[p])
    user_answer = input("Enter your most prefered answer: ")
    if user_answer == answers[p]:
        print("Correct")
        score += 10
    else:
        print("Wrong")
        score -= 5

print(f"Congrats, Your exam is over and your total score is {score}")
