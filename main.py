import tkinter as tk
from tkinter import messagebox

class FlashcardsApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Flashcards App")
        
        self.questions_answers = [
            ("Question 1", "Answer 1"),
            ("Question 2", "Answer 2"),
            ("Question 3", "Answer 3"),
            ("Question 4", "Answer 4"),
            ("Question 5", "Answer 5")
        ]
        
        self.current_card = 0
        
        self.question_label = tk.Label(self.master, text="")
        self.question_label.pack(pady=20)
        
        self.show_question()
        
        self.show_answer_button = tk.Button(self.master, text="Show Answer", command=self.show_answer)
        self.show_answer_button.pack(pady=10)
        
        self.next_card_button = tk.Button(self.master, text="Next Card", command=self.next_card)
        self.next_card_button.pack(pady=10)
        
    def show_question(self):
        question = self.questions_answers[self.current_card][0]
        self.question_label.config(text=question)
        
    def show_answer(self):
        answer = self.questions_answers[self.current_card][1]
        messagebox.showinfo("Answer", answer)
        
    def next_card(self):
        self.current_card += 1
        if self.current_card < len(self.questions_answers):
            self.show_question()
        else:
            messagebox.showinfo("End", "No more cards")
            self.master.destroy()

def main():
    root = tk.Tk()
    app = FlashcardsApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
