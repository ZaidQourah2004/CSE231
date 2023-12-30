## Hash Function Implementation Guide

**Objective:** Implement a hash function that uses probing with double hashing for collision resolution.

### Steps:

1. **Primary & Secondary Hash Functions:**
   - **Primary Hashing:** Converts the key into an index within the hash table's capacity. The objective is to distribute the data evenly across the hash table. 
   - **Secondary Hashing (Double Hashing):** Used as a "step size" when collisions occur. Instead of stepping linearly (i.e., `index+1`), we step by the result of this secondary hash function. This ensures a better distribution during collision resolution.

2. **Initialization:**
   - Start with the result of the primary hash function as your initial index. 
   - Initialize a probe counter to track the number of steps taken in collision resolution.

3. **Probing the Hash Table:**
   - Check the node at the current index. Based on the node's status (None, occupied, deleted), decide the next action.
   
   - **Scenarios to consider:**
     - If the node is None: This means the key doesn't exist in the table. If you're inserting, you've found the right spot.
     - If the node is marked as deleted and you're inserting: Again, this is an available spot for your new entry.
     - If the node contains the desired key and is not marked as deleted: If you're searching, you've found the key. If you're inserting, this is where you'd overwrite the value (or decide your next action).

   - If none of the above scenarios match, there's a collision. You must then resolve it.

4. **Collision Resolution:**
   - Use the secondary hash function to determine your next step size.
   - Calculate the new index by adding this step size to the current index (modulus the table capacity to ensure you don't exceed the table's boundaries).
   - Continue probing with this new step until you find a match or an available slot.

5. **Return Value:**
   - Once you've either found a match or an available slot, return the index.
