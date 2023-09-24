# pandora-parser

pandora-parser is a program designed to automate some of the busy-work in the National Cyber League (NCL) 2023 Gymnasium challenge [Pandora](https://cyberskyline.com/module/64a82dca2e238f05f404230f/5879108318592673927d3dd6/587952a318592673927d49ed). The challenge consists of interpreting network traffic logs in order to reverse engineer a custom protocol named Pandora. To answer many of the questions, one would have to manually count out bytes to collect the required information. This program takes care of the counting for you, outputs the relevant data in an easily-readable format, and gives you the time to focus on learning concepts, not counting.

# Installation

Simply clone the github repository with:

```
  git clone https://github.com/massey-n/pandora-parser
```

# Usage

```
  python3 pandora-parser.py -i path-to-file
```

This program assumes that you have copied the raw TCP stream data as-is to a text file. It will not work properly if any lines have been altered or removed. It will take care of cleaning irrelevant data on its own.

# Note

This program does **not** solve the entire challenge for you, it only automates the repetitive parts. I woul only ever recommend automating something if you're confident in your understanding, so make sure you're comfortable with **why** this works before typing in commands. I would highly recommend watching the [official walkthrough](https://www.youtube.com/watch?v=70grYjg3fuE&t=50s) provided by NCL, it does an excellent job explaining how to solve this challenge. 

If you have any questions about why or how pandora-parser does something the way that it does, feel free to ask! I'm still learning myself, but I'm happy to answer any questions you might have. You'll get the fastest response to non-issue questions by messaging me on [Discord](https://discordapp.com/users/arkryder).

Lastly, this was designed for the Fall 2023 Pandora challenge. If NCL chooses to make a major update to the challenge there's a chance pandora-parser will no longer work. With a bit of modification (removing some checks and adjusting how it parses the data), it could be adapted, potentially even for a wider scope than *just* Pandora, but as-is I can only guarantee it works with this specific challenge from this specific year.

Thank you for using my tool, and have a lovely day!
