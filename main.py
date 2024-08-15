from tkinter import Tk
from vote import VotingSystem
from gui import Gui

def main():
    window = Tk()
    window.title('Voting Ballot')
    window.geometry('600x400')
    window.resizable(True, True)

    candidates = ["John", "Jane"]
    voting_system = VotingSystem(candidates=candidates)
    app = Gui(window, voting_system)
    window.mainloop()

if __name__ == "__main__":
    main()
