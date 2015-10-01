#!/Applications/Mathematica.app/Contents/MacOS/MathematicaScript -script
value=ToExpression[$ScriptCommandLine[[2]]];

(*The next line prints the script name.*)
(*Print[$ScriptCommandLine[[1]]];*)

Print[value];