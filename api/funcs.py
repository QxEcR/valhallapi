def isgame(game):
    games = ["cod", "valo", "fort", "ow"]
    return game in games


def isRank(rank):
    ranks = ["Diamond", "Gold", "Silver", "Bronze", "NA"]
    return rank in ranks


def rankOrder(game):
    ranks = ["Diamond", "Gold", "Silver", "Bronze", "NA"]
    return ranks.index(game) + 1
