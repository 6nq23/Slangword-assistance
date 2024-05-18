import random
import schedule
from plyer import notification
import time

# Define a dictionary of slang words with examples and meanings
slang_words = {
  "GOAT": ("Greatest Of All Time", "Used to describe someone who is the absolute best at something."),
  "SUS": ("Suspicious", "Used to express doubt or suspicion about someone or something."),
  "ICYWW": ("In Case You Were Wondering", "Used to introduce information that someone might not be aware of."),
  "Yeet": ("To throw something with force", "Can also be used as an expression of excitement or approval."),
  "Lowkey": ("Actually, secretly, or mildly", "Used to emphasize that something is true but not necessarily well-known."),
  "Bestie": ("Best friend", "A close and trusted friend."),
  "Extra": ("Very or excessively", "Used to describe something that is over-the-top."),
  "Woke": ("Aware of and actively engaged in social justice and related issues.", "Can also be used more generally to mean 'intelligent' or 'with it'."),
  "Finna": ("Fixing to" or "about to", "A contraction used in some dialects of English."),
  "Bae": ("Before anyone else" or "baby", "A term of endearment for a romantic partner."),
  "Lit": ("Excellent or exciting", "Used to describe something that is cool or awesome."),
  "Cringe": ("To feel embarrassed or awkward on behalf of someone else", "Can also be used as a noun to describe something embarrassing."),
  "Flex": ("To boast or show off", "Often used to show off material possessions or achievements."),
  "Fire": ("Excellent or impressive", "Similar to 'lit'"),
  "Shade": ("Subtle but pointed criticism", "Often delivered in a seemingly complimentary way."),
  "Savage": ("Brutal or mean", "Can also be used to describe something that is very cool or impressive."),
  "Bruh": ("Dude" or "man", "A term used to address someone, often in a casual or surprised way."),
  "SMH": ("Shaking My Head", "Used to express disapproval, disappointment, or disbelief."),
  "FOMO": ("Fear Of Missing Out", "Anxiety that you're missing out on something exciting that other people are doing."),
  "TBT": ("Throwback Thursday", "A social media trend of posting old photos on Thursdays."),
  "Bussin": ("Very good or delicious", "Often used to describe food."),
  "Cheugy": ("Out of date or trying too hard to be trendy", "Can also be used to describe people, fashion, or other things."),
  "Drip": ("Fashion sense or style", "Often used to describe someone who is dressed very well."),
  "Wokefish": ("Someone who pretends to be very aware of social justice issues but does not actually care.",  "Often used as a critical term."),
  "Cap": ("A lie or something that is not true", "Often used to tell someone to stop exaggerating."),
  "Gas": ("Disrespectful or rude behavior", "Can also be used to describe something that is very funny."),
  "Low-key": ("Actually, secretly, or mildly", "Used to emphasize that something is true but not necessarily well-known."),
  "Finna": ("Fixing to" or "about to", "A contraction used in some dialects of English."),
  "Bae": ("Before anyone else" or "baby", "A term of endearment for a romantic partner."),
  "Thirsty": ("Desperately wanting attention or validation", "Often used to describe someone who is being too clingy or attention-seeking on social media."),
  "Fam": ("Friends or family", "A close-knit group of people."),
  "Mood": ("Current emotional state", "Often used to express how you're feeling."),
  "Yeet": ("To throw something with force", "Can also be used as an expression of excitement or approval."),
  "Big brain": ("Very intelligent or quick-witted", "Often used sarcastically."),
  "Periodt": ("For emphasis, similar to 'period'", "Used to add emphasis to a statement and suggest that it is undeniable."),
}


def show_slang_popup():
  # Pick a random slang word
  random_word = random.choice(list(slang_words.keys()))
  definition, example = slang_words[random_word]
  
  # Create the notification message
  message = f"{random_word}: {definition}\nExample: {example}"
  
  # Display the notification
  notification.notify(
      title="Slang of the Hour!",
      message=message,
      app_name="Slang Learner",
      timeout=10  # Notification stays for 10 seconds
  )

# Schedule the function to run every hour
schedule.every().hour.do(show_slang_popup)

while True:
  # Keep the script running in the background
  schedule.run_pending()
  time.sleep(1)  # Check for scheduled tasks every second
