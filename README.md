[![Build Status](https://travis-ci.org/Pavel-Durov/prisoners-riddle.svg?branch=master)](https://travis-ci.org/Pavel-Durov/prisoners-riddle)
# Prisoners riddle

### The riddle

10 prisoners are in circle-shape prison.
Each prisoner can see the rest 9 prisoners.
Each prisoner receives a number between 1-10 (there is a possibility that one, two or more will have the same number).
The number of each prisoner is hanged above the cell, in a way that each prisoner cannot see the number of itself but can see all other prisoners numbers…
Each prisoner can guess his number, if at least one prisoner guesses right - all prisoners will be free.

Prisoners are allowed to establish a strategy before they enter the cells, but once they are in and get the numbers - they cannot communicate.

Question:
What strategy prisoners can take in order to ensure that at least one of them will guess his number for sure?
## Tests:



Running tests:

```
 python -m unittest discover -s ./test -p "*_test.py"
```

