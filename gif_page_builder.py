# defaults

import os

contents_top = '''
<html>
    <head>
      <meta content="text/html; charset=UTF-8" http-equiv="content-type">
      <title>Hello</title>
    </head>
    <body>
        <section id="gifs" style="width: 100%; height: auto">'''

contents_bottom ='''     </section>
    </body>
</html>'''


# list and store all filenames.gif in current assigned directory

def list_gifs():
	path = "c:\inetpub\wwwroot\_gif"
	inc_ext = ['gif']
	file_names = [fn for fn in os.listdir(path) if any(fn.endswith(ext) for ext in inc_ext)]
	return file_names

# generate html

def build_html():
    test = list_gifs()

    print(contents_top)
    for item in test: 
        print("""           <a href="%s"><img src="%s" style="height:128px;border:0"></a>""" % (item, item))
    print(contents_bottom)


call = build_html()
print (call)

# write to filename
filename = "index.html"
def write_html(text, filename):
    output = open(filename, "w")
    output.write(text)
    output.close()

