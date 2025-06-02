class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props 

    def __eq__(self, other):
        if not isinstance(other, HTMLNode):
            return False
        return (self.tag == other.tag and
                self.value == other.value and
                self.children == other.children and
                self.props == other.props)

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        if self.props is not None and not isinstance(self.props, dict):
            raise TypeError("'props' should be of type 'dict' or None")
        if self.props is not None:
            output = ""
            for key, value in self.props.items():
                output += f"{key}=\"{value}\" "
            return output.strip()
        else:
            return ""