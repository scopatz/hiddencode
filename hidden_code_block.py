"""Simple, inelegant 

Thanks to 
"""

from docutils import nodes
from sphinx.directives.code import CodeBlock
from sphinx.util.compat import make_admonition

class hidden_code_block(nodes.General, nodes.FixedTextElement):
    pass


js_showhide = """\
<script type="text/javascript">
    function showhide(element){
        if (!document.getElementById)
            return

        if (element.style.display == "block")
            element.style.display = "none"
        else
            element.style.display = "block"
    };
</script>
"""

class HiddenCodeBlock(CodeBlock):
    """Hidden code block is Hidden"""

    def run(self):
        # Body of the method is more or less copied from CodeBlock
        code = u'\n'.join(self.content)
        hcb = hidden_code_block(code, code)
        hcb['language'] = self.arguments[0]
        hcb['linenos'] = 'linenos' in self.options
        hcb.line = self.lineno
        return [hcb]


def visit_hcb_html(self, node):
    """Visit hidden code block"""
    # We want to use the original highlighter so that we don't
    # have to reimplement it.  However it raises a SkipNode 
    # error at the end of the function call.  Thus we intercept
    # it and raise it again later.
    try: 
        self.visit_literal_block(node)
    except nodes.SkipNode:
        pass

    # The last element of the body should be the literal code 
    # block that was just made.
    code_block = self.body[-1]

    divname = 'hiddencodeblock{}'.format(hash(node))
    divheader = ("""<a href="javascript:showhide(document.getElementById('{dname}'))">"""
                 """+ show/hide code</a><br />"""
                 '''<div id="{dname}" style="display: none">''').format(dname=divname)


    code_block = js_showhide + divheader + code_block + "</div>"

    # reassign and exit
    self.body[-1] = code_block
    raise nodes.SkipNode


def depart_hcb_html(self, node):
    """Depart hidden code block"""
    # Stub because of SkipNode in visit


def setup(app):
    app.add_directive('hidden-code-block', HiddenCodeBlock)
    app.add_node(hidden_code_block, html=(visit_hcb_html, depart_hcb_html))
