from typing import List
from collections import defaultdict

import pprint
import re

class Component:
	def __init__(self, first, second):
		self.values = [first, second]

	def __repr__(self):
		output_string = ""

		for value in self.values:
			output_string += ("%s " % value)

		output_string += "\n"

		return output_string

	def addToComponent(self, value):
		self.values.append(value)

	def getValues(self, word):
		return self.values

class Graph:
	def __init__(self, synonyms):
		self.components = defaultdict(Component)
		self.initialize(synonyms)

	def __repr__(self):
		output_string = ""

		for key, values in self.components.items():
			output_string += ("Key: %s\n" % key)
			output_string += ("Values: %s\n" % values)

		return output_string

	def findSynonyms(self, word):
		return self.components[word]

	def initialize(self, synonyms):
		for synonymn_pair in synonyms:
			first, second = synonymn_pair

			# if neither of the synonyms we are currently processing
			# are already in a component, make a new component that
			# holds both
			# otherwise, add the missing synonym to the existing component
			if (not first in self.components and
				not second in self.components):
				# one of the 
				new_component = Component(first, second)
				self.components[first] = new_component
				self.components[second] = new_component
			else:
				first_exists = first in self.components 
				existing_component = self.components[first] if first_exists else self.components[second]
				existing_component.addToComponent(second if first_exists else first)

				if (first_exists):
					self.components[second] = existing_component
				else:
					self.components[first] = existing_component

class Solution:
	def helper(self, graph, remaining_words):

		"""
		for index, word in enumerate(wordsInSentence):
			# recursively continue
			all_sentences.append(
		return all_sentences

		"""

		if (len(remaining_words) == 0):
			return []

		if (len(remaining_words) == 1):
			word = remaining_words.pop(0)
			if word in graph.components:
				return graph.components[word].getValues(word)
			else:
				return [word]
			
		# process the first word in the list
		# try each synonym of the first word
		# recursively process the rest of the list
		word = remaining_words.pop(0)
		prefixes = [word]

		if (word in graph.components):
			prefixes.extend([prefix for prefix in graph.components[word].getValues(word) if prefix != word])

		print("Prefixes: %s" % (prefixes))

		outputs = []

		for prefix in prefixes:
			# we are adding a list (to our list)
			# now we have a list of lists!!!
			print("Inputs to recursion: %s" % (remaining_words))
			recursive_result = self.helper(graph, remaining_words)

			print("Recursive result: %s" % (recursive_result))

			for remaining_list in recursive_result:
				print("Output so far %s" % (outputs))
				print("Word we are processing: %s" % (word))
				print("Prefix: %s" % prefix)
				print("Remaining list: %s" % remaining_list)
				print("Trying to add: %s" % (prefix + " " + remaining_list))
				print("\n")
				outputs.append(prefix + " " + remaining_list)

		return outputs
		
	def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
		# 1) make a graph of all "synonyms" of a word
		# 2) for each word in the input list
		# 2.1) find all synonyms
		# 2.2) using each synonym as the current word, generate the sentences that can be formed with the remaining list

		# 1) make a graph of all "synonyms" of a word
		graph = Graph(synonyms)

		# 2) for each word in the input list
		# 2.1) find all synonyms
		# 2.2) using each synonym as the current word, generate the sentences that can be formed with the remaining list
		wordsInSentence = re.split('[^a-zA-z]', text)
		
		return self.helper(graph, wordsInSentence)

# testcase 1
input_synonyms_1 = [["happy","joy"],["sad","sorrow"],["joy","cheerful"]]
input_text_1 = "I am happy today but was sad yesterday"
expected_output_1 = ["I am cheerful today but was sad yesterday","I am cheerful today but was sorrow yesterday","I am happy today but was sad yesterday","I am happy today but was sorrow yesterday","I am joy today but was sad yesterday","I am joy today but was sorrow yesterday"]

# testcase 2
input_synonyms_2 = [["happy","joy"],["cheerful","glad"]]
input_text_2 = "I am happy today but was sad yesterday"
expected_output_2 = ["I am happy today but was sad yesterday","I am joy today but was sad yesterday"]

# testcase 3 
input_synonyms_3 = [["happy","joy"]]
input_text_3 = "Be happy"
expected_output_3 = ["Be happy", "Be joy"]

# run the tests
debug = True

tests = [
	# (input_synonyms_1, input_text_1, expected_output_1),
	 (input_synonyms_2, input_text_2, expected_output_2),
	# (input_synonyms_3, input_text_3, expected_output_3),
]

for test_value in tests:
	input_synonym_value, input_text, expected_output = test_value

	print("Inputs\n")
	print("Synonyms: %s" % (input_synonym_value))
	print("Text: %s" % (input_text))
	print("\n")

	actual_output = Solution().generateSentences(input_synonym_value, input_text)
	print("Expected output: %s" % (expected_output))

	print("Actual output: %s" % (actual_output))
	print("\n" * 2)

	if debug:
		print("We are in DEBUG mode!!\n")
	else:
		assert(expected_output) == actual_output
