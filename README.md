# Distribution_From_Function
This code takes in a start-point, an end-point, the wanted number of Riemann sums, the number of random samples, and the function itself. 

The start-point and end-point are pretty self-explanitory, the random values will be sampled between them.

The wanted number of Riemann sums is the amount of possible values you want to consider in the function between the start-point and the end-point. This can be a major source of slowdown if this is larger than ~500.

The number of random samples is also pretty self-explanitory, it is the number of random values you want to test. This can be a major source of slowdown if this is larger than ~1000000. 
If the number of random samples is put less than 1000, the program also returns the actual values in addition to graphing it (this is for debugging or data-copying).

The function is the function you want to create a probability density of. If you leave the question blank, it gives -x^2+13*x as a sample function. The function supports all standard mathmatical opporations without additional formating, more specifically: sin, cos, tan, sqrt, log, exp, ^, +, *, /, -. All other opporations you have to include an "np." beforehand.
