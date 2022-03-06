# Document Collection Processing
Python version: 3.8.8

External packages: bs4, nltk(used only for the Porter/Snowball stemmers)

In information retrieval (IR) experiments, a document is usually the basic unit to be indexed and
retrieved, such as a webpage or a pure text file. To simply the processing of documents, we
usually compile small document files into large collection files. Each single collection file
contains the contents of many small documents. trectext and trecweb are two popular document collection formats. The codes are written to process the documents stored in these two types of collections

Objective:

To preprocess documents from 2 collection files - "trectext" and "trecweb". This includes reading documents from the collection files.
Normalize documents text. This includes tokenizing words, removing "stop words" , stemming and normalizing tokens.
NOTES ON CLASSES:
Task 1: Reading Documents from Collection Files
-PreProcessData.DocumentCollection is a general interface for sequentially reading
documents from collection files
-PreProcessData.TrectextCollection is the class for trectext format
-PreProcessData.TrecwebCollection is the class for trecweb format

Task 2: Normalize Document Texts
-PreProcessData.TextTokenizer is a class for sequentially reading words from a sequence of
characters

PreProcessData.TextNormalizer is the class that transforms each word to its lowercase
version, and conduct stemming on each word.
PreProcessData.StopwordsRemover is the class that can recognize whether a word is a stop
word or not.
