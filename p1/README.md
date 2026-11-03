# Vehicle Service Management System

**Problem Statement:** PS No. 79  
**Language:** Python 3

## About
This program helps a service centre add, view, update and delete vehicle service
records. It calculates the service price with 18% GST and saves records in a
text file.

## Service prices before GST

| Service | Price |
|---|---:|
| Oil Change | Rs. 1,500 |
| Wheel Alignment | Rs. 800 |
| Full Service | Rs. 4,500 |
| Brake Repair | Rs. 2,200 |

## How to run

1. Keep `vs.py` and `services.txt` in the same folder.
2. Open a terminal in that folder.
3. Run `python vs.py`.
4. Use the menu to add, view, update or delete records.

No extra Python library is required.

## Testing the four cases from the problem statement

Use the main program menu to perform the cases in order:

1. Choose **1 (Add record)** and enter:
   - Reg no: `MH12AB1234`
   - Owner: `Rohit Patil`
   - Vehicle: `Car`
   - Service: `Oil Change`
   - Expected cost including GST: Rs. 1770.00; status: Pending.

2. Choose **3 (Update status)**:
   - Reg no: `MH12AB1234`
   - New status: `Completed`
   - Expected message: `Status updated: Pending -> Completed`.

3. Choose **1 (Add record)** and enter:
   - Reg no: `MH14ZZ0001`
   - Owner: `Asha Nair`
   - Vehicle: `Car`
   - Service: `Painting`
   - Expected: invalid service type message.

   Then choose **4 (Delete record)** and enter `KA01ZZ9999`.
   Expected: no record found message.

4. Choose **1 (Add record)** and enter:
   - Reg no: `CG07XY4321`
   - Owner: `Amit Das`
   - Vehicle: `Bike`
   - Service: `Full Service`
   - Expected cost including GST: Rs. 5310.00; status: Pending.

   Then choose **4 (Delete record)** and enter `CG07XY4321`.
   Expected: record deleted message.

**Important:** The four test cases are performed through `vs.py` itself.
There is no separate test runner. `services.txt` is only used to store saved
vehicle records; it does not contain test instructions or program code.

## Concepts used
- Class and object
- Dictionary
- Functions
- If-else conditions
- For and while loops
- File handling
- CRUD operations
