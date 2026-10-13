from leads_sample import leads

# get the budget from the lead (use 0 if it's missing)
# get the interest from the lead
# if budget >= 3000 and interest is "high" -> HOT
# elif budget >= 1000 or interest is "medium" -> WARM
# else -> COLD

def score_lead(Lead):
    budget = Lead.get("budget", 0)
    if budget is None:
            budget = 0
    interest = Lead.get("interest")

    if budget >= 3000 and interest == "high":
        return "HOT"
    elif budget >= 1000 or interest == "medium":
        return "WARM"
    else:
        return "COLD"

for lead in leads:
     print(lead["name"], score_lead(lead))