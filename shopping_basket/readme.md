# Shopping basket pricer package

Basket pricer is a tool that allows pricing systems to calculate a price of products stored in a shopping basket.

## Getting Started
Install the package with pipenv:

`pipenv install`


## Features
Basket pricer can calculate:
* sub-total price of all products stored in a shopping basket,
* discount which shall be applied to the sub-total price based on predefined offers,
* total price (sub-total minus discount)

Currently, there are 3 discount offers supported:
1. Buy X products for a price of Y number of products
2. Buy X products, get Y products free
3. X percent discount

## Requirements
There are 3 basic requirements for the pricer:
1. Shopping basket has to be provided as a mapping (dict) of products (string) to number of products (integer)
2. Catalogue has to be provided as a mapping (dict) of products (string) to price of a product (float/integer)
3. Offers is optional but if provided, it has to be a mapping (dict) of products (string) to a list of discounts for
   a given product (list of strings or a string if a only single discount shall be applied)
   
## Usage
Basic usage is included in the quick_tests.script.py file. Other examples:

Given the basket: `>>> basket = {'apple': 2, 'banana': 1}`,
a catalogue: `>>> catalogue = {'apple': 1.0, 'banana': 0.52`}
and offers: `>>> offers = {'apple': '2get1'}`

One can perform the following operations:

1) Initialize the pricer:

`>>> pricer = basket_pricer.BasketPricer(basket, catalogue, offers)`

2) Display sub-total, discount, total by using print() or simply invoking pricer:

`>>> print(pricer)`

`>>> pricer()`

3) sub-total, discount, total are available as pricer attributes:

`>>> print(f"{pricer.sub-total} | {pricer.discount} | {pricer.total}")`

4) sub-total, discount and total can be calculated with dedicated methods:

`>>> pricer.sub_total(); pricer.discount(); pricer.total()`

5) When basket gets replaced for existing pricer, all amounts are being recalculated:

`>>> second_basket = {'apple': 2, 'banana': 1}`

`>>> pricer.basket = second_basket; pricer()`

## Notice

>All files were formatted with default Black rules (version 20.8b1)
