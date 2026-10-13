calls = []

def add_call(customer_id, minutes):
    calls.append([customer_id, minutes])

def answer_call():
    if calls:
        print("Answered call:", calls.pop(0))
    else:
        print("No calls waiting")

def show_calls():
    print("Waiting calls:", calls)

add_call("C101", 4)
add_call("C102", 7)

show_calls()
answer_call()
show_calls()