allDocs = ["MainDoc.tex", "Chapter1.tex", "Chapter2.tex", "Chapter3.tex", "Chapter4.tex", "Chapter5.tex", "Chapter6.tex"]

print "Checking for todos in: "+str(allDocs)
 
html = file("todo.html", mode='w')

html.write("<html>\n")
html.write("<title>List of TODOs for thesis</title>\n")
html.write("<body>\n\n")


htmlString = ""
todoTotal = 0
starTotal = 0
hilite = "FF9900"

htmlString = "<div id=\"container\" style=\"width:700px; margin:25px 50px;\">\n"

import os.path

for docName in allDocs:
    
    if os.path.exists(docName):
        doc = file(docName, mode="r")
        lineNum = 0
        todoCount = 0
        starCount = 0
        todoStart = "\\todo{"
        docString = ""
        for line in doc:
            lineNum+=1
            if todoStart in line:
                index = line.find(todoStart)
                end = line.find("}",index)
                contents = line[index+len(todoStart):end]
                stars = contents.count("*")
                '''
                intStart = int(float.fromhex("FFFFFF"))
                intFin = int(float.fromhex(hilite))
                intTgt = intStart - int(stars * (intStart - intFin)/5)
                hexStr = hex(intTgt)[2:9]
                '''
                hexStr = ["FFFFFF", "FFFFCC", "FFFF99", "FFCC66", "FFCC00", "FF9900"]
                
                docString += "<p style=\"background-color:%s\">Line %i: <b style=\"color:red\">%s</b></p>\n"%(hexStr[stars], lineNum, contents)
                todoCount+=1
                starCount+=stars
                
        docString = "\n%s<br/>" %(docString)
        docString = "\n<h2>%s with <b style=\"color:red\">%i</b> TODOs, <b style=\"color:%s\">%i</b> stars</h2>\n%s" %(docName, todoCount, hilite, starCount, docString)
        htmlString += docString
        todoTotal += todoCount
        starTotal += starCount

htmlString = "<h1>List of TODOs for thesis, <b style=\"color:red\">%i</b> in total, <b style=\"color:%s\">%i</b> stars</h1>\n\n%s"%(todoTotal, hilite, starTotal, htmlString)

html.write(htmlString)

html.write("</div>\n")
html.write("</body>\n")
html.write("</html>\n")

html.close()

print "TODO list written to file: "+html.name

print "\n    %i todos in total\n    %i stars"%(todoTotal, starTotal)

import os

if os.path.isfile("MainDoc.log"):
    log = file("MainDoc.log", mode="r")
    for line in log:
	if "Output written on MainDoc.pdf (" in line:
	    print "    "+line[31:-3]

if os.path.isfile("MainDoc.aux"):
    aux = file("MainDoc.aux", mode="r")
    refcount = 0
    for line in aux:
	if "bibcite{" in line:
	    refcount = refcount+1

    print "    %i references\n"%refcount



 

