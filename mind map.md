🗺️ Wordlist Generator — Build Map

Stage 1 — Collect input ✅ (you’ve basically done this)

Ask questions, store answers in a dict
Fix: dict key → single string value

Stage 2 — Extract base words

Pull just the values from your dict
Filter out empty/blank answers
Result: a clean flat list like ['sarah', 'connor', '1995', ...]

Stage 3 — Normalize the words

Should they all be lowercase first? (makes mutations predictable)
Strip extra whitespace from input (.strip())
Think: do you want to keep an original-case version too?

Stage 4 — Write ONE mutation function

Pick the simplest mutation first: e.g. “add common suffixes” (123, !, 01)
Function signature idea: add_suffixes(word) -> list of words
Test it alone on one word before anything else

Stage 5 — Write more mutation functions (one at a time)

Capitalize first letter
Leetspeak substitution (a→4, e→3, etc.)
Combine two base words together (e.g. name + pet)
Each one: input a word (or two), output a list of variants

Stage 6 — Combine all mutations into one pipeline

Loop over every base word
Run it through each mutation function
Collect everything into one big list

Stage 7 — Clean the final list

Remove duplicates (think: set())
Maybe filter by length (real passwords are usually 6+ chars)

Stage 8 — Save to file

Write the list to wordlist.txt, one word per line

Stage 9 — Polish (portfolio-level touches)

Add a README explaining purpose + ethics disclaimer
Add command-line args (optional, e.g. using argparse) instead of only input()
Add a word count printed to the user at the end

Stage 10 — Stretch goals (optional)

Use itertools.product() to generate combos more elegantly
Let user choose which mutations to apply
Add a “strength estimate” — how many words were generated