cd $PWD"/templates/Test_Reports/"
sed -i -- 's/amp;/ /g' *.tex

if test -f my_latex_tamplate_copy.tex;  then

pdflatex -f my_latex_tamplate_copy.tex

fi

if test -f trial_copy.tex;  then

pdflatex  trial_copy.tex

fi

if test -f trial_without_mix_copy.tex;  then

pdflatex -f trial_without_mix_copy.tex

fi

if test -f my_tamplate_without_mix_copy.tex;  then

pdflatex my_tamplate_without_mix_copy.tex

fi

if test -f soil_building_copy.tex;  then

pdflatex soil_building_copy.tex

fi

if test -f set_copy.tex;  then

pdflatex set_copy.tex

fi

if test -f bridge_copy.tex;  then

pdflatex bridge_copy.tex

fi

mv  *.pdf ../../../static/Download/
rm -f *.log
rm -f *.out
rm -f *.aux
rm -f *_copy.tex

