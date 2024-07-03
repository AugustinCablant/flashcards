#imports
import tkinter as tk
from tkinter import messagebox, ttk
import pandas as pd 
import random

#data
df = pd.read_csv('dataframe.csv')

#class
class FlashcardsApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Flashcards App")
        
        self.flashcards = []
        self.current_card = 0
        self.language_direction = 'fr_en'  # Par défaut, français vers anglais
        
        # Créer les flashcards à partir du dataframe initial
        for index, row in df.iterrows():
            if self.language_direction == 'fr_en':
                self.flashcards.append({
                    'type': row['type'],
                    'question': row['Question'],
                    'answer': row['Rep']
                })
            else:  # Anglais vers français
                self.flashcards.append({
                    'type': row['type'],
                    'question': row['Rep'],
                    'answer': row['Question']
                })
        
        # Mélanger les flashcards
        random.shuffle(self.flashcards)
        
        # Label pour le type de carte
        self.type_label = tk.Label(self.master, text="Choose flashcard type:")
        self.type_label.pack(pady=10)
        
        # Menu déroulant pour choisir le type de carte
        self.type_var = tk.StringVar(self.master)
        self.type_var.set("All")  # Valeur par défaut
        self.type_menu = ttk.Combobox(self.master, textvariable=self.type_var, values=["All", "gram", "voc"])
        self.type_menu.pack(pady=5)
        
        # Bouton radio pour choisir la direction de la langue
        self.language_direction_var = tk.StringVar()
        self.language_direction_var.set("fr_en")  # Par défaut, français vers anglais
        self.language_radio_fr_en = tk.Radiobutton(self.master, text="French to English", variable=self.language_direction_var, value="fr_en", command=self.change_language_direction)
        self.language_radio_fr_en.pack(anchor=tk.W)
        self.language_radio_en_fr = tk.Radiobutton(self.master, text="English to French", variable=self.language_direction_var, value="en_fr", command=self.change_language_direction)
        self.language_radio_en_fr.pack(anchor=tk.W)
        
        # Bouton pour démarrer l'application de flashcards
        self.start_button = tk.Button(self.master, text="Start Flashcards", command=self.start_flashcards)
        self.start_button.pack(pady=10)
        
        self.question_label = tk.Label(self.master, text="", wraplength=600, justify="center", font=("Arial", 18))
        self.question_label.pack(pady=20)
        
        self.answer_entry = tk.Entry(self.master, font=("Arial", 14))
        self.answer_entry.pack(pady=10)
        
        self.check_answer_button = tk.Button(self.master, text="Check Answer", command=self.check_answer)
        self.check_answer_button.pack(pady=10)
        
        self.next_card_button = tk.Button(self.master, text="Next Card", command=self.next_card)
        self.next_card_button.pack(pady=10)
        
        # Champ d'entrée pour ajouter une nouvelle question
        self.new_question_entry = tk.Entry(self.master, font=("Arial", 14))
        self.new_question_entry.pack(pady=10)
        
        # Champ d'entrée pour ajouter une nouvelle réponse
        self.new_answer_entry = tk.Entry(self.master, font=("Arial", 14))
        self.new_answer_entry.pack(pady=10)
        
        # Bouton pour ajouter une nouvelle flashcard
        self.add_card_button = tk.Button(self.master, text="Add Flashcard", command=self.add_flashcard)
        self.add_card_button.pack(pady=10)
        
    def change_language_direction(self):
        # Changer la direction de la langue selon la sélection de l'utilisateur
        self.language_direction = self.language_direction_var.get()
        
        # Rafraîchir les flashcards selon la nouvelle direction de la langue
        self.flashcards.clear()
        for index, row in df.iterrows():
            if self.language_direction == 'fr_en':
                self.flashcards.append({
                    'type': row['Type'],
                    'question': row['Question'],
                    'answer': row['Answer']
                })
            else:  # Anglais vers français
                self.flashcards.append({
                    'type': row['Type'],
                    'question': row['Answer'],
                    'answer': row['Question']
                })
        
        # Mélanger les flashcards
        random.shuffle(self.flashcards)
    
    def start_flashcards(self):
        selected_type = self.type_var.get()
        
        # Filtrer les flashcards selon le type choisi
        if selected_type == "All":
            self.filtered_flashcards = self.flashcards
        else:
            self.filtered_flashcards = [card for card in self.flashcards if card['type'] == selected_type]
        
        # Mélanger les flashcards filtrées
        random.shuffle(self.filtered_flashcards)
        
        # Afficher la première carte
        self.current_card = 0
        self.show_next_card()
    
    def show_next_card(self):
        if self.current_card < len(self.filtered_flashcards):
            question = self.filtered_flashcards[self.current_card]['question']
            self.question_label.config(text=question)
            self.answer_entry.delete(0, tk.END)
        else:
            messagebox.showinfo("End", "No more cards")
            self.master.destroy()
    
    def check_answer(self):
        if self.current_card < len(self.filtered_flashcards):
            user_answer = self.answer_entry.get()
            correct_answer = self.filtered_flashcards[self.current_card]['answer']
            
            if user_answer.strip().lower() == correct_answer.lower():
                messagebox.showinfo("Correct", "Well done! Your answer is correct.")
            else:
                messagebox.showinfo("Incorrect", f"Sorry, the correct answer is:\n\n{correct_answer}")
            
            # Move to the next card
            self.current_card += 1
            self.show_next_card()
    
    def next_card(self):
        # Move to the next card without checking the answer
        self.current_card += 1
        self.show_next_card()
    
    def add_flashcard(self):
        new_question = self.new_question_entry.get()
        new_answer = self.new_answer_entry.get()
        
        if new_question and new_answer:
            new_flashcard = {
                'type': 'custom',  # Type personnalisé pour les nouvelles flashcards
                'question': new_question,
                'answer': new_answer
            }
            
            # Ajouter la nouvelle flashcard selon la direction de la langue
            if self.language_direction == 'fr_en':
                self.flashcards.append({
                    'type': 'custom',
                    'question': new_question,
                    'answer': new_answer
                })
            else:  # Anglais vers français
                self.flashcards.append({
                    'type': 'custom',
                    'question': new_answer,
                    'answer': new_question
                })
            
            self.new_question_entry.delete(0, tk.END)
            self.new_answer_entry.delete(0, tk.END)
            
            messagebox.showinfo("Success", "Flashcard added successfully!")
        else:
            messagebox.showwarning("Warning", "Please enter both question and answer.")

def main():
    root = tk.Tk()
    app = FlashcardsApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()


