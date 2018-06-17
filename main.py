
from DMFileParser import load_sdp_data
from OKGBuilder import createOKGStructure
from os import path
import sys
sys.path.append(path.abspath('../../../../Code/QASemDep/'))
from SentenceGraph import SentenceGraph


#    case study:
#        sentences[390] = "The doctor stated he was told his physical safety was in jeopardy"
#        Result:
#       {
#           'element_mentions': {'jeopardy', 'told', 'doctor', 'stated', 'was', 'safety'},
#           'statement_edge_mentions': [('stated', 'doctor', 'Who'),
#                                       ('told', 'doctor', 'What'),
#                                       ('told', 'he', 'Who'),
#                                       ('stated', 'told', 'Who'),
#                                       ('told', 'physical', 'What'),
#                                       ('told', 'safety', 'What'),
#                                       ('told', 'jeopardy', 'What')]
#       }

def convert_okr_to_sentence_graph(okr_graph):
    sentence_graph = SentenceGraph(okr_graph['sentence'])
    indices = okr_graph['word_indices']
    for edge in okr_graph["statement_edge_mentions"]:
        sentence_graph.add_edge_by_indices((indices[edge[0]],indices[edge[0]]), \
                                           (indices[edge[0]], indices[edge[1]]),\
                                           "label")

    return sentence_graph

if __name__ == "__main__":
    sentences = load_sdp_data("res\\dm-sentences.pred")

    okr_graph = createOKGStructure(sentences[390])
    sentence_graph = convert_okr_to_sentence_graph(okr_graph)
