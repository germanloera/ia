def mean(data, period, end):
    if end < period:
        return 0
    else:
        values = data[end - period: end]
        return sum(values) / period


def moving_average(data, period):
    close = data["Close"]
    data["MA_"+ str(period)] = [ mean(close, period, x) for x in range(len(close)) ]
    return data

#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
