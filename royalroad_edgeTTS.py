from asyncore import write
from bs4 import BeautifulSoup
import streamlit as st
import requests,edge_tts,subprocess


headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
}
web_page_url = ""
web_page_url = st.text_input('url :')

def get_content_html(url):
    page_content = requests.get(url=web_page_url, headers=headers).text
    soup = BeautifulSoup(page_content, "html.parser")
    text = soup.find_all('p')
    return text 
    
if web_page_url != "" :
    content_text = get_content_html(web_page_url)
    text_in_one_block = ""
    with st.expander('Text Found'):
        for i in content_text:
            if i.string != None:
                text_in_one_block+= i.string
                text_in_one_block+= "\n"
                st.write(i.string)
    # x = re.split("\n", soup.p.text)
    # for i in x :
    #     st.text(i)
    output_file = None
if st.button('Text to speech'):
    output_file = subprocess.check_output(['edge-tts','-t', text_in_one_block])
    col1, col2 = st.columns([3,1])
    with col1:
        st.audio(output_file,'mp3')
    with col2:
        st.download_button('download the mp3 file',output_file,file_name="chapter.mp3", mime="audio/mp3")
    st.balloons()
    

    

# st.download_button("Save the audiobook")


