from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text: str, text_type: TextType, url: str | None = None) -> None:
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other) -> bool:
        if self.text == other.text and self.text_type == other.text_type and self.url == other.url:
            return True
        else:
            return False
        
    def __repr__(self) -> str:
        string = f'TextNode({self.text}, {self.text_type}, {self.url})'
        return string
    
def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    tag = None
    prop = None
    value = None
    if text_node.text_type == TextType.TEXT:
        value = text_node.text
    if text_node.text_type == TextType.BOLD:
        tag = 'b'
        value = text_node.text
    if text_node.text_type == TextType.ITALIC:
        tag = 'i'
        value = text_node.text
    if text_node.text_type == TextType.CODE:
        tag = 'code'
        value = text_node.text
    if text_node.text_type == TextType.LINK:
        tag = 'a'
        prop = {'href':text_node.url}
    if text_node.text_type == TextType.IMAGE:
        tag = 'img'
        prop = {'src': text_node.url, 'alt': text_node.text}
    
    return LeafNode(tag = tag, value = value, props = prop)

def split_nodes_delimiter(
    old_nodes: list[TextNode], delimiter: str, text_type: TextType
) -> list[TextNode]:
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes


            
