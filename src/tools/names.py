info = [
['function composition and inverse functions', [
    'function composition and inherited domain and range',
    'function decomposition',
    'parametric functions and how they relate to function composition',
    'inverse functions and inherited domain and range']],

['transformations of all functions', [
    'graphical transformations by comparing two functions and listing the graphical transformations',
    'graphical transformations by rewriting a function from a list of transformations',
    'graphical transformations by transforming a graph given transformations',
    'all graphical transformations by using each type of transformation']],

['power functions, their graphs and applications', [
    'graphs of different power functions',
    'writing a power function from a list of data',
    'applications of power functions through direct or indirect variation']],

['polynomial functions, their graphs and applications', [
    'graphs of polynomial functions by graphing a polynomial that shows comprehension of how multiplicity and end behavior affect the graph',
    'factoring a higher degree polynomial with and without complex zeros',
    'factoring a higher degree polynomial that has a leading coefficiant that is not one',
    'solving polynomial equations and inequalities',
    'applications of polynomial functions']],

['rational functions, their graphs, and applications', [
    'graphs of rational functions including all intercepts and asymptotes',
    'algebraic manipulation of rational functions',
    'utilizing rational functions through applications',
    'solving rational functions inequalities']],

['exponential and logistic functions, their graphs and applications', [
    'writing exponential models', 
    'writing logistic models',
    'graphing exponential functions',
    'applying exponential models',
    'applying logistic models']],

['logarithmic functions their graphs and applications', [
    'rewriting exponentials into logarithms and logarithms into exponentials using common log, natural log, and logarithms of other bases',
    'properties of logarithms',
    'graphs of logarithms',
    'applications of logarithms']],

['vectors and their applications', [
    'different forms of vectors',
    'vector application',
    'finding the angle between two vectors']],

['polar coordinates and equations', [
    'how to graph polar coordinates',
    'converting polar coordinates to rectangular coordinates and rectangular to polar',
    'converting polar equations to rectangular equations and rectangular to polar',
    'graphs of polar equations']],

['conic sections their graphs and applications', [
    'how to make conic models that fit given conditions',
    'how to graph conic sections from equations',
    'the applications of conic sections',
    'how to algebraically manipulate conic equations into standard form',
    'parabolas, ellipses and hyperbolas']],

['sequences and series', [
    'geometric and arithmetic sequences',
    'defining sequences explicitly and recursively',
    'summations notation',
    'summing finite arithmetic and geometric sequences',
    'summing infinite geometric sequences']],

['limits', [
    'how to write asymptotes in limit notation', 
    'removable discontinuity']],
]


for index, entry in enumerate(info):
    objective, proficiencies = entry
    print index+1, objective.capitalize()
