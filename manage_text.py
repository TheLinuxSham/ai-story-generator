from pypdf import PdfReader
import re
import os

pdf_file_dir = "./uploads"
list_personas = []
list_user_stories = []


def allowed_file_extensions(filename):
    if "." in filename and filename.rsplit(".", 1)[1].lower() == "pdf":
        return True
    else:
        return False


def get_filenames_from_uploads(path="fileuploads/"):
    filenames = []
    for filename in os.listdir(path):
        if os.path.isfile(os.path.join(path, filename)):
            if allowed_file_extensions(filename):
                filenames.append(filename)
    return filenames


def get_text_from_pdf_file(filepath: str):
    file = PdfReader(filepath)
    body = ""
    for page in file.pages:
        body = page.extract_text()
        body = re.sub(r"\r", "", body)
    try:
        return body
    except TypeError:
        print(
            f"Expected String for file parsing, but got following instead: {body}\n"

        )


def sanitize_string_from_html(input_string: str):
    input_string = re.sub(r"\r", "", input_string)
    return input_string


def sanitize_string_for_list(input_string: str, separator: str, target_list: list):
    pattern = r'[a-zA-Z.]'
    split_list = input_string.split(separator)
    for item in split_list:
        if re.search(pattern, item):
            sanitized_input_string = item.lstrip()
            sanitized_input_string = re.sub(r'\..*', '.', sanitized_input_string, count=1)
            target_list.append(sanitized_input_string)


def remove_existing_txt(filepath: str):
    if os.path.isfile(filepath):
        os.remove(filepath)


def write_to_txt(input_list: list, file_path: str):
    remove_existing_txt(file_path)
    with open(file_path, 'a') as file:
        for item in input_list:
            file.write(f"{item}\n")
