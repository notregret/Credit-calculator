import math
import argparse


class Credit():
    def pay(self, principal, periods, interest):
        i = interest / 12 / 100
        a = principal * ((i * (1 + i) ** periods) / (((1 + i) ** periods) - 1))

        a = math.ceil(a)
        print(f'Your annuity payment = {a}')
        overpayment = a * periods - principal
        print(f'Overpayment = {overpayment}')



    def ann_(self, m_payment, periods, interest):

        i = interest / 12 / 100
        P = m_payment / ((i * (1 + i) ** periods) / (((1 + i) ** periods) - 1))
        overpayment = m_payment * periods - P
        print("Your credit principal", math.floor(P), "!")
        print(f'Overpayment = {overpayment}')


    def years_(self, principal, m_payment, interest):
        i = interest / 12 / 100
        n = math.log(m_payment / (m_payment - i * principal), 1 + i)
        h = math.ceil(n)
        years = h // 12
        months = h - years * 12
        if years == 0:
            if months > 1:
                print(months, "months")
            else:
                print(months, "month")
        elif months == 0:
            if years > 1:
                print(years, "years")
            else:
                print(years, "year")
        else:
            if years > 1 and months > 1:
                print("You need", years, "years and", months, "months to repay this credit!")
            elif years == 1 and months > 1:
                print("You need", years, "year and", months, "months to repay this credit!")
            elif years > 1 and months == 1:
                print("You need", years, "years and", months, "month to repay this credit!")
            else:
                print("You need", years, "year and", months, "month to repay this credit!")
        overpayment = m_payment * h - principal
        print(f'Overpayment = {overpayment}')
    def diff_(self, principal, periods, interest):
        i = interest / (12 * 100)
        e = 0
        for t in range(1, periods + 1):
            d = math.ceil((principal / periods) + i * (principal - (principal * (t - 1)) / periods))
            print("Month", t, ": paid out", math.ceil(d))
            e += d
            print(e)
        print("Overpayment = ", e - principal)

    def main(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("--type", "--type")
        parser.add_argument("--payment", "--payment", type=int)
        parser.add_argument("--principal", "--principal", type=int)
        parser.add_argument("--periods", "--periods", type=int)
        parser.add_argument("--interest", "--interest", type=float)
        args = parser.parse_args()
        if args.type == "annuity":
            if args.periods is None and args.principal and args.payment and args.interest:
                self.years_(args.principal, args.payment, args.interest)
            elif args.principal is None and args.payment and args.periods and args.interest:
                self.ann_(args.payment, args.periods, args.interest)
            elif args.payment is None and args.principal and args.periods and args.interest:
                self.pay(args.principal, args.periods, args.interest)
            else:
                print("Incorrect parameters")
        elif args.type == "diff" and args.principal and args.periods and args.interest:
            self.diff_(args.principal, args.periods, args.interest)
        else:
            print("Incorrect parameters")


credit = Credit()
credit.main()
