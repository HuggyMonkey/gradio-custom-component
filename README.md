# Gradio Custom Utility Components Library

A library of Gradio custom utility components for client-side text extraction, text transformations, text manipulation, and file conversions. The components were built with the intent to facilitate the developement/prototyping of machine learning and AI applications using Gradio by making it easy to preprocess and convert data from common file formats directly in the browser. Essentially creating plug and play components for common application task such as Q/A and context enrichment.


- **Client-side preprocessing**: Reduces server load and latency by handling text extraction and conversion in the user's browser.
- **Supports common file formats**: Extracts text from PDF, DOCX, and Markdown files etc, converting them into data types compatible with AI and ML models.
- **Composable Gradio components**: Easily integrate these utilities into your Gradio apps for rapid prototyping and deployment.
- **Privacy-friendly**: Sensitive data never leaves the user's device during preprocessing.


## Component General Features

- Extract text from files (client-side, no server upload required)
- View and preview extracted content
- Upload files from device or by URL
- Simple interface
- Easy integration

## Example Use Cases

- Preprocessing documents for NLP or LLM pipelines
- Building document Q&A or summarization apps
- Converting user-uploaded files to plain text for AI model input
- Privacy-preserving document analysis

## Available Components

### PDF Utilities (`simpletextextractfrompdf`)
- Upload and extract text from PDF files on your device
- Fetch and extract text from a PDF by URL
- Render and preview PDF files in the browser
- View extracted text

pip install gradio-simpletextextractfrompdf

[https://pypi.org/project/gradio-simpletextextractfrompdf/](https://pypi.org/project/gradio-simpletextextractfrompdf/)

[https://huggingface.co/spaces/HuggyMonkey/SimpleTextExtractFromPDFDemo](https://huggingface.co/spaces/HuggyMonkey/SimpleTextExtractFromPDFDemo)

### Word Document Utilities (`simpletextextractfromworddoc`)
- Upload and extract text from Word documents on your device
- Fetch and extract text from a Word document by URL
- View extracted text

### Markdown Utilities (`dotmdtostring`)
- Upload and extract text from Markdown files on your device
- Fetch and extract text from a Markdown file by URL
- Render and preview Markdown content

## Features Still Cooking
- .txt
- .csv
- .powerpoint
- .excel
- .html
- **Input Version: file -> string | Output Version: string -> file

## Installation

Clone this repository and install dependencies for each component as needed.  

Gradio Custom Component Guide
[https://www.gradio.app/guides/custom-components-in-five-minutes](https://www.gradio.app/guides/custom-components-in-five-minutes)

## Contributing

Contributions, bug reports, and feature requests are welcome! Please open an issue or submit a pull request.

## License

[Apache-2.0](LICENSE)

---