import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    # Purpose: Make sure __eq__ returns True for identical HTMLNode instances.
    def test_eq(self):
        node1 = HTMLNode("a", "boot.dev", None, {"href": "https://boot.dev", "target": "_blank"})
        node2 = HTMLNode("a", "boot.dev", None, {"href": "https://boot.dev", "target": "_blank"})
        self.assertEqual(node1, node2)

    # Purpose: Make sure __eq__ correctly returns False for differing HTMLNode instances.
    def test_neq(self):
        node1 = HTMLNode("a", "boot.dev", None, {"href": "https://boot.dev", "target": "_blank"})
        node2 = HTMLNode("img", "boot.dev logo", None, {"src": "https://www.boot.dev/img/bootdev-logo-full-small.webp"})
        self.assertNotEqual(node1, node2)
    
    # Purpose: Make sure the output of __repr__ is as expected
    def test_repr(self):
        node = HTMLNode("p", "Hello", None, {"class": "intro"})
        output = repr(node)
        self.assertIn("HTMLNode(", output)
        self.assertIn("Hello", output)
        self.assertIn("{'class':", output)

    # Purpose: Make sure the output of props_to_html is as expected
    def test_props_to_html_valid_dict(self):
        node = HTMLNode("a", "text", None, {"href": "https://example.com", "target": "_blank"})
        expected = 'href="https://example.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected)
    
    # Purpose: Make sure that defaults are applied correctly
    def test_arguments_defaults(self):
        node = HTMLNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)