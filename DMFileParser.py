
COLUMNS_TEST = "id, form, lemma, pos".split(", ")
COLUMNS_TRAIN = COLUMNS_TEST + "top, pred, frame,".split(", ")

def token_line_to_data(line_str):
    """
    :param line_str: a line for a token
    :return: SdpToken: a dict representation for the data of the token.
    "arg1", "arg2" and so on are the keys for columns len(COLUMNS_TRAIN) +1, len(COLUMNS_TRAIN) +2 and so on.
    """
    def column_key_iterator():
        # the first columns are constants
        for key in COLUMNS_TRAIN:
            yield key
        # after these, iterating "argOf#1" "argOf#2" etc
        i=0
        while True:
            i+=1
            yield "argOf#" + str(i)

    return dict((key, data) for key,data in zip(column_key_iterator() ,line_str.split()))

def read_SdpSentence(block):
    tokens_data = {}
    # first line in block is sentence id
    block_lines = [line.strip() for line in block.splitlines()]
    sentence_id = block_lines[0].lstrip("#")
    for line in block_lines[1:]:    # each line stands for a token
        data = token_line_to_data(line)
        id = int(data["id"])     # id is index of token (starting at 1)
        tokens_data[id] = data
    # retrieve sentence for FORM field
    sentence = ' '.join(tokens_data[i]["form"] for i in range(1, len(tokens_data)+1))
    return {"sentence" : sentence,
            "sentence_id" : sentence_id,
            "tokens" : tokens_data,
            "raw": block}

def load_sdp_data(filename):
    """ return a list of SdpSentence (json object\python dict) """
    SdpSentences = []
    with open(filename, "r", encoding="utf-8") as f:
        next(f) # skip first line in file
        block = ""
        for line in f:
            if not line.strip(): # empty line - declaring a new block
                # wrap and parse last block
                SdpSentence = read_SdpSentence(block)
                SdpSentences.append(SdpSentence)
                # logging.debug("collected annotation for sentence: " + SdpSentence["sentence"])
                block = ""

            else:
                block += line
    return SdpSentences