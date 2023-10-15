#include <iostream>
using std::cout;
using std::cin;
using std::endl;
using std::size_t;
#include <string>
using std::string;

bool AtListPosition(const string& wordlist, const string& word,size_t position) 
{
  size_t word_size = word.size();
  size_t ch_counter = 0;
  size_t word_list_size = wordlist.size();

  if (position + word_size > word_list_size) 
  {
    return false;
  }
  // In case word is too big to prevent unnesacary iterating through characters.
  for (; ch_counter < word_size; ch_counter++, position++) // iterating through each ch of given word.

  {
    if (position >= word_list_size) return false;

    if (wordlist.at(position) != word.at(ch_counter)) // if the letters dont match
      return false;

    else 
    {
      if (ch_counter == 0 and position != 0)

      {
        if (wordlist.at(position - 1) != ',')  // deals with cases where word can be a substring of another word
        {
          return false;
        }
      }

      if (ch_counter + 1 == word_size) 
      {
        if (word_list_size == position + 1) // if word is last word on word-list

        {
          return true;
        }

        else 
        {
          if (wordlist.at(position + 1) != ',') 
          {
            return false;
          }
          // Above statement tackles issue where the word is in the middle of the wordlist but is not followed up by comma
          // ie: different word
        }
      }

      if (word_list_size == position + 1) // last iteration of loop
      {
        if (wordlist.at(position) == word.at(ch_counter)) // confirms all characters are the same
        {
          return true;
        }
      }
    }
  }
  return true;
}

size_t FindInList(const string& wordlist, const string& word,
                  size_t position = 0) {
  size_t word_list_size = wordlist.size();
  for (; position < word_list_size; position++) // loops through each ch of wordlist
  {
    if (AtListPosition(wordlist, word, position)) // checks if word starts at specified position in wordlist for each ch
    {
      return position;
    }
  }
  return string::npos; // if word is not in list
}

string GetFirstInList(const std::string& wordlist, string* word1,string* word2) 
{
  size_t word_1_pos = FindInList(wordlist, *word1);
  size_t word_2_pos = FindInList(wordlist, *word2);

  if (word_1_pos > word_2_pos)
    return *word2;
  else if (word_1_pos < word_2_pos)
    return *word1;
  else
    return "N/A"; // if words are in same position (word1 is word2)
} // gets position of both words in wordlist and returns the one with lowest position

size_t CountInList(const string& wordlist, const string& word) 
{
  size_t count = 0;
  size_t position = 0;

  while ((position = FindInList(wordlist, word, position)) != string::npos) 
  {
    count++;
    position++;
  }

  return count;
} // loops through each ch and if a position is returned ie: word is in position then the count is increaced.

int main() {
  string word1, word2;
  cin >> word1 >> word2;
  string wordlist;

  while (cin >> wordlist) {

      cout << GetFirstInList(wordlist, &word1, &word2) << ' '
           << CountInList(wordlist, word1) << ' '
           << CountInList(wordlist, word2) << endl;
    }
}