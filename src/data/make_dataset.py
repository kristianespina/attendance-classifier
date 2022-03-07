# Script to generate data set
import random
import pandas as pd

ACTIONS = {
    "attendance.timein": "attendance.timein",
    "attendance.timeout": "attendance.timeout",
    "attendance.break": "attendance.break",
    "attendance.resume": "attendance.resume",
    "unknown": "unknown",
}

def generate_attendance_modifiers(modifier: str, time_in_modifier: str, time_out_modifier: str, break_modifier: str, resume_modifier: str):
    return {
        "modifier": modifier,
        ACTIONS["attendance.timein"]: time_in_modifier,
        ACTIONS["attendance.timeout"]: time_out_modifier,
        ACTIONS["attendance.break"]: break_modifier,
        ACTIONS["attendance.resume"]: resume_modifier,
        ACTIONS["unknown"]: ACTIONS["unknown"]
    }
action = ["attendance.timein", "attendance.timeout", "attendance.break", "attendance.resume", "attendance.timein", "attendance.timeout", "attendance.resume", "unknown"]
words = ["time in", "time out", "break", "back", "timein", "timeout", "resume", "time"]

modifiers = [
    # generate_attendance_modifiers("<modifier>", "<attendance.timein>", "<attendance.timeout>", "<attendance.break>", "<attendance.resume>"),
    generate_attendance_modifiers("", None, None, None, None),
    generate_attendance_modifiers("po", None, None, None, None),
    generate_attendance_modifiers("muna", None, ACTIONS["attendance.break"], None, None),
    generate_attendance_modifiers("po muna", None, ACTIONS["attendance.break"], None, None),
    generate_attendance_modifiers("muna po", None, ACTIONS["attendance.break"], None, None),
    generate_attendance_modifiers("for now", None, ACTIONS["attendance.break"], None, None),
    generate_attendance_modifiers("ulit", ACTIONS["attendance.resume"], None, None, None),
    generate_attendance_modifiers("again", ACTIONS["attendance.resume"], None, None, None),
]

data = []

for i, word in enumerate(words):
  for modifier in modifiers:
    data.append({
      "command": " ".join([word, modifier["modifier"]]) if modifier["modifier"] != "" else word,
      "result": modifier[action[i]] or action[i]
    })


synthetic_data = data# * 5

# Write csv
df = pd.DataFrame(synthetic_data)
df.to_csv("./dataset/attendance.csv", index=False)