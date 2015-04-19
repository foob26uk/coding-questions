
# 1.11
# just hash the set of attributes, so H[set of attributes] = unique key value of user
# if set of attributes is a set of strings, can concatenate sorted set, and use that as
# key or use bit vector if universe of attributes is small

# for approximate matching, minhash, simhash, other similar algos