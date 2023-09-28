import tkinter as tk
from tkinter import messagebox

tasks_list = []
counter = 0


def addTask():
  global counter
  task = task_entry.get()
  if task == "":
    messagebox.showerror("Error", "Task not entered")
  else:
    task += "\n"
    tasks_list.append(task)
    counter += 1
    print(tasks_list)
    task_entry.set("")
    textArea.insert('end', str(counter) + "." + task)


def deleteTask():
  global counter
  id = id_entry.get()

  if id == "":
    messagebox.showerror("Error", "Id not entered")
  elif int(id) > len(tasks_list):
    messagebox.showerror("Error", "Id not found")
  else:
    tasks_list.pop(int(id) - 1)
    counter -= 1
    id_entry.set("")
    print(tasks_list)
    textArea.delete(1.0, 'end')
    for i in range(len(tasks_list)):
      textArea.insert('end', str(i + 1) + "." + tasks_list[i])


window = tk.Tk()
window.title("ToDo App")
window.geometry("300x300")

task_entry = tk.StringVar()
id_entry = tk.StringVar()

textArea = tk.Text(window)
textArea.place(x=50, y=120, width=200, height=100)

enterTask = tk.Label(window, text="Enter Your Task")
enterTask.place(x=100, y=10)

enterTaskEntry = tk.Entry(window, textvariable=task_entry)
enterTaskEntry.place(x=50, y=40, width=200, height=30)

submit = tk.Button(window, text="Submit", command=addTask)
submit.place(x=115, y=80)

taskNr = tk.Label(window, text="Task Number")
taskNr.place(x=50, y=240)

taskNrEntry = tk.Entry(window, textvariable=id_entry)
taskNrEntry.place(x=140, y=240, width=30)

delete = tk.Button(window, text="Delete", command=deleteTask)
delete.place(x=180, y=240)

tk.mainloop()
