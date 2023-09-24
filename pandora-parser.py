'''
Author: Noah Massey
File: pandora-parser.py
Description: A program to aid in parsing the network logs from NCL Fall 2023 Gymnasium's Pandora challenge.
		If you do not understand why this program is doing something, please watch NCL's walkthrough or message me,
		as the point of the challenge is to learn, not to blindly run scripts. This is just to make busywork easier.
'''

import argparse

def main(userFile):
	asciiArt() #Spit out ascii art that makes me look like a better programmer than I actually am
	try:
		with open(userFile) as log:
			lines = log.read().splitlines()	#Reads, cleans up, and assigns each line to an array
			if len(lines) < 10 and lines[0] == "00000005": #Ensures that this is the correct data
				lenReq, dataReq = requestParse(lines)
				lenResp, dataResp = responseParse(lines)
			else:
				raise ValueError
		print("\n\nRequest Lengths:\n")
		for request in lenReq.items():
			print(f'{request[0]}: {request[1]}\n')
		print("\n\nRequest Data:\n")
		for request in dataReq.items():
			print(f'{request[0]}: {request[1]}\n')
		print(f'\n\nResponse Length:\n\n{lenResp} bytes per response\n')
		print("\n\nResponse Data:\n")
		for response in dataResp.items():
			print(f'{response[0]}: {response[1]}\n')
	except FileNotFoundError:
		print(f'\nError: Your file {userFile} was not found.')
	except ValueError:
		print(f'\nError: Your file does not contain raw TCP data from Pandora!\n\nPlease make sure you have the correct data and try again.')
	return None

def requestParse(lines):
	'''
	Get the lengths and data from each client request

	:param lines: The list of lines from the TCP stream file
	:return lenReq, dataReq
	:rtype: dict
	'''

	requestInfo = lines[3]  #The lentgth and data that the client is sending
	counter = 1  #Keep track of the number of encrypt requests
	startIndex = 0  #Initialize to the start index of the len bytes
	endIndex = 8  #Initialize to the end index of the len bytes
	lenReq = {}
	dataReq = {}

	while True:
		if endIndex > len(requestInfo):
			break
		else:
			length = int(requestInfo[startIndex:endIndex],16)  #Get length bytes and convert from hex
			startIndex = endIndex  #Move to the start of the next chunk of request data
			endIndex += length * 2 + 4  #Multiply length by 2 (as data is in bytes) and add 4 (for the check bytes)
			data = requestInfo[startIndex:endIndex]  #Get the request data
			dictString = f'Request #{counter}'  #Make the keys look nice
			lenReq[dictString] = length  #Add the length to the relevant dict
			dataReq[dictString] = data  #Add the data to the relevant dict
			counter += 1  #Keep track of which request this is
			startIndex = endIndex  #Move to the start of the next len chunk
			endIndex += 8  #Move to the end of the next len chunk

	return lenReq, dataReq

def responseParse(lines):
	'''
	Get the lengths and data from each server response

	:param lines: The list of lines from the TCP stream file
	:return: lenResp, dataResp
	:rtype: dict
	'''

	lenResp = int(lines[2], 16) // 5  #The length of the server's responses (translated from hex and divided by the num of requests
	responseInfo = lines[4] + lines[5]  #The data that the server is sending
	counter = 1  #Keep track of the nubmer of responses
	startIndex = 0
	endIndex = lenResp * 2  #Initialize to the end of the first response
	dataResp = {}

	while True:
		if endIndex > len(responseInfo):
			break
		else:
			data = responseInfo[startIndex:endIndex]
			startIndex += lenResp * 2  #Move to the next response
			endIndex += lenResp * 2
			dictString = f'Response #{counter}'  #Make the keys look nice
			dataResp[dictString] = data  #Add data to the dict
			counter += 1  #Keep track of which response this is

	return lenResp, dataResp

def asciiArt():
	print("                        _")
	print("                       | |")
	print("  _ __   __ _ _ __   __| | ___  _ __ __ _   _ __  _   _ ")
	print(" | '_ \ / _` | '_ \ / _` |/ _ \| '__/ _` | | '_ \| | | |")
	print(" | |_) | (_| | | | | (_| | (_) | | | (_| |_| |_) | |_| |")
	print(" | .__/ \__,_|_| |_|\__,_|\___/|_|  \__,_(_) .__/ \__, |")
	print(" | |                                       | |     __/ |")
	print(" |_|        Written by: Noah Massey        |_|    |___/ ")


'''Setup Argument Parser to allow user to input file and have a help menu'''
parser = argparse.ArgumentParser(description='This program sorts through raw TCP traffic data for NCL\'s Pandora challenge')
parser.add_argument('-i', '--input', help='input the path to your raw TCP traffic file')
args = parser.parse_args()

if args.input:
        userFile = args.input
        main(userFile)
else:
        print('No input data file specified! Try again using \"python3 pandora-parser.py -i file.txt\"')
