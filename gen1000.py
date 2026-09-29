# -*- coding: utf-8 -*-
import itertools, random

themes = [
("Todo","нормально"),("Budget Tracker","нормально"),("Notes App","легко"),("Chat","сложно"),
("URL Shortener","легко"),("Weather Dashboard","легко"),("Quiz App","легко"),("Recipe Book","легко"),
("Fitness Tracker","нормально"),("Event Booking","сложно"),("E-commerce Store","сложно"),("Blog Platform","нормально"),
("Job Board","сложно"),("Social Network","очень сложно"),("Photo Gallery","легко"),("Music Player","нормально"),
("Video Streaming","очень сложно"),("Podcast App","нормально"),("Book Library","нормально"),("Inventory System","нормально"),
("CRM","сложно"),("CMS","сложно"),("Landing Page","очень легко"),("Portfolio","очень легко"),("Forum","сложно"),
("Wiki","нормально"),("Poll/Survey","легко"),("Calendar Scheduler","нормально"),("Helpdesk Tickets","нормально"),
("Restaurant Ordering","сложно"),("Hotel Booking","сложно"),("Flight Booking","сложно"),("Car Rental","сложно"),
("Real Estate Listings","сложно"),("Dating App","сложно"),("Learning LMS","сложно"),("Flashcards","легко"),
("Habit Tracker","легко"),("Password Manager","нормально"),("File Sharing","нормально")
]

stacks = [
("на чистом HTML/CSS/JS","очень легко"),
("на React","легко"),
("на Vue 3","легко"),
("на Svelte","легко"),
("на Angular","нормально"),
("на Next.js","нормально"),
("на Nuxt","нормально"),
("на Python + Tkinter","легко"),
("на Python + Flask","легко"),
("на Python + FastAPI","нормально"),
("на Django","нормально"),
("на Node.js + Express","легко"),
("на Go + Gin","нормально"),
("на Rust + Actix","сложно"),
("на Java Spring Boot","нормально"),
("на C# ASP.NET Core","нормально"),
("на PHP + Laravel","нормально"),
("Ruby on Rails","нормально"),
("mobile Flutter","нормально"),
("mobile React Native","нормально"),
("native Android (Kotlin)","нормально"),
("native iOS (SwiftUI)","нормально"),
("desktop Electron","нормально"),
("desktop Qt/C++","сложно"),
("CLI на Bash","очень легко"),
("CLI на PowerShell","легко"),
("в Telegram Bot API","легко"),
("в Discord.js","легко"),
("с GraphQL","нормально"),
("с WebSocket real-time","сложно"),
("с PostgreSQL","нормально"),
("с MongoDB","легко"),
("с Redis очередями","нормально"),
("с Docker Compose","нормально"),
("с Kubernetes деплоем","сложно"),
("с CI/CD GitHub Actions","нормально"),
("с OAuth2/JWT авторизацией","нормально"),
("с платёжными интеграциями (Stripe demo)","сложно"),
("с ML-фичами (recommendation)","сложно"),
("с offline-first PWA","нормально"),
("с тестами Playwright","нормально"),
("на Serverless (Cloud Functions)","сложно"),
("с микросервисной архитектурой","очень сложно"),
("с event sourcing и CQRS","очень сложно"),
("с распределённой consensus-логикой","невозможно")
]

base_diff_map = {t[0]: t[1] for t in themes}
order = ["очень легко","легко","нормально","сложно","очень сложно","невозможно"]
idx = {d:i for i,d in enumerate(order)}

def bump(b, s):
    # combine base theme difficulty and stack complexity heuristically
    bi = idx[b]; si = {"очень легко":0,"легко":1,"нормально":2,"сложно":3,"очень сложно":4,"невозможно":5}[s]
    val = max(bi, si)
    if bi>=2 and si>=2: val = min(5, val+ (1 if (bi==si==3) else 0))
    return order[min(val,5)]

combos=[]
for th,_ in themes:
    for st,_ in stacks:
        combos.append((th,st))
random.seed(1)
random.shuffle(combos)

lines=[]
seen=set()
for th, st in combos:
    name = f"{th} {st}"
    if name in seen: continue
    seen.add(name)
    d = bump(base_diff_map[th], dict(stacks)[st])
    lines.append((name,d))
    if len(lines)==1000: break

with open("/workspace/projects_1000.txt","w",encoding="utf-8") as f:
    for i,(n,d) in enumerate(lines,1):
        f.write(f"{i}. {n} — {d}\n")
print(len(lines))
from collections import Counter
print(Counter(d for _,d in lines))
