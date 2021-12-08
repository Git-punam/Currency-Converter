import requests
from tabulate import tabulate

class Converter:
    def __init__(self,url):
        self.data=requests.get(url).json()
        self.currency_rate=self.data['rates']

    def convert(self,from_currency,amount,to_currency):
        initial_amount=amount
        if(from_currency!= 'USD'):
            amount = amount / self.currency_rate[from_currency]
        amount = round(amount * self.currency_rate[to_currency], 4)
        print(initial_amount,from_currency,"is equivalent to:", amount,to_currency)


if __name__ == '__main__':
    
    table=[]
    print("Please check below currencies:")
    list1 = ["USD", "AED", "AFN", "ALL", "AMD", "ANG", "AOA", "ARS", "AUD", "AWG", "AZN", "BAM", "BBD", "BDT", "BGN",
             "BHD"]
    list2 = ["BIF", "BMD", "BND", "BOB", "BRL", "BSD", "BTN", "BWP", "BYN", "BZD", "CAD", "CDF", "CHF", "CLP", "CNY",
             "COP"]
    list3 = ["CRC", "CUC", "CUP", "CVE", "CZK", "DJF", "DKK", "DOP", "DZD", "EGP", "ERN", "ETB", "EUR", "FJD", "FKP",
             "FOK"]
    list4 = ["GBP", "GEL", "GGP", "GHS", "GIP", "GMD", "GNF", "GTQ", "GYD", "HKD", "HNL", "HRK", "HTG", "HUF", "IDR",
             "ILS"]
    list5 = ["IMP", "INR", "IQD", "IRR", "ISK", "JMD", "JOD", "JPY", "KES", "KGS", "KHR", "KID", "KMF", "KRW", "KWD",
             "KYD"]
    list6 = ["KZT", "LAK", "LBP", "LKR", "LRD", "LSL", "LYD", "MAD", "MDL", "MGA", "MKD", "MMK", "MNT", "MOP", "MRU",
             "MUR"]
    list7 = ["MVR", "MWK", "MXN", "MYR", "MZN", "NAD", "NGN", "NIO", "NOK", "NPR", "NZD", "OMR", "PAB", "PEN", "PGK",
             "PHP"]
    list8 = ["PKR", "PLN", "PYG", "QAR", "RON", "RSD", "RUB", "RWF", "SAR", "SBD", "SCR", "SDG", "SEK", "SGD", "SHP",
             "SLL"]
    list9 = ["SOS", "SRD", "SSP", "STN", "SYP", "SZL", "THB", "TJS", "TMT", "TND", "TOP", "TRY", "TTD", "TVD", "TWD",
             "TZS"]
    list10 = ["UAH", "UGX", "UYU", "UZS", "VES", "VND", "VUV", "WST", "XAF", "XCD", "XDR", "XOF", "XPF", "YER", "ZAR",
              "ZMW"]
    table.append(list1)
    table.append(list2)
    table.append(list3)
    table.append(list4)
    table.append(list5)
    table.append(list6)
    table.append(list7)
    table.append(list8)
    table.append(list9)
    table.append(list10)
    print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
    from_currency=input("Currency you want to converted from:")
    amount=float(input("Please enter amount:"))
    to_currency=input("Currency you want to converted to:")
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    cc = Converter(url)
    cc.convert(from_currency,amount,to_currency)


