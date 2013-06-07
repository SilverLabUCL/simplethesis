MAIN           = MainDoc
BIBFILE        = MainDoc
CHAPTERPREFIX  = Chapter
TODO	       = todo

PDFLATEX       = pdflatex
RTFLATEX       = latex2rtf
BIBTEX         = bibtex
INDEX          = makeindex

default: all

all: buildmain cleanmost todo cleanlog
	
buildmain: cleanmain
	$(PDFLATEX) -draftmode $(MAIN).tex 
	$(BIBTEX) $(BIBFILE)
	$(INDEX) $(BIBFILE)
	$(PDFLATEX) -draftmode $(MAIN).tex
	$(PDFLATEX) $(MAIN).tex

	
todo:
	python $(TODO).py
	date

cleanmost:
	rm -rf $(MAIN).out $(MAIN).toc $(MAIN).idx $(MAIN).lot $(MAIN).lof $(MAIN).ind $(MAIN).ilg $(MAIN).blg $(MAIN).bbl $(MAIN).dvi $(CHAPTERPREFIX)1.aux $(CHAPTERPREFIX)2.aux $(CHAPTERPREFIX)3.aux $(CHAPTERPREFIX)4.aux $(CHAPTERPREFIX)5.aux $(CHAPTERPREFIX)6.aux 

cleanlog:
	rm -rf $(MAIN).log $(MAIN).aux 


cleanmain:
	rm -rf $(MAIN).pdf $(TODO).html 
	
clean: cleanmost cleanlog cleanmain


rtf: cleanmain
	$(PDFLATEX) $(MAIN).tex
	$(BIBTEX) $(BIBFILE)
	$(INDEX) $(BIBFILE)
	$(PDFLATEX) $(MAIN).tex
	$(RTFLATEX) $(MAIN).tex
