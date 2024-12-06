from tkinter import *
from datetime import datetime

def update_clock():
    current_time = datetime.now().strftime("%H:%M:%S")
    label.config(text=current_time)
    label.after(1000, update_clock)

def calculate_logout_time():
    try:
        in_time = datetime.strptime(entry_in_time.get(), "%H:%M")
        out_time = datetime.strptime(entry_out_time.get(), "%H:%M")
        time_difference = out_time - in_time  # Calculate the difference
        total_seconds = int(time_difference.total_seconds())
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        label_logout_time.config(text=f"Total Time: {hours:02}:{minutes:02}:{seconds:02}")
    except Exception as e:
        label_logout_time.config(text=f"Error: {e}")

# Main Tkinter window
root = Tk()
root.title("Desktop Timer")

# Current clock display
label = Label(root, font=("Arial", 30))
label.pack()

# In Time input
label_in_time = Label(root, text="In Time (HH:MM):")
label_in_time.pack()
entry_in_time = Entry(root)
entry_in_time.pack()

# Out Time input
label_out_time = Label(root, text="Out Time (HH:MM):")
label_out_time.pack()
entry_out_time = Entry(root)
entry_out_time.pack()

# Button to calculate total time
button = Button(root, text="Calculate Total Time", command=calculate_logout_time)
button.pack()

# Label to display the result
label_logout_time = Label(root, font=("Arial", 20))
label_logout_time.pack()

# Start the clock update loop
update_clock()

# Run the Tkinter main loop
root.mainloop()