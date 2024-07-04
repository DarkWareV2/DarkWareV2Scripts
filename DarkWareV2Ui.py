import tkinter as tk
from tkinter import PhotoImage, messagebox, simpledialog
import os
import pyperclip
import platform
import webbrowser
import subprocess

script_dir = os.path.dirname(__file__)

CORRECT_KEY = "PermFreeKeyForJob483gfjn54jkghnytuhsdk49gjkemf39jhfgdgdfgdg4g¤GRH&#¤E&%/&"
CORRECT_KEY = "@p0NVB}vtJ[\l^r0<]6Y'?A^&XV0$+C08pg%/E`:£2Yg,EnbD~!)k3Vwu_6GQCr0MCU/)N1S3eRLm`niKVovQ5_ItZ3uTCff#yYu`5||:uJsXu7c0e5F"GZr5%BW9I,1Gq8&£"3K0+24&Z'XBL8RI{xLR*^_KAaY]vTO6ZA.1O*WliE26WrHEJ'?"8{{£3m+|XBrG£~wN=j{s6}qM2PyP57-AP;R5n£X0M{7/\tGnE{UOG=67-'C#.mUY'*FPvIoyKJoznj\[*so^6\VPZn23b@Wj7t>'`D~Zl>o7Io6INh"J+N(yBnq`WV}gl~w(O4]<9w_hW`rgj158.hvE)4K%`]\5s2fbMaAJh{3N`2Q<R"pJ.0R\£enS#6B@Nz|D;5H)=_[qaoc.-E#}4$q%>u}l,1CG#7c=K7%5*Re}c$8a3m;=E2AvOy9([7l!,nbN#0-k5-LfG1.:$53F#t.Cd)1b`N@r?5£uRDB2pnT:X\\Fb~nd%!a3S6mi)]t@cC6nr:rvy0:7ACk#yfJ7>t%Zt*UKsnivQdKLNmNBnN]i=ztv}H7=*@6JH#ie!TL#MZPxmet8Q?zLkb+jL7bCQ4CGiij1)X~~5s4)vyRZjxFKuKn@hY?]^CME=%X4:,~UFPR8*d5xBZ]Cs0twW=a7nxnx3cctkYEu_Dgd,VNtU@+}}U^5sMy5sGwe>KoafoBYV=V8zR@6?,Aep+P4~L]1HZ6H#mh.%r!Gv7KegEzVT)?kGMp84YdbgkL1*kbrYpB6uuiYaeCkdLPPkhP#F6?-?57m8TpHN3nA,C!tW!8b5Q=MfVCkY>6cXsu1FeoogpbWuvET_Kt>L,WpUpGm5iEGW*M%VyH+.!CNC=M.xr^h>27_-wG##Tg6cJQLFt2M8*#?Y)4TNFs5Y:CFgAU6Xc+!TkHd.o3:v*)ewQb^.!2Lao*k7Ry_WPnXND_Asxy4yGm2>)kF)s!!>uMsJN1!i^hwvNC*!ef7%WZ5uZ_GLH#7EAna}KD
@p0NVB}vtJ[\l^r0<]6Y'?A^&XV0$+C08pg%/E`:£2Yg,EnbD~!)k3Vwu_6GQCr0MCU/)N1S3eRLm`niKVovQ5_ItZ3uTCff#yYu`5||:uJsXu7c0e5F"GZr5%BW9I,1Gq8&£"3K0+24&Z'XBL8RI{xLR*^_KAaY]vTO6ZA.1O*WliE26WrHEJ'?"8{{£3m+|XBrG£~wN=j{s6}qM2PyP57-AP;R5n£X0M{7/\tGnE{UOG=67-'C#.mUY'*FPvIoyKJoznj\[*so^6\VPZn23b@Wj7t>'`D~Zl>o7Io6INh"J+N(yBnq`WV}gl~w(O4]<9w_hW`rgj158.hvE)4K%`]\5s2fbMaAJh{3N`2Q<R"pJ.0R\£enS#6B@Nz|D;5H)=_[qaoc.-E#}4$q%>u}l,1CG#7c=K7%5*Re}c$8a3m;=E2AvOy9([7l!,nbN#0-k5-LfG1.:$53F#t.Cd)1b`N@r?5£uRDB2pnT:X\\Fb~nd%!a3S6mi)]t@cC6nr:rvy0:7ACk#yfJ7>t%Zt*UKsnivQdKLNmNBnN]i=ztv}H7=*@6JH#ie!TL#MZPxmet8Q?zLkb+jL7bCQ4CGiij1)X~~5s4)vyRZjxFKuKn@hY?]^CME=%X4:,~UFPR8*d5xBZ]Cs0twW=a7nxnx3cctkYEu_Dgd,VNtU@+}}U^5sMy5sGwe>KoafoBYV=V8zR@6?,Aep+P4~L]1HZ6H#mh.%r!Gv7KegEzVT)?kGMp84YdbgkL1*kbrYpB6uuiYaeCkdLPPkhP#F6?-?57m8TpHN3nA,C!tW!8b5Q=MfVCkY>6cXsu1FeoogpbWuvET_Kt>L,WpUpGm5iEGW*M%VyH+.!CNC=M.xr^h>27_-wG##Tg6cJQLFt2M8*#?Y)4TNFs5Y:CFgAU6Xc+!TkHd.o3:v*)ewQb^.!2Lao*k7Ry_WPnXND_Asxy4yGm2>)kF)s!!>uMsJN1!i^hwvNC*!ef7%WZ5uZ_GLH#7EAna}KD"
PREMIUM_KEY = "GiftedByOwnerKey"


# Initial state of topmost (0 = off, 1 = on)
topmost_enabled = 0

def validate_key():
    entered_key = key_entry.get().strip()
    if entered_key == CORRECT_KEY or entered_key == PREMIUM_KEY:
        messagebox.showinfo("Success", "Key is valid.")
        key_entry.delete(0, tk.END)
        show_main_window()
    else:
        messagebox.showerror("Error", "Invalid key.")

def copy_key_link():
    link = "https://raw.githubusercontent.com/DarkWareV2/DarkWareV2Scripts/main/Key.txt"
    pyperclip.copy(link)
    messagebox.showinfo("Copied", "Key link copied to clipboard.")

def check_windows_version():
    version = platform.version()
    if "Professional" in version or "Pro" in version:
        return True
    return False

def open_buy_link():
    buy_link = "https://www.productkeys.com/product/windows-11-professional-retail/?utm_source=Google%20Shopping&utm_campaign=ProductKeys-GoogleFeed-DK&utm_medium=cpc&utm_term=5041&gad_source=1&gclid=Cj0KCQjw7ZO0BhDYARIsAFttkChb_QtB3x6Yteomf5_lD35Y0SPBWAqUMFc13U4iTHv8nOBwNlsXZYgaAhgQEALw_wcB"
    webbrowser.open(buy_link)

def toggle_topmost():
    global topmost_enabled
    if topmost_enabled == 1:
        root.attributes("-topmost", 0)  # Disable topmost
        topmost_enabled = 0
    else:
        root.attributes("-topmost", 1)  # Enable topmost
        topmost_enabled = 1

def toggle_topmost_with_key():
    entered_key = simpledialog.askstring("Enter Premium Key", "Enter Premium key to enable topmost:")
    if entered_key == PREMIUM_KEY:
        toggle_topmost()
    else:
        messagebox.showerror("Invalid Key", "Premium key is incorrect.")

def inject_button_click():
    if check_windows_version():
        injector_path = os.path.join(script_dir, "Injector", "DarkWareV2Injector.exe")
        if os.path.exists(injector_path):
            subprocess.run(injector_path, check=True)
        else:
            messagebox.showerror("Error", "Injector executable not found.")
    else:
        response = messagebox.askquestion("Need Windows Pro Version", "You need a Windows Pro version. Would you like to buy it?")
        if response == "yes":
            open_buy_link()

def show_main_window():
    key_frame.pack_forget()
    main_frame.pack(fill=tk.BOTH, expand=True)

    image_path = os.path.join(script_dir, "EXECUTER LOOKS", "DarkWareV2Background.png")
    if os.path.exists(image_path):
        image = PhotoImage(file=image_path)
        image_width = image.width()
        image_height = image.height()

        root.geometry(f"{image_width}x{image_height}")

        canvas = tk.Canvas(main_frame, width=image_width, height=image_height, highlightthickness=0)
        canvas.pack()

        canvas.create_image(0, 0, anchor='nw', image=image)
        main_frame.image = image

        # Create a text box in the center of the main window
        text_box = tk.Text(main_frame, bd=5, font=('Arial', 12), foreground='black', background='white', wrap=tk.WORD)
        text_box.config(state=tk.NORMAL)  # Make the text box editable
        text_box_width = 300
        text_box_height = 200
        text_box_x = (image_width - text_box_width) // 2
        text_box_y = (image_height - text_box_height) // 2
        canvas.create_window(text_box_x, text_box_y, anchor='nw', width=text_box_width, height=text_box_height, window=text_box)

        # Rainbow outline animation for the text box
        outline_rect = canvas.create_rectangle(text_box_x, text_box_y, text_box_x + text_box_width, text_box_y + text_box_height, width=10, outline='')

        rainbow_colors = ["#FF0000", "#FF7F00", "#FFFF00", "#00FF00", "#0000FF", "#4B0082", "#8B00FF"]
        num_colors = len(rainbow_colors)
        color_index = 0

        def update_outline_color():
            nonlocal color_index
            color_index = (color_index + 1) % num_colors
            next_color_index = (color_index + 1) % num_colors

            current_color = rainbow_colors[color_index]
            next_color = rainbow_colors[next_color_index]

            blend_colors_smoothly(current_color, next_color, 0)

        def blend_colors_smoothly(color1, color2, step):
            def blend(color1, color2, ratio):
                r1, g1, b1 = int(color1[1:3], 16), int(color1[3:5], 16), int(color1[5:], 16)
                r2, g2, b2 = int(color2[1:3], 16), int(color2[3:5], 16), int(color2[5:], 16)

                r = int(r1 * (1 - ratio) + r2 * ratio)
                g = int(g1 * (1 - ratio) + g2 * ratio)
                b = int(b1 * (1 - ratio) + b2 * ratio)

                return f"#{r:02x}{g:02x}{b:02x}"

            if step > 10:
                return
            
            blend_color = blend(color1, color2, step / 10)
            canvas.itemconfig(outline_rect, outline=blend_color)
            root.after(50, blend_colors_smoothly, color1, color2, step + 1)

            if step == 10:
                root.after(200, update_outline_color)

        update_outline_color()

        # Function to handle window dragging
        def start_drag(event):
            global x, y
            x = event.x
            y = event.y

        def drag_window(event):
            x_new = event.x_root - x
            y_new = event.y_root - y
            root.geometry(f"+{x_new}+{y_new}")

        canvas.bind("<ButtonPress-1>", start_drag)
        canvas.bind("<B1-Motion>", drag_window)

        # Create buttons
        button_margin = 10

        exit_button_path = os.path.join(script_dir, "EXECUTER LOOKS", "DarkWareV2ExitButton.png")
        if os.path.exists(exit_button_path):
            exit_button_image = PhotoImage(file=exit_button_path)
            exit_button = tk.Button(main_frame, image=exit_button_image, bd=0, highlightthickness=0, command=close_window)
            exit_button.image = exit_button_image
            canvas.create_window(image_width - exit_button_image.width() - button_margin, button_margin, anchor='nw', window=exit_button)

        injector_button_path = os.path.join(script_dir, "EXECUTER LOOKS", "DarkWareV2Injector.png")
        if os.path.exists(injector_button_path):
            injector_button_image = PhotoImage(file=injector_button_path)
            injector_button = tk.Button(main_frame, image=injector_button_image, bd=0, highlightthickness=0, command=inject_button_click)
            injector_button.image = injector_button_image
            canvas.create_window(image_width - injector_button_image.width() - button_margin, image_height - injector_button_image.height() - button_margin, anchor='nw', window=injector_button)

        settings_button_path = os.path.join(script_dir, "EXECUTER LOOKS", "DarkWareV2Settings.png")
        if os.path.exists(settings_button_path):
            settings_button_image = PhotoImage(file=settings_button_path)
            settings_button = tk.Button(main_frame, image=settings_button_image, bd=0, highlightthickness=0, command=open_settings_window)
            settings_button.image = settings_button_image
            canvas.create_window(button_margin, button_margin, anchor='nw', window=settings_button)

    else:
        print(f"Error: The background image 'DarkWareV2Background.png' does not exist in the directory '{script_dir}'.")

def open_settings_window():
    settings_window = tk.Toplevel(root)
    settings_window.title("Settings")
    settings_window.geometry("400x300")

    settings_background_path = os.path.join(script_dir, "EXECUTER LOOKS", "DarkWareV2SettingsBackground.png")
    if os.path.exists(settings_background_path):
        settings_background_image = PhotoImage(file=settings_background_path)
        settings_background_label = tk.Label(settings_window, image=settings_background_image)
        settings_background_label.pack(fill=tk.BOTH, expand=True)

        toggle_topmost_button = tk.Button(settings_window, text="Toggle Topmost", font=('Arial', 14), command=toggle_topmost_with_key)
        toggle_topmost_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    else:
        print(f"Error: The settings background image 'DarkWareV2SettingsBackground.png' does not exist in the directory '{script_dir}'.")

def close_window():
    root.destroy()

root = tk.Tk()
root.overrideredirect(True)

key_frame = tk.Frame(root)
key_frame.pack(fill=tk.BOTH, expand=True)

main_frame = tk.Frame(root)

key_entry = tk.Entry(key_frame, bd=5, font=('Arial', 14), foreground='black')
key_entry.pack(pady=20, side=tk.LEFT, padx=10)

validate_button = tk.Button(key_frame, text="Check Key", font=('Arial', 14), command=validate_key)
validate_button.pack(pady=20, side=tk.LEFT, padx=10)

copy_link_button = tk.Button(key_frame, text="Copy Key Link", font=('Arial', 14), command=copy_key_link)
copy_link_button.pack(pady=20, side=tk.LEFT, padx=10)

root.mainloop()
