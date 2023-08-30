# Weekly report 7

### Hour Reporting
| **date** | **time (h)** | **what I did** 
| --------- | ----------- | --------- 
| 28.8 | 1.5 | debugging, updating documentation
| 29.8 | 2 | fixing function next_move to start iteration from the middle, improving scoring
| 30.8 | 5.3 | changing small things in code to improve readability, debugging, testing class minimax, updating documentation
| total: | x

### Progress
Core functionality is done. The program is too slow right now. Testing isn't where I would like it to be.

### Problems
I spent a lot of time debugging. The player won after the first move and after printing the rack, I saw that the program had been changing the real rack instead of the copy. Finally realized the problem was that I needed to make a deep copy instead of a shallow copy because my rack is a nested list. After that i realized the list was still a little crooked, because the letters were wider than the number zeros, so I thought about how to fix that and found a way to print the list without the quotes so the rack is straight. 

### Next
I need to find the bottleneck in my code and improve the time complexity.
