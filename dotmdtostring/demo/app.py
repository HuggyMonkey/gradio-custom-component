
import gradio as gr
from gradio_dotmdtostring import dotMDtoString


def first_200_chars(text):
    return text[:200]


demo = gr.Interface(
    fn=first_200_chars,
    inputs=dotMDtoString(),
    outputs=gr.Textbox(label="First 200 characters of the extracted text"),
    title="dotMDtoString",
    description="""
## Component Description
This space is to demo the usage of the dotMDtoString component.
This component provides a simple interface to convert a markdown file to a string.
The demo app here uses the dotMDtoString component as an input component to convert a markdown file to a string and then show the first 200 characters of the converted string.
""",
)


if __name__ == "__main__":
    demo.launch()
