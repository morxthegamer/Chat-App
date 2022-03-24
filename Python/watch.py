import time

CHAT_FILE = "../chat.yaml"

def main():
  while (True):
    with open(CHAT_FILE, "r") as f:
      FILE = f.read()
      time.sleep(2)
      print(FILE)

if __name__ == "__main__":
  main()