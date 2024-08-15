from tkinter import *
from vote import VotingSystem

class Gui:
    def __init__(self, window: Tk, voting_system: VotingSystem):
        self.window = window
        self.voting_system = voting_system
        self.selected_candidate = None

        window.title("Voting Ballot")
        window.geometry("500x400")
        window.resizable(False, False)

        self.title_label = Label(window, text="Vote For Class President", font=("Arial", 16))
        self.title_label.pack(pady=10)

        self.name_label = Label(window, text="Please enter your Name:")
        self.name_label.pack(pady=5)
        self.name_entry = Entry(window, width=20)
        self.name_entry.pack(pady=5)

        self.candidate_var = IntVar()
        self.candidate_var.set(0)

        self.radio_john = Radiobutton(window, text="John", variable=self.candidate_var, value=1)
        self.radio_john.pack(pady=5)
        self.radio_jane = Radiobutton(window, text="Jane", variable=self.candidate_var, value=2)
        self.radio_jane.pack(pady=5)

        self.submit_button = Button(window, text="Submit Vote", command=self.submit_vote)
        self.submit_button.pack(pady=10)

        self.results_button = Button(window, text="Final Results", command=self.show_results)
        self.results_button.pack(pady=10)

        self.result_label = Label(window, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)

    def submit_vote(self):
        name = self.name_entry.get().strip()
        candidate_index = self.candidate_var.get()

        if not name:
            self.result_label.config(text="Need a name.")
            return

        if candidate_index == 0:
            self.result_label.config(text="Please select a candidate.")
            return

        try:
            self.voting_system.vote(name, candidate_index)
            self.name_entry.delete(0, END)
            self.candidate_var.set(0)
            self.result_label.config(text="Vote submitted successfully.")
        except ValueError as e:
            self.result_label.config(text=str(e))

    def show_results(self):
        john_votes = self.voting_system.get_vote_count("John")
        jane_votes = self.voting_system.get_vote_count("Jane")

        if john_votes == 0 and jane_votes == 0:
            self.result_label.config(text="There needs to be at least 1 vote to see Results.")
        elif john_votes == jane_votes:
            self.result_label.config(text="There can not be a tie.")
        else:
            if hasattr(self, 'results_window') and self.results_window is not None:
                return

            self.window.withdraw()

            self.results_window = Toplevel()
            self.results_window.title("Voting Results")
            self.results_window.geometry("400x300")

            winner = self.voting_system.get_winner()
            results_text = f"{winner} WINS!" if winner else "No votes have been casted yet."

            result_label = Label(self.results_window, text=results_text, font=("Arial", 24))
            result_label.pack(pady=20)

            vote_count_label = Label(self.results_window, text=f"John: {john_votes} votes\nJane: {jane_votes} votes", font=("Arial", 18))
            vote_count_label.pack(pady=20)

            exit_button = Button(self.results_window, text="Exit", command=self.exit_application)
            exit_button.pack(pady=10)

    def exit_application(self):
        self.results_window.destroy()
        self.window.quit()
