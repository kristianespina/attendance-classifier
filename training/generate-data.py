import random
import pandas as pd

action = ["TIMEIN", "TIMEOUT", "BREAK", "RESUME", "TIMEIN", "TIMEOUT"]
words = ["time in", "time out", "break", "back", "timein", "timeout"]
suffixes = ["", " po", " muna", " ulit", " po muna", " po muna ulit", " po ulit",  " muna ulit"]

def generate_typo(command):
  # convert the message to a list of characters
  message = list(command["command"])

  typo_prob = 0.15 # percent (out of 1.0) of characters to become typos

  # the number of characters that will be typos
  n_chars_to_flip = round(len(message) * typo_prob)
  # is a letter capitalized?
  capitalization = [False] * len(message)
  # make all characters lowercase & record uppercase
  for i in range(len(message)):
      capitalization[i] = message[i].isupper()
      message[i] = message[i].lower()

  # list of characters that will be flipped
  pos_to_flip = []
  for i in range(n_chars_to_flip):
      pos_to_flip.append(random.randint(0, len(message) - 1))

  # dictionary... for each letter list of letters
  # nearby on the keyboard
  nearbykeys = {
      'a': ['q','w','s','x','z'],
      'b': ['v','g','h','n'],
      'c': ['x','d','f','v'],
      'd': ['s','e','r','f','c','x'],
      'e': ['w','s','d','r'],
      'f': ['d','r','t','g','v','c'],
      'g': ['f','t','y','h','b','v'],
      'h': ['g','y','u','j','n','b'],
      'i': ['u','j','k','o'],
      'j': ['h','u','i','k','n','m'],
      'k': ['j','i','o','l','m'],
      'l': ['k','o','p'],
      'm': ['n','j','k','l'],
      'n': ['b','h','j','m'],
      'o': ['i','k','l','p'],
      'p': ['o','l'],
      'q': ['w','a','s'],
      'r': ['e','d','f','t'],
      's': ['w','e','d','x','z','a'],
      't': ['r','f','g','y'],
      'u': ['y','h','j','i'],
      'v': ['c','f','g','v','b'],
      'w': ['q','a','s','e'],
      'x': ['z','s','d','c'],
      'y': ['t','g','h','u'],
      'z': ['a','s','x'],
      ' ': ['c','v','b','n','m']
  }

  # insert typos
  for pos in pos_to_flip:
      # try-except in case of special characters
      try:
          typo_arrays = nearbykeys[message[pos]]
          message[pos] = random.choice(typo_arrays)
      except:
          break

  # reinsert capitalization
  for i in range(len(message)):
      if (capitalization[i]):
          message[i] = message[i].upper()

  # recombine the message into a string
  message = ''.join(message)

  return {"command": message, "result": command["result"]}

data = []

for i, word in enumerate(words):
  for suffix in suffixes:
    data.append({
      "command": f"{word}{suffix}",
      "result": action[i]
    })

noisy_data_1 = list(map(generate_typo, data.copy()))
noisy_data_2 = list(map(generate_typo, data.copy()))

synthetic_data = data + data + noisy_data_1 + noisy_data_2

# Write csv
df = pd.DataFrame(synthetic_data)
df.to_csv("../dataset/attendance.csv", index=False)