#include <iostream>
using namespace std;

int main() {

  float currPrice = 1.50;
  float locFactor = 0.00;
  float rate = 0.01;
  float GRF = 0.00;
  float CPF = 0.1;

  string loc = "";
  cout << "Enter state: ";
  cin >> loc;
        if(loc == "Texas") {
            locFactor = 0.02;
        }

        else {
            locFactor = 0.04;
        }
  
  int gallons = 0;
  cout << "Enter number of gallons: ";
  cin >> gallons;
        if(gallons > 1000) {
            GRF = 0.02;
        }

        else {
            GRF = 0.03;
        }

  float margin = currPrice * (locFactor - rate + GRF + CPF);
  float suggestedPrice = currPrice + margin;
  float total = gallons * suggestedPrice;

  cout << "Your total is $";
  printf("%.2f", total);

}