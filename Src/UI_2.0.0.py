import translator_info as bt
import py_to_scad as pyscad

def sp_menu():
    print('''
    ╭────────── MENÚ DE OPCIONES
    ├───> ¿Qué desea hacer?
    ├ 1. Traducir de español a braille
    ├ 2. Traducir de braille a español
    ╰ 0. Salir''')

def en_menu():
    print('''
    ╭────────── OPTION MENU
    ├───> What would you like to do?
    ├ 1. Translate from spanish to braille
    ├ 2. Translate from braille to spanish
    ╰ 0. Exit''')

def saveastxt(filename, sp, braille):
    with open(f'{filename}.txt', 'w', encoding='utf-8') as f:
        f.write("Español / Spanish:");f.write("\n");f.write(sp);f.write("\n\n")
        f.write("Braille:");f.write("\n");f.write(braille)

def saveas3d(filename, sp):
    pyscad.pytoscad(filename, sp)
    pyscad.conversion(filename)

print("""
╭──────────────────────────────────────────────────────────────────────╮
    Para poder ver los cáracteres de braille, se debe cambiar
    la fuente por defecto de la consola y usar una que soporte los 
    cáracteres. 
    Recomendada: Cascadia Code (bit.ly/3OOIlaX)
    Instalada en el sistema: MS Gothic
╰──────────────────────────────────────────────────────────────────────╯""")

print("""
╭──────────────────────────────────────────────────────────────────────╮
    To be able to see the braille characters, you need to change
    the console's default font and use one that supports the
    characters.
    Recommended: Cascadia Code (bit.ly/3OOIlaX)
    Installed on the system: MS Gothic
╰──────────────────────────────────────────────────────────────────────╯""")

while True:
    sp_menu()
    print("")
    en_menu()

    option = input("╰> ")

    if option == "1":
        sp_txt = input("Ingrese el texto a traducir (sp-braille)\n"
        "Enter the text to translate (sp-braille)\n╰> ")
        sp_trad = bt.tradBraille(sp_txt)
        print(sp_trad)
        print("Traducción completa / Translation complete\n")

        try:
            txtorno = input("¿Desea guardarlo como archito de texto?\n"
            "Would you like to save it as text file?\n╰> ")
            if txtorno == "Si" or txtorno == "si" or txtorno == "yes" or txtorno == "Yes":
                txtfname = input("Ingrese el nombre del archivo:\n"
                "Enter the name of the file:\n╰> ")
                saveastxt(txtfname, sp_txt, sp_trad)
            elif txtorno  == "No" or txtorno == "no":
                pass

            modelorno = input("¿Desea guardarlo como modelo 3D?\n"
            "Would you like to save it as 3D model?\n╰> ")
            if modelorno == "Si" or modelorno == "si" or modelorno == "yes" or modelorno == "Yes":
                modelfname = input("Ingrese el nombre del archivo:\n"
                "Enter the name of the file:\n╰> ")
                print("\n>> Esto podrá tomar un tiempo, no cierres la consola hasta que veas el archivo .stl en tus archivos <╯")
                print(">> This might take a while, do not close your console until you see the .stl file <╯")
                saveas3d(modelfname, sp_txt)


            elif modelorno  == "No" or modelorno == "no":
                pass
        except:
            print("Input error")

    elif option == "2":
            bt_txt = input("Ingrese el texto a traducir (braille-sp)\n"
            "Enter the text to translate (braille-sp)\n╰> ")
            bt_trad = bt.tradEsp(bt_txt)
            print(bt_trad)
            print("Traducción completa / Translation complete\n")

            try:
                txtorno = input("¿Desea guardarlo como archito de texto?\n"
                "Would you like to save it as text file?\n╰> ")
                if txtorno == "Si" or txtorno == "si" or txtorno == "yes" or txtorno == "Yes":
                    txtfname = input("Ingrese el nombre del archivo:\n"
                    "Enter the name of the file:\n╰> ")
                    saveastxt(txtfname, bt_trad, bt_txt)

                modelorno = input("¿Desea guardarlo como modelo 3D?\n"
                "Would you like to save it as 3D model?\n╰> ")
                if modelorno == "Si" or modelorno == "si" or modelorno == "yes" or modelorno == "Yes":
                    modelfname = input("Ingrese el nombre del archivo:\n"
                    "Enter the name of the file:\n╰> ")
                    print("\n>> Esto podrá tomar un tiempo, no cierres la consola hasta que veas el archivo .stl en tus archivos <╯")
                    print(">> This might take a while, do not close your console until you see the .stl file <╯")
                    saveas3d(modelfname, bt_trad)

                elif modelorno  == "No" or modelorno == "no":
                    pass
            except:
                print("Input error")
    elif option == "0":
        break

    else:
        print("Input error")

exit()