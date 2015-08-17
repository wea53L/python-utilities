# just reads the contents of a directory to build a super simple index.html
# intended use is to build a gif index. 
# 2015 Warren Kopp - if you think you can use this, feel free

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
    allfiles = os.listdir("c:\inetpub\wwwroot\_gif")
    # print allfiles # debug/testing
    return allfiles

# generate html

def build_html():
    test = list_gifs()

    print contents_top
    for item in test: 
        print """           <a href="%s"><img src="%s" style="height:128px;border:0"></a>""" % (item, item)   
    print contents_bottom


call = build_html()
print call

# write to filename
filename = "index.html"
def write_html(text, filename):
    output = open(filename, "w")
    output.write(text)
    output.close()

