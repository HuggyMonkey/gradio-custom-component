import gradio as gr
from gradio_simpletextextractfromworddoc import SimpleTextExtractFromWordDoc


def first_200_chars(text):
    return text[:200]


demo = gr.Interface(
    fn=first_200_chars,
    inputs=SimpleTextExtractFromWordDoc(),
    outputs=gr.Textbox(label="First 200 characters of the extracted text"),
    title="Simple Text Extract From Word Doc",
    description="""
## Component Description
This space is to demo the usage of the SimpleTextExtractFromWordDoc component.
This component provides a simple interface to extract text from a Word document. The extracted text can be submitted as a string input to a function for further processing.
- **Text Extraction Only:** Only the text content is extracted from the Word document. Images and table structures are not preserved.
- **Input Component:** The component is primarily designed to be used as an input, allowing users to submit the extracted text to other functions.
- **Output Display:** When used as an output component, the extracted string content is displayed in a textarea.
The demo app here uses the SimpleTextExtractFromWordDoc component as an input component to extract the text from a PDF file and then show the first 200 characters of the extracted text.
""",
)


if __name__ == "__main__":
    demo.launch()
