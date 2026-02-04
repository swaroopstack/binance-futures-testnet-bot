from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)

def create_order_payload(
    symbol: str,
    side: str,
    order_type: str,
    quantity: float,
    price: float | None = None
) -> dict:

    side = validate_side(side)
    order_type = validate_order_type(order_type)
    quantity = validate_quantity(quantity)
    validate_price(price, order_type)

    payload = {
        "symbol": symbol.upper(),
        "side": side,
        "type": order_type,
        "quantity": quantity,
        "newOrderRespType": "RESULT"
    }

    if order_type == "LIMIT":
        payload["price"] = price
        payload["timeInForce"] = "GTC"

    return payload
