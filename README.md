# Extractive Text Summarizer
Extractive Text Summarizer is a pdf summarizer, in this user provide the pdf that needed to be summarized and also the desired length of output summary which is basically how many sentences does the user want from original pdf as a summary of pdf , then this app will provide the summarized text on next page which user can copy.It's an extractive approach in which algorithm tries to extract sentnces from original text which are highly correlated to each other and also give a good summary of text. It uses Text Rank Algorithm where score between each sentence is basically a cosine similarity in this way  i am not only extracting random sentences but interconnected sentences. Used kivy to make GUI on windows.

## How to run the app
1. Either fork or downlod app files.
2. Install all dependencies given in requirements.txt file in cmd using  pip install -r requirements.txt
3. run userinterface.py file
4. App will appear on screen

## How to use app
1. Choose file from folder window which need to be summarized(after selecting file it will take tim, wait until selected file path is displayed on screen).
2. Type length of how many sentences you want in summarized text and then press enter(make sure to press enter after writing length otherwise it won't take it)
3. Now press on summarize button and wait , if your file is big it will take , don't press twice on summarize button otherwise will cause error.
4. After some time you will be directed to next page where your summarized text will be displayed.

## Features
1. Let you select pdf and length of summarized text.
2. Will display error message if you didn't select path or enter the length.
3. Once summarized text displayed you can get back to original screen by pressing "Back" button.

## Future fetaures
1. Show user some loading screen when he presses "Summarize" button , bcoz algorithm will run in background and user won't know he/she has to wait for process to complete and he/she may press button again causing app to crash.
2. Allow user to download summarized text in pdf format, for know you can only see text and you have copy and paste summarized text yourself.
3. Maybe use flask, which can be hosted online can be a good idea.


## Dependencie
- Nltk
- Gensim
- Sklearn
- Networkx
- Kivy
- Kivymd

## What the app looks like



# Main Page

![alt text](https://github.com/kashif-flask/Text-summarizer/blob/master/images/main_page.PNG)





# Choose File

![alt text](https://github.com/kashif-flask/Text-summarizer/blob/master/images/Choose.PNG)







# Summarized text

![alt text](https://github.com/kashif-flask/Text-summarizer/blob/master/images/summarized_text.PNG)
