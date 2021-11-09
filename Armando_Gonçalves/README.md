# Calculator with login menu

This is a simple calculator written in python that will perform simple calculations, solve linear and quadratic equations and graph basic functions.

It has a login menu, where you do your user and password registration to access the calculator.

### How to use the calculator

You should edit the "calculadora.txt" file with the calculations you'd like to perform. Use one line for each order.

--- Syntaxe ---


- Use + - * / ^ ( ) for the usual operations (no sqrt() functionality);

- calc[] : Do calculations. **Example:**

`calc[2*(3+4/2)-(3^2)+1]`

> Output: 
>
>4

- eq[] : Solve linear and quadratic equations. Use a, b and c for the parameters. **Example:**

`eq[2,4] # This corresponds to 2x+4=0 where a = 2 and b = 4` 
> Output: 
>
>x=-2

- graph[] : Graph a  basic function (sin(x); cos(x); exp(x); log(x); sqrt(x)). **Example:**

`graph[exp(x)]`

> ![O gráfico de e^x](/Figure_1.png "Exponencial")

---

Project made for [*Hacker School*](http://hackerschool.tecnico.ulisboa.pt/). 

By arpg