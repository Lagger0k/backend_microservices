import requests


def main():
    while True:
        text = input("Ведите текст сообщения... ")
        payload = {"text": text}
        requests.get("http://localhost/queue_reverse_text", params=payload)


if __name__ == "__main__":
    main()
