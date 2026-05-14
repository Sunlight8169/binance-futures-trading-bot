from bot.client import client
from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)
from bot.logging_config import logger



def place_market_order(symbol, side, quantity):


    
    try:
        
        validate_side(side)
        validate_order_type("MARKET")
        validate_quantity(quantity)
        
        logger.info(
            f"Placing MARKET order: {side} {quantity} {symbol} "
            )
        
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )
        
        print("\nMarket Order Placed Successfully!")
        print("\nOrder Summary")
        print(f"Symbol: {order['symbol']}")
        print(f"Side: {order['side']}")
        print(f"Order Type: {order['type']}")
        print(f"Status: {order['status']}")
        print(f"Order ID: {order['orderId']}")
        print(f"Quantity: {order['origQty']}")
        print(f"Executed Quantity: {order['executedQty']}")
        print(f"Average Price: {order['avgPrice']}")
        
        logger.info(f"Market Order Response: {order}")
        
        
    except ValueError as ve:
        print(f"\nValidation Error: {ve}")
        logger.error(f"Validation Error: {ve}")
            

    except Exception as e:
        print(f"\nAPI Error: {e}")
        logger.error(f"API Error: {e}")
        

def place_limit_order(symbol, side, quantity, price):
    
    try:
        
        validate_side(side)
        validate_order_type("LIMIT")
        validate_quantity(quantity)
        validate_price(price)
        
        logger.info(
            f"Placing LIMIT order: {side} {quantity} {symbol} at {price} "
            )
        
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC"
            
        )
        print("\nLimit Order Placed Successfully!")
        print("\nOrder Summary")
        print(f"Symbol: {order['symbol']}")
        print(f"Side: {order['side']}")
        print(f"Order Type: {order['type']}")
        print(f"Status: {order['status']}")
        print(f"Order ID: {order['orderId']}")
        print(f"Quantity: {order['origQty']}")
        print(f"Executed Quantity: {order['executedQty']}")
        print(f"Average Price: {order['avgPrice']}")
        
        logger.info(f"Limit Order Response: {order}")
        

    except ValueError as ve:
        print(f"\nValidation Error: {ve}")
        logger.error(f"Validation Error: {ve}")
        

    except Exception as e:
        print("Error Placing limit order:")
        print(e)
        logger.error(f"API Error: {e}")
        