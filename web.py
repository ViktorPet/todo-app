import streamlit  as st 

from modules.functions import get_todos, write_todos

todos = get_todos()
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    write_todos(todos)
    print(todo)
    
    



st.title("My todo App")
st.subheader("My first web application with Python")
st.write("This is application to boost your productivity")
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()
            

st.text_input(label="", placeholder="Add new todo...."
              ,on_change=add_todo, key="new_todo")
  

print("Hello")

st.session_state
