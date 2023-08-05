import pandas as pd
import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration
from prompt_utils import construct_prompt

def main():

    """
        load dataset
    """
    train_df = pd.read_csv("data/train.csv", index_col="id")
    test_df = pd.read_csv("data/test.csv", index_col="id")


    """
        setting
    """
    llm = '/kaggle/input/flan-t5/pytorch/base/2'
    device = "cuda-0" if torch.cuda.is_available() else "cpu"
    model = T5ForConditionalGeneration.from_pretrained(llm).to(device)
    tokenizer = T5Tokenizer.from_pretrained(llm)


    """
        create answer
    """
    for index in range(len(test_df)):
        prompt = construct_prompt(train_df.iloc[index, :])




if __name__=="__main__":
    main()

