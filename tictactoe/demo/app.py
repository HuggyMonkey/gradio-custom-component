
import gradio as gr
from gradio_tictactoe import tictactoe


with gr.Blocks() as demo:
    gr.Markdown("# Change the value (keep it JSON) and the front-end will update automatically.")
    tictactoe(value={"message": "Hello from Gradio!"}, label="Static")


if __name__ == "__main__":
    demo.launch()
