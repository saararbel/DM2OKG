
from DMFileParser import load_sdp_data
from OKGBuilder import createOKGStructure

sentences = load_sdp_data("res\dm-sentences.pred")

"""
case study:
    sentences[390] = "The doctor stated he was told his physical safety was in jeopardy"
    Results:
    {
        'element_mentions': {'jeopardy', 'told', 'doctor', 'stated', 'was', 'safety'},
        'statement_edge_mentions': [('stated', 'doctor', 'Who'),
                                    ('told', 'doctor', 'What'),
                                    ('told', 'he', 'Who'),
                                    ('stated', 'told', 'Who'),
                                    ('told', 'physical', 'What'),
                                    ('told', 'safety', 'What'),
                                    ('told', 'jeopardy', 'What')]
    }
"""
print(createOKGStructure(sentences[390]))