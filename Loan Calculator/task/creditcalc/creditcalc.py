import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--type')
parser.add_argument('--payment')
parser.add_argument('--principal')
parser.add_argument('--periods')
parser.add_argument('--interest')

args = parser.parse_args()

if args.type not in ['diff', 'annuity']:
    print("Incorrect parameters")
    exit()

if args.type == 'diff' and args.principal and args.interest and args.payment:
    print("Incorrect parameters")
    exit()

if args.type == 'annuity' and args.principal and args.payment and args.periods:
    print("Incorrect parameters")
    exit()

arg_list = [args.type, args.principal, args.interest, args.periods, args.payment]
arg_list = [x for x in arg_list if x is not None]

if len(arg_list) < 4:
    print("Incorrect parameters")
    exit()

if args.principal and float(args.principal) <= 0:
    print("Incorrect parameters")
    exit()

if args.payment and float(args.payment) <= 0:
    print("Incorrect parameters")
    exit()

if args.periods and float(args.periods) <= 0:
    print("Incorrect parameters")
    exit()

if args.interest and float(args.interest) <= 0:
    print("Incorrect parameters")
    exit()


def get_diff_payment(p, i, n, m):
    return math.ceil((p / n) + (i * (p - (p * ((m - 1) / n)))))


def get_month_payment(p, i, n):
    return math.ceil(p * (i * math.pow(1 + i, n)) / (math.pow(1 + i, n) - 1))


def get_principal(a, i, n):
    return math.floor(a / (i * math.pow(1 + i, n) / (math.pow(1 + i, n) - 1)))


def get_payment_period(p, i, s):
    return math.ceil(math.log(s / (s - i * p), 1 + i))


def generate_repayment_message(months):
    year = months // 12
    month = months % 12

    message = "It will take "

    if year > 0:
        message += f'{year} year'

        if year > 1:
            message += 's'

        message += ' '

    if year > 0 and month > 0:
        message += 'and '

    if month > 0:
        message += f'{month} month'

        if month > 1:
            message += 's'

        message += ' '

    message += 'to repay this loan!'

    return message


if args.type == 'diff' and args.principal and args.periods and args.interest:

    interest_rate = float(args.interest) / (12 * 100)
    periods = int(args.periods)
    principal = float(args.principal)

    total = 0

    for month in range(periods):
        amount = get_diff_payment(principal, interest_rate, periods, month + 1)
        print(f"Month 1: payment is {amount}")
        total += amount

    overpaid = int(total - principal)

    print()
    print(f"Overpayment = {overpaid}")
    exit()

if args.type == 'annuity' and args.principal and args.payment and args.interest:
    interest_rate = float(args.interest) / (12 * 100)
    payment = float(args.payment)
    principal = float(args.principal)
    month_count = get_payment_period(principal, interest_rate, payment)

    overpaid = int(month_count * payment - principal)

    print(generate_repayment_message(month_count))
    print(f"Overpayment = {overpaid}")
    exit()

if args.type == 'annuity' and args.principal and args.periods and args.interest:
    interest_rate = float(args.interest) / (12 * 100)
    period = int(args.periods)
    principal = float(args.principal)

    monthly_payment = get_month_payment(principal, interest_rate, period)

    print(f"Your monthly payment = {monthly_payment}")
    exit()

if args.type == 'annuity' and args.payment and args.periods and args.interest:
    interest_rate = float(args.interest) / (12 * 100)
    period = int(args.periods)
    payment = float(args.payment)

    principal = get_principal(payment, interest_rate, period)

    overpaid = int((payment * period) - principal)

    print(f"Your loan principal = {principal}")
    print(f"Overpayment = {overpaid}")
    exit()