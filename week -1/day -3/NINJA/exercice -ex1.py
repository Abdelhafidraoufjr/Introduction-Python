class Phone:
    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.call_history = []
        self.messages = []

    def call(self, other_phone):
        log = f"{self.phone_number} a appelé {other_phone.phone_number}"
        print(log)
        self.call_history.append(log)

    def show_call_history(self):
        print("📞 Historique des appels :")
        for call in self.call_history:
            print("-", call)

    def send_message(self, other_phone, content):
        message = {
            "to": other_phone.phone_number,
            "from": self.phone_number,
            "content": content
        }
        self.messages.append(message)
        other_phone.messages.append(message)

    def show_outgoing_messages(self):
        print("📤 Messages envoyés :")
        for msg in self.messages:
            if msg["from"] == self.phone_number:
                print(f"À {msg['to']} : {msg['content']}")

    def show_incoming_messages(self):
        print("📥 Messages reçus :")
        for msg in self.messages:
            if msg["to"] == self.phone_number:
                print(f"De {msg['from']} : {msg['content']}")

    def show_messages_from(self, number):
        print(f"📨 Messages reçus de {number} :")
        for msg in self.messages:
            if msg["to"] == self.phone_number and msg["from"] == number:
                print(f"- {msg['content']}")
if __name__ == "__main__":
    phone1 = Phone("0600000001")
    phone2 = Phone("0600000002")

    phone1.call(phone2)
    phone1.show_call_history()

    phone1.send_message(phone2, "Salut, comment ça va ?")
    phone2.send_message(phone1, "Très bien, merci !")

    phone1.show_outgoing_messages()
    phone1.show_incoming_messages()

    phone1.show_messages_from("0600000002")
