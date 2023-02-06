from pyeditorjs import EditorJsParser

def parse_html(editor_js_data):
    data = editor_js_data
    parser = EditorJsParser(data)
    return parser.html(sanitize=True)