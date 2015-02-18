import subprocess
import unittest
import os

TWITTER_NLP = "../"
RESULT_FILENAME = TWITTER_NLP+"test/result_test.txt"
RESULT_EXPECTED_FILENAME =  TWITTER_NLP+"test/result_expected.txt"
def setUpModule():
	#if we don't have yet a to store reference result we create one
	if(os.path.isfile(RESULT_EXPECTED_FILENAME)):
		subprocess.call("cat "+TWITTER_NLP+"test.1k.txt | python "+TWITTER_NLP+"python/ner/extractEntities2.py > "+RESULT_EXPECTED_FILENAME, shell=True)


	status = subprocess.call("cat "+TWITTER_NLP+"test.1k.txt | python "+TWITTER_NLP+"python/ner/extractEntities2.py > "+RESULT_FILENAME, shell=True)
	assert status == 0

class BasicProcessingExampleTest(unittest.TestCase):
	def test_size_result_file_didnt_change(self):
		statInfoNewResult = os.stat(RESULT_FILENAME);
		statInfoExpectedResult = os.stat(RESULT_EXPECTED_FILENAME)
		self.assertEqual(int(statInfoExpectedResult.st_size/10),int(statInfoNewResult.st_size/10))

	def test_text_content_file_didnt_change(self):
		lines_result = tuple(open(RESULT_FILENAME, 'r'))
		lines_expected_result = tuple(open(RESULT_EXPECTED_FILENAME, 'r'))
		for i in range(0,len(lines_result)-1):
			self.assertEqual(lines_result[i],lines_expected_result[i])
	''' assure that at least we don't get twice time more slow'''
	def test_average_performance_didnt_change(self):
		lines_result = tuple(open(RESULT_FILENAME, 'r'))
		lines_expected_result = tuple(open(RESULT_EXPECTED_FILENAME, 'r'))
		#format performance line : Average time per tweet = 0.0104345694169s
		performance_result = lines_result[len(lines_result)-1].split("=")[1].split("s")[0]
		performance_expected_result = lines_expected_result[len(lines_expected_result)-1].split("=")[1].split("s")[0]
		value_performance_result = int(float(performance_result)*100)
		value_performance_expected_result = int(float(performance_expected_result)*100)
		self.assertTrue(value_performance_expected_result <= value_performance_result)
		


if __name__ == '__main__':
	unittest.main()

