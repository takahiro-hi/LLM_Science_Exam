import pandas as pd
import numpy as np
import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration
from prompt_utils import construct_prompt



def main():

    """
        load dataset
    """
    train_df = pd.read_csv("/kaggle/input/kaggle-llm-science-exam/train.csv", index_col="id")
    test_df = pd.read_csv("/kaggle/input/kaggle-llm-science-exam/test.csv", index_col="id")
    
    train_df = train_df.assign(prediction = None)
    test_df= test_df.assign(prediction = None)


    """
        setting
    """
    llm_path = "/kaggle/input/flan-t5/pytorch/xl/3"
    device = "cuda-0" if torch.cuda.is_available() else "cpu"
    
    tokenizer = T5Tokenizer.from_pretrained(llm_path)
    model = T5ForConditionalGeneration.from_pretrained(llm_path, device_map="auto")


    """
        create answer
    """
    for index in range(len(test_df)):
        
        prompt = construct_prompt(test_df.iloc[index, :])    
        input_ids = tokenizer(prompt, return_tensors="pt").input_ids.to("cuda")
        
        if len(input_ids) > tokenizer.model_max_length:
            print(f"Error <{index}>, num_tokens:{len(input_ids)}")
            
        with torch.no_grad():
            outputs = model.generate(input_ids)
            test_df.loc[index]["prediction"] = tokenizer.decode(outputs[0], skip_special_tokens=True)


    """
        reshape answers
    """
    test_df= test_df.assign(submission = None)

    for index in range(len(test_df)):
        
        labels = ["A", "B", "C", "D", "E"]
        label = test_df.loc[index]["prediction"]
        
        labels.remove(label)
        
        test_df.loc[index]["submission"] =  label+" "+ " ".join(labels)


    """
        make submission
    """
    submission = pd.read_csv("/kaggle/input/kaggle-llm-science-exam/sample_submission.csv", index_col="id")
    submission["prediction"] = test_df['submission']

    submission.to_csv('submission.csv')




if __name__=="__main__":
    main()

