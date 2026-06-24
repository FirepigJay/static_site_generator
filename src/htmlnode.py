class HTMLNode:
    def __init__(self, tag: str | None = None, value:str | None = None, children:list[HTMLNode] | None = None, props:dict | None = None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        string = ''
        if self.props is not None:
            for key, value in self.props.items():
                string += f' {key}={value}'
        return string
            
    def __repr__(self) -> str:
        string = ''
        string += f'\ntag: {self.tag}'
        string += f'\nvalue: {self.value}'
        string += f'\nchildren: {self.children}'
        string += f'\nprops: {self.props_to_html()}'
        return string
    
class LeafNode(HTMLNode):
    def __init__(self, tag: str | None, value: str | None, props:dict | None = None):
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self) -> str:
        if self.value is None:
            raise ValueError('No value')
        if self.tag == None:
            return self.value
        else:
            props = self.props
            if self.props is None:
                props = ''
            return f'<{self.tag}{props}>{self.value}</{self.tag}>'
    
    def __repr__(self) -> str:
        string = ''
        string += f'\ntag: {self.tag}'
        string += f'\nvalue: {self.value}'
        string += f'\nprops: {self.props_to_html()}'
        return string

       

    