import wolframalpha
client = wolframalpha.Client('R9H998-R88PKEQYE9')

while True:
    q = str(input('Question:'))
    res =  client.query(q)
    out = next(res.results).text
    print(out)