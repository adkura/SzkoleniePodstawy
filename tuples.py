marketing = ["loyality program", "client promotion", "market research"]

marketing.append("public relations")
print(marketing[3])

marketing.insert(2, "investor relations")


emailMarketing = marketing.copy()
emailMarketing.sort()

internalEmails = ["internal communication"]

emailMarketing.extend(internalEmails)

newTuple = tuple(emailMarketing)

print(marketing)
print(emailMarketing)
print(internalEmails)
print(newTuple)
