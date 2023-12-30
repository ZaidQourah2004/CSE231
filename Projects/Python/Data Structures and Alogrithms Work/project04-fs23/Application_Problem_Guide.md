## Guiding Students Through the Plagiarism Detection Problem

### 1. Understand the Problem:

Before diving into the solution, it's essential to fully grasp the problem. The primary goal here is to check if two songs share a significant number of similar melodies.

#### Key takeaways:
- **Melody Similarity**: Two melodies are deemed similar if they have identical relative differences in notes, even if they're in different key signatures.
- **Similarity Threshold**: There's a defined threshold (`max_similarity`) for the number of acceptable similarities. Exceeding this threshold implies plagiarism.

### 2. Break the Problem Down:

The best way to approach complex problems is to break them down into manageable pieces:

1. **Representation of Melody**: The first step is understanding how a melody is represented and identifying what makes two melodies similar.
2. **Building a Data Structure**: Store the melodies of your song in a structure that allows quick look-up.
3. **Comparison**: Go through each melody in the competitor's song and check for similarity with your song's melodies.
4. **Counting Similarities**: Keep track of how many melodies from the competitor's song are similar to those in your song.

### 3. Analyzing the Code:

#### Melody Representation:
The primary goal is to convert each melody into a representation unaffected by key changes. This is achieved by using relative changes between notes.

For example:
- Original melody: [3, 5, 9]
- Relative changes: [2, 4]
 
#### Using a Hash Table:
The `HashTable` is employed to store the melodies of your song. Each melody (after converting to relative changes) is stored as a unique key in the hash table. This allows for quick checks to determine if a particular melody is present.

### 4. Approach:

1. **Initialize** a hash table.
2. **Insert** every melody (represented by its relative changes) of your song into this hash table.
3. **Check** each melody of the competitor's song against your hash table. If you find a match, it means there's a similar melody.
4. **Count** the number of similarities.
5. **Compare** the similarity count with `max_similarity` to determine if there's plagiarism.

### 5. Pitfalls & Tips:

1. **Melody Length**: Only melodies of the same length can be considered similar. Ensure to compare melodies of equal length.
2. **Early Termination**: If the number of similar melodies exceeds `max_similarity`, you can immediately return `True` without checking the remaining melodies. This optimization can save time.
3. **Handling Empty Songs**: If either of the songs is empty, there are no similarities, so return `False`.

