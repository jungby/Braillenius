import subprocess

def conversion(files,filename):
    for f in files:
        if f.find(f"{filename}.scad"):                              #   gets the .scad file in directory
            of = f.replace('.scad', '.stl')                         #   name of the outfile .stl
            cmd = ["openscad-2021.01\openscad.exe", "-o", of, f]    #   creates openscad command
            print(cmd)
            subprocess.run(cmd)