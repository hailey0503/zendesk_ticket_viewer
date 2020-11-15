import requests
import json

zendesk = 'https://berkeley0503.zendesk.com'
	
def userinput(user_input):
	if user_input == '1':
		url = zendesk + '/api/v2/tickets.json?page[size]=25' 
		meta, links = get_ticket_list(url)
		hasmore = meta['has_more']
		
		while hasmore:
			next = links['next']
			prev = links['prev']
			next_page_input = input("\n\n\n" + 
	   								#"* Press ticket id to view a ticket\n" +
	   								"* Press N for next 25 tickets\n" +
						   			"* Press P for previous 25 tickets\n" +
									"* Press V to view a ticket\n" + 
									"* Press R to return to menu\n" +
									"* Press Q to exit\n" +
									"\n\nYour Input: ")
			if next_page_input.upper() == 'N':
				meta, links = get_ticket_list(next)
				hasmore = meta['has_more']
			elif next_page_input.upper() == 'P':
				meta, links = get_ticket_list(prev)
				hasmore = meta['has_more']
			elif next_page_input.upper() == 'V':
				ticket_id = input("* Enter ticket id: ")
				get_ticket(ticket_id)
			elif next_page_input.upper() == 'R':
				break
			elif next_page_input.upper() =='Q':
				exit() 
			else:
				print("Please enter correct input ")
		
	elif user_input == '2':
		ticket_id = input('Ticket ID: ')
		get_ticket(ticket_id)
	elif user_input.upper() == 'Q':
		exit()
	else:
		print("Please enter correct input ")


			
def credential():
	with open('credential.json') as f:
		data = json.load(f)
		credentials = data["id"], data["password"]
		session = requests.Session()
		session.auth = credentials
		return session



def get_ticket(ticket_id):
	session = credential()
	url = zendesk + '/api/v2/tickets/' + ticket_id + '.json'

	response = session.get(url)
	if response.status_code != 200:
		print('Error with status code {}'.format(response.status_code))
		exit()
		
	data = response.json()
	response.close()
	ticket = data['ticket']

	header = '{:5}{:50}{:15}{:23}{:23}{:10}'.format('ID', 'Subject', 'Requester', 'Requested on', 'Updated on', 'Group ID')
	print(header)
	
	ticket_id = ticket['id']
	subject = ticket['subject']
	requester_id = ticket['requester_id']
	created_at = ticket['created_at']
	updated_at = ticket['updated_at']
	group_id = ticket['group_id']
	element = '{:5}{:50}{:15}{:23}{:23}{:10}'.format(str(ticket_id), subject, str(requester_id), created_at, updated_at, str(group_id))
	print(element)	


		
def get_ticket_list(url):
	session = credential()
	response = session.get(url)
	if response.status_code != 200:
		print('Error with status code {}'.format(response.status_code))
		exit()
	data = response.json()
	response.close()
	tickets = data['tickets']
	meta = data['meta']
	links = data['links']

	hasmore = meta['has_more']
	next = links['next']
	prev = links['prev']

	header = '{:5}{:50}{:15}{:23}{:23}{:10}'.format('ID', 'Subject', 'Requester', 'Requested on', 'Updated on', 'Group ID')
	print(header)
	for ticket in tickets:
		ticket_id = ticket['id']
		subject = ticket['subject']
		requester_id = ticket['requester_id']
		created_at = ticket['created_at']
		updated_at = ticket['updated_at']
		group_id = ticket['group_id']
		element = '{:5}{:50}{:15}{:23}{:23}{:10}'.format(str(ticket_id), subject, str(requester_id), created_at, updated_at, str(group_id))
		print(element)
	
	return (meta, links)	

def main():
	while True:
		print("\n**** Welcome to the ticket viewer ****\n\n\n\n")
		print("* Press 1 to view all tickets\n\n")
		print("* Press 2 to view a ticket\n\n")
		print("* Press Q to exit\n\n\n\n\n")
		user_input = input('Your Input: ')
		userinput(user_input)

if __name__ == '__main__':
    main()


		



