# Silver Bars

## Local Setup
* Clone/ download repository into desired directory
* `cd` into root of the project
* If you are not already using Python3 locally, make a virtual environment that is running it
* Run `python app.py` to launch the command line interface
* Run `python tests/liv_orders_test.py` to run the tests

## Specification

Imagine you're working as a programmer for a company called SilverBars Marketplace and you have just received a new requirement. In it we would like to display to our users how much demand for silver bars there is on the market.
To do this we would like to have a 'Live Order Board' that can provide us with the following functionality:
1) Register an order. Order must contain these fields:
* user id
* order quantity (e.g.: 3.5 kg)
* price per kg (e.g.: £303)
* order type: BUY or SELL
2) Cancel a registered order - this will remove the order from 'Live Order Board'
3) Get summary information of live orders (see explanation below) Imagine we have received the following orders:
* a) SELL: 3.5 kg for £306 [user1]
* b) SELL: 1.2 kg for £310 [user2]
* c) SELL: 1.5 kg for £307 [user3]
* d) SELL: 2.0 kg for £306 [user4]
Our ‘Live Order Board’ should provide us the following summary information: - 5.5 kg for £306 // order a + order d
* 1.5 kg for £307 // order c
* 1.2 kg for £310 // order b
The first thing to note here is that orders for the same price should be merged together (even when they are from different users). In this case it can be seen that order a) and d) were for the same amount (£306) and this is why only their sum (5.5 kg) is displayed (for £306) and not the individual orders (3.5 kg and 2.0 kg).The last thing to note is that for SELL orders the orders with lowest prices are displayed first. Opposite is true for the BUY orders.
Notes:
* Please provide a simple implementation of the live order board in any software language
* No database, UI/WEB or a standalone runnable is needed for this assignment

## Technology Used
* Python 3.7.0
* Built in libraries: uuid and unittest

## Approach
* Read spec and identify objects and functions required
* Implement simplest solutions first e.g. Simple create, delete, list functionality
* Increase complexity to adhere to spec
* Refactor
* Test



## Limitations
* Time
    * I only had a couple of hours to spend on this project and so I went for the simplest approach

## Improvements
* Defend edge cases such as invalid user input and attribute types
* Create a Web UI using Webapp2, instead of the CLI
* Store objects in Google Datastore database
* Host the application using Appengine
* Create secure log in with Google Users
* Create more tests that cover edge cases
* Encapsulate more logic out of the controller (app.py)
