import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import threading
import os
import sv_ttk  # Import the theme library

# Import the function we wrote in our other file
from image_processor import process_images

class ImageProcessorApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Bulk Image Processor")
        self.geometry("700x700")

        # --- Initialize all our variables ---
        self.input_folder_path = tk.StringVar()
        self.output_folder_path = tk.StringVar()
        self.convert_var = tk.BooleanVar()
        self.format_var = tk.StringVar(value="jpeg")
        self.resize_var = tk.BooleanVar()
        self.width_var = tk.StringVar(value="1024")
        self.crop_var = tk.BooleanVar()
        self.crop_ratio_var = tk.StringVar(value="16:9")
        self.watermark_var = tk.BooleanVar()
        self.watermark_text_var = tk.StringVar(value="© Your Name")
        self.quality_var = tk.IntVar(value=95)

        # --- Create a main frame to hold all other widgets ---
        main_frame = ttk.Frame(self, padding="10")
        main_frame.pack(fill="both", expand=True)

        # --- 1. Folder Selection Frame ---
        folder_frame = ttk.LabelFrame(main_frame, text="Folder Selection", padding="10")
        folder_frame.pack(fill="x", pady=10)
        folder_frame.columnconfigure(1, weight=1)

        input_btn = ttk.Button(folder_frame, text="Select Input Folder", command=self.select_input_folder)
        input_btn.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        input_label = ttk.Label(folder_frame, textvariable=self.input_folder_path, wraplength=400)
        input_label.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        output_btn = ttk.Button(folder_frame, text="Select Output Folder", command=self.select_output_folder)
        output_btn.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        output_label = ttk.Label(folder_frame, textvariable=self.output_folder_path, wraplength=400)
        output_label.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        # --- 2. Processing Options Frame ---
        options_frame = ttk.LabelFrame(main_frame, text="Processing Options", padding="10")
        options_frame.pack(fill="x", pady=10)
        options_frame.columnconfigure(1, weight=1)

        # Helper function to link a checkbox to its input widgets
        def toggle_widget_state(bool_var, *widgets):
            def on_toggle(*args):
                state = "normal" if bool_var.get() else "disabled"
                for widget in widgets:
                    widget.config(state=state)
            on_toggle() # Set initial state
            bool_var.trace_add("write", on_toggle)

        # Convert
        convert_check = ttk.Checkbutton(options_frame, text="Convert to Format", variable=self.convert_var)
        convert_check.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        format_combo = ttk.Combobox(options_frame, textvariable=self.format_var, values=["jpeg", "png", "webp", "gif"], width=8)
        format_combo.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        toggle_widget_state(self.convert_var, format_combo)

        # Resize
        resize_check = ttk.Checkbutton(options_frame, text="Resize Image", variable=self.resize_var)
        resize_check.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        width_entry = ttk.Entry(options_frame, textvariable=self.width_var, width=10)
        width_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        ttk.Label(options_frame, text="px wide").grid(row=1, column=2, padx=5, sticky="w")
        toggle_widget_state(self.resize_var, width_entry)

        # Crop
        crop_check = ttk.Checkbutton(options_frame, text="Crop to Ratio", variable=self.crop_var)
        crop_check.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        crop_entry = ttk.Entry(options_frame, textvariable=self.crop_ratio_var, width=10)
        crop_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")
        ttk.Label(options_frame, text="(e.g., 16:9, 1:1)").grid(row=2, column=2, padx=5, sticky="w")
        toggle_widget_state(self.crop_var, crop_entry)

        # Watermark
        watermark_check = ttk.Checkbutton(options_frame, text="Add Watermark", variable=self.watermark_var)
        watermark_check.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        watermark_entry = ttk.Entry(options_frame, textvariable=self.watermark_text_var, width=30)
        watermark_entry.grid(row=3, column=1, columnspan=2, padx=5, pady=5, sticky="ew")
        toggle_widget_state(self.watermark_var, watermark_entry)

        # Quality
        quality_label = ttk.Label(options_frame, text="JPEG/WEBP Quality")
        quality_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
        quality_spinbox = ttk.Spinbox(options_frame, from_=1, to=100, textvariable=self.quality_var, width=8)
        quality_spinbox.grid(row=4, column=1, padx=5, pady=5, sticky="w")

        # --- 3. Action Frame ---
        action_frame = ttk.Frame(main_frame, padding="10")
        action_frame.pack(fill="x")

        self.start_button = ttk.Button(action_frame, text="Start Processing", command=self.start_processing_thread, style="Accent.TButton")
        self.start_button.pack(pady=10)

        self.progress_bar = ttk.Progressbar(action_frame, orient="horizontal", mode="determinate")
        self.progress_bar.pack(fill="x", pady=5, ipady=5)

        # --- 4. Log/Status Frame ---
        log_frame = ttk.LabelFrame(main_frame, text="Log", padding="10")
        log_frame.pack(fill="both", expand=True, pady=10)

        self.log_text = tk.Text(log_frame, height=10, state="disabled")
        self.log_text.pack(fill="both", expand=True)

    def select_input_folder(self):
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.input_folder_path.set(folder_selected)

    def select_output_folder(self):
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.output_folder_path.set(folder_selected)

    def log(self, message):
        self.log_text.config(state="normal")
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.config(state="disabled")
        self.log_text.see(tk.END)

    def start_processing_thread(self):
        self.start_button.config(state="disabled")
        self.progress_bar["value"] = 0 # Reset progress bar
        processing_thread = threading.Thread(target=self.start_processing)
        processing_thread.daemon = True
        processing_thread.start()

    def start_processing(self):
        self.log("--- Starting Process ---")

        in_dir = self.input_folder_path.get()
        out_dir = self.output_folder_path.get()

        if not in_dir or not out_dir:
            messagebox.showerror("Error", "Input and Output folders must be selected.")
            self.start_button.config(state="normal")
            return

        new_format = self.format_var.get() if self.convert_var.get() else None
        new_width = int(self.width_var.get()) if self.resize_var.get() else None
        crop_ratio = self.crop_ratio_var.get() if self.crop_var.get() else None
        watermark_text = self.watermark_text_var.get() if self.watermark_var.get() else None
        quality = self.quality_var.get()

        try:
            valid_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp')
            image_files = [f for f in os.listdir(in_dir) if os.path.isfile(os.path.join(in_dir, f)) and f.lower().endswith(valid_extensions)]
            total_images = len(image_files)
            self.progress_bar["maximum"] = total_images

            if total_images == 0:
                self.log("No valid image files found in the input directory.")
                messagebox.showwarning("Warning", "No valid image files found to process.")
                self.start_button.config(state="normal")
                return

            # Since we process all images at once now, just call it once
            process_images(
                input_dir=in_dir,
                output_dir=out_dir,
                new_width=new_width,
                new_format=new_format,
                watermark_text=watermark_text,
                crop_ratio=crop_ratio,
                quality=quality,
                logger=self.log
            )

            # Fake the progress bar for now as we process all at once
            self.progress_bar["value"] = total_images
            self.update_idletasks()

            self.log("--- Processing Complete! ---")
            messagebox.showinfo("Success", "All images have been processed successfully!")

        except Exception as e:
            self.log(f"An error occurred: {e}")
            messagebox.showerror("Error", f"An unexpected error occurred:\n{e}")
        finally:
            self.start_button.config(state="normal")


if __name__ == "__main__":
    app = ImageProcessorApp()
    sv_ttk.set_theme("dark")
    app.mainloop()
