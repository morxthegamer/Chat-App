import time

CHAT_FILE = "../chat.yaml"

def main():
  with open(CHAT_FILE, "r") as f:
    while (True):
      time.sleep(1)
      print(f.read())

if __name__ == "__main__":
  main()