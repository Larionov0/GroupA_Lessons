text = 'I love pizza. lkjdasl nasl;fn ;lnasgo;agli agln erliealir laierf'

"""
{
 : 3
l: 1
p: 1
z: 2
I: 2
}
"""
symbols_counts = {}
for symbol in text:
    if symbol in symbols_counts:
        symbols_counts[symbol] += 1
    else:
        symbols_counts[symbol] = 1

for symbol, count in symbols_counts.items():
    print(symbol, ':', count)
