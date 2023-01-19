## >> Instructions

>Please read before using it to prevent issues when running.

TO HAVE IN MIND:

- <b>It's not necessary to download python (or even the files) to use it, there's a .exe file available on [releases](https://github.com/jungby/Braillenius/releases) with the latest features.</b>

- If you want to use the 3D model generation, it's a must to download OpenScad from this [link](https://openscad.org/downloads.html).

- To visualize the braille translation using the UI, you need to change your terminal/console's font to one that supports the characters.

- Python users need to install the following library if you want to use the GUI:
`pip install PyQt5`

---

## >> How to 

#### **HOW TO DOWNLOAD THE PROJECT AND USE THE FILES**

1. While on [this page](https://github.com/jungby/Braillenius) click the green button "Code" and then "Download ZIP".

    _You can also find the executables on the releases_


[![screenshot-1.png](https://i.postimg.cc/ZnWcs5SV/screenshot-1.png)](https://postimg.cc/9wjZrVz7)

_If you are familiar with git, clone it instead._


2. Open the folder you downloaded and extract it.

What files should I open?
- For python users, gui (version).py or ui (version).py, Braillenius (version).exe

#### **HOW TO DOWNLOAD OPENSCAD AND ADD IT TO THE PROJECT**

1. Click [OpenScad for 32-bit systems](https://files.openscad.org/OpenSCAD-2021.01-x86-32.zip) or [OpenScad for 64-bit systems](https://files.openscad.org/OpenSCAD-2021.01-x86-64.zip).
2. Go to the folder where you saved braillenius, then go to the 1.2 version and save the .zip file there.
3. Unzip the file you just downloaded.

    [![extract-file.gif](https://i.postimg.cc/hPvsmd4W/extract-file.gif)](https://postimg.cc/PPG1sN82)

4. (Optional) Delete the .zip file.

---

#### **HOW TO INSTALL A FONT AND USE IT ON THE TERMINAL**

>You can skip steps 1,2 and 3 if you want to use your window's default font (MS Gothic)
1. Find a font that supports braille characters or download the recommended one here -> [Cascadia Font](https://github.com/microsoft/cascadia-code/releases/download/v2111.01/CascadiaCode-2111.01.zip)
2. Extract the files in CascadiaCode-2111.01\ or create a folder where you unzip the file.
3. Open the folder where you saved Cascadia Code files, go to tff folder, select every tff file, right click in one of them and click Install.

    [![extract-font-compressed.gif](https://i.postimg.cc/DwrFhfjS/extract-font-compressed.gif)](https://postimg.cc/21SgFYfY)

4. Open your terminal/console.

    For Windows Terminal users, press Ctrl + , click Defaults, Appearance, select the font on Font face and Save.
    [![change-terminal-font-compressed.gif](https://i.postimg.cc/mr7mbsDk/change-terminal-font-compressed.gif)](https://postimg.cc/jWdHXByY)

    For Command Prompt users, right click on top of the window, Properties, choose Font tab, select the fond and Ok.
    [![change-cmd-font.gif](https://i.postimg.cc/GhTFKtzT/change-cmd-font.gif)](https://postimg.cc/QHsKxX2j)
    
5. Close your terminal/console and open the UI file you want to run.