import unittest
from htmlnode import HTMLNode,LeafNode

class TestTextNode(unittest.TestCase):
    def test_props_to_html(self):
        html1 = HTMLNode('tag string', 'value string', props = {"href": "https://www.google.com",
    "target": "_blank"})
        html2 = HTMLNode(value = 'value string', props = {"href": "https://www.google.com",
    "target": "_blank"})
        html3 = HTMLNode('tag string', props = {"href": "https://www.google.com",
    "target": "_blank"})
        html4 = HTMLNode('tag string', 'value string', [html1, html2, html3], {"href": "https://www.google.com",
    "target": "_blank"})
        html5 = HTMLNode(props = {"href": "https://www.google.com",
    "target": "_blank"})
        html6 = HTMLNode('tag string', 'value string', [html5, html4])
        print(html1)
        print(html2)
        print(html3)
        print(html4)
        print(html5)
        print(html6)
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

if __name__ == "__main__":
    unittest.main()