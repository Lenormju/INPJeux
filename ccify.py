#!/bin/python3

STEP = 35

dict_addresses = {}
if 'raw_input' not in globals():
	raw_input = input # Py2 and Py3-compatibility patch

total_raw_addresses = ''
while 1:
	# this loop addresses a limitation of shells to type up to 4096 characters on the same line, so it reads as much as it can, then ask it with a padding again and again until it is fully consumed
	raw_addresses = raw_input('>')
	total_raw_addresses += raw_addresses
	#print('input length: ' + str(len(raw_addresses)) +'|' + str(len(raw_addresses.encode('utf8'))) + ' characters')
	if len(raw_addresses.encode('utf8')) < 4095 : break
	print('input too long, please split it')
	print(raw_addresses[-20::] + '...')
	
print("\n\n\n")

raw_addresses_splitted = total_raw_addresses.split(',')

for raw_address in raw_addresses_splitted:
	if raw_address.find('<') == -1:
		dict_addresses[raw_address] = ''
	else:
		name = raw_address.split('<')[0]
		address = raw_address.split('<')[1].split('>')[0]
		if address not in dict_addresses:
			#print('new address: ' + address)
			dict_addresses[address] = name
		else:
			print('duplicate: ' + raw_address)


print('input: ' + str(len(dict_addresses)) + ' unique addresses')

contacts = list(dict_addresses.items())
contacts.sort(key=lambda c: c[1].lower().strip())
length = len(contacts)
for i in range(0, len(contacts), STEP) :
    print(','.join(c[1] + '<' + c[0] + '>' for c in contacts[i:min(i+STEP, length)]))

