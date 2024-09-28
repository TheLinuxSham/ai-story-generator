from flask import Flask, render_template, request, send_file, redirect, url_for
from werkzeug.utils import secure_filename
from llm import run_llm
from manage_text import get_filenames_from_uploads, get_text_from_pdf_file, list_personas, \
    list_user_stories, allowed_file_extensions, sanitize_string_for_list, write_to_txt, \
    sanitize_string_from_html
import os

app = Flask(__name__)


# display index website
@app.route("/")
def index():
    filenames = get_filenames_from_uploads()
    return render_template(
        "index.html",
        filenames=filenames,
        personas=list_personas,
        user_stories=list_user_stories,
    )


# route to append text to list
@app.route("/input/text", methods=["POST"])
def text_upload():
    text = request.form["text"]
    list_personas.append(text)
    return redirect(url_for('index'))


# route to upload pdf files
@app.route("/input/upload", methods=["POST"])
def file_upload():
    if request.method == "POST":
        files = request.files.getlist("file")
        for file in files:
            filename = secure_filename(file.filename)
            if file and allowed_file_extensions(file.filename) is True:
                file.save(f"fileuploads/{filename}")
            else:
                return f"Die Datei wurde nicht hochgeladen.\nPDF (*.pdf) erwartet, hochgeladen wurde: {file.filename}"
    return redirect(url_for('index'))


# route to delete or parse pdf files
@app.route("/backend/manage/files", methods=["POST"])
def manage_uploads():
    selected_filenames = request.form.getlist("filename_checkbox")
    action = request.form.get("filenamesSelection")
    if action == "deleteFile":
        for filename in selected_filenames:
            os.remove(f"fileuploads/{filename}")
    if action == "parseFile":
        for filename in selected_filenames:
            text = get_text_from_pdf_file(f"fileuploads/{filename}")
            list_personas.append(text)
    return redirect(url_for('index'))


# route to delete text that has been saved to a list in manage_text.py
@app.route("/backend/manage/personas", methods=["POST"])
def manage_personas():
    selected_personas = request.form.getlist("persona_checkbox")
    action = request.form.get("parsedTextSelection")
    if action == "delete":
        for persona in selected_personas:
            persona = sanitize_string_from_html(persona)
            if persona in list_personas:
                list_personas.remove(persona)
    return redirect(url_for('index'))


# route to generate user stories with text from list_personas in manage_text.py
@app.route("/backend/llm/generate_text", methods=["GET", "POST"])
def artificial_intelligence():
    if request.method == "GET":
        for persona in list_personas:
            sanitize_string_for_list(run_llm(persona), "*", list_user_stories)
        return redirect(url_for('index'))
    if request.method == "POST":
        return redirect(url_for('index'))


# route to either delete existing user stories or generate new ones. Will append to list_user_stories in manage_text.py
@app.route("/backend/manage/user_stories", methods=["POST"])
def manage_user_stories():
    selected_user_stories = request.form.getlist("user_story_checkbox")
    action = request.form.get("userStorySelection")
    if action == "delete":
        for user_story in selected_user_stories:
            user_story = sanitize_string_from_html(user_story)
            if user_story in list_user_stories:
                list_user_stories.remove(user_story)
    if action == "regenerate":
        for user_story in selected_user_stories:
            list_user_stories.append(run_llm(user_story, generate="redo"))
    return redirect(url_for('index'))


# route to fetch all user stories in list_user_stories and append them to a txt. Can be downloaded
@app.route("/backend/download/txt", methods=["GET"])
def download():
    filepath = "output.txt"
    write_to_txt(list_user_stories, filepath)
    if os.path.exists(filepath):
        return send_file(filepath, as_attachment=True)
    else:
        return "File not found!", 404


if __name__ == "__main__":
    app.run()
