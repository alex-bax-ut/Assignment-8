# Alexein Baxley
# Repository Link: https://github.com/alex-bax-ut/Assignment-8
import math

from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

# This function loads a series of sprite images stored in a folder with a
# consistent naming pattern: sprite_# or sprite_##. It returns a list of the images.
def load_sprite(sprite_folder_name, number_of_frames):
    frames = []
    padding = math.ceil(math.log(number_of_frames - 1, 10))
    for frame in range(number_of_frames):
        folder_and_file_name = sprite_folder_name + "/sprite_" + str(frame).rjust(padding, '0') + ".png"
        frames.append(QPixmap(folder_and_file_name))

    return frames
class SpritePreview(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sprite Animation Preview")
        # This loads the provided sprite and would need to be changed for your own.
        self.num_frames = 21
        self.frames = load_sprite('spriteImages',self.num_frames)

        # Add any other instance variables needed to track information as the program
        # runs here

        # Make the GUI in the setupUI method
        self.setupUI()


    def setupUI(self):
        # An application needs a central widget - often a QFrame
        frame = QFrame()

        # Add a lot of code here to make layouts, more QFrame or QWidgets, and
        # the other components of the program.
        # Create needed connections between the UI components and slot methods
        # you define in this class.
        main_layout = QHBoxLayout()


        self.image = QLabel(self)
        self.image.setPixmap(self.frames[0])
        self.currentFrame = 0

        self.frame_timer = QTimer()
        self.frame_timer.timeout.connect(self.update)

        self.start_button = QPushButton("START")
        self.start_button.clicked.connect(self.start_frames)

        self.slider = QSlider()
        self.slider.setRange(1, 100)
        self.slider.setTickInterval(10)
        self.slider.setTickPosition(QSlider.TickPosition.TicksRight)

        self.frame_text = QLabel(self)
        self.frame_text.setText("Frames per second:")
        self.fps_text = QLabel(self)
        self.fps_text.setText("Frames per second")
        self.fps_text.setText(str(self.slider.value()))

        self.slider.valueChanged.connect(self.slider_update)

        main_layout.addWidget(self.image)
        main_layout.addWidget(self.slider)
        main_layout.addWidget(self.frame_text)
        main_layout.addWidget(self.fps_text)
        main_layout.addWidget(self.start_button)
        self.add_menu()

        frame.setLayout(main_layout)
        self.setCentralWidget(frame)

    #quits application
    def quit(self):
        QApplication.quit()

    #updates sprite
    def update(self):
        self.currentFrame += 1

        if self.currentFrame >= self.num_frames:
            self.currentFrame = 0

        self.image.setPixmap(self.frames[self.currentFrame])

    #updates fps based on slider value
    def slider_update(self, value):
        self.fps_text.setText(str(value))
        self.frame_timer.setInterval(1000//value)

    #stops animation of sprite
    def stop_frames(self):
            self.frame_timer.stop()
            self.start_button.setText("START")

    #starts animation of sprite
    def start_frames(self):
        if self.start_button.text() == "START":
            fps_val = self.slider.value()
            self.frame_timer.start(1000//fps_val)
            self.start_button.setText("STOP")
        else:
            self.stop_frames()

    #creates menu
    def add_menu(self):
        menubar = QMenuBar(None)
        self.setMenuBar(menubar)

        #add exit action
        file_menu = menubar.addMenu("&File")

        #add pause option
        pause_action = QAction('&Pause', self)
        pause_action.triggered.connect(self.stop_frames)
        file_menu.addAction(pause_action)

        file_menu.addSeparator()

        exit_action = QAction('&Exit', self)
        exit_action.triggered.connect(self.quit)
        file_menu.addAction(exit_action)

def main():
    app = QApplication([])
    # Create our custom application
    window = SpritePreview()
    # And show it
    window.show()
    app.exec()

if __name__ == "__main__":
    main()

