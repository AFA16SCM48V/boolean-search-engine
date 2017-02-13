#Python 2.7.3
import re
import os
import collections
import time
import string
class index:
	def __init__(self,path):
		self.filenames = []
		self.doc_id_dict = {}  
		self.doc_id = 1
		self.ordered={}
		self.doc_id_dict = {}
		self.total = {}
		self.fileIndex = {}
		self.term = {}
		self.all_words = []
		self.temp_dict = {}
		self.path = path
		self.filenames = os.listdir(self.path)
		self.file_to_terms = {}
		self.new_doc_id={}
		self.ordered={}

	def buildIndex(self):
	#function to read documents from collection, tokenize and build the index with tokens
	#index should also contain positional information of the terms in the document --- term: [(ID1,[pos1,pos2,..]), (ID2, [pos1,pos2,]),.]
	#use unique document IDs
		print "Running build index function"
		start = time.time()
		for file in self.filenames:
			file_path = os.path.join(self.path,file)
			self.pattern = re.compile('[\W_]+')
			self.file_to_terms[file] = open(file_path, 'r').read().lower();
			self.file_to_terms[file] = self.pattern.sub(' ',self.file_to_terms[file])
			re.sub(r'[\W_]+','', self.file_to_terms[file])
			self.file_to_terms[file] = self.file_to_terms[file].split()
		for filename in self.file_to_terms.keys():
			self.all_words = self.all_words + self.file_to_terms[filename]

		for i in self.file_to_terms.keys():
			self.temp_dict[filename] = list(set(self.file_to_terms[filename]))
			self.file_to_terms[filename]=[]
		for i in self.temp_dict.keys():
			for w in self.temp_dict[i]:
				if w.isalpha():
					self.file_to_terms[filename].append(w)

		temp= list(set(self.all_words))
		self.all_words=[]

		for i in temp:
			if i.isalpha():
				self.all_words.append(i)

		for filename in self.file_to_terms.keys():
			self.doc_id_dict[filename] = self.doc_id
			self.new_doc_id[self.doc_id] = filename
			self.doc_id += 1
		for word in self.all_words:
			self.term[word] = {}
			self.words_in_file ={}
			for filename in self.file_to_terms.keys():
				self.doc_id = self.doc_id_dict[filename]
				for index, word1 in enumerate(self.file_to_terms[filename]):
					if word == word1:
						self.words_in_file[self.doc_id] = []
						self.words_in_file[self.doc_id].append(index)
			self.term[word] = self.words_in_file 
		end = time.time()
		print 'Retrieved in '+str(end-start) +' sec.'
		
	def and_query(self, query_terms):
	#function for identifying relevant docs using the index
		print "Running and query function"
		print "Results for the query: ",query_terms
		start = time.time()
		result = self.new_doc_id.keys()
		for i in query_terms:
			i = i.lower()
			if not i in self.term:
				print "The words are not present in the given files"
				return -1
			if self.term[i].keys() != []:
				result = list(set(self.term[i].keys()).intersection(result))
		for i in result:
			print self.new_doc_id[i]
		end = time.time()
		print "Total docs retrieved: ", len(result)
		print 'Retrieved in '+str(end-start) +' sec.'

	def print_dict(self):
	#function to print the terms and posting list in the index
		print "Running the print_dict function"
		start = time.time()
		print self.term
		end = time.time()
		print 'Retrieved in '+str(end-start) +' sec.'

	def print_doc_list(self):
	# function to print the documents and their document id
		print "Running the doc_list function"
		start = time.time()
		for id in self.doc_id_dict.keys():
			print "Doc ID:", id, "==>", self.doc_id_dict[id]
		end = time.time()
		print 'Retrieved in '+str(end-start) +' sec.'
