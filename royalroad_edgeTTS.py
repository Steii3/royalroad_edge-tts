# encoding=utf8
from asyncore import write
from bs4 import BeautifulSoup
import streamlit as st
import requests,edge_tts,subprocess
import re , json
import asyncio
st.title("RoyalRoad Edge-TTS")
headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
}


# with open("language.json")as json_data :
#     data = json.load(json_data)
# print(data)
# expander_options = st.expander("options")

# with  expander_options:
    
    
#     async def retVoiceList():
#             return await edge_tts.list_voices()

#     names = {}

#     with st.spinner("Loading Microsoft Edge TTS ...") :
        
#         for voice in asyncio.run(retVoiceList()):
#             # st.write(voice)
#             name = voice["Name"]
#             fname = voice["FriendlyName"]
#             local = voice["Locale"]
#             gender = voice["Gender"]
#             # print(fname)
#             # print(local)
#             names[fname] = name
            
#             st.selectbox("language :",('English','French','Italian'))
            

    # print(names)

# st.write(retVoiceList())
web_page_url = ""
web_page_url = st.text_input('url :',placeholder='https://www.royalroad.com/fiction/######/')

if web_page_url != "" :
    try :
        page_content = requests.get(url=web_page_url, headers=headers).text
    except :

        st.error('Error, URL not valid', icon="🚨")
    else : 
        soup = BeautifulSoup(page_content, "html.parser")
        
        # text = soup.select('div.chapter-inner')[0].find_all('p')
        for br in soup.find_all("br"):
            br.replace_with("\n")
        
        
        title_found = soup.title.text    
        text_found = soup.select('div.chapter-inner')[0].text
        
        
     
        
        with st.expander('Text Found'):
            st.write(text_found)
  
    output_file = None
if st.button('Text to speech'):
     with st.spinner('Processing text'):
    
        output_file = subprocess.check_output(['edge-tts','-t', text_found])
        col1, col2 = st.columns([3,1])
        with col1:
            st.audio(output_file,'mp3')
        with col2:
            st.download_button('download the mp3 file',output_file,file_name=title_found + ".mp3", mime="audio/mp3")
                
        st.success('Done!')
        st.balloons()
    
    

# st.download_button("Save the audiobook")


