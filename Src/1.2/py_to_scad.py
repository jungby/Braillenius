import default
import re
import subprocess
from pathlib import Path
import scad_to_stl
from os import listdir

def pytoscad(filename, originaltxt):
    lineas_traducir = dict()
    arrays_posiciones = dict()
    char_qty_perline = dict()
    new_line = ""
    #---------------------------------------------------------------#
    text = originaltxt
    #---------------------------------------------------------------#
    file_name = filename
    created_file = open(file_name+".scad","w", encoding='utf-8')
    #---------------------------------------------------------------#
    lines = text.splitlines()
    quantity_to_translate = len(lines)

    for i in range(quantity_to_translate):

        #---------------------------------------------------------------#

        #   STORES POSITIONS FOR THE DICT
        positioning = []

        #   STORES LINE_TO_TRANSLATE INSIDE THE DICT
        line_to_translate = lines[i]
        lineas_traducir[i] = line_to_translate

        #---------------------------------------------------------------#
        
        spacing = -1

        #   SPACES MANAGMENT
        for j in line_to_translate:
            if j == " ":
                spacing += 1
                positioning.append(spacing)
            elif j.isnumeric():
                spacing += 2
                positioning.append(spacing)
            else:
                spacing += 1
                positioning.append(spacing)

        #---------------------------------------------------------------#

        #   STORES POSITIONING ON DICT
        arrays_posiciones[i] = positioning
        char_qty_perline[i] = spacing

    #--------------------------------------------------------------------------------------------------#

    #   ITERATES TO GET THE LONGEST LINE
    for i in range(quantity_to_translate):
        if i == 0:
            longestline = char_qty_perline[i]
        else:
            if char_qty_perline[i] > char_qty_perline[i-1]:
                longestline = char_qty_perline[i]

    #--------------------------------------------------------------------------------------------------#

    translate = -1

    if True:
            created_file.write(
                f'{default.sphere_faces}'+
                f'{default.dots}'+
                f'{default.spheres}')

            for i in range(quantity_to_translate):
                to_translate = lineas_traducir[i]
                to_translate = re.sub(r'\"',r'\\"',to_translate)
                
                #   CHECKS IF ITS A LETTER, NUMBER OR JUST A BLANK SPACE
                for k in to_translate:
                    if k.isalpha() or 'á' or 'é' or 'í' or 'ó' or 'ú' or 'ü':
                        pass
                    else:
                        if k.isnumeric():
                            new_line += default.number(k)
                        elif k == " ":
                            new_line += " "

                        to_translate = new_line

                #   CAPS ARE NOT SUPPORTED
                to_translate = to_translate.lower()

                translate = int(translate)
                translate += 1

                created_file = open(file_name+".scad","a", encoding='utf-8')
                created_file.write("//"+to_translate+"\n")

                translate = str(translate)

                created_file.write(
                f"translate([-3,-3-(10*{translate}),-0.5])\n"
                +"    cube([(8 +("+ str(longestline)+")*6),11,0.6]);\n"
                + 'module ' + (f"trad{translate}") +'(txt){\n'+
                '\tfor(i=[0:len(txt)-1])translate([6*i,(-10*'+(translate)+')]){\n'+
                '\t\tBrailleDots(dots [search(txt[i],dots)[0]][1]);\n'+
                '\t\t}\n'+
                '}\n'+
                f'trad{translate}("{to_translate}");\n\n')
            created_file.close()

def conversion():
    files = listdir('.')
    for f in files:
        if f.find(".scad") >= 0:                                    #   gets all .scad files in directory
            of = f.replace('.scad', '.stl')                         #   name of the outfile .stl
            cmd = ["openscad-2021.01\openscad.exe", "-o", of, f]    #   creates openscad command
            print(cmd)
            subprocess.run(cmd)