from justwatch import JustWatch

just_watch = JustWatch(country='US')

results = just_watch.search_for_item(query='the matrix')

print(results['items'][0]['title'])

# Print list of functions available in JustWatch class
# print(dir(just_watch))