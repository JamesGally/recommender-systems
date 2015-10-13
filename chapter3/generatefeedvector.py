import feedparser
import re

# Returns title and dictionary of word counts for an RSS feed
def getwordcounts(url):
  # Parse the feed
  d=feedparser.parse(url)
  wc={}

  for e in d.entries:
    if 'summary' in e:
      summary= e.summary
    else
      summary = d.description

    words=getwords(d.title + ' ' + summary)

    for word in words:
      wc.setdefault(word,0)
      wc[word]+=1

  return d.feed.title,wc


def getwords(html):
  # Remove all HTML tags
  txt=re.compile(r'<[^>]+>').sub('',html)

  # Split words by all non-alpha characters
  words=re.compile(r'[^A-Z^a-z]+').split(txt)

  # Convert to lowercase
  return [word.lower() for word in words if word != '']
