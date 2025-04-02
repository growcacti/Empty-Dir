import os
import threading
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

class DirectoryCheckerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Directory Checker")

        self.empty_dirs = []
        self.deleted_dirs = []
        self.excluded_dirs = set()  # Stores directories to be excluded from deletion

        # Create and place widgets using grid layout
        frame = tk.Frame(root)
        frame.grid(row=0, column=0, padx=10, pady=10)

        self.check_button = tk.Button(frame, fg="black", bd=6, bg="light pink", text="Check Directories", command=self.start_check_thread)
        self.check_button.grid(row=0, column=0, padx=5, pady=5)

        self.delete_button = tk.Button(frame, fg="black", bd=8, bg="wheat", text="Delete Selected Directories", command=self.start_delete_thread, state=tk.DISABLED)
        self.delete_button.grid(row=0, column=1, padx=5, pady=5)

        self.delete_all_button = tk.Button(frame, fg="black", bd=6, bg="light cyan", text="Delete All Empty Directories", command=self.start_delete_all_thread, state=tk.DISABLED)
        self.delete_all_button.grid(row=0, column=2, padx=5, pady=5)

        self.omit_button = tk.Button(frame, fg="black", bd=6, bg="light blue", text="Omit Selected Directory", command=self.omit_selected_directory)
        self.omit_button.grid(row=0, column=3, padx=5, pady=5)

        self.save_button = tk.Button(frame, fg="black", bd=6, bg="orange", text="Save Report", command=self.save_report)
        self.save_button.grid(row=0, column=4, padx=5, pady=5)

        self.undo_button = tk.Button(frame, fg="black", bd=6, bg="light green", text="Undo Deletions", command=self.undo_deletions, state=tk.DISABLED)
        self.undo_button.grid(row=0, column=5, padx=5, pady=5)

        self.text_widget = tk.Text(frame, bd=10, bg="light cyan", width=80, height=20)
        self.text_widget.grid(row=1, column=0, columnspan=6, padx=5, pady=5)

        self.listbox = tk.Listbox(frame,bd=11,bg="thistle", selectmode=tk.MULTIPLE, width=80, height=10)
        self.listbox.grid(row=2, column=0, columnspan=6, padx=5, pady=5)

        self.progress = ttk.Progressbar(frame, orient=tk.HORIZONTAL, length=100, mode='determinate')
        self.progress.grid(row=3, column=0, columnspan=6, padx=5, pady=5)

        self.status_label = tk.Label(frame, fg="black", bd=6, bg="light green", text="")
        self.status_label.grid(row=4, column=0, columnspan=6, padx=5, pady=5)

    def check_directories(self, path):
        self.empty_dirs = []
        self.excluded_dirs.clear()
        self.listbox.delete(0, tk.END)
        total_dirs = sum([len(dirs) for _, dirs, _ in os.walk(path)])
        progress_step = 100 / total_dirs if total_dirs > 0 else 0
        progress = 0

        for root, dirs, files in os.walk(path):
            if not dirs and not files:
                self.empty_dirs.append(root)
                self.text_widget.insert(tk.END, f"Empty Directory: {root}\n")
                self.listbox.insert(tk.END, root)
            progress += progress_step
            self.update_progress(progress)
        
        self.update_progress(100)
        self.status_label.config(text="Scan Completed")

        if self.empty_dirs:
            self.delete_button.config(state=tk.NORMAL)
            self.delete_all_button.config(state=tk.NORMAL)
        else:
            self.delete_button.config(state=tk.DISABLED)
            self.delete_all_button.config(state=tk.DISABLED)
            self.text_widget.insert(tk.END, "No empty directories found.\n")

    def update_progress(self, value):
        self.progress['value'] = value
        self.root.update_idletasks()

    def delete_directories(self, selected_dirs):
        total_dirs = len(selected_dirs)
        progress_step = 100 / total_dirs if total_dirs > 0 else 0
        progress = 0

        for index in selected_dirs:
            directory = self.listbox.get(index)
            if directory in self.excluded_dirs:
                self.text_widget.insert(tk.END, f"Skipped Directory (Omitted): {directory}\n")
                continue
            try:
                os.rmdir(directory)
                self.deleted_dirs.append(directory)
                self.text_widget.insert(tk.END, f"Deleted Directory: {directory}\n")
            except Exception as e:
                self.text_widget.insert(tk.END, f"Failed to Delete {directory}: {str(e)}\n")
            progress += progress_step
            self.update_progress(progress)
        
        self.update_progress(100)
        self.status_label.config(text="Deletion Completed")
        self.undo_button.config(state=tk.NORMAL)

    def delete_all_empty_directories(self):
        total_dirs = len(self.empty_dirs)
        progress_step = 100 / total_dirs if total_dirs > 0 else 0
        progress = 0

        for directory in self.empty_dirs:
            if directory in self.excluded_dirs:
                self.text_widget.insert(tk.END, f"Skipped Directory (Omitted): {directory}\n")
                continue
            try:
                os.rmdir(directory)
                self.deleted_dirs.append(directory)
                self.text_widget.insert(tk.END, f"Deleted Directory: {directory}\n")
            except Exception as e:
                self.text_widget.insert(tk.END, f"Failed to Delete {directory}: {str(e)}\n")
            progress += progress_step
            self.update_progress(progress)

        self.update_progress(100)
        self.status_label.config(text="All Empty Directories Deleted")
        self.undo_button.config(state=tk.NORMAL)

    def omit_selected_directory(self):
        selected_dirs = self.listbox.curselection()
        for index in selected_dirs:
            directory = self.listbox.get(index)
            self.excluded_dirs.add(directory)
            self.text_widget.insert(tk.END, f"Omitted Directory: {directory}\n")
        self.status_label.config(text="Omissions Updated")

    def save_report(self):
        report = self.text_widget.get("1.0", tk.END)
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text files", "*.txt"),
                                                            ("All files", "*.*")])
        if file_path:
            with open(file_path, 'w') as file:
                file.write(report)
            messagebox.showinfo("Save Report", "Report saved successfully!")

    def start_check_thread(self):
        threading.Thread(target=self.start_check).start()

    def start_check(self):
        path = filedialog.askdirectory()
        if path:
            self.text_widget.delete("1.0", tk.END)
            self.status_label.config(text="Scanning...")
            self.update_progress(0)
            self.check_directories(path)

    def start_delete_thread(self):
        threading.Thread(target=self.start_delete).start()

    def start_delete(self):
        selected_dirs = self.listbox.curselection()
        if selected_dirs:
            self.text_widget.delete("1.0", tk.END)
            self.status_label.config(text="Deleting...")
            self.update_progress(0)
            self.delete_directories(selected_dirs)

    def start_delete_all_thread(self):
        threading.Thread(target=self.start_delete_all).start()

    def start_delete_all(self):
        self.text_widget.delete("1.0", tk.END)
        self.status_label.config(text="Deleting All Empty Directories...")
        self.update_progress(0)
        self.delete_all_empty_directories()

    def undo_deletions(self):
        for directory in self.deleted_dirs:
            try:
                os.makedirs(directory)
                self.text_widget.insert(tk.END, f"Restored Directory: {directory}\n")
            except Exception as e:
                self.text_widget.insert(tk.END, f"Failed to Restore {directory}: {str(e)}\n")
        self.deleted_dirs = []
        self.undo_button.config(state=tk.DISABLED)
        self.status_label.config(text="Undo Completed")

# Create the main application window
root = tk.Tk()
app = DirectoryCheckerApp(root)

# Start the Tkinter event loop
root.mainloop()
