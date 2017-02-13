python > output.txt  <<EOF

execfile('/home/jchohan/index.py')

a=index('/home/jchohan/collection/')

a.buildIndex()
a.print_dict()

a.and_query(['edward','years','the' ])

a.and_query(['their','indian'])

a.and_query(['everywhere','minnesota','but'])

a.print_doc_list()

EOF



The merge algorithm used in the code is a basic intersection method .
We have taken the query terms from the list and  firstly they are converted into lowercase.
Then we check if the word has a related document ID in the Terms dictionary.
In case there is a Document ID that is related to the query term , the that is added into
the result dictionary.
This result Dictionary will contain the Docid and we will be printing the filenames associated to the 
Docid
 