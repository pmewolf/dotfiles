#include <iostream>
#include <vector>

using std::vector;
using std::cin;
using std::cout;

long long MaxPairwiseProduct(const vector<int>& numbers) {
    int n = numbers.size();
    
    int max_index1=0;
    for(int i=0; i<n; i++)
        if( numbers[i] > numbers[max_index1] )
            max_index1 = i;

    int max_index2=0;
    for(int i=0; i<n; i++)
        if( (i != max_index1 ) && (numbers[i] > numbers[max_index2]))
            max_index2 = i;

    return ((long long)(numbers[max_index1]*numbers[max_index2]));


    //for (int i = 0; i < n; ++i) {
    //  for (int j = i + 1; j < n; ++j) {
    //    if (numbers[i] * numbers[j] > result) {
    //      result = numbers[i] * numbers[j];
    //    }
    //  }
    //}
    //return result;
}

int main() {
    /*
    int n;
    cin >> n;
    vector<int> numbers(n);
    for (int i = 0; i < n; ++i) {
        cin >> numbers[i];
    }

    long long result = MaxPairwiseProduct(numbers);
    */

    long long result = MaxPairwiseProduct(vector<int>(100000,0));
    cout << result << "\n";
    return 0;
}
