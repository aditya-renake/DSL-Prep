events = []

events.append("Login")
events.append("Payment")
events.append("Logout")
print("Events:", events)

# Process the first event
print("Processed:", events.pop(0))
print("Remaining:", events)

# Cancel an event
events.remove("Logout")
print("After cancel:", events)