# Airline Seating algorithm


## Getting Started



### Prerequisites


```
python 3.6 or above
```


End with an example of getting some data out of the system or using it for a little demo

## Running the program

input_seating_grid : 2D array that represents the columns and rows
e.g
```
[[3,2] ,[4,3], [2,3], [3,4]]
```
input_passenger_num : interger which represents number of passengers


```
#sample code

input_seating_grid = [[3, 2], [4, 3], [2, 3], [3, 4]]
input_passenger_num = 30

output_grid = run_main(input_passenger_num, input_seating_grid)

```

```
python train_seating_arrangement.py

```
Output : result.txt

Sample Output in terminal
```
W19 M25 A1  A2  M26 M27 A3  A4  A5  A6  M28 W20
W21 M29 A7  A8  M30 MX  A9  A10 A11 A12 MX  W22
XX  XX  XX  A13 MX  MX  A14 A15 A16 A17 MX  W23
XX  XX  XX  XX  XX  XX  XX  XX  XX  A18 MX  W24
```


## Authors

* **Leo Lo** - *Initial work*
