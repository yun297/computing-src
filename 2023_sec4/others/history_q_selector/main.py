import random

questions = {
    "Boom & Bust": [
        "What were the causes of the boom of the 1920s?",
        "How did the boom impact different groups of people?",
        # "Did the boom benefit all Americans? Which groups benefitted and who did not?",
        "What were the causes of the Great Depression?",
        "How did the Great Depression impact different groups of people?"

    ], 
    "The New Deal": [
        "What were the aims of the New Deal?",
        "What methods/agencies did the New Deal employ?",
        "What were the aims of the various alphabet agencies?",
        "Were the alphabet agencies successful?",
        "What were the successes of the New Deal?",
        "In what ways was the New Deal not very successful?"
    ],
    "The Cold War": [
        "What were the causes of the Cold War?",
        "What roles did the USA and USSR play in causing the Cold War?",
        # "What were some impacts of the Cold War?"

    ],
    "Korean War": [
        "What were the causes of the Korean War?",
        "What were the impacts of the Korean War?"

    ]
}

topics = [
    "Boom & Bust",
    "The New Deal",
    "The Cold War",
    "Korean War"
]

def generate():
    rand_topic = topics[random.randint(0, 3)]
    rand_question = questions[rand_topic][random.randint(0, len(questions[rand_topic]) - 1)]

    print(rand_topic + ":", rand_question, end = "\n\n")
    
    generate_again = input("Generate? Hit \"ENTER\" to continue. ")
    if generate_again == "":
        generate()
    else:
        exit()
        
generate()