all:  build/V102.pdf

build:
	mkdir -p build

build/V102.pdf: build/TB-Diagramm.pdf

build/TB-Diagramm.pdf: python/Schubmodul.py rohdaten/Drahtdurchmesser.txt rohdaten/Erdmagnetfeld.txt rohdaten/MagnetischerMoment.txt rohdaten/Schubmodul.txt | build
	python python/Schubmodul.py


build/V102.pdf: FORCE | build
	  TEXINPUTS="$(call translate,build:)" \
	  BIBINPUTS=build: \
	  max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
		--interaction=nonstopmode
		--halt-on-error
	V102.tex

clean:
	rm -rf build

FORCE:

.PHONY: all clean
