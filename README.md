### Simple template for a thesis based on UCL preferred style

This is a template for a [UCL](http://www.ucl.ac.uk) style thesis. Based on files developed by Tom Nielsen.

The main title/abstract is contained in MainDoc.tex. This includes the separate files for Chapter 1/2 etc.

MainDoc.bib contains the references in bibtex format, these are generally downloadable from journals' websites.

To build MainDoc.pdf type:

    make
    
This will also generate todo.html, a web page with a list of TODOs (using [todo.py](https://github.com/SilverLabUCL/simplethesis/blob/master/todo.py)) if you have any statements in any tex doc of the format: 

    \todo{This is an important reminder! ****}

Any questions, contact @pgleeson.
