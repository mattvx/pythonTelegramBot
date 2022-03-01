import feedparser, telegram, time

newsToken = "PASTE_BOT_TOKEN_HERE"

bot = telegram.Bot(token=newsToken)

while True:

    t1 = time.mktime(time.gmtime())

    time.sleep(120)

    NewsFeed = feedparser.parse("http://feeds.bbci.co.uk/news/world/europe/rss.xml")
    entry = NewsFeed.entries

    for i in entry:
        unparsedTime = i.published_parsed
        t2 = time.mktime(unparsedTime)
        # the following 4 lines are needed for logging only
        print(t1, "current epoch")
        print(t2,  "parsed news epoch")
        timeDiff = t2 - t1
        print(timeDiff)
            
        if t2 >= t1:
            print("\t\t\tNew News Detected!!!")
            newsTitle = i.title + "\n"
            newsBody = i.summary + "\n\n"
            news1 = newsTitle + "\n" + newsBody
            status = bot.send_message(chat_id="@CHAT_WHERE_TO_POST", text=news1, parse_mode=telegram.ParseMode.HTML)
        
    print("\n\n")
