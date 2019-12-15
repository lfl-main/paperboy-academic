# paperboy-academic
This code searches RSS feeds for keywords and authors, then pushes the matching articles in a readable format to your chosen slack channel. It should be straightforward to push articles to another medium such as email or basecamp.

For this code to work, you need to populate some text files and create the app in your slack workspace to obtain a slack bot token.

You can create the app in your slack workspace by going to https://api.slack.com/apps. Be sure to enable the slack bot user. After installing the app to your workspace, copy the bot user token from the OAuth & Permissions tab. Next, add the token to your system environment variables using the following command:
Windows cmd line:
setx SLACK_TOKEN xoxb-xxxxxxxxxx-xxxxxxxxxxx-xxxxxxxxxxxxx
MacOS terminal:
echo 'export SLACK_TOKEN=xoxb-xxxxxxxxxx-xxxxxxxxxxx-xxxxxxxxxxxxx' >> ~/.zshenv

The text files are populated as follows:

authors.txt specifies authors you want to search for. Each line should have one author. Be sure to include any variations such as middle initial in a new line. For Example, authors.txt may contain the following lines:
James Farmer
James T Farmer
J Farmer
JT Farmer
Darian Hartsell
Darian M Hartsell

The period after initials should not be included, as the search program will remove periods. i.e., an article with author "J.T. Farmer" will be matched with the line "JT Farmer" from authors.txt. I highly recommend searching Google scholar for any authors you want to track to see if they often use a middle initial.

feeds.txt specifies the journals you want to pull from. Any URL that leads to an RSS feed can be used. Obtain the URLs for your desired RSS feeds from a google search. Each URL should be on a new line. As an example, feeds.txt may contain the following lines
https://arxiv.org/rss/quant-ph
http://www.nature.com/nphys/current_issue/rss
http://feeds.aps.org/rss/recent/prl.xml

keywords.txt specifies the keywords, each one on a new line. The matches must be exact, though capitalization does not matter. i.e., qubit and QuBiT are equivalent, but quantum limited and quantum-limited are not. Example lines for keywords.txt
quantum heat engine
photon pump
correlated noise
fault-tolerant
tunable-coupling
quantum channel
fluxonium
transmon
nanobridge
andreev

Finally, channel.txt should contain one line: the channel ID for the slack channel you wish to post to. This is not the name of the channel, but rather a 9 digit alphanumeric identifier. If you open slack in a web browser, this id is visible in the URL. Alternatively, just google how to find your slack channel ID.
AS AN IMPORTANT NOTE: don't blow up your colleagues slack with repeated messages while youre getting the keywords and urls sorted out. You can just call editor or journalist independently, or create a private slack channel for testing.
