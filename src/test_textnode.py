import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("test node with url", TextType.LINK, 'http:testlink.com')
        node4 = TextNode("test node with url", TextType.LINK, 'http:testlink.com1')
        node5 = TextNode("This is a text node", TextType.ITALIC)
        self.assertEqual(node, node2)
        self.assertNotEqual(node, node3)
        self.assertNotEqual(node3, node4)
        self.assertNotEqual(node2, node5)

if __name__ == "__main__":
    unittest.main()