#include <iostream>

#include <string>

#include <map>

#include <vector>

#include <unordered_map>

#include <algorithm>

#include <limits>

#include <set>

#include "exchange.hpp"

void Exchange::MakeDeposit(const std::string & username,
  const std::string & asset, int amount) {
  current_users.insert(
    username); // adds the user, if user does not exist in portfolios map
  portfolios[username][asset] +=
    amount; // adds the asset to the user's account
}

void Exchange::PrintUserPortfolios(std::ostream & os) {
  os << "User Portfolios (in alphabetical order):\n";
  for (const auto & user: portfolios) {
    // Create a set to store the assets in alphabetical order
    std::set < std::string > sortedAssets;
    for (const auto & asset: user.second) {
      sortedAssets.insert(asset.first);
    }

    // Check if the user has any assets with a positive quantity
    bool asset_check = false;
    if (current_users.count(user.first)) {
      asset_check = 1;
    }

    // Print the username and assets only if the user has assets with a positive
    // quantity
    if (asset_check) {
      os << user.first << "'s Portfolio: ";
      for (const auto & asset: sortedAssets) {
        if (portfolios[user.first][asset] >
          0) // prints the user's assets if applicable
        {
          os << portfolios[user.first][asset] << " " << asset << ", ";
        }
      }
      os << std::endl;
    }
  }
}

bool Exchange::MakeWithdrawal(const std::string & username,
  const std::string & asset, int amount) {
  auto & userPortfolio = portfolios[username];

  if (userPortfolio[asset] >= amount) // checks if user has enough of the
  // currency they wish to withdraw
  {
    userPortfolio[asset] -= amount;
    return true;
  }

  return false;
}

bool Exchange::checkAssets(const Order & order) {
  const std::string & username = order.username;
  const std::string & side = order.side;
  const std::string & asset = order.asset;

  if (side == "Sell") {
    return portfolios[username][asset] >= order.amount;
  } else if (side == "Buy") {
    return portfolios[username]["USD"] >= order.price * order.amount;
  }
  return false;
}

// Helper function to remove funds or assets from the user's portfolio when
// placing an order
void Exchange::removeOrder(const Order & order) {
  const std::string & username = order.username;
  const std::string & side = order.side;
  const std::string & asset = order.asset;
  if (checkAssets(order)) {
    if (side == "Sell") {
      portfolios[username][asset] -= order.amount;
    } else if (side == "Buy") {
      portfolios[username]["USD"] -= order.amount * order.price;
    }
  }
}

void Exchange::executeTrade(Order & buyOrder, Order & sellOrder,
  int traded_quantity, bool buyer_is_taker) {
  // Update the portfolios
  portfolios[buyOrder.username][buyOrder.asset] += traded_quantity;

  auto buy_order_position =
    (std::find(allOrders.begin(), allOrders.end(), buyOrder));
  auto sell_order_position =
    (std::find(allOrders.begin(), allOrders.end(), sellOrder));
  // above two variables find the sell and buy orders that will be involved in
  // the executed trade
  buyOrder.amount -= traded_quantity;
  sellOrder.amount -= traded_quantity;
  ( * buy_order_position).amount -= traded_quantity;
  ( * sell_order_position).amount -= traded_quantity;

  int price;
  if (buyer_is_taker) {
    price = buyOrder.price;
  } else {
    price = sellOrder.price;
  }
  int executedCost = traded_quantity * price;

  // Update USD balances
  portfolios[sellOrder.username]["USD"] += executedCost;

  filledOrders[buyOrder.username].push_back(buyOrder);
  filledOrders[sellOrder.username].push_back(sellOrder);

  Trade executedTrade {
    .buyer = buyOrder.username,
      .seller = sellOrder.username,
      .asset = buyOrder.asset,
      .amount = traded_quantity,
      .price = price,
  };
  tradeHistory.push_back(executedTrade); // adds trade to trade history after
  // trade has been executed
}

void Exchange::processFilledOrders(Order & order) {
  // Lambda function to process buy orders
  auto processBuyOrder = [ & ](Order & buyOrder) {
    // Iterate through sell orders
    for (auto & sellOrderList: sellOrders) {
      // If the buy order price is lower than the sell order price, no match is
      // possible, so break
      if (buyOrder.price < sellOrderList.first) break;

      bool flag = false;
      std::vector < std::vector < Order > ::iterator > eliminator;

      // Iterate through sell orders at the given price
      for (auto & sellOrder: sellOrderList.second) {
        // If assets don't match, continue to the next sell order
        if (buyOrder.asset != sellOrder.asset) continue;

        // Determine the quantity that can be executed
        int executedQuantity = std::min(buyOrder.amount, sellOrder.amount);
        // Execute the trade
        executeTrade(buyOrder, sellOrder, executedQuantity, true);

        // If the buy order is completely filled, remove it and set the flag to
        // true
        if (buyOrder.amount == 0) {
          buyOrders[buyOrder.price].pop_back();
          allOrders.pop_back();
          flag = true;
          break;
        }

        // If the sell order is completely filled, mark it for removal and
        // remove it from allOrders
        if (sellOrder.amount == 0) {
          eliminator.push_back(std::find(sellOrderList.second.begin(),
            sellOrderList.second.end(),
            sellOrder));
          allOrders.erase(
            std::find(allOrders.begin(), allOrders.end(), sellOrder));
        }
      }

      // Remove completely filled sell orders at the given price
      for (auto iter = eliminator.rbegin(); iter != eliminator.rend(); ++iter) {
        sellOrderList.second.erase( * iter);
      }

      // If the buy order is completely filled, break out of the loop
      if (flag) break;
    }
  };

  // Lambda function to process sell orders
  auto processSellOrder = [ & ](Order & sellOrder) {
    // Iterate through buy orders in reverse order (highest price first)
    for (auto buyOrderList = buyOrders.rbegin(); buyOrderList != buyOrders.rend(); ++buyOrderList) {
      // If the sell order price is higher than the buy order price, no match is
      // possible, so break
      if (sellOrder.price > buyOrderList -> first) break;

      bool flag = false;
      std::vector < std::vector < Order > ::iterator > eliminator;

      // Iterate through buy orders at the given price
      for (auto & buyOrder: buyOrderList -> second) {
        // If assets don't match, continue to the next buy order
        if (sellOrder.asset != buyOrder.asset) continue;

        // Determine the quantity that can be executed
        int executedQuantity = std::min(sellOrder.amount, buyOrder.amount);
        // Execute the trade
        executeTrade(buyOrder, sellOrder, executedQuantity, false);

        // If the sell order is completely filled, remove it and set the flag to
        // true
        if (sellOrder.amount == 0) {
          sellOrders[sellOrder.price].pop_back();
          allOrders.pop_back();
          flag = true;
          break;
        }

        // If the buy order is completely filled, mark it for removal and remove
        // it from allOrders
        if (buyOrder.amount == 0) {
          eliminator.push_back(std::find(buyOrderList -> second.begin(),
            buyOrderList -> second.end(), buyOrder));
          allOrders.erase(
            std::find(allOrders.begin(), allOrders.end(), buyOrder));
        }
      }

      // Remove completely filled buy orders at the given price
      for (auto iter = eliminator.rbegin(); iter != eliminator.rend(); ++iter) {
        buyOrderList -> second.erase( * iter);
      }

      // If the sell order is completely filled, break out of the loop
      if (flag) break;
    }
  };

  // Check the side of the given order and call the appropriate lambda function
  // to process it
  if (order.side == "Buy") {
    processBuyOrder(order);
  } else if (order.side == "Sell") {
    processSellOrder(order);
  }
}

bool Exchange::AddOrder(const Order & order) {
  all_assets.insert(order.asset);
  // Check if the user has sufficient assets to cover the trade
  if (!checkAssets(order)) {
    return false;
  }

  allOrders.push_back(order);
  // Remove funds or assets from the user's portfolio
  removeOrder(order);

  if (order.side == "Buy") {
    buyOrders[order.price].push_back(order);
    processFilledOrders(buyOrders[order.price].back());
  } else if (order.side == "Sell") {
    sellOrders[order.price].push_back(order);
    processFilledOrders(sellOrders[order.price].back());
  }

  return true;
}

void Exchange::PrintUsersOrders(std::ostream & os) const {
  std::vector < std::string > usernames;
  for (const auto & portfolio: portfolios) // loops through each user portfolio
  {
    usernames.push_back(portfolio.first);
  }
  std::sort(usernames.begin(), usernames.end()); // sorts users alphabetically

  os << "Users Orders (in alphabetical order):\n";
  for (const std::string & username: usernames) {
    os << username << "'s Open Orders (in chronological order):\n";

    for (const auto & allOrder: allOrders) {
      if (allOrder.username == username && allOrder.amount != 0) {
        os << allOrder << "\n";
      }
    }

    os << username << "'s Filled Orders (in chronological order):\n";

    for (const Trade & trade:
        tradeHistory) // loops through each trade executed
    {
      if (trade.buyer == username) {
        os << "Buy " << trade.amount << " " << trade.asset << " at " <<
          trade.price << " USD by " << trade.buyer << "\n";
      }
      if (trade.seller == username) {
        os << "Sell " << trade.amount << " " << trade.asset << " at " <<
          trade.price << " USD by " << trade.seller << "\n";
      }
    }
  }
}

void Exchange::PrintTradeHistory(std::ostream & os) {
  os << "Trade History (in chronological order):\n";
  for (const auto & trade: tradeHistory) {
    os << trade.buyer << " Bought " << trade.amount << " of " << trade.asset <<
      " From " << trade.seller << " for " << trade.price << " USD\n";
  }
}

void Exchange::PrintBidAskSpread(std::ostream & os) {
  // Print header for the bid-ask spread information
  os << "Asset Bid Ask Spread (in alphabetical order):\n";

  // Iterate through all assets (currencies)
  for (auto & currency: all_assets) {
    // Initialize a low_sell_order with a high price value
    Order low_sell_order {
      "",
      "",
      currency,
      -1,
      std::numeric_limits < int > ::max()
    };
    // Initialize a high_buy_order with a low price value
    Order high_buy_order {
      "",
      "",
      currency,
      -1,
      0
    };

    // Iterate through all orders
    for (const auto & allOrder: allOrders) {
      // Check if the current order's asset matches the current currency
      if (allOrder.asset == currency) {
        // Update the low_sell_order if the current order has a lower price and
        // is a sell order
        if (allOrder.price < low_sell_order.price && allOrder.side == "Sell") {
          low_sell_order = allOrder;
        }
        // Update the high_buy_order if the current order has a higher price and
        // is a buy order
        if (allOrder.price > high_buy_order.price && allOrder.side == "Buy") {
          high_buy_order = allOrder;
        }
      }
    }

    // Print the highest open buy order price for the current currency
    os << currency << ": Highest Open Buy = ";
    if (high_buy_order.price > 0)
      os << high_buy_order.price;
    else
      os << "NA";

    // Print the lowest open sell order price for the current currency
    os << " USD and Lowest Open Sell = ";

    if (low_sell_order.price < std::numeric_limits < int > ::max())
      os << low_sell_order.price;
    else
      os << "NA";

    os << " USD\n";
  }
}