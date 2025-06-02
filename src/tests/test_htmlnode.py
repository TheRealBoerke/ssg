import unittest
from htmlnode import HTMLNode

class TestHTMLNode():
    def test_eq(self):
        node1 = HTMLNode("a", "boot.dev", None, {"href": "https://boot.dev", "target": "_blank"})
        node2 = HTMLNode("a", "boot.dev", None, {"href": "https://boot.dev", "target": "_blank"})
        self.assertEqual(node1, node2)

    def test_neq(self):
        node1 = HTMLNode("a", "boot.dev", None, {"href": "https://boot.dev", "target": "_blank"})
        node2 = HTMLNode("img", "boot.dev logo", None, {"src": "https://www.boot.dev/img/bootdev-logo-full-small.webp"})
        self.assertEqual(node1, node2)
    
    def test_repr(self):
        node = HTMLNode("p", "Hello", None, {"class": "intro"})
        output = repr(node)
        self.assertIn("HTMLNode(", output)
        self.assertIn("Hello", output)
        self.assertIn("{'class':", output)