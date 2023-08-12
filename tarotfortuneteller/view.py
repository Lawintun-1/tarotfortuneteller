from PIL import Image, ImageTk
import tkinter as tk

class View:
    def __init__(self, root):
        self.root = root
        self.root.title("Tarot Fortune Teller")
        self.root.configure(bg="#404040")
        self.card_frame = None
        self.questions = None

    def set_controller(self, controller):
        self.controller = controller

    def show_page(self):
        # Clear existing widgets
        for widget in self.root.winfo_children():
            widget.destroy()
        self.questions = self.controller.get_questions()
        # Configure root window for full screen
        self.root.attributes("-fullscreen", True)

        # Calculate button width based on screen width
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        button_height = 3
        button_width = 20

        # Create and grid the image
        back_card_image = tk.PhotoImage(file="Asset/cover.png")
        back_card_label = tk.Label(self.root, image=back_card_image)
        back_card_label.image = back_card_image
        back_card_label.grid(row=1, column=0, rowspan=len(self.questions) - 2, sticky="nsew")

        # Create label for the text
        text_label = tk.Label(self.root, text="Tarot Fortune Teller", font=("Helvetica", 24, "italic", "bold"),
                              bg="#404040", fg="lightblue")
        text_label.grid(row=0, column=0, columnspan=1, padx=10, pady=20, sticky="nsew")

        # Create button frame
        button_frame = tk.Frame(self.root, bg="#404040")
        button_frame.grid(row=1, column=1, rowspan=len(self.questions) - 2, sticky="nsew")

        # Create and grid buttons
        for index, question in enumerate(self.questions):
            button = tk.Button(button_frame, text=question, width=button_width, height=button_height,
                               command=lambda q=question: self.controller.on_question_button_click(q),
                               bg="light blue", fg="black")
            button.grid(row=index, column=0, padx=10, pady=20, sticky="nsew")

        # Exit button
        exit_button = tk.Button(button_frame, text="Exit", width=button_width, height=button_height,
                                command=self.controller.on_exit_button_click,
                                bg="red", fg="white")
        exit_button.grid(row=len(self.questions), column=0, padx=10, pady=20, sticky="nsew")

        # Configure grid weights to expand column 0 (back card) and column 1 (button group)
        self.root.grid_rowconfigure(2, weight=1)  # Back card row
        self.root.grid_rowconfigure(3, weight=1)  # First button row
        self.root.grid_columnconfigure(1, weight=1)  # Button group column

        #self.root.grid_rowconfigure(2, weight=1)

    def show_page_2(self, question):
        # Clear existing widgets
        for widget in self.root.winfo_children():
            widget.destroy()

        # Configure root window for full screen
        self.root.attributes("-fullscreen", True)

        # Set background color
        self.root.configure(bg="#404040")

        # Calculate button dimensions based on screen size
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        button_height = 3
        button_width = 20

        # Create a new frame for the card grid
        self.card_frame = tk.Frame(self.root, bg="#404040")
        self.card_frame.pack(side="left", fill="y")

        # Create and place the back and shuffle buttons
        button_frame = tk.Frame(self.root, bg="#404040")
        button_frame.pack(side="right", fill="y")

        back_button = tk.Button(button_frame, text=" << Back", width=button_width, height=button_height, fg="white",bg="gray",
                                command=self.controller.on_back_button_click)
        back_button.pack(side="top", padx=10, pady=20)

        # Create the shuffle button and save a reference to it in the View class
        shuffle_button = tk.Button(button_frame, text="Shuffle", width=button_width, height=button_height, bg="lightblue",fg="black",
                                   command=lambda q=question: self.controller.on_shuffle_button_click(q))
        shuffle_button.pack(side="top", padx=10, pady=20)
        self.shuffle_button = shuffle_button

        # Function to place card with a delay
        self.create_card_images(question)

        # Adjust alignment
        self.root.grid_columnconfigure(0, weight=4)  # Cards take up 4/5 of the screen width
        self.root.grid_columnconfigure(1, weight=1)  # Button group takes up 1/5 of the screen width

    def shuffle_cards(self, question):
        # Disable the shuffle button
        shuffle_button = self.shuffle_button
        shuffle_button.config(state=tk.DISABLED)

        card_frame = self.card_frame
        cards = card_frame.winfo_children()
        for card in cards:
            card.destroy()

        # Create and place new card images with delay
        self.create_card_images(question)

        # Enable the shuffle button after the shuffle process is complete
        shuffle_button.config(state=tk.NORMAL)

    def create_card_images(self,question):
        def place_card(row, col, card_label):
            card_label.grid(row=row, column=col, padx=10, pady=20)

        for i in range(22):
            if i < 14:
                row = i // 7
                col = i % 7
                if i < 7:
                    delay = 600
                if 7 <= i < 14:
                    delay = 1200
            else:
                row = 2
                col = i - 14
                delay = 1900

            card_image_path = self.controller.get_card_path(i)
            pil_image = Image.open(card_image_path)
            resized_pil_image = pil_image.resize((120, 220), Image.LANCZOS)
            card_image = ImageTk.PhotoImage(resized_pil_image)
            card_label = tk.Label(self.card_frame, image=card_image, bg="#404040")
            card_label.image = card_image

            self.root.after(delay, place_card, row, col, card_label)
            card_label.bind("<Button-1>", lambda event, card_index=i: self.controller.on_card_click(question))

            '''place_card(row, col, card_label)
            card_label.bind("<Button-1>", lambda event, card_index=i: self.controller.on_card_click(question))'''

    def show_page_3(self, question):
        button_height = 3
        button_width = 20

        # Clear existing widgets
        for widget in self.root.winfo_children():
            widget.destroy()

        # Configure root window for full screen
        self.root.attributes("-fullscreen", True)

        # Set background color
        self.root.configure(bg="#404040")

        # Calculate screen dimensions
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Calculate dimensions for the images
        first_image_width = screen_width // 4
        first_image_height = (3 * screen_height) // 5

        second_image_width = screen_width // 2
        second_image_height = (3 * screen_height) // 5

        # Create a frame for the back button
        back_button_frame = tk.Frame(self.root, bg="#404040")
        back_button_frame.pack(side="top", fill="x")

        # Create and grid back button
        back_button = tk.Button(back_button_frame, text="<< Back", width=button_width, height=button_height, bg="gray", fg="white",
                                command=lambda: self.controller.on_back_button_click_3(question))
        back_button.pack(side="right", padx=10, pady=20)
        first_image_path = self.controller.get_tarot_card_image_path(
            question)  # Update with the path to your first image
        base_name = self.controller.get_tarot_prediction_image_name(first_image_path)
        # Create a frame for the text label
        card_name = self.controller.get_tarot_random_card_name(base_name)
        text_frame = tk.Frame(self.root, bg="#404040")
        text_frame.pack(side="top", fill="x")

        # Create and grid the "the card" text label
        text_label = tk.Label(text_frame, text=card_name, font=("Helvetica", 36, "bold"),
                              bg="#404040", fg="white")
        text_label.pack(side="left", padx=20, pady=20)

        # Create frame for images
        image_frame = tk.Frame(self.root, bg="#404040")
        image_frame.pack(fill="both", expand=True)

        # Load and display the first image on the right side

        first_image = Image.open(first_image_path)
        first_image = first_image.resize((first_image_width, first_image_height), Image.LANCZOS)
        first_image = ImageTk.PhotoImage(first_image)
        first_image_label = tk.Label(image_frame, image=first_image, bg="#404040")
        first_image_label.image = first_image
        first_image_label.pack(side="left", padx=10, pady=20, fill="both", expand=True)
        card = base_name
        # Load and display the second image on the left side
        second_image_path = self.controller.get_tarot_prediction_image_path(
            question,card)  # Update with the path to your second image
        second_image = Image.open(second_image_path)
        second_image = second_image.resize((second_image_width, second_image_height), Image.LANCZOS)
        second_image = ImageTk.PhotoImage(second_image)
        second_image_label = tk.Label(image_frame, image=second_image, bg="#404040")
        second_image_label.image = second_image
        second_image_label.pack(side="right", padx=10, pady=20, fill="both", expand=True)
