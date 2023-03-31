# Backend Homework Assignment

Code Philosophy
----------------------------
At Recar, we strive to write clean and simple code, covered with unit tests, and easy to maintain. We also put a high value on consistency. We expect to see the same values conveyed in the problem solution.

Requirements
----------------------------
* We recommend picking your favorite programming language. No constraints here. We want you to show us what you're able to do with the tools you already know well.
* Your solution should match the philosophy described above.
* Using additional libraries (non-standard) is prohibited. That constraint is not applied for unit tests and build.
* There should be an easy way to start the solution and tests. (in python case, it could be something like: "make main", "pytest tests.py")
* A short documentation of design decisions and assumptions can be provided in the code itself.
* Make sure your input data is loaded from a file (default name 'input.txt' is assumed)
* Make sure your solution outputs data to a file output.txt in a format described below
* Your design should be flexible enough to allow adding new rules and modifying existing ones easily


Problem
----------------------------
When something is purchased, it has to be shipped, various shipping options are available. 
Each item, depending on its size gets an appropriate package size assigned to it:

  * S - Small
  * M - Medium 
  * L - Large 

Shipping price depends on package size and a provider:

| Provider | Package Size | Price  |
|---|---|---|
| SimoSiuntos| S| 1.50 € |
| SimoSiuntos| M| 4.90 € |
| SimoSiuntos| L| 6.90 € |
| JonasShipping| S| 2 €|
| JonasShipping| M| 3 €|
| JonasShipping| L| 4 €|


**Your task is to create a shipment discount calculation module.**

First, you have to implement such rules:
  * All S shipments should always match the lowest S package price among the providers.
  * The third L shipment via SimoSiuntos should be free, but only once a calendar month.
  * Accumulated discounts cannot exceed 10 € in a calendar month. If there are not enough funds to fully
  cover a discount this calendar month, it should be covered partially.

**Your design should be flexible enough to allow adding new rules and modifying existing ones easily.**

Member's transactions are listed in a file 'input.txt', each line containing: date (without hours, in ISO format), package size code, and carrier code, separated with whitespace:
```
2015-02-01 S JonasShipping
2015-02-02 S JonasShipping
2015-02-03 L SimoSiuntos
2015-02-05 S SimoSiuntos
2015-02-06 S JonasShipping
2015-02-06 L SimoSiuntos
2015-02-07 L JonasShipping
2015-02-08 M JonasShipping
2015-02-09 L SimoSiuntos
2015-02-10 L SimoSiuntos
2015-02-10 S JonasShipping
2015-02-10 S JonasShipping
2015-02-11 L SimoSiuntos
2015-02-12 M JonasShipping
2015-02-13 M SimoSiuntos
2015-02-15 S JonasShipping
2015-02-17 L SimoSiuntos
2015-02-17 S JonasShipping
2015-02-24 L SimoSiuntos
2015-02-29 CUSPS
2015-03-01 S JonasShipping
```
Your program should output transactions and append reduced shipment price and a shipment discount (or '-' if there is none). The program should append 'Ignored' word if the line format is wrong or carrier/sizes are unrecognized.
```
2015-02-01 S JonasShipping 1.50 0.50
2015-02-02 S JonasShipping 1.50 0.50
2015-02-03 L SimoSiuntos 6.90 -
2015-02-05 S SimoSiuntos 1.50 -
2015-02-06 S JonasShipping 1.50 0.50
2015-02-06 L SimoSiuntos 6.90 -
2015-02-07 L JonasShipping 4.00 -
2015-02-08 M JonasShipping 3.00 -
2015-02-09 L SimoSiuntos 0.00 6.90
2015-02-10 L SimoSiuntos 6.90 -
2015-02-10 S JonasShipping 1.50 0.50
2015-02-10 S JonasShipping 1.50 0.50
2015-02-11 L SimoSiuntos 6.90 -
2015-02-12 M JonasShipping 3.00 -
2015-02-13 M SimoSiuntos 4.90 -
2015-02-15 S JonasShipping 1.50 0.50
2015-02-17 L SimoSiuntos 6.90 -
2015-02-17 S JonasShipping 1.90 0.10
2015-02-24 L SimoSiuntos 6.90 -
2015-02-29 CUSPS Ignored
2015-03-01 S JonasShipping 1.50 0.50
```

Evaluation Criteria
----------------------------
* Your solution will be evaluated based on how well all requirements are implemented.