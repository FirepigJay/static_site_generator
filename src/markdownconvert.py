import re

def extract_markdown_images(text:str) -> list[str]:
    image_text = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return image_text

def extract_markdown_links(text:str) -> list[str]:
    link_text = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return link_text