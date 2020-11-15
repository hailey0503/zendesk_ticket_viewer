import unittest
from unittest.mock import patch

import Zendesk_Ticket_Viewer
import io
import logging
import sys
import difflib

class Test_ticket_view(unittest.TestCase):

	@patch('builtins.input', side_effect=['1', 'Q'])
	# @patch('sys.stdout', new_callable=io.StringIO)
	# def test_get_ticket(self, mock_output, mock_input):
	def test_get_25_tickets(self, mock_input):
		capturedOutput = io.StringIO()
		sys.stdout = capturedOutput
		#logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
		#root = logging.getLogger('LOG')
		
		with self.assertRaises(SystemExit) as cm:
			result = Zendesk_Ticket_Viewer.main()

		output = capturedOutput.getvalue()
		sys.stdout = sys.__stdout__

		# root.debug(f'mock_output {output}')

		with open("test1.txt","r") as f:
			read_data = f.read()
			#root.debug(f'file read {read_data}')
			#for i, s in enumerate(difflib.ndiff(output, read_data)):
			#	if s[0]==' ': continue
			#	elif s[0]=='-':
			#		root.debug(u'Delete "{}" from position {}'.format(s[-1],i))
			#	elif s[0]=='+':
			#		 root.debug(u'Add "{}" to position {}'.format(s[-1],i))                  
			self.assertEqual(output, read_data)


		# root.debug(f'exception {cm.exception}')
		# self.assertEqual(cm.exception.code, 0)

	@patch('builtins.input', side_effect=['1', 'N', 'Q'])
	# @patch('sys.stdout', new_callable=io.StringIO)
	# def test_get_ticket(self, mock_output, mock_input):
	def test_get_50_tickets(self, mock_input):
		capturedOutput = io.StringIO()
		sys.stdout = capturedOutput
		#logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
		#root = logging.getLogger('LOG')
		
		with self.assertRaises(SystemExit) as cm:
			result = Zendesk_Ticket_Viewer.main()

		output = capturedOutput.getvalue()
		sys.stdout = sys.__stdout__

		# root.debug(f'mock_output {output}')

		with open("test2.txt","r") as f:
			read_data = f.read()
			#root.debug(f'file read {read_data}')
			#for i, s in enumerate(difflib.ndiff(output, read_data)):
			#	if s[0]==' ': continue
			#	elif s[0]=='-':
			#		root.debug(u'Delete "{}" from position {}'.format(s[-1],i))
			#	elif s[0]=='+':
			#		 root.debug(u'Add "{}" to position {}'.format(s[-1],i))                  
			self.assertEqual(output, read_data)


		# root.debug(f'exception {cm.exception}')
		# self.assertEqual(cm.exception.code, 0)

	@patch('builtins.input', side_effect=['2', '14', 'Q'])
	# @patch('sys.stdout', new_callable=io.StringIO)
	# def test_get_ticket(self, mock_output, mock_input):
	def test_get_one_ticket(self, mock_input):
		capturedOutput = io.StringIO()
		sys.stdout = capturedOutput
		#logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
		#root = logging.getLogger('LOG')
		
		with self.assertRaises(SystemExit) as cm:
			result = Zendesk_Ticket_Viewer.main()

		output = capturedOutput.getvalue()
		sys.stdout = sys.__stdout__

		# root.debug(f'mock_output {output}')

		with open("test3.txt","r") as f:
			read_data = f.read()
			#root.debug(f'file read {read_data}')
			#for i, s in enumerate(difflib.ndiff(output, read_data)):
			#	if s[0]==' ': continue
			#	elif s[0]=='-':
			#		root.debug(u'Delete "{}" from position {}'.format(s[-1],i))
			#	elif s[0]=='+':
			#		 root.debug(u'Add "{}" to position {}'.format(s[-1],i))                  
			self.assertEqual(output, read_data)


		# root.debug(f'exception {cm.exception}')
		# self.assertEqual(cm.exception.code, 0)

	def tearDown(self):
		Zendesk_Ticket_Viewer.close()
		
if __name__ == "__main__":
	unittest.main()