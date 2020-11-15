import unittest
from unittest.mock import patch

import Zendesk_Ticket_Viewer
import io


class Test_ticket_view(unittest.TestCase):

    @patch('builtins.input', side_effect=['1', 'N'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_ticket(self, mock_output, mock_input):
        result = Zendesk_Ticket_Viewer.main()
        file = open("test1.txt","a") 
        
        self.assertEqual(mock_output.getvalue(), file.read())
        
if __name__ == "__main__":
    unittest.main()