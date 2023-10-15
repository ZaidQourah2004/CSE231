#include <iostream>
#include <fstream>
#include <unordered_map>
#include <string>
#include <algorithm>
#include <vector>

bool OpenFile(const std::string& filename, std::ifstream& infile) {
  infile.open(filename);
  if (!infile) {
    std::cerr << " Error: Cannot open "
              << "'" << filename << "'." << std::endl;
    return false;
  }
  return true;
}

std::unordered_map<char, char> ReadEncodingPairs() {
  std::unordered_map<char, char> pairs;
  std::string input;

  while (std::cin >> input) {
    if (input == "q") {
      return pairs;
    }

    if (input.size() != 2) {
      std::cerr << "Error: Invalid input '" << input << "'." << std::endl;
      exit(1);
    }

    char first = input.at(0);
    char second = input.at(1);

    if (pairs.count(first) > 0 && pairs[first] != second)
    /* first condition in if-statement checks if the key (first char in input)
    has already been added to the map as a key by iterating through the map and
    checking each key in each key-value pair
    second conditional in if-statement checks for the value associated with the
    key "first" in the map "pairs" is not equal to "second"  */
    {
      std::cerr << "Error: The character '" << first
                << "' is already encoded as '" << pairs[first] << "'."
                << std::endl;
      exit(1);
    }

    pairs[first] = second;  // adds the key-value pair " first : second " to the
                            // map as no errors raised
  }

  return pairs;
}

std::string ApplyEncoding(
    const std::string& input,
    const std::unordered_map<char, char>& encoding_pairs) {
  std::string output = "";
  for (char c : input)  // iterates through each char in a line
  {
    auto it = encoding_pairs.find(
        c);  // "it" points to the value associated with the key
    if (it != encoding_pairs.end())  // if key does exist
    {
      output += it->second;  // adds value of key-value pair to output
    } else {
      output += c;  // adds original char since there its not associated with
                    // another letter
    }
  }
  return output;
}

void ProcessFile(const std::string& filename,
                 const std::unordered_map<char, char>& encoding_pairs) {
  std::ifstream infile;
  if (!OpenFile(filename, infile)) {
    return;
  }
  std::vector<std::string> encoded_lines;  // makes a vector of strings where
                                           // each element of the vector is a
                                           // line

  std::string line;
  while (std::getline(infile, line)) {
    std::string encoded_line = ApplyEncoding(
        line, encoding_pairs);  // applys encoding to all chars on each line
    encoded_lines.push_back(encoded_line);  // adds line as a string as an
                                            // element of the vector
                                            // "encoded_lines"
  }

  // Below for-loop removes duplicates while preserving order
  for (auto it = encoded_lines.begin(); it != encoded_lines.end();
       ++it)  // iterates through each element in vector
  {
    if (std::count(encoded_lines.begin(), it, *it) > 0)
    // above if-statement checks all elements in vector up until current vector
    // and sees if a string (a word) is already in vector.
    {
      it = encoded_lines.erase(it);
      --it;  // so that no string is skipped
    }
  }

  for (const auto& line :
       encoded_lines)  // loops through each element of vector (each line)
  {
    std::cout << line << std::endl;
  }
}

int main()

{
  std::string filename;
  std::cin >> filename;
  std::ifstream infile;
  bool file = OpenFile(filename, infile);
  if (!file) return 1;
  std::unordered_map<char, char> pairs = ReadEncodingPairs();
  ProcessFile(filename, pairs);
}
