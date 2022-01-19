import requests
from time import sleep


recentsPlays_webhook = "https://discord.com/api/webhooks/"
top_webhook = "https://discord.com/api/webhooks/"

scoresaber_id = "76561198272483934"



response = requests.get(f"https://scoresaber.com/api/player/{scoresaber_id}/scores?limit=1&sort=recent&withMetadata=true").json()
last_recent = (response["playerScores"][0]["score"]["timeSet"])

response2 = requests.get(f"https://scoresaber.com/api/player/{scoresaber_id}/basic").json()
last_ppcount = (response2["pp"])


print(f"PP - {last_ppcount}PP")
print(f"Last Play - {last_recent}")



def post_topPlays():
    plays = requests.get(f"https://scoresaber.com/api/player/{scoresaber_id}/scores?limit=8&sort=top&withMetadata=true").json()

    weight_1 = round(((plays["playerScores"][0]["score"]["pp"]) * (plays["playerScores"][0]["score"]["weight"])), 3)
    perc_1 = round((plays["playerScores"][0]["score"]["baseScore"]) / (plays["playerScores"][0]["leaderboard"]["maxScore"])*100, 2)

    weight_2 = round(((plays["playerScores"][1]["score"]["pp"]) * (plays["playerScores"][1]["score"]["weight"])), 3)
    perc_2 = round((plays["playerScores"][1]["score"]["baseScore"]) / (plays["playerScores"][1]["leaderboard"]["maxScore"])*100, 2)

    weight_3 = round(((plays["playerScores"][2]["score"]["pp"]) * (plays["playerScores"][2]["score"]["weight"])), 3)
    perc_3 = round((plays["playerScores"][2]["score"]["baseScore"]) / (plays["playerScores"][2]["leaderboard"]["maxScore"])*100, 2)

    weight_4 = round(((plays["playerScores"][3]["score"]["pp"]) * (plays["playerScores"][3]["score"]["weight"])), 3)
    perc_4 = round((plays["playerScores"][3]["score"]["baseScore"]) / (plays["playerScores"][3]["leaderboard"]["maxScore"])*100, 2)

    weight_5 = round(((plays["playerScores"][4]["score"]["pp"]) * (plays["playerScores"][4]["score"]["weight"])), 3)
    perc_5 = round((plays["playerScores"][4]["score"]["baseScore"]) / (plays["playerScores"][4]["leaderboard"]["maxScore"])*100, 2)

    weight_6 = round(((plays["playerScores"][5]["score"]["pp"]) * (plays["playerScores"][5]["score"]["weight"])), 3)
    perc_6 = round((plays["playerScores"][5]["score"]["baseScore"]) / (plays["playerScores"][5]["leaderboard"]["maxScore"])*100, 2)

    weight_7 = round(((plays["playerScores"][6]["score"]["pp"]) * (plays["playerScores"][6]["score"]["weight"])), 3)
    perc_7 = round((plays["playerScores"][6]["score"]["baseScore"]) / (plays["playerScores"][6]["leaderboard"]["maxScore"])*100, 2)

    weight_8 = round(((plays["playerScores"][7]["score"]["pp"]) * (plays["playerScores"][7]["score"]["weight"])), 3)
    perc_8 = round((plays["playerScores"][7]["score"]["baseScore"]) / (plays["playerScores"][7]["leaderboard"]["maxScore"])*100, 2)

    randomWaifu_R = requests.get("https://api.waifu.im/sfw/waifu/").json()
    randomWaifu = (randomWaifu_R["images"][0]["url"])

    headers = {
        "embeds": [
            {
                "title": "TOP PLAYS",
                "color": 0x00f7ff,
                "description": "",
                "timestamp": "",
                "url": "",
                "author": {
                    "name": "",
                    "url": ""
                },
                "image": {"url": randomWaifu},
                "thumbnail": {},
                "footer": {},
                "fields": [
                    {
                    "name": (plays["playerScores"][0]["leaderboard"]["songName"]) + " | " + str((plays["playerScores"][0]["leaderboard"]["stars"])) + "☆ - " + str(perc_1) + "%",
                    "value": str((plays["playerScores"][0]["score"]["pp"])) + "pp" + " (" + str(weight_1) +"pp)"
                    },
                    {
                    "name": (plays["playerScores"][1]["leaderboard"]["songName"]) + " | " + str((plays["playerScores"][1]["leaderboard"]["stars"])) + "☆ - " + str(perc_2) + "%",
                    "value": str((plays["playerScores"][1]["score"]["pp"])) + "pp" + " (" + str(weight_2) +"pp)"
                    },
                    {
                    "name": (plays["playerScores"][2]["leaderboard"]["songName"]) + " | " + str((plays["playerScores"][2]["leaderboard"]["stars"])) + "☆ - " + str(perc_3) + "%",
                    "value": str((plays["playerScores"][2]["score"]["pp"])) + "pp" + " (" + str(weight_3) +"pp)"
                    },
                                        {
                    "name": (plays["playerScores"][3]["leaderboard"]["songName"]) + " | " + str((plays["playerScores"][3]["leaderboard"]["stars"])) + "☆ - " + str(perc_4) + "%",
                    "value": str((plays["playerScores"][3]["score"]["pp"])) + "pp" + " (" + str(weight_4) +"pp)"
                    },
                                        {
                    "name": (plays["playerScores"][4]["leaderboard"]["songName"]) + " | " + str((plays["playerScores"][4]["leaderboard"]["stars"])) + "☆ - " + str(perc_5) + "%",
                    "value": str((plays["playerScores"][4]["score"]["pp"])) + "pp" + " (" + str(weight_5) +"pp)"
                    },
                                        {
                    "name": (plays["playerScores"][5]["leaderboard"]["songName"]) + " | " + str((plays["playerScores"][5]["leaderboard"]["stars"])) + "☆ - " + str(perc_6) + "%",
                    "value": str((plays["playerScores"][5]["score"]["pp"])) + "pp" + " (" + str(weight_6) +"pp)"
                    },
                                        {
                    "name": (plays["playerScores"][6]["leaderboard"]["songName"]) + " | " + str((plays["playerScores"][6]["leaderboard"]["stars"])) + "☆ - " + str(perc_7) + "%",
                    "value": str((plays["playerScores"][6]["score"]["pp"])) + "pp" + " (" + str(weight_7) +"pp)"
                    },
                                        {
                    "name": (plays["playerScores"][7]["leaderboard"]["songName"]) + " | " + str((plays["playerScores"][7]["leaderboard"]["stars"])) + "☆ - " + str(perc_8) + "%",
                    "value": str((plays["playerScores"][7]["score"]["pp"])) + "pp" + " (" + str(weight_8) +"pp)"
                    }
                ]
                }
            ],
    }

    hook_response = requests.post(top_webhook, json=headers)
    print(hook_response.text)



while True:
    r = requests.get(f"https://scoresaber.com/api/player/{scoresaber_id}/scores?limit=1&sort=recent&withMetadata=true").json()

    if (r["playerScores"][0]["score"]["timeSet"]) != last_recent:
        last_recent = (r["playerScores"][0]["score"]["timeSet"])
        
        if (r["playerScores"][0]["leaderboard"]["ranked"]) == False:
            if (r["playerScores"][0]["score"]["missedNotes"]) == 0:
                headers = {
                    "username": "",
                    "avatar_url": "",
                    "content": "",
                    "embeds": [
                        {
                        "title": (r["playerScores"][0]["leaderboard"]["songName"]),
                        "color": 8382010,
                        "description": "good job uwu (unranked)",
                        "timestamp": (r["playerScores"][0]["score"]["timeSet"]),
                        "url": "",
                        "author": {
                            "name": "",
                            "url": ""
                        },
                        "image": {},
                        "thumbnail": {"url": (r["playerScores"][0]["leaderboard"]["coverImage"])},
                        "footer": {},
                        "fields": [
                            {
                            "name": "Rank",
                            "value": "#" + str((r["playerScores"][0]["score"]["rank"]))
                            },
                            {
                            "name": "Missed Notes",
                            "value": "FC ✅"
                            },
                            {
                            "name": "Score",
                            "value": (r["playerScores"][0]["score"]["baseScore"])
                            }
                        ]
                        }
                    ],
                }
            else:
                headers = {
                    "username": "",
                    "avatar_url": "",
                    "content": "",
                    "embeds": [
                        {
                        "title": (r["playerScores"][0]["leaderboard"]["songName"]),
                        "color": 8382010,
                        "description": "good job uwu (unranked)",
                        "timestamp": (r["playerScores"][0]["score"]["timeSet"]),
                        "url": "",
                        "author": {
                            "name": "",
                            "url": ""
                        },
                        "image": {},
                        "thumbnail": {"url": "https://cdn.scoresaber.com/covers/85F2204FE701F2E88AAF29331009446687A9BCB6.png"},
                        "footer": {},
                        "fields": [
                            {
                            "name": "Rank",
                            "value": "#" + str((r["playerScores"][0]["score"]["rank"]))
                            },
                            {
                            "name": "Missed Notes",
                            "value": str((r["playerScores"][0]["score"]["missedNotes"])) + "❌"
                            },
                            {
                            "name": "Score",
                            "value": (r["playerScores"][0]["score"]["baseScore"])
                            }
                        ]
                        }
                    ],
                }

            hook_response = requests.post(recentsPlays_webhook, json=headers)
            print(hook_response.text)
        else:
            acc = round(((r["playerScores"][0]["score"]["baseScore"]) / (r["playerScores"][0]["leaderboard"]["maxScore"]))*100, 2)
            weighted = round(((r["playerScores"][0]["score"]["pp"]) * (r["playerScores"][0]["score"]["weight"])), 3)

            accinfo_response = requests.get(f"https://scoresaber.com/api/player/{scoresaber_id}/basic").json()
            added_pp = round((accinfo_response["pp"]) - last_ppcount, 3)


            if (r["playerScores"][0]["score"]["missedNotes"]) == 0:
                headers = {
                    "username": "",
                    "avatar_url": "",
                    "content": "",
                    "embeds": [
                        {
                        "title": (r["playerScores"][0]["leaderboard"]["songName"]) + " " + str((r["playerScores"][0]["leaderboard"]["stars"])) + "☆" + " - " + str(acc) + "%",
                        "color": 8382010,
                        "description": "good job uwu (ranked)",
                        "timestamp": (r["playerScores"][0]["score"]["timeSet"]),
                        "url": "",
                        "author": {
                            "name": "",
                            "url": ""
                        },
                        "image": {},
                        "thumbnail": {"url": (r["playerScores"][0]["leaderboard"]["coverImage"])},
                        "footer": {},
                        "fields": [
                            {
                            "name": "Rank",
                            "value": "#" + str((r["playerScores"][0]["score"]["rank"]))
                            },
                            {
                            "name": "Missed Notes",
                            "value": "FC ✅"
                            },
                            {
                            "name": "PP",
                            "value": str(round((r["playerScores"][0]["score"]["pp"]), 3)) + " pp🍆"
                            },
                            {
                            "name": "WEIGHTED PP",
                            "value": "+" + str(weighted) + " pp" + " (+" + str(added_pp) + ")"
                            }
                        ]
                        }
                    ],
                }
            else:
                headers = {
                    "username": "",
                    "avatar_url": "",
                    "content": "",
                    "embeds": [
                        {
                        "title": (r["playerScores"][0]["leaderboard"]["songName"]) + " " + str((r["playerScores"][0]["leaderboard"]["stars"])) + "☆" + " - " + str(acc) + "%",
                        "color": 8382010,
                        "description": "good job uwu (ranked)",
                        "timestamp": (r["playerScores"][0]["score"]["timeSet"]),
                        "url": "",
                        "author": {
                            "name": "",
                            "url": ""
                        },
                        "image": {},
                        "thumbnail": {"url": (r["playerScores"][0]["leaderboard"]["coverImage"])},
                        "footer": {},
                        "fields": [
                            {
                            "name": "Rank",
                            "value": "#" + str((r["playerScores"][0]["score"]["rank"]))
                            },
                            {
                            "name": "Missed Notes",
                            "value": str((r["playerScores"][0]["score"]["missedNotes"])) + "❌"
                            },
                            {
                            "name": "PP",
                            "value": str(round((r["playerScores"][0]["score"]["pp"]), 3)) + " pp🍆"
                            },
                            {
                            "name": "WEIGHTED PP",
                            "value": "+" + str(weighted) + " pp" + " (+" + str(added_pp) + ")"
                            }
                        ]
                        }
                    ],
                }

            hook_response = requests.post(recentsPlays_webhook, json=headers)
            print(hook_response.text)

        post_topPlays()
    else:
        print("no new scores sadge")
        sleep(1)
