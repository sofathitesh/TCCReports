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
 right=30mm,
 top=20mm,
 bottom=20mm,
 }
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
\LARGE{\textbf{SOIL INVESTIGATION REPORT}}
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
\newcommand{\depth}[2]{
\vspace{0.2cm}
\begin{center}
\begin{tabular}{l l l l l l l l }
dc &=& {#1} , dq &=& d$\gamma$&=& {#2}
\end{tabular}
\end{center}
}
\newcommand{\shapefactor}[3]{
\vspace{0.2cm}
\begin{center}
\begin{tabular}{l l l l l l l l}
Sc &=& {#1} Sq &=& {#2} S$\gamma$ &=& {#3}
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
\newcommand{\soilproperty}[4]{
\vspace{0.2cm}
\begin{center}
\begin{tabular}{l l l l l}
$\gamma$ &=& {#1}kN/$m^3$ , &c = & {#2} kN/$m^2$\\
$\phi$ &=& {#3}$^{\circ}$ , &$\phi'$  =& {#4}$^{\circ}$ 
\end{tabular}
\end{center}

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
\newcommand{\remark}[1]{
\begin{enumerate}
\item{The bore hole log showing the nature of sub-soil stratum along with standard
penetration test values(N) at different depths \& laboratory test results is attached.}
\item{The safe \textbf{net} allowable bearing capacity for circular raft {{#1}} m diameter at a depth
of {{#2}} m from existing surface is {#3} kN/m^2}
\item{The sub-soil water was encountered at a depth {{water}} m at the time of field soil}
\end{enumerate}
}
\newcommand{\standardvalue}[6]{
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
\newcommand{\reff}[2]{
\begin{tabular}{l l l l l}
Depth of foundation &= &Df &= &{#1}\\
Diameter of circular raft foundation &= &B &= &{#2}
\end{tabular}\\
}