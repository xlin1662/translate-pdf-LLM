# from transformers import GPT2Tokenizer


# def count_token(chunk: str, tokenizer: GPT2Tokenizer) -> int:
#     return len(tokenizer.encode(chunk))


def write_to_html(text_list: list, output_html_path: str):
    with open(output_html_path, 'w', encoding='utf-8') as file:
        file.write('<!DOCTYPE html>\n')
        file.write('<html>\n')
        file.write('<head>\n')
        file.write('<meta charset="UTF-8">\n')
        file.write('<style>\n')
        file.write('@media print {\n')
        file.write('  .page { page-break-after: always; }\n')
        file.write('}\n')
        file.write('@media screen {\n')
        file.write('  .page { page-break-after: always; }\n')
        file.write('}\n')
        file.write('</style>\n')
        file.write('</head>\n')
        file.write('<body>\n')

        for text in text_list:
            # Replace newline characters with <br> tags
            html_text = text.replace('\n', '<br>\n')
            file.write('<div class="page">\n')
            file.write(f'<p>{html_text}</p>\n')
            file.write('</div>\n')

        file.write('</body>\n')
        file.write('</html>\n')



def write_to_html_2(text_list: list, output_html_path: str):
    with open(output_html_path, 'w', encoding='utf-8') as file:
        file.write('<!DOCTYPE html>\n')
        file.write('<html>\n')
        file.write('<head>\n')
        file.write('<meta charset="UTF-8">\n')
        file.write('<style>\n')
        file.write('@media print {\n')
        file.write('  .page { page-break-after: always; position: relative; }\n')
        file.write('  .page-number { position: absolute; bottom: 10px; right: 10px; }\n')
        file.write('}\n')
        file.write('@media screen {\n')
        file.write('  .page { page-break-after: always; position: relative; }\n')
        file.write('  .page-number { position: absolute; bottom: 10px; right: 10px; }\n')
        file.write('}\n')
        file.write('button { display: block; margin: 20px auto; }\n')
        file.write('</style>\n')
        file.write('<script>\n')
        file.write('function goToPage(pageId) {\n')
        file.write('  document.getElementById(pageId).scrollIntoView({ behavior: "smooth" });\n')
        file.write('}\n')
        file.write('</script>\n')
        file.write('</head>\n')
        file.write('<body>\n')

        for i, text in enumerate(text_list):
            # Replace newline characters with <br> tags
            html_text = text.replace('\n', '<br>\n')
            page_id = f'page-{i}'
            file.write(f'<div class="page" id="{page_id}">\n')
            file.write(f'<p>{html_text}</p>\n')
            if i < len(text_list) - 1:
                next_page_id = f'page-{i + 1}'
                file.write(f'<button onclick="goToPage(\'{next_page_id}\')">Next Page</button>\n')
            # Add the page number
            file.write(f'<div class="page-number">Page {i + 1}</div>\n')
            file.write('</div>\n')

        file.write('</body>\n')
        file.write('</html>\n')


""" 
def tokenize(text_arr: list):
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    res = []
    for page in text_arr:
        res.append(count_token(page, tokenizer))
    maximum, total = max(res), sum(res)
    return maximum, total 
"""