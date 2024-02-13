import streamlit as st

st.title('CHATBOT')

prompt = st.chat_input('user')

if "messages" not in st.session_state:
	st.session_state.messages = []

for message in st.session_state.messages:
	user_input = st.chat_message(message['role'])
	user_input.write(message['content'])

st.chat_message('user').write(prompt)

if prompt and prompt != '':
	st.session_state.messages.append({'role': 'user', 'content': prompt})


if prompt == 'hi':
	st.chat_message("assistant").write('hello')
	st.session_state.messages.append({'role': 'assistant', 'content': 'hello' })
elif prompt == 'good morning':
	st.chat_message("assistant").write('good moring!')
	st.session_state.messages.append({'role': 'assistant', 'content': 'good moring!'})
elif prompt == 'how are you?':
	st.chat_message("assistant").write('im fine!')
	st.session_state.messages.append({'role': 'assistant', 'content': 'im fine!'})
elif prompt == 'good':
	st.chat_message("assistant").write('yeah')
	st.session_state.messages.append({'role': 'assistant', 'content': 'yeah'})


    