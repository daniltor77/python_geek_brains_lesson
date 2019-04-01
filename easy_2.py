def lucky_ticket(ticket_number):
	output=str(ticket_number)
	if int(output[0])+int(output[1])+int(output[2])==int(output[3])+int(output[4])+int(output[5]):
		return(True)
	else:
		return(False)

print(my_round(input("Enter: ")))
