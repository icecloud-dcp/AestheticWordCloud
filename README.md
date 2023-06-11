# Streamlit Word Cloud Generator

This is a powerful and interactive Word Cloud generator built with [Streamlit](https://streamlit.io/). The application takes text as an input, processes it by cleaning and lemmatizing, and generates a beautiful word cloud. The processing steps involve removing emojis, special elements, punctuation, and stop words, converting text to lowercase, and lemmatizing words. Users can also select words that they consider unnecessary, and these will be removed from the final word cloud. 

The resulting word cloud is rendered with a resolution of 3000x2000 pixels, with words colored in black and set against a serene teal background. The word cloud is then saved as a `.png` file.

![Sample Word Cloud](sample_wordcloud.png)

## Getting Started

### Prerequisites

Ensure you have the following installed on your system:

- Python 3.6 or higher
- Streamlit
- Spacy
- NLTK
- wordcloud
- matplotlib
- pandas
- textblob
- re

To install the required packages, you can use pip:

```sh
pip install streamlit spacy nltk wordcloud matplotlib pandas textblob
```

Ensure that you download the `en_core_web_sm` model for Spacy:

```sh
python -m spacy download en_core_web_sm
```

### Running the Application

To run this application, navigate to the folder where you have the script and type the following command in your terminal:

```sh
streamlit run wordcloud.py
```

A new tab should open in your default web browser where you can interact with the application. Paste the text you want to use to generate the word cloud, optionally select unnecessary words to exclude, and watch your word cloud come to life.

## License

This project is licensed under the terms of the MIT license.
