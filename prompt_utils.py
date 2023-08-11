def construct_prompt(df):

    prompt = ""

    preamble = """You are given one question and five statements. 
You should select one statements which is best answer for given question.

==========
# Example
question: Who was the first person to describe the pulmonary circulation system?

A) Galen
B) Avicenna
C) Hippocrates
D) Aristotle
E) Ibn al-Nafis

Answer: E
==========

Now, let's begin!
"""

    prompt += preamble

    prompt += "question: " + df["prompt"] + "\n\n"
    for label in ["A", "B", "C", "D", "E"]:
        prompt += label + "): " + df[label] + "\n"

    prompt += "\nAnswer: "

    
    return prompt
