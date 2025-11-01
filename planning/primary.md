# Shavian Discord Bot

The scripts this document is referring to are the *primary* scripts, responsible for importing and otherwise handling communications with the addons.

## Planning 20251030-20251031

For ease of use, it is possible ot use a Python file to import all the addons rather than acting as a fully-fledge router. to integrate other languages, use a Python script to initialize the program and use the script in and of itself as a router. This permits functionality in other languages but with the added overhead of interlangauge communication. One (quite rudimentary) method is to use HTTP across localhost, however other, more efficient methods should be researched.

The methods to create an addon in Python can be broken down into 2 candidates, with the restriction that `main.py` should handle the primary communication because it holds the login tokens and the main instance itself. The first candidate involves `main.py` sending over the `ShavBot` instance, or its equivalent, to the addon. The second candidate involves the usage of predefined helper functions being sent to the addon, which arguably may be more complex and yield less returns in comparison to the first method, but should only be used as a fallback if it is impossible to implement the latter.