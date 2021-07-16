# Create a guest list and print a message to invite each guest to dinner
guests = ["Ajitesh", "Mummy", "Papa", "Jatin", "Sharan"]
print("Dear " + guests[0] + ", Please come for dinner")
print("Dear " + guests[1] + ", Please come for dinner")
print("Dear " + guests[2] + ", Please come for dinner")
print("Dear " + guests[3] + ", Please come for dinner")
print("Dear " + guests[4] + ", Please come for dinner")

# One of the guests cannot come, so invite someone else in their place
# Also print the guest who cannot come.

cannot_come = guests.pop(2)
guests.insert(2, "Alka")
print("Dear " + guests[0] + ", Please come for dinner")
print("Dear " + guests[1] + ", Please come for dinner")
print("Dear " + guests[2] + ", Please come for dinner")
print("Dear " + guests[3] + ", Please come for dinner")
print("Dear " + guests[4] + ", Please come for dinner")
print(cannot_come + " cannot come for dinner")

# Got bigger dinner table, invite 3 more guests
guests.insert(0, "Somya")
guests.insert(4, "Shifali")
guests.append("Rahul")
print("Dear " + guests[0] + ", Please come for dinner")
print("Dear " + guests[1] + ", Please come for dinner")
print("Dear " + guests[2] + ", Please come for dinner")
print("Dear " + guests[3] + ", Please come for dinner")
print("Dear " + guests[4] + ", Please come for dinner")
print("Dear " + guests[5] + ", Please come for dinner")
print("Dear " + guests[6] + ", Please come for dinner")
print("Dear " + guests[7] + ", Please come for dinner")

# Only have table for 2, so invite only 2 guests and apologise to others
print("Dear " + guests.pop() + ", Only have space for 2 guests, Sorry you are not invited anymore")
print("Dear " + guests.pop() + ", Only have space for 2 guests, Sorry you are not invited anymore")
print("Dear " + guests.pop() + ", Only have space for 2 guests, Sorry you are not invited anymore")
print("Dear " + guests.pop() + ", Only have space for 2 guests, Sorry you are not invited anymore")
print("Dear " + guests.pop() + ", Only have space for 2 guests, Sorry you are not invited anymore")
print("Dear " + guests.pop() + ", Only have space for 2 guests, Sorry you are not invited anymore")
print("Dear " + guests[0] + ", Please come for dinner")
print("Dear " + guests[1] + ", Please come for dinner")

# Cancel dinner party
print("Dear " + guests[1] + ", Dinner party is cancelled")
del guests[1]
print("Dear " + guests[0] + ", Dinner party is cancelled")
del guests[0]

print(guests)

