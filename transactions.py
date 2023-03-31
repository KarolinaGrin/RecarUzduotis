from datetime import datetime
from collections import defaultdict

class ShipmentDiscountCalculator:
    def __init__(self):
        self.providers = {
            "SimoSiuntos": {
                "S": 1.5,
                "M": 4.9,
                "L": 6.9,
            },
            "JonasShipping": {
                "S": 2.00,
                "M": 3.00,
                "L": 4.00,
            },
        }
        self.shipment_counts = defaultdict(int)
        self.shipment_discounts = defaultdict(float)
        self.total_discounts = 0
        self.discount_limit = 10
        self.third_l_shipment_month = None
        self.num_l_shipments = defaultdict(int)

    def process_transaction(self, transaction):
        try:
            date_str, size_code, provider_code = transaction.split()
            date = datetime.fromisoformat(date_str)
            if size_code in self.providers[provider_code]:
                shipment_cost = self.providers[provider_code][size_code]
                shipment_discount = 0.0
                
                if size_code == "S":
                    lowest_s_cost = min([self.providers[p]["S"] for p in self.providers])
                    if shipment_cost > lowest_s_cost:
                        shipment_discount = shipment_cost - lowest_s_cost
                        shipment_cost = lowest_s_cost

                elif size_code == "L" and provider_code == "SimoSiuntos":
                    month = date.month
                    if self.third_l_shipment_month != month:
                        self.third_l_shipment_month = month
                        self.num_l_shipments.clear()
                    
                    self.num_l_shipments[provider_code] += 1
                    if self.num_l_shipments[provider_code] == 3:
                        self.num_l_shipments[provider_code] = 0
                        shipment_discount = shipment_cost
                        shipment_cost = 0.0
                
                if self.total_discounts + shipment_discount > self.discount_limit:
                    shipment_discount = max(0, self.discount_limit - self.total_discounts)
                    self.total_discounts = self.discount_limit
                else:
                    self.total_discounts += shipment_discount
                
                shipment_cost = round(shipment_cost, 2)
                shipment_discount = round(shipment_discount, 2)
                
                self.shipment_counts[size_code] += 1
                self.shipment_discounts[provider_code] += shipment_discount
                
                print("{} {} {} {:.2f} {}".format(date_str, size_code, provider_code, shipment_cost, '-' if shipment_discount == 0.00 else '{:.2f}'.format(shipment_discount)))


                return
        except (ValueError, TypeError, KeyError):
            pass
        
        print(f"{transaction.strip()} Ignored")

calculator = ShipmentDiscountCalculator()

with open("input.txt") as file:
    for line in file:
        calculator.process_transaction(line)