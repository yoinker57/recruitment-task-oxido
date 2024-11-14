from openai import OpenAI
import os

key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=key)


def read_article(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print(f"File {filename} not found.")
        exit(1)


def process_article(article_content):
    prompt = f"""Convert the following article into HTML format according to these guidelines:
HTML Structure: Use appropriate HTML tags, such as <h1>, <h2>, <p>, <ul>, <ol>, etc., to structure and organize the content clearly.
Image Placement: Identify sections where images could enhance the content, and insert an <img> tag with the attribute src="image_placeholder.jpg".
Each image should include an alt attribute with a detailed prompt that we can use to generate the image.
Add a caption under each image using an appropriate HTML tag, like <figcaption>.
No CSS or JavaScript: The returned HTML should only include content meant to go between <body> and </body> tags.
Do not include <html>, <head>, <body>, or `html` code blocks around the result.
Here is the article to convert:

{article_content}

Return the resulting HTML code in a ready-to-use format without any additional sufixes or prefixes."""

    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant that converts articles into HTML format.",
        },
        {"role": "user", "content": prompt},
    ]

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
        )
    except Exception as e:
        print(e)
        exit(1)

    return response.choices[0].message.content


def save_as_html(content, filename="artykul.html"):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)


if __name__ == "__main__":
    article_file = "artykul.txt"
    article_content = read_article(article_file)
    html_content = process_article(article_content)
    save_as_html(html_content)
