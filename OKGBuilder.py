
PREDICATE_SYMBOL = "+"
ARGS = ["argOf#1", "argOf#2"]
EMPTY = "_"


def isNounOrVerb(pos):
    return pos == "NN" or pos == "VBD" or pos == "VBN"


def createOKGStructure(sentence_ctx):
    okg = {"element_mentions": [], "statement_edge_mentions": []}

    sentence_elements = []
    statement_edge_mentions = []
    sentence_tokens = sentence_ctx["tokens"]
    sentence_predicates = {}
    count = 1

    for tokenId in sentence_tokens:
        # represent verb or noun
        if isNounOrVerb(sentence_tokens[tokenId]["pos"]):
            sentence_elements.append(sentence_tokens[tokenId]["form"])
        if sentence_tokens[tokenId]["pred"] == PREDICATE_SYMBOL:
            sentence_predicates[count] = sentence_tokens[tokenId]["form"]
            count += 1

    okg["element_mentions"] = set(sentence_elements)

    for tokenId in sentence_tokens:
        for idx,arg in enumerate(ARGS):
            if (sentence_tokens[tokenId][arg] != EMPTY):
                statement_edge_mentions.append(
                    (sentence_predicates[idx+1], sentence_tokens[tokenId]["form"], sentence_tokens[tokenId][arg]))

    okg["statement_edge_mentions"] = statement_edge_mentions

    return okg
