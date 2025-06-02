import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("This is a nice website", TextType.LINK, "https://boot.dev")
        node2 = TextNode("This is a nice website", TextType.LINK, "https://boot.dev")
        self.assertEqual(node1, node2)
    
    def test_neq_text(self):
        node1 = TextNode("This is a nice website", TextType.LINK, "https://boot.dev")
        node2 = TextNode("This is a horrible website", TextType.LINK, "https://boot.dev")
        self.assertNotEqual(node1, node2)
    
    def test_neq_text_type(self):
        node1 = TextNode("This is a nice website", TextType.LINK, "https://boot.dev")
        node2 = TextNode("This is a nice website", TextType.IMAGE, "https://boot.dev")
        self.assertNotEqual(node1, node2)
    
    def test_neq_text_type(self):
        node1 = TextNode("This is a nice website", TextType.LINK, "https://boot.dev")
        node2 = TextNode("This is a nice website", TextType.BOLD)
        self.assertNotEqual(node1, node2)
    