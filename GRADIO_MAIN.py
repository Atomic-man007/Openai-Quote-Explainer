##################### GRADIO CODE ###################################

# IMPORTING LIBRARIES
import os
import openai
import easyocr
import tempfile
import gradio as gr
from PIL import Image
from gtts import gTTS
import soundfile as sf
from gradio import components
from langchain.llms import OpenAI
from langchain import PromptTemplate, LLMChain

from dotenv import load_dotenv, find_dotenv

# Load environment variables from .env file
load_dotenv(find_dotenv())

# OCR FUNCTION


def get_ocr_text(image_file):
    reader = easyocr.Reader(['en'])
    result = reader.readtext(image_file)
    extracted_text = '\n'.join([detection[1] for detection in result])
    text = extracted_text.replace("\n", " ")
    return text


def get_answer(text):
    template = """
    Please provide a detailed explanation of the meaning of the following quote: {text} """
    prompt = PromptTemplate(template=template, input_variables=["text"])
    llm = OpenAI()
    llm_chain = LLMChain(prompt=prompt, llm=llm)
    answer = llm_chain.run(text)
    return answer


def quote_explainer_app(image):
    # SPECIFY OPENAI API KEY
    openai.api_key = os.environ.get('OPENAI_API_KEY')

    ocr_text = get_ocr_text(image)
    generated_answer = get_answer(ocr_text)

    # SPEECH GENERATION
    tts = gTTS(text=generated_answer, lang="en", slow=False)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio_file:
        temp_audio_path = temp_audio_file.name
        tts.save(temp_audio_path)

    data, sample_rate = sf.read(temp_audio_path)
    return generated_answer, temp_audio_path


iface = gr.Interface(
    fn=quote_explainer_app,
    inputs=components.Image(type="pil"),
    outputs=[components.Textbox(label="GENERATED TEXT"),
             components.Audio(label="GENERATED AUDIO")]
)

if __name__ == "__main__":
    iface.launch()
