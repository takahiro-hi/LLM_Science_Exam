def construct_prompt(df):

    prompt = ""

    preamble = """You are given one question and five statements. 
You should select one statements which is best answer for given question.
    
================================
## Example
question: Which of the following statements accurately descirbes the frame problem
    
A) It is difficult to systematize the vast amount of knowledge that humans possess.
B) It is difficult to solve any real-world problem using knowledge with finite information processing capacity.
C) It is difficult to connect symbols such as word strings with the meanings they represent.
D) It is difficult to develop fast computers to process huge amounts of knowledge.
E) It is difficult to develop the Internet to take sufficient data.
    
Answer: B
================================

Now, let's begin!
"""

    prompt += preamble

    prompt += "question: " + df["prompt"] + "\n\n"
    for label in ["A", "B", "C", "D", "E"]:
        prompt += label + "): " + df[label] + "\n"

    prompt += "\nAnswer: "

    
    return prompt