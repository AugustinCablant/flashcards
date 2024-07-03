#imports
import tkinter as tk
from tkinter import messagebox
import pandas as pd 


#data
df = pd.read_csv('dataframe.csv')
questions = [q for q in df['Question'].values]
answers = [a for a in df['Rep'].values]

#class
class FlashcardsApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Flashcards App")
        
        self.questions_answers = [
            (q, a)
            for q,a in zip(questions, answers)
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
