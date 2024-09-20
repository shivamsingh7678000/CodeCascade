import tkinter as tk
from tkinter import messagebox

class MovieTicketBookingSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Movie Ticket Booking System")
        self.root.geometry("400x300")

        # Create frames for different sections
        self.movie_frame = tk.Frame(self.root)
        self.seat_frame = tk.Frame(self.root)
        self.payment_frame = tk.Frame(self.root)

        # Create labels and entries for movie selection
        self.movie_label = tk.Label(self.movie_frame, text="Select a Movie:")
        self.movie_label.pack()
        self.movie_var = tk.StringVar()
        self.movie_menu = tk.OptionMenu(self.movie_frame, self.movie_var, "INCEPTION", "INTERSTELLAR", "OPPENHEIMER")
        self.movie_menu.pack()

        # Create labels and entries for seat reservation
        self.seat_label = tk.Label(self.seat_frame, text="Select a Seat:")
        self.seat_label.pack()
        self.seat_var = tk.StringVar()
        self.seat_menu = tk.OptionMenu(self.seat_frame, self.seat_var, "A1", "A2", "A3","A4","A5")
        self.seat_menu.pack()

        # Create labels and entries for payment processing
        self.payment_label = tk.Label(self.payment_frame, text="Enter Payment Details:")
        self.payment_label.pack()
        self.card_number_label = tk.Label(self.payment_frame, text="Card Number:")
        self.card_number_label.pack()
        self.card_number_entry = tk.Entry(self.payment_frame, width=20)
        self.card_number_entry.pack()
        self.exp_date_label = tk.Label(self.payment_frame, text="Expiration Date:")
        self.exp_date_label.pack()
        self.exp_date_entry = tk.Entry(self.payment_frame, width=20)
        self.exp_date_entry.pack()
        self.cvv_label = tk.Label(self.payment_frame, text="CVV:")
        self.cvv_label.pack()
        self.cvv_entry = tk.Entry(self.payment_frame, width=20)
        self.cvv_entry.pack()
        
        

        # Create buttons for booking and canceling
        self.book_button = tk.Button(self.root, text="Book Ticket", command=self.book_ticket)
        self.book_button.pack()
        self.cancel_button = tk.Button(self.root, text="Cancel", command=self.cancel)
        self.cancel_button.pack()

        # Pack the frames
        self.movie_frame.pack()
        self.seat_frame.pack()
        self.payment_frame.pack()

    def book_ticket(self):
        # Get the selected movie and seat
        movie = self.movie_var.get()
        seat = self.seat_var.get()

        # Get the payment details
        card_number = self.card_number_entry.get()
        exp_date = self.exp_date_entry.get()
        cvv = self.cvv_entry.get()

        # Process the payment ( dummy implementation )
        if card_number and exp_date and cvv:
            print("Payment processed successfully!")
            messagebox.showinfo("Booking Successful", f"Your ticket for {movie} has been booked for seat {seat}!")
        else:
            messagebox.showerror("Error", "Please enter valid payment details!")

    def cancel(self):
        self.root.destroy()

root = tk.Tk()
app = MovieTicketBookingSystem(root)
root.mainloop()