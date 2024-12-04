#include <iostream>
#include <vector>
#include <fstream>
#include <sstream>

using namespace std;

struct Result
{
  vector<int> values;
  vector<int> sizes;
  int sum;
};

Result solve(int length, vector<int> values, vector<int> sizes, int remaining_space, int cumulative_value);
void printVector(const vector<int> &vec);
void printResult(Result result);

int main(int argc, char *argv[])
{
  if (argc != 2)
  {
    cerr << "Usage: " << argv[0] << " filename.txt" << endl;
    return 1;
  }

  ifstream infile(argv[1]);
  if (!infile)
  {
    cerr << "Error: Unable to open file." << endl;
    return 1;
  }

  vector<int> values;
  vector<int> sizes;
  int length;
  int remaining_space;

  string line;
  while (getline(infile, line))
  {
    stringstream ss(line);
    string key;
    ss >> key;

    if (key == "Length:")
    {
      ss >> length;
    }
    else if (key == "Values:")
    {
      int num;
      while (ss >> num)
      {
        values.push_back(num);
      }
    }
    else if (key == "Weights:" || key == "Sizes:")
    {
      int num;
      while (ss >> num)
      {
        sizes.push_back(num);
      }
    }
    else if (key == "Remaining" && ss >> key && key == "Space:")
    {
      ss >> remaining_space;
    }
  }

  cout << "Input Length:" << endl;
  cout << length << endl;
  cout << "Input Values:" << endl;
  printVector(values);
  cout << "Input Sizes:" << endl;
  printVector(sizes);
  cout << "Input Maximum Space:" << endl;
  cout << remaining_space << endl;

  Result result = solve(length, values, sizes, remaining_space, 0);
  cout << "\nSOLUTION:\n" << endl;
  printResult(result);

  infile.close();

  return 0;
}

Result solve(int length, vector<int> values, vector<int> sizes, int remaining_space, int cumulative_value)
{
  if (remaining_space == 0)
  {
    return {vector<int>(), vector<int>(), cumulative_value};
  }
  if (length == 1)
  {
    return {vector<int>(), vector<int>(), ((sizes[0] <= remaining_space) ? values[0] : 0) + cumulative_value};
  }

  int max_value = 0;
  vector<int> best_values;
  vector<int> best_sizes;

  for (int i = 0; i < length; i++)
  {
    if (sizes[i] <= remaining_space)
    {
      vector<int> new_values = values;
      vector<int> new_sizes = sizes;
      new_values.erase(new_values.begin() + i);
      new_sizes.erase(new_sizes.begin() + i);
      Result result = solve(length - 1, new_values, new_sizes, remaining_space - sizes[i], cumulative_value + values[i]);

      if (result.sum > max_value)
      {
        max_value = result.sum;
        result.values.push_back(values[i]);
        best_values = result.values;
        result.sizes.push_back(sizes[i]);
        best_sizes = result.sizes;
      }
    }
  }
  return {best_values, best_sizes, max_value};
}

void printVector(const vector<int> &vec)
{
  cout << "[ ";
  for (size_t i = 0; i < vec.size(); ++i)
  {
    cout << vec[i];
    if (i != vec.size() - 1)
    {
      cout << ", ";
    }
  }
  cout << " ]" << endl;
}

void printResult(Result result)
{
  cout << "Values:" << endl;
  printVector(result.values);
  cout << "Sizes:" << endl;
  printVector(result.sizes);
  cout << "Total Value:\n";
  cout << result.sum << endl;
}