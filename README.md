# Python Projects Collection

Hey there! 👋 Welcome to my collection of Python projects. I built these while learning and experimenting with Python, and I'm excited to share them with you. Some are simple utilities I use daily, others are just fun projects I created to explore different concepts.

## What's Inside?

This repo has 8 different projects - ranging from basic tools to more complex applications. Whether you're learning Python or just looking for some useful scripts, there's something here for you:

| Project | What it does | Level |
|---------|-------------|------------|
| 🧮 Calculator | Your basic calculator - does math stuff | Beginner |
| 💰 Millionaire | Quiz game - test your knowledge! | Intermediate |
| 📰 News-API | Get the latest news delivered to your terminal | Intermediate |
| 🤖 AI Chatbot | Talk to an AI - pretty cool! | Advanced |
| 📝 Bulk Rename | Rename a bunch of files at once (life saver!) | Beginner |
| 💧 Drink Water Reminder | Stay hydrated with regular reminders | Beginner |
| 📄 PDF Merger | Combine multiple PDFs into one | Intermediate |
| 📱 QR Code Generator | Turn text/URLs into QR codes | Beginner |

## Getting Started

Alright, let's get you up and running!

### What You'll Need

- Python 3.7+ (if you don't have it, grab it from [python.org](https://python.org))
- pip (usually comes with Python)
- That's pretty much it!

### Let's Do This

1. **Grab the code:**
```bash
git clone https://github.com/Harshits9/Python-Projects.git
cd Python-Projects
```

2. **Pick a project and jump in:**
```bash
cd Calculator  # or whatever project you want to try
```

3. **Install what you need:**
```bash
pip install -r requirements.txt  # if there's a requirements file
```

4. **Run it:**
```bash
python main.py  # check the project folder for the actual filename
```

## The Projects

Let me walk you through each one:

### 🧮 Calculator
Just a straightforward calculator. Nothing fancy, but it gets the job done for basic math.

What it can do:
- Add, subtract, multiply, divide
- Handles errors so you don't crash it
- Simple and easy to use

```bash
cd Calculator
python calculator.py
```

---

### 💰 Millionaire
Ever watched "Who Wants to Be a Millionaire?" This is basically that, but in your terminal. Answer questions, climb the ladder, have fun!

What's cool about it:
- Multiple choice questions
- Questions get harder as you go
- Keeps track of your score

```bash
cd Millionaire
python millionaire.py
```

---

### 📰 News-API
Pulls the latest news headlines straight from the web. Stay updated without opening a browser!

Features:
- Real-time news (as real-time as APIs can be)
- Filter by categories
- Works with News API

You'll need:
- A free API key from [News API](https://newsapi.org/)

```bash
cd News-API
# Drop your API key in the config
python news.py
```

---

### 🤖 AI Chatbot
A chatbot that actually talks back! It's pretty smart and can hold a conversation (well, sort of).

Cool stuff:
- Understands natural language
- Remembers context
- You can tweak its personality

```bash
cd ai-chatbot
python chatbot.py
```

---

### 📝 Bulk Rename
Ever needed to rename like 50 files at once? Yeah, this saves you from doing it manually. You're welcome.

Why it's useful:
- Rename multiple files in one go
- Use patterns for naming
- See what changes before you commit

```bash
cd bulk-rename
python bulk_rename.py
```

---

### 💧 Drink Water Reminder
I built this because I kept forgetting to drink water while coding. Now it bugs me every hour (in a good way).

What it does:
- Sends you reminders to drink water
- You can adjust the timing
- Tracks your hydration (kinda)

```bash
cd drink-water-reminder
python reminder.py
```

---

### 📄 PDF Merger
Got a bunch of PDFs you need to combine? This does it for you without any sketchy online converters.

Features:
- Merge as many PDFs as you want
- Keeps everything formatted nicely
- Arrange pages however you like

Needs:
- PyPDF2 library

```bash
cd pdfmerger
python merger.py
```

---

### 📱 QR Code Generator
Makes QR codes from whatever you throw at it - text, URLs, you name it.

What you can do:
- Generate QR codes instantly
- Customize size and quality
- Save them as images

Needs:
- qrcode library

```bash
cd qr-code-genrator
python qr_generator.py
```

## Setting Things Up

Most of these projects need some extra packages. Here's what you might need:

```bash
pip install requests
pip install PyPDF2
pip install qrcode
pip install pillow
pip install plyer  # for those desktop notifications
```

Or if there's a requirements.txt, just run:

```bash
pip install -r requirements.txt
```

Easy peasy!

## Want to Contribute?

Found a bug? Have an idea to make something better? Cool! Here's how you can help out:

1. Fork this repo
2. Create your branch (`git checkout -b cool-new-feature`)
3. Make your changes
4. Commit them (`git commit -am 'Added something awesome'`)
5. Push it up (`git push origin cool-new-feature`)
6. Open a Pull Request

I'm open to all kinds of contributions - bug fixes, new features, documentation improvements, whatever!

## What's Next?

Things I'm planning to add (when I get time):

- Tests for everything (I know, I know...)
- GUI versions for some of these
- Better docs
- Maybe some error logging
- More customization options

## Hit Me Up

Questions? Suggestions? Just want to say hi?

- GitHub: [@Harshits9](https://github.com/Harshits9)
- Check out the repo: [Python-Projects](https://github.com/Harshits9/Python-Projects)

## Like What You See?

If these projects helped you or you learned something, drop a ⭐ on the repo! It really makes my day.

---

Thanks for checking this out! Happy coding! 🐍✨
