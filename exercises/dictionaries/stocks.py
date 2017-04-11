stockDict = {
    "GM": "General Motors",
    "CAT": "Caterpillar",
    "EK": "Eastman Kodak",
    "APPL": "Apple Inc"
    }

purchases = [('GM', 100, '10-sep-2001', 48),
             ('CAT', 100, '10-apr-1999', 24),
             ('GM', 200, '1-jul-1998', 56),
             ('APPL', 150, '1-aug-1998', 78),
             ('CAT', 75, '17-oct-2002', 24),
             ('EK', 45, '1-aug-1998', 65)]

for purchase in purchases:
    ticker_key = purchase[0]
    shares_purchased = purchase[1]
    purchase_price = purchase[3]
    purchase_date = purchase[2]
    total_price = shares_purchased * purchase_price
    company_name = stockDict[ticker_key]
    print("On {}, I purchased {} shares of {} stock for ${}".format(purchase_date, shares_purchased, company_name, total_price)+".")
