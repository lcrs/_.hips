# Prints function definitions found in Houdini's OpenCL includes folder

import os, subprocess, json

ctags = 'uctags-2025.11.27-macos-10.15-x86_64.debug/bin/ctags'
includedir = '/Applications/Houdini/Houdini21.0.512/Frameworks/Houdini.framework/Versions/Current/Resources/houdini/ocl/include'
headerdir = '/Applications/Houdini/Houdini21.0.512/Frameworks/Houdini.framework/Versions/Current/Resources/houdini/ocl/include'
outputfile = "Ls_houCLfuncs.cl"

try:
    os.makedirs('preprocessed')
except:
    pass

output = open(outputfile, 'w')
output.write("Functions found under " + headerdir + ":\n\n")

headers = sorted(os.listdir(headerdir))
for header in headers:
    subprocess.run(['cpp', '-E', '-I'+includedir, '-D__OPENCL_VERSION__', '-nostdinc', os.path.join(headerdir, header), os.path.join('preprocessed', header)])
    c = subprocess.run([ctags, '--output-format=json', '--fields=*', '--kinds-c=f', '-o', '-', os.path.join('preprocessed', header)], capture_output=True)
    for line in c.stdout.splitlines():
        j = json.loads(line)
        try:
            output.write(header + ": " + j['typeref'][9:] + " " + j['name'] + j['signature'] + "\n")
        except:
            print('Failed to print tag:', j)

output.close()
