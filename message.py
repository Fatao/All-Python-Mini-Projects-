

receiver = input("Enter receiver phone number: ")
sender = input("Enter sender phone number: ")
message = input("Enter message to send: ")


start_time = time.time()
end_time = start_time + 3600  # 1 hour in seconds

while time.time() < end_time:
    message = client.messages.create(
        body=message,
        from_=sender,
        to=receiver
    )
    time.sleep(3)
