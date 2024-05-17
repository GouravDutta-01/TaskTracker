from js import document

def add_task(event):
    task_input = document.getElementById("task-input")
    task_text = task_input.value
    if task_text.strip() == "":
        return

    task_input.value = ""

    todo_list = document.getElementById("todo-list")
    new_task = document.createElement("li")
    new_task.classList.add("list-group-item", "d-flex", "justify-content-between", "align-items-center")

    task_span = document.createElement("span")
    task_span.textContent = task_text
    task_span.classList.add("w-75")
    new_task.appendChild(task_span)

    button_container = document.createElement("div")
    button_container.classList.add("btn-group")

    complete_button = document.createElement("button")
    complete_button.textContent = "Complete"
    complete_button.classList.add("btn", "btn-success", "btn-sm", "mr-1", "mx-2")
    complete_button.onclick = lambda e: mark_complete(task_span, complete_button)  
    button_container.appendChild(complete_button)

    delete_button = document.createElement("button")
    delete_button.textContent = "Delete"
    delete_button.classList.add("btn", "btn-danger", "btn-sm")
    delete_button.onclick = lambda e: delete_task(new_task)
    button_container.appendChild(delete_button)
    
    new_task.appendChild(button_container)
    todo_list.appendChild(new_task)

    update_task_summary()

def mark_complete(task_span, complete_button):
    task_span.classList.toggle("completed")
    if task_span.classList.contains("completed"):
        task_span.style.textDecoration = "line-through"
        task_span.style.color = "gray"
        complete_button.textContent = "Undo" 
    else:
        task_span.style.textDecoration = ""
        task_span.style.color = ""
        complete_button.textContent = "Complete" 

    update_task_summary()

def delete_task(task_item):
    task_item.remove()
    update_task_summary()

def update_task_summary():
    todo_list = document.getElementById("todo-list")
    tasks = todo_list.getElementsByTagName("li")
    total_tasks = len(tasks)
    if total_tasks == 0:
        completed_percent = 0
        not_completed_percent = 0
    else:
        completed_tasks = sum(1 for task in tasks if task.querySelector("span").classList.contains("completed"))
        completed_percent = (completed_tasks / total_tasks) * 100
        not_completed_percent = 100 - completed_percent

    completed_bar = document.getElementById("completed-bar")
    not_completed_bar = document.getElementById("not-completed-bar")
    completed_bar.style.width = f"{completed_percent}%"
    not_completed_bar.style.width = f"{not_completed_percent}%"

add_task_button = document.getElementById("add-task-button")
add_task_button.onclick = add_task
