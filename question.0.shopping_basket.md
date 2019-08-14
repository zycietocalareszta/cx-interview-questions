# Shopping Basket

## Requirements

You are implementing a simple "shopping basket" for a supermarket. This is an important component of a shopping system whose responsibility is to calculate the final price of the items *contained* in the basket.

### Definitions

* **sub-total**: The undescounted cost of items in a basket.
* **discount**: The amount of discount which must be applied to the subtotal in order to calculate the final price of the goods in the basket.
* **total**: The final price of goods in the basking once the discount has been applied. 

### Behavior

* A basket may contain products from a "Catalogue".
* Products may be added to or removed from the basket. 
* Given the contents of the basket, and the current "Offers", the basket will determine which offers are applicable, calculate the sub-total, discount and total. 
* The design of the shopping basket should accomodate changes to the catalogue and offers.

Other considerations:
* We are only interested in the behavior of the shopping basket component. You do not need to build an API, web-interface or database.
* We expect that your solution can be implemented in plain python without any 3rd party libries. If you feel you need to include a library in your solution please provide a mechanism for us to quickly install it.
* Please provide some instructions which will help us run and test your code.
* Your solution should return the sub-total, discount and total to 2 decimal places as calculated for the basket contents.
* You can assume all prices are in £GBP, no need to consider any other currencies.

### Catalogue

Use the following products and prices in your catalogue (you can represent this within your solution however you like):

The catalogue currentluy contains these items:

* **Baked Beans** £0.99
* **Biscuits** £1.20
* **Sardines** £1.89

### Offers

The supermarket currently has these offers:

* ***Baked Beans***: buy 2 get 1 free
* ***Sardines***: 25% discount

## Examples

Examples of what would be expected for a couple of different baskets...

### Basket 1

* Baked Beans x 4
* Biscuits x 1

Should give the results:

* sub-total: £5.16
* discount: £0.99
* total: £4.17

### Basket 2

* Baked Beans x 2
* Biscuits x 1
* Sardines x 2

Should give:

* sub-total: £6.96
* discount: £0.95
* total: £6.01

