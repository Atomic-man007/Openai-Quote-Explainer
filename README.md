# Quote Explainer using OpenAI and EasyOCR

## Aim

The main aim of this project is to extract and understand the elaborated meaning of a quote that is uploaded as an image. This is achieved by utilizing the EasyOCR library for Optical Character Recognition (OCR) and OpenAI's language model for text interpretation.

## Project Overview

In this project, we utilize the EasyOCR library for extracting text from an image containing a quote. The extracted text is then passed to OpenAI's language model using langchain to interact easily with openai api, which generates a more comprehensive and elaborated meaning of the given quote.

## OCR Example

![Alt text](./resources/gandhi-great-quotes.jpg?raw=true "Gandhi Quote")

answer:

`'Live as if you were to die tomorrow Learn as if you were to live forever: Mahatma Gandhi +Alireza Yavari'`

## Getting Started

Follow these steps to get started with the project:

1. **Installation:**

   - Install the required Python libraries using the following command:
     ```bash
     pip install openai easyocr gtts soundfile sounddevice langchain
     ```

2. **API Key Setup:**

   - Obtain an API key from OpenAI by signing up on their platform.
   - Set up your OpenAI API key as an environment variable:
     ```bash
     export OPENAI_API_KEY=your_api_key_here
     ```

3. **Running the Project:**
   - Place the image containing the quote you want to analyze in the project directory or provide the path to the image in the code.
   - Run the Python script `quote_explainer.py` using the following command:
     ```bash
     python quote_explainer.py *path_to_your_image*.jpg
     ```
   - The script will use EasyOCR to perform OCR on the image, extract the quote, and send it to OpenAI's language model for interpretation.
   - The generated elaborated meaning of the quote will be displayed in the terminal.

## Customization

- You can customize the project by experimenting with different preprocessing techniques for better OCR results, adjusting the language model's parameters, or enhancing the user interface.

## Note

- Keep in mind that OCR and language model results may not always be accurate. Preprocessing and error handling can be added to improve the overall reliability of the project.

## Acknowledgments

- This project was inspired by the capabilities of EasyOCR and OpenAI's language model.

---

Feel free to reach out if you have any questions or suggestions for improvement.

```

```
