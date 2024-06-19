import PyPDF2
from openai import OpenAI
import pdfkit
from utils import *
import os
# from transformers import GPT2Tokenizer



def translate(chunk: str, model='gpt-3.5-turbo', target_language="Chinese, simplified") -> str:
    """Translate a chunk of text."""
    client = OpenAI()
    prompt = f'Translate the following text from English to {target_language} (for locations, you can keep them in English): {chunk}'
    response = client.chat.completions.create(
        messages=[{"role": "user", "content":prompt}],
        model=model,
    )
    result = response.choices[0].message.content.strip()
    return result
    

def read_pdf(file_path: str) -> list:
    """Read pdf file. Each page converted to a string. Return a list of str."""
    pdf_reader = PyPDF2.PdfReader(open(file_path, 'rb'))
    text = []
    n = len(pdf_reader.pages)
    for page_num in range(n):
        page = pdf_reader.pages[page_num]
        text.append(page.extract_text())
    return text


def write_pdf(text: str, output_path: str):
    pdfkit.from_string(text, output_path)




if __name__ == "__main__":
    input_pdf_path = input("Enter your input PDF path: ")  
    # output_pdf_path = # input("Enter your output PDF path: ")  
    text = read_pdf(input_pdf_path)
    # print(tokenize(text))
   
 
    n = len(text)
    translated_txt = []
    try: 
        for idx in range(n):
            print("page ", str(idx+1))
            translated_txt.append(translate(text[idx]))
            # write to html output every 50 pages
            if idx+1 % 50 == 0 or idx == n-1:
               output_idx = int(idx / 50)
               write_to_html_2(translated_txt, f"output_{output_idx}.html") 
               translated_txt = [] # empty the translated text array 
    except Exception as e:
        print(f"An error occurs: {e} \n\n")
        print("Writing finished translated text pages to HTML output ...")
        write_to_html_2(translated_txt, f"output.html")
    
    
