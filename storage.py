import json

def save_event(data):
    try:
        with open("events.json","r") as f:
            events = json.load(f)
    except:
        events = []

    events.append(data)

    with open("events.json","w") as f:
        json.dump(events,f)

