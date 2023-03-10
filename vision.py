import cv2
import tkinter as tk
from PIL import Image, ImageTk
import subprocess
def show_frame():
    ret, frame = cap.read()
    if ret:
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(image)
        photo = ImageTk.PhotoImage(image)
        canvas.create_image(0, 0, image=photo, anchor=tk.NW)
        canvas.photo = photo
    root.after(15, show_frame)

def take_photo():
    ret, frame = cap.read()
    if ret:
        cv2.imwrite(filename='saved_img.jpg', img=frame)
        print("Image saved!")

cap = cv2.VideoCapture(0)

root = tk.Tk()
root.title("Camera App")


def run_vision():
    # Call the vision_ai.py script
    import subprocess
    subprocess.call(["python", "vision_ai.py"])

    # Load the output image
    img = cv2.imread('saved_img.jpg')

    # Display the output image
    cv2.imshow('Object Detection', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


canvas = tk.Canvas(root, width=640, height=480)
canvas.pack()

btn_photo = tk.Button(root, text="CamShoot", command=take_photo)
btn_photo.pack()

btn_quit = tk.Button(root, text="Quit", command=root.destroy)
btn_quit.pack()

btn_vision = tk.Button(root, text="Vision AI", command=run_vision)
btn_vision.pack()


show_frame()

root.mainloop()

cap.release()
cv2.destroyAllWindows()
