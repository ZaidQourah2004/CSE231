#pragma once
#include <set>
#include <iostream>
#include <string>
#include <unordered_map>
#include <map>
#include <vector>
#include <iostream>
#include "useraccount.hpp"
#include "utility.hpp"

class Exchange {
 public:

// Required Functions:

  void MakeDeposit(const std::string& username, const std::string& asset, int amount); 

  void PrintUserPortfolios(std::ostream& os); 

  bool MakeWithdrawal(const std::string& username, const std::string& asset, int amount); 
  
  bool AddOrder(const Order& order); 

  void PrintUsersOrders(std::ostream& os) const; 

  void PrintTradeHistory(std::ostream& os); 

  void PrintTradeHistory(std::ostream& os) const; 

  void PrintBidAskSpread(std::ostream& os); 

  void PrintBidAskSpread(std::ostream& os) const; 


// Helper Functions used for readability and to improve code modularity

  bool checkAssets(const Order& order);

  void removeOrder(const Order& order);
  
  void executeTrade(Order& buyOrder, Order& sellOrder, int executedQuantity, bool logic);

  void processFilledOrders(Order& order);

// Class data members

  std::map<std::string, std::map<std::string, int>> portfolios;
  std::map<int, std::vector<Order>> buyOrders;
  std::map<int, std::vector<Order>> sellOrders;
  std::map<std::string, std::vector<Order>> filledOrders;
  std::vector<Trade> tradeHistory;
  std::vector<Order> allOrders;
  std::set<std::string> current_users;
  std::set<std::string> all_assets;
};