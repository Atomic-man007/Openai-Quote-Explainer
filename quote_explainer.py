# QUOTE EXPLAINER USING OPENAI AND LANGCHAIN

# AIM: THE MAIN AIM OF THIS PROJECT IS TO FIND ELABORATED MEANING OF A QUOTE(UPLOADED AS IMAGE) BY INTERACTING WITH OPENAI USING LANGCHAIN

# IMPORTING LIBRARIES
import os
import argparse
import easyocr
import openai
from gtts import gTTS
import soundfile as sf
import sounddevice as sd
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


def get_answer(question, text):
    template = """
    Please provide a detailed explanation of the meaning of the following quote: {text} """
    prompt = PromptTemplate(template=template, input_variables=["text"])
    llm = OpenAI()
    llm_chain = LLMChain(prompt=prompt, llm=llm)

    answer = llm_chain.run(question)
    return answer


def main():
    parser = argparse.ArgumentParser(
        description="Quote Explainer using OpenAI and LangChain")
    parser.add_argument("image", help="Path to the image containing the quote")
    args = parser.parse_args()

    image_file = args.image
    ocr_text = get_ocr_text(image_file)

    # SPECIFY OPENAI API KEY
    openai.api_key = os.environ.get('OPENAI_API_KEY')

    generated_answer = get_answer(ocr_text, args.image)

    # SPEECH GENERATION
    tts = gTTS(text=generated_answer, lang="en", slow=False)
    tts.save("output.mp3")

    # SPEECH PLAYBACK
    audio_file = "output.mp3"
    data, sample_rate = sf.read(audio_file)
    sd.play(data, sample_rate)
    sd.wait()


if __name__ == "__main__":
    main()
