import argparse

from bot.orders import (
    place_limit_order,
    place_market_order
)

parser = argparse.ArgumentParser(
    description="Binance Futures Trading Bot"
)

parser.add_argument("--symbol",required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--quantity", type=float, required=True)
parser.add_argument("--price", type=float)

args = parser.parse_args()

symbol = args.symbol.upper()
side = args.side.upper()
order_type = args.type.upper()
quantity = args.quantity
price = args.price

if order_type == "MARKET":
    
    place_market_order(
      symbol=symbol,
      side=side,
      quantity=quantity
    )
   
elif order_type == "LIMIT":
   
   if price is None:
       print("LIMIT order requires --price")
   else:
       place_limit_order(
           symbol=symbol,
           side=side,
           quantity=quantity,
           price=price
        )

else:
    print("Invalid order type") 
    



