import streamlit as st
import functions

todos = functions.openfile()


def add_todo():
    new_todo = st.session_state['new_todo'] + "\n"
    todos.append(new_todo)
    functions.writefile(todos)
    st.session_state["new_todo"] = ''


st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to keep track of things i need to do")


for todo in todos:
    st.checkbox(todo, key=todo)
    if st.session_state[todo]:
        todos.remove(todo)
        functions.writefile(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label='TODOs', placeholder="add new todo...", on_change=add_todo, key='new_todo')

#st.session_state
