# Weekly report 7

### Hour Reporting
| **date** | **time (h)** | **what I did** 
| --------- | ----------- | --------- 
| 28.8 | 1.5 | debugging, finishing documentation
| 29.8 | 2 | fixing function next_move to start iteration from the middle, improving scoring
| total: | x

### Progress
Core functionality is done, although I would still like to improve it. Testing isn't where I would like it to be.

### Problems
I spent a lot of time debugging. The player won after the first move and after printing the rack, I saw that the program had been changing the real rack instead of the copy. Finally realized the problem was that I needed to make a deep copy instead of a shallow copy because my rack is a nested list. After that i realized the list was still a little crooked, because the letters were wider than the number zeros, so I thought about how to fix that and if I needed to just change the colors into numbers (but that would mean fixing unittests).
