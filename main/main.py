import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):

    def __init__(self):
        super().__init__()
        # Add title
        self.setWindowTitle("Hello")

        # Set vertical layout
        self.setLayout(qtw.QVBoxLayout())

        # Create a label
        my_label = qtw.QLabel("Hello World!, What is your name?")
        
        # Change font size of label
        my_label.setFont(qtg.QFont("Times New Roman", 18))
        self.layout().addWidget(my_label)

        #Create an entry box
        my_entry = qtw.QLineEdit()
        my_entry.setObjectName("name_field")
        my_entry.setText("Type your name here...")
        self.layout().addWidget(my_entry)        

        # Create button

        button = qtw.QPushButton("Press me!",
                                 clicked = lambda: press_it())
        self.layout().addWidget(button)   

        def press_it():
            my_label.setText(f'Hello, {my_entry.text()}')
            

        
        
        self.show()



app = qtw.QApplication([])
mw = MainWindow()

app.exec_()