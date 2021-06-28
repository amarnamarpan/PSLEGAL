import os
import pslegal as psl
import extract_noun_phrases as npe
import pickle


if __name__ == '__main__':

    # ## TRAINING ##
    # legal_folder = 'cleaned_insc_data_1'
    # ## legal_folder is a folder that contains all legal documents ini text format
    #
    # nonlegal_folder = r'20_newsgroups\cleaned'
    # ## same as legal folder but containing non legal documents instead
    #
    # pvect = psl.PSlegalVectorizer(version=1)
    # print('Starting the training process...')
    # print()
    # pvect.efficient_fit(legal_folder, nonlegal_folder,gram='nnp')
    # print()
    # print('training the model completed...')
    # print()
    # with open('saved_model', 'wb') as wfp:
    #     pickle.dump(pvect,wfp,protocol=3)

    ## Uncomment the above if it's needed to train a new model on a new dataset.

    ## The default model provided is the model that was trained using
    ## 33.5K INSC cases and 20K non-legal documents.

    ## Using saved model to get scores for noun phrases ##
    ## Loading trained and saved model ##
    with open('saved_model','rb') as rfp:
        pvect = pickle.load(rfp)
    ## Fitting a document before extracting catchphrases
    with open('example_doc.txt') as rfp:
        text = rfp.read()
    nnps = npe.extract(text)
    pvect.fit_doc(nnps)
    ## Scoring the noun phrases from the document last fitted
    scored_nnps=[]
    for nnp in nnps:
        scored_nnps.append((pvect.get_score([nnp]),nnp,))
    print(sorted(scored_nnps,reverse=True))
