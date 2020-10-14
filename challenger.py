import pyRofex

def run():
    pyRofex.initialize(user          = "orianaosorio55151",
                        password     = "uugnnI5#",
                        account      = "REM5151",
                        environment  = pyRofex.Environment.REMARKET)

    md = pyRofex.get_market_data(ticker="DOOct20", entries=[pyRofex.MarketDataEntry.BIDS, pyRofex.MarketDataEntry.LAST, pyRofex.MarketDataEntry.OFFERS])

    if md["marketData"]["LA"] is not None and len(md["marketData"]["LA"]) > 0:
        # mostrar el último precio
        print(md["marketData"]["LA"]["price"])
    
    if md["marketData"]["BI"] is not None and len(md["marketData"]["BI"]) > 0:
        # mostrar el último precio de BIDS
        print(md["marketData"]["BI"][0]["price"])


if __name__ == '_main_':
    run()