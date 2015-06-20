from yahoo_finance import Share


PORTFOLIO = {
    'HILL': {
        'avg_buy': 7.14,
        'volume': 15,
    },
    'BRCD': {
        'avg_buy': 12.35,
        'volume': 15,
    },
}


def investment_check(portfolio):
    revenue_initial = 0
    revenue_total = 0

    print('{:=<44}'.format(''))

    for symbol, s in portfolio.items():
        share = Share(symbol)
        share_price = float(share.get_price())

        total_buy = s['volume'] * s['avg_buy']
        total_sale = s['volume'] * share_price

        revenue = total_sale - total_buy
        revenue_change = revenue / total_buy

        revenue_initial += total_buy
        revenue_total += total_sale

        print('{}\n'
              '{:>10} @ {:>6.2f}: ${:>11,.2f}\n'
              '{:>10} @ {:>6.2f}: ${:>11,.2f}\n'
              '{:>20} ${:>11,.2f} ({:+,.02%})\n'
              '{:-<44}'
              .format(
                  symbol,
                  s['volume'], s['avg_buy'], total_buy,
                  s['volume'], share_price, total_sale,
                  'Return:', revenue, revenue_change,
                  '',
              )
              )

    total_revenue = revenue_total - revenue_initial
    total_revenue_change = total_revenue / revenue_initial

    print('SUMMARY\n'
          '{:>20} ${:>11,.2f}\n'
          '{:>20} ${:>11,.2f}\n'
          '{:>20} ${:>11,.2f} ({:+,.02%})\n'
          '{:=<44}'
          .format(
              'INVESTMENT:', revenue_initial,
              'RETURN:', revenue_total,
              'TOTAL:', total_revenue, total_revenue_change,
              '',
          )
          )


if __name__ == '__main__':
    investment_check(PORTFOLIO)
