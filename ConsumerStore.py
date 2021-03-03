class Checkout():
    def __init__(self,price_dict,discount_dict):
        self.items = []
        self.price = price_dict
        self.discount_dict = discount_dict
        self.updated_items = []

    def scan(self,item):
        self.items.append(item)

    def total_amount(self):
        self.discount_func()
        amount = 0
        for i in self.updated_items:
            amount = amount + self.price.get(i)

        return amount


    def discount_func(self):
        updated_item = self.items.copy()
        count_dict = {}

        for item in updated_item:
            if item not in count_dict:
                count_dict[item] = 1
            else:
                count_dict[item] = count_dict.get(item)+1

        for prod in count_dict.keys():
            discount = self.discount_dict.get(prod)

            if "greater" in discount:
                count = int(discount.split("greater")[1])
                price = float(discount.split("greater")[0])
                if count_dict.get(prod) > count:
                    self.price[prod] = price

            if "free" in discount:
                free_prod = discount.split(" ")[1]
                for c in range(count_dict.get(prod)):
                    if free_prod in updated_item:
                        updated_item.remove(free_prod)

            if "pay_for" in discount:
                up_limit = int(discount.split("pay_for")[0])
                pay_for = int(discount.split("pay_for")[1])
                to_be_reduced = up_limit - pay_for
                tot_up_limit_reached = count_dict.get(prod)//up_limit
                tot_to_be_reduced = to_be_reduced*tot_up_limit_reached

                for count in range(tot_to_be_reduced):
                    updated_item.remove(prod)

        self.updated_items = updated_item


if __name__ == '__main__':
    price_dict = {"stv":549.99,"cac":1399.99,"nsh":109.50,"mch":30.00}
    discount_dict = {"stv":"499.99 greater 4" , "cac":"free mch" , "nsh":"3 pay_for 2" , "mch":"NA"}

    co = Checkout(price_dict=price_dict,discount_dict=discount_dict)
    co.scan("cac")
    co.scan("mch")
    co.scan("stv")


    print("$",co.total_amount())