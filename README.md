Hi! This is an explanation of my technical exercise code. 

Questions I had: 
- What is a more efficient way to get the list of expanded ranges and then flatten them into one single list? I do not feel like that part of my solution was as efficient as it could be. 

Assumptions I made:
- The ability to use outside libraries (Counter)
- That the mechanics do not need breaks, so no break period needed to be worked in. (Thankfully not real people!)
- The given lists of start and end times would not exceed a large enough amount that a run time of O(n) or higher would be inadvisable. 

Paths or Solutions I contemplated:
- I went with the initial solution that I contemplated, which was using Python so that I could use the Counter function. This is because I knew that this function was efficient and typically ran in constant time due to it using dictionaries.
  Because the given lists were static and hashable, I was able to use Counter.
- The idea behind my solution was that more than one mechanic was only needed if there was overlap, so all I needed to do was expand the range of the given start and end times and check for overlap. The amount of times that the most common
  number occurs is the minimum amount of mechanics needed. 
