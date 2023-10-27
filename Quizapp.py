#importing required libraries
import tkinter as tk
from tkinter import messagebox

class Quizapp:
    def __init__(self):
        self.quiz_data = [{'question':'1. The Centre for Cellular and Molecular Biology is situated at?',
                           'options':['Patna','Jaipur','Hyderabad','New Delhi'],
                           'answer': 2},
                           {'question':'2. Where is the Railway Staff College located?',
                            'options':['Pune','Allahabad','Vadodara','Delhi'],
                            'answer': 2},
                            {'question':'3. The famous Dilwara Temples are situated in?',
                             'options':['Uttar Pradesh','Rajasthan','Maharashtra','Madhya Pradesh'],
                             'answer': 1},
                             {'question':'4. Wadia Institute of Himalayan Geology is located at?',
                              'options':['Delhi','Shimla','Dehradun','Kulu'],
                              'answer': 2},
                              {'question':'5. Bijapur is known for its?',
                              'options':['severe drought condition','Gol Gumbaz','heavy rainfall','statue of Gomateswara'],
                              'answer': 1}]
        self.current_question_index = 0
        self.score = 0
        
        self.window = tk.Tk()
        self.window.title('Quiz App')

        self.question_label = tk.Label(self.window,text='')
        self.question_label.pack()

        self.options_frame = tk.Frame(self.window)
        self.options_frame.pack()

        self.option_buttons = []

        for i in range(4):
            button = tk.Button(self.options_frame,text='',width=30,command = lambda i=i:self.check_answer(i))
            button.pack(pady=5)
            self.option_buttons.append(button)
        self.next_question_button = tk.Button(self.window,text = 'Next>>',width=30,command=self.next_question)
        self.next_question_button.pack(pady=10)
    
    def check_answer(self,selected_option):
        question_data = self.quiz_data[self.current_question_index]
        answer = question_data['answer']
        if selected_option == answer:
            self.score += 1
            messagebox.showinfo('Correct','Bravooo')
        else:
            messagebox.showinfo('Incorrect','pappu lo kalu esav')
    
    def load_question(self):
        question_data = self.quiz_data[self.current_question_index]
        self.question_label.config(text = question_data['question'])
        options = question_data['options']
        for i in range(4):
            self.option_buttons[i].config(text = options[i])
    
    def next_question(self):
        self.current_question_index += 1
        if self.current_question_index == len(self.quiz_data):
            messagebox.showinfo('Quiz over','You scored '+str(self.score))
            self.window.quit()
        else:
            self.load_question()
          
    def start_quiz(self):
        self.load_question()
        self.window.mainloop()

quiz_app = Quizapp()
quiz_app.start_quiz()






