\LoadClass{article}
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{set}[2011/03/26 My custom CV class]
\RequirePackage{amsmath}
\RequirePackage{amssymb}
\RequirePackage{mathtools}
\RequirePackage{multirow,tabularx}
\RequirePackage{geometry}
\RequirePackage{fixltx2e}
\RequirePackage{hyperref}
\RequirePackage{color}

\newcommand{\pagesettings}{
\geometry{
 a4paper,
 total={210mm,297mm},
 left=30mm,
 right=26mm,
 top=20mm,
 bottom=20mm,
 }
}
\newcommand{\slitfactor}[4]{
\begin{tabular}{l l l l}
\vspace{0.5cm}
The average of bed particle size = m =  & ${#1} \over 100$ & = & {#2}mm\\
\vspace{0.5cm}	
Silt factor = f= 1.76 $\sqrt{m}$  &= 1.76 $\sqrt{#3}$  & = {#4}\\
\end{tabular}
}
\newcommand{\heading}[5]{
\begin{center}
\large{\textbf{#1}}\\
\small{\textbf{\emph{#2}}}\\
\large{\textbf{#3}}\\
\end{center}
\emph{email: \color{blue}{#4}}\hfill{Phone: {#5}}
\line(1,0){450}\\
}
\newcommand{\sethead}[1]{
\begin{center}
\textbf{\LARGE{#1}}
\end{center}
}

\newcommand{\listdata}[2]{
\vspace{0.5cm}

\begin{minipage}[t]{7cm} 
\large{\emph{\textbf{#1}}}
\end{minipage}
\begin{minipage}[t]{8cm} 
\large{\emph{\textbf{#2}}}
\end{minipage} 
}
\newcommand{\reportheading}[1]{
\begin{center}
\LARGE{\textbf{V-Bridge REPORT}}
\end{center}
}
\newcommand{\reportdetail}[2]{
\vspace{1cm}
\begin{minipage}[t]{6cm} 
\large{{\textbf{#1}}}
\end{minipage}
\begin{minipage}[t]{1cm} 
\large{:}
\end{minipage} 
\begin{minipage}[t]{8cm} 
\large{{{#2}}}
\end{minipage} 
}
\newcommand{\wallfound}[2]{
\vspace{0.5cm}
\begin{center}
\begin{tabular}{l l l l}
Depth of wall foundation, &$D_f$ &= &{#1}\\
Width of wall foundation, &B   &= &{#2}\\
\end{tabular}
\end{center}
}
\newcommand{\shapefactor}[3]{
\vspace{0.2cm}
\begin{center}
\begin{tabular}{l l l l l l l l}
Sc &=&  Sq &=& {#2} S$\gamma$ &=& {#3}
\end{tabular}
\end{center}
}
\newcommand{\bearingcapacity}[3]{
\vspace{0.2cm}
\begin{center}
\begin{tabular}{l l l l l l l l l}
Nc' &=& {#1}, Nq' &=& {#2} &and &N$\gamma'$  &=& {#3}\\
\end{tabular}
\end{center}
}
\newcommand{\colfound}[5]{
\vspace{0.5cm}
\begin{center}
\begin{tabular}{l l l l}
Depth of column foundation, $D_f$ &= & {#1} \\
Size of column foundation &= &{#2} x{#3} \\
Length of column foundation , L &= &{#4} \\
Width of column foundation, B &= &{#5}\\ 
\end{tabular}
\end{center}
}
\newcommand{\depth}[4]{
\begin{tabular}{l l}
Depth of {#1} foundation below the bed level of the {#2}, Df  = {#3} m \\
Width of {#1} foundation, B =   {#4} m	
\end{tabular}
}

\newcommand{\depthfactor}[2]{
\begin{tabular}{l l}
dc       =   {#1} ,   &    dq = dγ   &   =   {#2}
\end{tabular}
}

\newcommand{\soilproperty}[4]{
\vspace{0.2cm}
\begin{center}
\begin{tabular}{l l l l l}
$\gamma$ &=& {#1}kN/$m^3$ , &c = & {#2} kN/$m^2$\\
$\phi$ &=& {#3}$^{\circ}$ , &$\phi'$  =& {#4}$^{\circ}$ 
\end{tabular}
\end{center}\
}
\newcommand{\chaptertitle}[2]{
\begin{center}
\Large{\underline{\underline{\textbf{{#1}}}}}
\Large{\underline{\underline{\textbf{{#2}}}}}
\end{center}
}
\newcommand{\footer}[2]{
\vspace{2cm}
\begin{minipage}[t]{11cm} 
\small{{\textbf{{#1}}}}
\end{minipage}
\begin{minipage}[t]{8cm} 
\small{{\textbf{{#2}}}}
\end{minipage}
}
\newcommand{\remark}[9]{
\begin{enumerate}
\item{	The bore hole log showing the nature of sub-soil stratum along with standard penetration test values(N) at different depths \& laboratory test results is attached.}
\item{The safe \textbf{Net} allowable bearing capacity for {#1}foundation  of  size {#2} m x {#3}m at depth of {#4}m below  the bed level  of the is{#5}  kN/$m^2$ is {#6}. }
\item{The  safe Gross allowable bearing capacity  for {#1} foundation of  size {#2} m x {#3} m at depth of {#4} below  the bed level of the is{#5} kN/$m^2$ {#7}.}
\item{The value of silt factor is {#8} upto a depth of {#9} m below bed level of the .}
\end{enumerate}
}

\newcommand{\openwall}[5]{
\begin{tabular}{l l}
Depth of {#1} foundation below the bed level of the {#2}, Df &=   {#3} m \\
Size of  {#1} foundation	 &=	{#4} m x{#5} m\\
Length of {#1} foundation, L	&=	{#4} m		\\		
Width of {#1}foundation, B	&=	{#5} m	\\				
\end{tabular}
}
\newcommand{\standardvalue}[7]{
\begin{minipage}[t]{17cm}
\vspace{0.4cm}
\hspace{0.2cm}Safe net allowable bearing pressure for \\
\begin{tabular}{l l l l l l l l l l l}

B &=& {#1}, N &=& {#2} , S &=& {#3} \& w' &=& {#4} ] &=& {#5} kN/$m^2$ \\
\end{tabular}\\
\begin{tabular}{l l l}
Taking least of A \& B the safe net allowable bearing capacity &=& {#6} kN/$m^2$\\
\end{tabular}\\
\end{minipage}
}
\newcommand{\standardtwo}[6]{
The  safe gross  allowable  bearing capacity  for {#1} foundation {#2} m x{#3} m size at depth of  {#4} m below the bed level of the {#5} is  {#6} kN/m2.
}
\newcommand{\jet}[2]{
\begin{tabular}{l l l l l}
The average of bed particle size = m = /100  =     {#1} mm
Silt factor = f= 1.76√m      =     1.76√      =   
\end{tabular}
}
\newcommand{\gen}[9]{The hydraulic data used in these calculations have been supplied by the department.\\
\begin{tabular}{l l l l l l l}
\vspace{0.5cm}
Discharge &= Q &= {#1}  cusec   & = {#2}cumec. &\\
\vspace{0.5cm}
Bed width of the {#9}  &= B   &= {#3}  ft. & = {#4} m &\\
\vspace{0.5cm}
Discharge per unit width &= q &= $^Q/_B$  &= $^{#2}/_{#4}$    & = {#5}cum/s\\
\vspace{0.5cm} 
Normal depth of scour &= R &= 1.35 & [(${#3}\over{#6}$)$^2$]$^{1/3}$   &= {#7} m &\\
\vspace{0.5cm}              
Maximum depth of scour &= 2R &= 2 x{#7}  &= {#8}m &\\
\end{tabular}
}
\newcommand{\reftwo}[7]{
\begin{tabular}{l l l l l l}
\vspace{0.5cm}
Depth of foundation from full supply level &= $^4/_3 x{#1}$  &={#2} m \\
\vspace{0.5cm}
Full supply depth &=   y   &={#3}ft. & = {#4}m\\
\vspace{0.5cm}
Depth of foundation from bed level of the {#5}   &= {#2}- {#3}  &={#6} m,  Say    &={#7}m. \\
\end{tabular}
}
\newcommand{\jambo}[4]{
\vspace{0.5cm}
\begin{tabular}{l l}
\vspace{0.5cm}
Depth of foundation below the bed level of the , Df &={#1}m\\
\vspace{0.5cm}
Size of  foundation	&={#2} m x m\\
\vspace{0.5cm}
Length of foundation, L	&={#3}m\\
\vspace{0.5cm}				
Width of foundation, B	&={#4	}m
\end{tabular}
}		