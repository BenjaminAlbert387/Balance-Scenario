# Character definition
define y = Character("You")
define a = Character("Person A")

# HUD display
default boundary_score = 0
default communication_score = 0
default responsibility_score = 0

# Displays scores in the top of the screen
screen confidence_ui():
    vbox:
        xalign 0.98
        yalign 0.02
        spacing 5

        frame:
            text "Boundary Score (Recognises personal capacity, and avoids overcommitting): [boundary_score]"

        frame:
            text "Communication Score (Informs others early, and explains constraints constructively): [communication_score]"

        frame:
            text "Team Responsibility Score (Manages the overall impact on the charity): [responsibility_score]"

label start:

    show screen confidence_ui

    play sound "voice_lines/1.mp3"
    "Welcome! To continue, please press left click on your mouse / tap your mousepad while your cursor is on the game."

    play sound "voice_lines/2.mp3"
    "Great! This is a simulated scenario based on Balancing Commitments and Wellbeing."

    play sound "voice_lines/3.mp3"
    "Please note that this is a fictional video game, and there are no real names used."

    play sound "voice_lines/4.mp3"
    "During the game, you will have the option to 'choose your response' through key points."

    play sound "voice_lines/5.mp3"
    "There are no right or wrong answers, and many options will increase one score while lowering others. That is life!"

    play sound "voice_lines/6.mp3"
    "Once you are ready, press left click one more time and the simulated scenario will start!"

    # Scenario Start

    play sound "voice_lines/7.mp3"
    "Balancing Commitments and Wellbeing: Scenario Start"

    play sound "voice_lines/8.mp3"
    "Monday, 7:42 PM."

    play sound "voice_lines/9.mp3"
    "Your laptop is open. Three browser tabs are displaying deadlines, your phone is vibrating, and a mug of tea has been sitting untouched long enough to qualify as a historical artefact."

    play sound "voice_lines/10.mp3"
    y "{i}Right. Let's assess the situation rationally.{/i}"

    play sound "voice_lines/11.mp3"
    y "{i}I have a university assignment due Wednesday. I have a work deadline on Thursday. And I promised the charity that I would review a document before Friday's meeting.{/i}"

    play sound "voice_lines/12.mp3"
    y "{i}Three perfectly reasonable commitments. Individually manageable. Collectively, apparently a government experiment designed to discover how much stress one human being can absorb.{/i}"

    play sound "voice_lines/13.mp3"
    "Your phone vibrates again. A message from Person A appears."

    play sound "voice_lines/14.mp3"
    a "Hey! Have you got a minute?"

    play sound "voice_lines/15.mp3"
    y "{i}That question has never once meant one minute.{/i}"

    play sound "voice_lines/16.mp3"
    y "Hey. What's up?"

    play sound "voice_lines/17.mp3"
    a "Sorry to message so late. I know everyone's busy, but I've run into a problem with the charity's funding proposal."

    play sound "voice_lines/18.mp3"
    a "The draft needs reviewing before the board meeting on Friday. I thought I had most of it covered, but some of the figures don't match the latest budget."

    play sound "voice_lines/19.mp3"
    y "How much needs doing?"

    play sound "voice_lines/20.mp3"
    a "The figures need checking, the impact section needs updating, and we need someone to review the final version. I was hoping you could help me get it sorted by Wednesday evening."

    play sound "voice_lines/21.mp3"
    y "{i}Wednesday evening.{/i}"

    play sound "voice_lines/22.mp3"
    y "{i}The same Wednesday evening that my university assignment is due. The assignment I have been working on for three weeks. The assignment that currently consists of an introduction, two paragraphs and a deeply optimistic conclusion.{/i}"

    play sound "voice_lines/23.mp3"
    y "I might be able to help. How much work do you think it is?"

    play sound "voice_lines/24.mp3"
    a "A few hours, probably. Maybe four if the figures are a mess."

    play sound "voice_lines/25.mp3"
    y "{i}Four hours. That's almost a whole evening, assuming time has stopped existing for food, sleep and basic hygiene.{/i}"

    play sound "voice_lines/26.mp3"
    a "I wouldn't ask if it wasn't important. The funding could make a real difference to the people we support."

    play sound "voice_lines/27.mp3"
    y "{i}And that's the difficult part. This isn't meaningless admin. The proposal matters. People are relying on us to make sensible decisions and use the charity's resources properly.{/i}"

    play sound "voice_lines/28.mp3"
    y "{i}But my other commitments matter too. I do not want to become a person who survives exclusively on caffeine and calendar notifications.{/i}"

    play sound "voice_lines/29.mp3"
    "You pause before replying."

    play sound "voice_lines/30.mp3"
    menu:
            "How do you respond to Person A?"

            "Agree to do it all, even though the deadline is unrealistic.":
                $ boundary_score += -2
                $ communication_score += -1
                $ responsibility_score += 2

                play sound "voice_lines/31.mp3"
                y "Sure. Send everything over. I'll get it done by Wednesday."

                play sound "voice_lines/32.mp3"
                a "Really? Thank you. That takes a massive weight off my shoulders."

                play sound "voice_lines/33.mp3"
                y "{i}They sound relieved. That should feel good. So why does my stomach feel like it has just received an eviction notice?{/i}"

                play sound "voice_lines/34.mp3"
                y "{i}I've agreed without checking what I can realistically deliver. I might pull it off, but I've made a promise before understanding the full cost.{/i}"

            "Explain your deadline and ask what the highest-priority tasks are.":
                $ boundary_score += 2
                $ communication_score += 2
                $ responsibility_score += 1

                play sound "voice_lines/35.mp3"
                y "I want to help, but I've got an assignment due Wednesday evening. I can't promise to complete four hours of work by then."

                play sound "voice_lines/36.mp3"
                y "Could we identify which parts of the proposal are most urgent? I might be able to review a specific section or help find another person to share the work."

                play sound "voice_lines/37.mp3"
                a "That's fair. I hadn't realised your deadline was that close."

                play sound "voice_lines/38.mp3"
                y "{i}It's uncomfortable to say no to part of a request. But explaining what I can do is more useful than making a promise I might break.{/i}"

            "Tell Person A that the proposal is their problem to solve.":
                $ boundary_score += 1
                $ communication_score += -1
                $ responsibility_score += -2

                play sound "voice_lines/39.mp3"
                y "I'm busy with my own deadlines. You'll need to find someone else."

                play sound "voice_lines/40.mp3"
                a "Oh. Right. Okay."

                play sound "voice_lines/41.mp3"
                y "{i}My time is limited, and I'm allowed to protect it. But I haven't asked what support is available, or whether there's a smaller task I could reasonably take on.{/i}"

                play sound "voice_lines/42.mp3"
                y "{i}A boundary doesn't have to be a slammed door. Although, admittedly, a slammed door would be quite satisfying right now.{/i}"

    play sound "voice_lines/43.mp3"
    "Tuesday, 12:35 PM."

    play sound "voice_lines/44.mp3"
    "You are between commitments when Person A calls."

    play sound "voice_lines/45.mp3"
    a "Have you had a chance to look at the proposal?"

    play sound "voice_lines/46.mp3"
    y "Not properly yet. What's happened?"

    play sound "voice_lines/47.mp3"
    a "I checked the budget again this morning. The figures are more complicated than I thought, and the person who usually handles them is unavailable until Thursday."

    play sound "voice_lines/48.mp3"
    a "I'm worried we'll have to present something incomplete at the meeting."

    play sound "voice_lines/49.mp3"
    y "{i}There it is. The problem has grown while I've been trying to keep everything else moving.{/i}"

    play sound "voice_lines/50.mp3"
    y "{i}I could ignore the call and protect my afternoon. I could agree to take over the whole proposal. Or I could help establish what is actually possible before anyone makes another promise.{/i}"

    play sound "voice_lines/51.mp3"
    y "Have you spoken to the others about the missing figures?"

    play sound "voice_lines/52.mp3"
    a "Not yet. I didn't want to worry everyone before I had a solution."

    play sound "voice_lines/53.mp3"
    y "I can see why you'd want to fix it first. But if the deadline is at risk, the others need to know early enough to help."

    play sound "voice_lines/54.mp3"
    a "I know. I just don't want people thinking I've failed to prepare."

    play sound "voice_lines/55.mp3"
    y "{i}That sounds familiar. I sometimes treat asking for help as evidence that I should have been able to do everything myself.{/i}"

    play sound "voice_lines/56.mp3"
    y "{i}It is a particularly inefficient habit. Unfortunately, humans are not renowned for being efficient about their insecurities.{/i}"

    play sound "voice_lines/57.mp3"
    a "What do you think we should do?"

    play sound "voice_lines/58.mp3"
    menu:
            "How do you handle the growing workload?"

            "Take ownership of the entire proposal so Person A doesn't feel pressured.":
                $ boundary_score += -1
                $ communication_score += 0
                $ responsibility_score += 2

                play sound "voice_lines/59.mp3"
                y "I'll take over the proposal and try to get it finished. We can discuss the details later."

                play sound "voice_lines/60.mp3"
                a "Are you sure? I really appreciate it."

                play sound "voice_lines/61.mp3"
                y "{i}I'm trying to help, but I may have replaced one person's problem with two people's problems. If I cannot finish the work, the charity still has a problem, and now my other commitments are at risk too.{/i}"

            "Discuss what can realistically be completed and notify the relevant staff.":
                $ boundary_score += 1
                $ communication_score += 1
                $ responsibility_score += 1

                play sound "voice_lines/62.mp3"
                y "Let's list what actually needs to be finished before Friday and what can wait. We should also let the others know that the budget figures are unresolved."

                play sound "voice_lines/63.mp3"
                y "That gives us a chance to divide the work properly instead of hoping someone can absorb it all."

                play sound "voice_lines/64.mp3"
                a "I was worried they'd think I'd handled it badly."

                play sound "voice_lines/65.mp3"
                y "They might have questions, but giving them time to help is better than telling them at the last minute."

                play sound "voice_lines/66.mp3"
                a "Okay. I'll send a message to the group and explain what's missing."

                play sound "voice_lines/67.mp3"
                y "{i}This feels more constructive. I'm not abandoning the task, but I'm not pretending I can solve everything alone either.{/i}"

            "Tell Person A to stop worrying and just work harder.":
                $ boundary_score += 0
                $ communication_score += -1
                $ responsibility_score += 0

                play sound "voice_lines/68.mp3"
                y "We've all got deadlines. We just need to push through and get it done."

                play sound "voice_lines/69.mp3"
                a "Right. I'll keep working on it."

                play sound "voice_lines/70.mp3"
                y "{i}I've offered a slogan instead of a solution. Very efficient if the goal is to make someone feel worse without changing anything.{/i}"

    play sound "voice_lines/71.mp3"
    "Tuesday, 8:10 PM."

    play sound "voice_lines/72.mp3"
    "You return to your laptop. Your assignment is still unfinished, and a work email has arrived asking for revisions to a report due Thursday."

    play sound "voice_lines/73.mp3"
    y "{i}I have approximately two hours before I need to stop working if I want a reasonable amount of sleep.{/i}"

    play sound "voice_lines/74.mp3"
    y "{i}I could spend those hours on the assignment, the charity proposal, or my work report. There is no option where I magically become three people.{/i}"

    play sound "voice_lines/75.mp3"
    "Another message appears from Person A."

    play sound "voice_lines/76.mp3"
    a "I've updated the group. One person can check the figures tomorrow, and another can review the impact section. Could you look over the final document on Thursday evening?"

    play sound "voice_lines/77.mp3"
    y "{i}Thursday evening. My work report is due that day. I don't know how long the revisions will take.{/i}"

    play sound "voice_lines/78.mp3"
    y "Thanks for organising that. Thursday evening might be difficult because of my work deadline. Can we agree on a time after I know how much revision is needed?"

    play sound "voice_lines/79.mp3"
    a "Of course. Would it help if I sent you the current draft now, so you can see what needs reviewing?"

    play sound "voice_lines/80.mp3"
    y "Yes, as long as we're clear that I haven't committed to reviewing the whole document by a fixed time yet."

    play sound "voice_lines/81.mp3"
    a "That's fair. I'll send it over."

    play sound "voice_lines/82.mp3"
    y "{i}I'm noticing something. Saying what I can and cannot do doesn't automatically make people angry. Sometimes it gives them the information they need to plan around me.{/i}"

    play sound "voice_lines/83.mp3"
    y "{i}Who knew that communicating clearly could be more effective than silently panicking? Someone probably wrote an entire book about it.{/i}"

    play sound "voice_lines/84.mp3"
    "Wednesday, 6:20 PM."

    play sound "voice_lines/85.mp3"
    "You submit your university assignment with eleven minutes to spare. You do not celebrate. You simply close the laptop and stare at the wall for a moment."

    play sound "voice_lines/86.mp3"
    y "{i}Submitted. Not perfect, perhaps, but submitted. A rare victory for the concept of finishing things.{/i}"

    play sound "voice_lines/87.mp3"
    "Your phone rings. It is Person A."

    play sound "voice_lines/88.mp3"
    a "How did the assignment go?"

    play sound "voice_lines/89.mp3"
    y "It's submitted. I'm relieved, but I've still got my work report to finish."

    play sound "voice_lines/90.mp3"
    a "I'm glad you got it done. The others have checked the figures, and the proposal is nearly ready. We still need someone to check the final version."

    play sound "voice_lines/91.mp3"
    a "Would you have time tomorrow, if I send it over in the morning?"

    play sound "voice_lines/92.mp3"
    y "{i}I want to help. I also know that saying yes now could create another deadline I cannot meet. The final document might need a quick proofread, or it might need another four hours of work.{/i}"

    play sound "voice_lines/93.mp3"
    y "{i}Being responsible means taking the charity seriously. It also means being honest about the quality and amount of work I can deliver.{/i}"

    play sound "voice_lines/94.mp3"
    menu:
            "What do you agree to do?"

            "Promise to review the whole document tomorrow, regardless of your workload.":
                $ boundary_score += -3
                $ communication_score += 0
                $ responsibility_score += 3

                play sound "voice_lines/95.mp3"
                y "Yes, I'll review the whole thing tomorrow. Send it over and I'll fit it in."

                play sound "voice_lines/96.mp3"
                a "Brilliant. Thank you."

                play sound "voice_lines/97.mp3"
                y "{i}I have made another promise without checking the actual workload. I might manage it, but I have left no room for unexpected problems.{/i}"

            "Offer a defined amount of time and agree on priorities.":
                $ boundary_score += 1
                $ communication_score += 1
                $ responsibility_score += 1

                play sound "voice_lines/98.mp3"
                y "I can set aside an hour tomorrow evening after my work report is submitted. If you send the document in the morning, I'll focus on checking the sections that still need attention."

                play sound "voice_lines/99.mp3"
                y "If it needs more than that, we'll need to agree who can do the remaining work or whether the deadline needs to be reconsidered."

                play sound "voice_lines/100.mp3"
                a "That works. I'll flag the sections that need the most attention."

                play sound "voice_lines/101.mp3"
                y "Good. That way, we know what I can realistically contribute, and you can plan around it."

                play sound "voice_lines/102.mp3"
                a "Thanks. I appreciate you being clear about it."

                play sound "voice_lines/103.mp3"
                y "{i}A specific offer is more useful than a vague promise. It gives Person A something they can actually plan around.{/i}"

            "Withdraw from the task entirely without discussing alternatives.":
                $ boundary_score += 2
                $ communication_score += -1
                $ responsibility_score += -2

                play sound "voice_lines/104.mp3"
                y "I can't do it. I've got too much going on."

                play sound "voice_lines/105.mp3"
                a "Okay. I'll see if anyone else can help."

                play sound "voice_lines/106.mp3"
                y "{i}I may genuinely need to step back. But I haven't explained what I can offer, helped identify the remaining work, or checked whether the plan is still realistic.{/i}"

    play sound "voice_lines/107.mp3"
    "Thursday, 7:15 PM."

    play sound "voice_lines/108.mp3"
    "Your work report has been submitted. Your inbox is finally quiet."

    play sound "voice_lines/109.mp3"
    "You open the charity's latest message. The proposal is ready for the Friday meeting, and Person A has thanked everyone who contributed."

    play sound "voice_lines/110.mp3"
    a "We've got the proposal ready. Thanks for helping us work through it."

    play sound "voice_lines/111.mp3"
    y "I'm glad we got it sorted."

    play sound "voice_lines/112.mp3"
    a "I think I learned something from this week. I assumed I had to solve the problem before telling anyone about it."

    play sound "voice_lines/113.mp3"
    y "I can relate to that. I sometimes say yes because I don't want to disappoint people, even when I haven't worked out whether I can deliver."

    play sound "voice_lines/114.mp3"
    a "It's difficult to balance everything. The charity matters, but so do the people doing the work."

    play sound "voice_lines/115.mp3"
    y "{i}That's probably the point I needed to remember. A charity doesn't benefit from staff who exhaust themselves trying to prove they're committed.{/i}"

    play sound "voice_lines/116.mp3"
    y "{i}But boundaries aren't an excuse to disengage, either. Other people depend on us, and we need to communicate, share responsibility and make decisions that protect the work we're here to do.{/i}"

    play sound "voice_lines/117.mp3"
    a "Next time, I think I'll raise the problem earlier and ask for help before the deadline becomes urgent."

    play sound "voice_lines/118.mp3"
    y "And I'll check my actual capacity before agreeing to anything. At least, that's the plan."

    play sound "voice_lines/119.mp3"
    a "A plan is a start."

    play sound "voice_lines/120.mp3"
    y "{i}A plan, a calendar, and possibly a second mug of tea. The foundations of responsible leadership.{/i}"

    # Personal endings
    play sound "voice_lines/121.mp3"
    "Your decisions have shaped how you managed your commitments, communicated with others, and supported the charity."

    if boundary_score < 0:
        play sound "voice_lines/122.mp3"
        "Based on your chosen responses, you may have a tendency to overcommit without realising."

        play sound "voice_lines/123.mp3"
        "Advice: Before committing to a task, assess your existing workload and be honest about your availability."

        play sound "voice_lines/124.mp3"
        "Setting boundaries is not selfish. It helps you make commitments you can actually fulfil."

    elif boundary_score == 0:
        play sound "voice_lines/125.mp3"
        "Based on your chosen responses, you showed some awareness of your limits."

        play sound "voice_lines/126.mp3"
        "But, your decisions did not consistently demonstrate effective boundary-setting."

        play sound "voice_lines/127.mp3"
        "Advice: Practise distinguishing between what you would like to do and what you can realistically do."

        play sound "voice_lines/128.mp3"
        "Offer specific, manageable contributions rather than making open-ended promises."

    else:
        play sound "voice_lines/129.mp3"
        "You demonstrated an ability to recognise your limits and set realistic expectations around your commitments."

        play sound "voice_lines/130.mp3"
        "Advice: Continue communicating your capacity early."

        play sound "voice_lines/131.mp3"
        "Remember that setting a boundary works best when you also help identify a practical way forward."

    if communication_score < 0:
        play sound "voice_lines/132.mp3"
        "Based on your chosen responses, you may not always be fully clear to other people."

        play sound "voice_lines/133.mp3"
        "Your decisions may have left others uncertain about your availability, priorities, or the support you could provide."

        play sound "voice_lines/134.mp3"
        "Advice: Communicate early and directly when difficulties arise."

        play sound "voice_lines/135.mp3"
        "Explain what you can do, what you cannot do, and when others should expect an update."

    elif communication_score == 0:
        play sound "voice_lines/136.mp3"
        "Based on your chosen responses, you showed some confidence communicating to other people."

        play sound "voice_lines/137.mp3"
        "Advice: Ask questions before making commitments."

        play sound "voice_lines/138.mp3"
        "If a deadline is at risk, raise the issue early rather than waiting until the situation becomes urgent."

    else:
        play sound "voice_lines/139.mp3"
        "Based on your chosen responses, you demonstrated constructive communication by and discussing expectations with others."

        play sound "voice_lines/140.mp3"
        "Advice: Keep communication collaborative and explain your position."

        play sound "voice_lines/141.mp3"
        "Also, listen to other perspectives, and agree on clear next steps wherever possible."

    if responsibility_score < 0:
        play sound "voice_lines/142.mp3"
        "Based on your chosen responses, you may not have adequately considered the impact of your actions on others."

        play sound "voice_lines/143.mp3"
        "Advice: Consider who depends on the work being completed."

        play sound "voice_lines/144.mp3"
        "When you cannot take on a task, communicate this promptly and help identify alternatives where possible."

    elif responsibility_score == 0:
        play sound "voice_lines/145.mp3"
        "Based on your chosen responses, you considered some of the charity's needs."

        play sound "voice_lines/146.mp3"
        "There may have been opportunities to share responsibility or plan more effectively."

        play sound "voice_lines/147.mp3"
        "Advice: Focus on solutions rather than simply accepting or rejecting tasks."

        play sound "voice_lines/148.mp3"
        "Clarify priorities, involve relevant  staff and agree who is responsible for each action."

    else:
        play sound "voice_lines/149.mp3"
        "You demonstrated consideration for the charity's needs while recognising that responsibility should be shared."

        play sound "voice_lines/150.mp3"
        "Advice: Continue balancing organisational priorities with individual capacity."

        play sound "voice_lines/151.mp3"
        "Effective leadership means supporting the charity without assuming that one person must solve every problem."

    play sound "voice_lines/152.mp3"
    "Human-centred leadership is not about always saying yes, or always protecting your own time."

    play sound "voice_lines/153.mp3"
    "It is about making considered decisions that respect both people and responsibilities."

    play sound "voice_lines/154.mp3"
    "You close your laptop."

    play sound "voice_lines/155.mp3"
    "For once, tomorrow's to-do list contains a realistic number of tasks."

    play sound "voice_lines/156.mp3"
    "Simulated Scenario Finished! Press left click on your mouse / tap your mousepad to return to the menu."

    return