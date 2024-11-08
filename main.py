import requests
import json
import sys
import os


class Colors:
    light_green = "\033[1;32m"
    light_blue = "\033[1;34m"
    light_red = "\033[1;31m"
    end = "\033[0m"


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Welcome to HunterAI, ask me anything!\n")
    get_response()


def get_response():
    lr = Colors.light_red
    lb = Colors.light_blue
    lg = Colors.light_green
    end = Colors.end
    prompt = "Prompt "
    exit_hint = "(q to exit): "
    full_prompt = lg + prompt + end + lr + exit_hint + end

    question = str(input(full_prompt))

    if question == "q":
        print(
            lb,
            "\nThank you for choosing HunterAI, your locally run AI solution "
            "for your every need. Bye!\n",
            end,
            )
        sys.exit(0)

    data = {
        "model": "mistral",
        "messages": [{"role": "user", "content": question}],
        "stream": False,
    }
    url = "http://localhost:8080/api/chat"

    response = requests.post(url, json=data)
    response_json = json.loads(response.text)

    ai_reply = response_json["message"]["content"]

    print("\n", ai_reply, "\n")
    get_response()


if __name__ == "__main__":
    main()
