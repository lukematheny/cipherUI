# Import
from string import ascii_lowercase as low
from random import choice

# Random sentence generator
def random_sentence(minLen, onlyLetterLen=False):
    
    '''
    random_sentence(minLen, onlyLetterLen=False)
    
    Generates a random sentence with its length based on minLen.
    
    Arguments:
    minLen -- Specifies minimum length of message in characters
    onlyLetterLen -- False for minLen to apply to all characters, True for
                     minLen to apply to only Letters
    
    Steps:
    1. A random leadin, subject, verb, and object are put.
    2. The amount of characters in total are determined if onlyLetterLen is
       False, otherwise the amount of letters in total are determined.
    3. Steps 1-2 are repeated and all random sentences are put in a list until
       the determined amount of characters or letters are greater than minLen.
    
    Returns the sentences.
    '''
    
    ## Variables
    # General
    sentences, length = [], 0
    minLen = (int(minLen) + 1, int(minLen))[minLen == int(minLen)]
    onlyLetterLen = bool(onlyLetterLen)
    # Sentence part lists
    leadins = ['To characterize a linguistic level L, ',
               'On the other hand, ',
               'This suggests that ',
               'It appears that ',
               'Furthermore, ',
               'We will bring evidence in favor of the following thesis: ',
               'To provide a constituent structure for T(Z,K), ',
               'From C1, it follows that ',
               'For any transformation which is sufficiently diversified in '
               + 'application to be of any interest, ',
               'Analogously, ',
               'Clearly, ',
               'Note that ',
               'Of course, ',
               'Suppose, for instance, that ',
               'Thus ',
               'With this clarification, ',
               'Conversely, ',
               'We have already seen that ',
               'By combining adjunctions and certain deformations, ',
               'I suggested that these results would follow from the '
               + 'assumption that ',
               'If the position of the trace in (99c) were only relatively '
               + 'inaccessible to movement, ',
               'However, this assumption is not correct, since ',
               'Comparing these examples with their parasitic gap '
               + 'counterparts in (96) and (97), we see that ',
               'In the discussion of resumptive pronouns following (81), ', 
               'So far, ',
               'Nevertheless, ',
               'For one thing, ',
               'Summarizing, then, we assume that ',
               'A consequence of the approach just outlined is that ',
               'Presumably, ',
               'On our assumptions, ',
               'It may be, then, that ',
               'It must be emphasized, once again, that ',
               'Let us continue to suppose that ',
               'Notice, incidentally, that ']
    subjects = ['the notion of level of grammaticalness ',
                'a case of semigrammaticalness of a different sort ',
                'most of the methodological work in modern linguistics ',
                'a subset of English sentences interesting on quite '
                + 'independent grounds ',
                'the natural general principle that will subsume this case ',
                'an important property of these three types of EC ',
                'any associated supporting element ',
                'the appearance of parasitic gaps in domains relatively '
                + 'inaccessible to ordinary extraction ',
                'the speaker-hearer\'s linguistic intuition ',
                'the descriptive power of the base component ',
                'the earlier discussion of deviance ',
                'this analysis of a formative as a pair of sets of features ',
                'this selectionally introduced contextual feature ',
                'a descriptively adequate grammar ',
                'the fundamental error of regarding functional notions as '
                + 'categorial ',
                'relational information ',
                'the systematic use of complex symbols ',
                'the theory of syntactic features developed earlier ']
    verbs = ['can be defined in such a way as to impose ',
             'delimits ',
             'suffices to account for ',
             'cannot be arbitrary in ',
             'is not subject to ',
             'does not readily tolerate ',
             'raises serious doubts about ',
             'is not quite equivalent to ',
             'does not affect the structure of ',
             'may remedy and, at the same time, eliminate ',
             'is not to be considered in determining ',
             'is to be regarded as ',
             'is unspecified with respect to ',
             'is, apparently, determined by ',
             'is necessary to impose an interpretation on ',
             'appears to correlate rather closely with ',
             'is rather different from ']
    objects = ['problems of phonemic and morphological analysis.',
               'a corpus of utterance tokens upon which conformity has been '
               + 'defined by the paired utterance test.',
               'the traditional practice of grammarians.',
               'the levels of acceptability from fairly high (e.g. (99a)) to '
               + 'virtual gibberish (e.g. (98d)).',
               'a stipulation to place the constructions into these various '
               + 'categories.',
               'a descriptive fact.',
               'a parasitic gap construction.',
               'the extended c-command discussed in connection with (34).',
               'the ultimate standard that determines the accuracy of any '
               + 'proposed grammar.',
               'the system of base rules exclusive of the lexicon.',
               'irrelevant intervening contexts in selectional rules.',
               'nondistinctness in the sense of distinctive feature theory.',
               'a general convention regarding the forms of the grammar.',
               'an abstract underlying order.',
               'an important distinction in language use.',
               'the requirement that branching is not tolerated within the '
               + 'dominance scope of a complex symbol.',
               'the strong generative capacity of the theory.']
    
    ## Generate
    while length < minLen:
        sentences.append(choice(leadins) + choice(subjects) 
                         + choice(verbs) + choice(objects))
        if onlyLetterLen:
            sentenceLen = len([x for x in sentences[-1].lower() if x in low])
        else:
            sentenceLen = len(sentences[-1]) + 1
            if length == 0: sentenceLen -= 1
        length += sentenceLen
    sentences = ' '.join(sentences)
    
    ## Return sentences
    return sentences