### Description

This program translates English PDF files into languages you want. It parses the text in your input file and translate using OpenAI GPT 3.5. The output would be generated and stored in HTML file(s). 

### Usage

Before running PDF translation, make sure to store your OpenAI API key in environment variable. `pip install PyPDF2 openai` to install PyPDF and OpenAI libraries. 

Store your API key as environment variable. Use `python3 translate.py` and then enter path to your input PDF file. The program generates HTML files, the number of which depending on the number of pages in your input file.

For now, the default LLM is GPT 3.5, the default target language is Chinese (simplified). If you want to customize, you'll have to go to the source code to make changes.
