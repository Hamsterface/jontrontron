Jenny (XJ-9)

Commands start with "Jenny, " or "Hey Jenny, "
Alternatively, you can call her XJ-9, which will give the following responses (per user):
	First time: "I'll do it this time, but next time call me Jenny.", followed by the normal response
	Second time: "I told you to call me Jenny."; does not execute response.
	After second time randomly selects from:
		"I'm not listening."
		"My *name* is Jenny."
		"Why do you keep calling me that? You're not my mother."
		Will add more later.
	Resets after an hour of not being called XJ-9 (by that user).
	Maybe have different responses for me, being as I *am* her creator.

"say hi to the world."
	first: "Hello."
	second: "Alright, fine. \"Hello, world!\""

Markov
"what do you think about (.*)?"
if the last two words form a known key:
	"I think that "+markov chain starting from the given words+"."
if the last two words do not form a key:
	"I don't know anything about "+given words+"."
if less than two words are given:
	"I don't know what you mean."

Code execution
"run this for me: `(.*)`"
	runs it as python
	"Alright, I ran that, and it came back `"+return value+"`. Can I go now?"
	
"(?:find|get) .* a picture of (.*)\."
	"Hopefully this is what you want. I didn't really check."
	first google image result for search terms
	
"(?:find|get) .* a video of (.*)\."
	"I mean, it was a pretty quick search, but here's what I found."
	first youtube result
	
If a user does not have permission to use a command
	"You can't just tell me what to do. Go ask someone else."