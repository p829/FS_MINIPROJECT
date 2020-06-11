import tkinter as tk
import time
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk
from im_comp import *

window = tk.Tk()
myText1=StringVar()
myText2=StringVar()
myText3=StringVar()
myText4=StringVar()
window.title('PNG Image Compressor (using K MEANS)')
window.geometry("800x600+30+40")


lbl = tk.Label(window, text="PLEASE ENTER THE ABSOLUTE PATH OF THE IMAGE TO BE COMPRESSED", fg='black',font=("Helvetica", 10))
lbl.place(x=175, y=50)
txtfld1 = Entry(window, text="", bg='white', fg='black', bd=5, width=80)
txtfld1.place(x=170, y=70)
lb1_1 = Label(window, text="K(number of colours in the image) AND \nNO_OF_ITERATIONS(number of iterations) \nNO_OF_ITERATIONS CAN BE SAME AS K BECAUSE ONE ITERATION FOR ONE colour.\nYOU CAN ALSO REDUCE THE VALUE OF NO_OF_ITERATIONS \nBUT THE VALUE OF NO_OF_ITERATIONS DHOULD NOT BE GREATER THAN THE VALUE OF K", fg='blue', font=("Helvetica", 10))
lb1_1.place(x=120, y=120)
lb2 = Label(window, text="PLEASE ENTER THE VALUE OF K", fg='black', font=("Helvetica", 10))
lb2.place(x=310, y=210)
txtfld2 = Entry(window, text="", bg='white', fg='black', bd=5)
txtfld2.place(x=350, y=230)
lb3 = Label(window, text="PLEASE ENTER THE VALUE OF NO_OF_ITERATIONS", fg='black', font=("Helvetica", 10))
lb3.place(x=240, y=260)
txtfld3 = Entry(window, text="", bg='white', fg='black', bd=5)
txtfld3.place(x=350, y=280)
lb4 = Label(window, text="SIZE OF THE IMAGE BEFORE COMPRESSION", fg='black', font=("Helvetica", 10))
lb4.place(x=180, y=380)
lb4_1 = Label(window, text=0, textvariable=myText1, fg='black', font=("Helvetica", 10))
lb4_1.place(x=480, y=380)
lb4_2 = Label(window, text='KB', fg='black', font=("Helvetica", 10))
lb4_2.place(x=610, y=380)
lb5 = Label(window, text="SIZE OF THE IMAGE AFTER COMPRESSION", fg='black', font=("Helvetica", 10))
lb5.place(x=180, y=410)
lb5_1 = Label(window, text=0, textvariable=myText2, fg='black', font=("Helvetica", 10))
lb5_1.place(x=480, y=410)
lb5_2 = Label(window, text='KB', fg='black', font=("Helvetica", 10))
lb5_2.place(x=610, y=410)
lb6 = Label(window, text="IMAGE SIZE REDUCED BY", fg='black', font=("Helvetica", 10))
lb6.place(x=180, y=440)
lb6_1 = Label(window, text=0, textvariable=myText4, fg='black', font=("Helvetica", 10))
lb6_1.place(x=480, y=440)
lb6_2 = Label(window, text='%', fg='black', font=("Helvetica", 10))
lb6_2.place(x=610, y=440)
lb7 = Label(window, text="TIME TAKEN", fg='black', font=("Helvetica", 10))
lb7.place(x=180, y=470)
lb7_1 = Label(window, text=0, textvariable=myText3, fg='black', font=("Helvetica", 10))
lb7_1.place(x=480, y=470)
lb7_2 = Label(window, text='MINS', fg='black', font=("Helvetica", 10))
lb7_2.place(x=610, y=470)
lb8 = Label(window, text="COMPLETED!", fg='red', font=("Helvetica", 20))
lb8.place(x=340, y=550)


def hello():

    # Load the image
    x = txtfld1.get()

    start = time.time()

    image1 = Image.open(x)
    image1.show()
    image = np.asarray(image1) / 255
    w, h, d = image.shape

    # Get the feature matrix X
    X = image.reshape((w * h, d))
    K = int(txtfld2.get())
    no_of_iterations = int(txtfld3.get())

    # Get colours
    print('Running K-means')
    colours, a = K_mean_value(X, K, no_of_iterations)

    # Indexes for colour for each pixel
    index_value = closest_centroid(X, colours)

    # Reconstruct the image
    index_value = np.array(index_value, dtype=np.uint8)
    X_redone = np.array(colours[index_value, :] * 255, dtype=np.uint8).reshape((w, h, d))
    compressed_image = Image.fromarray(X_redone)

    # Save reconstructed image to disk
    compressed_image.save('out.png')

    image2 = Image.open('out.png')
    image2.show()

    y = os.stat(x).st_size
    y = y / 1024
    myText1.set(y)

    z = os.stat('out.png').st_size
    z = z / 1024
    myText2.set(z)

    ratio = z * 1.0 / y
    ratio1 = (round(ratio * 100, 2))
    final = 100 - ratio1
    myText4.set(final)

    end = time.time()

    # total time taken
    tt = (end - start)
    time_taken = tt / 60
    myText3.set(time_taken)


    print('Done')




btn1 = tk.Button(window, text="SHOW", fg='black', command=hello)
btn1.place(x=390, y=310)
lb9 = Label(window, text="IMAGE BEFORE AND AFTER COMPRESSION WILL BE OPENED", fg='black', font=("Helvetica", 10))
lb9.place(x=210, y=340)

window.mainloop()






