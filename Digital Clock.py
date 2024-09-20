import tkinter as tk
import time

# Function to update the time
def update_time():
    current_time = time.strftime('%H:%M:%S')  # Format: HH:MM:SS
    label.config(text=current_time)           # Update label text
    label.after(1000, update_time)            # Call this function again after 1 second

# Create the main window
root = tk.Tk()
root.title('Digital Clock')

# Create a label to display the time
label = tk.Label(root, font=('Helvetica', 48), fg='black')
label.pack(pady=20)

# Call the update_time function to initialize
update_time()

# Start the main event loop
root.mainloop()
