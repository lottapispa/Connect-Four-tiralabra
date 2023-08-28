# Weekly report 7

### Hour Reporting
| **date** | **time (h)** | **what I did** 
| --------- | ----------- | --------- 
| 28.8 | x | debugging, finishing documentation
| total: | x

### Progress
Core functionality is done. Testing isn't where I would like it to be.

### Problems
I spent a lot of time debugging. The player won after the first move and after printing the rack, I saw that the program  
had been changing the real rack instead of the copy. Finally realized the problem was that I needed to  
make a deep copy instead of a shallow copy because my rack is a nested list.
