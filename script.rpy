# Character definition
define y = Character("You")
define a = Character("Person A")

# HUD display
default boundary_score = 0
default communication_score = 0
default responsibility_score = 0

screen confidence_ui():
    vbox:
        xalign 0.98
        yalign 0.02
        spacing 5

        frame:
            text "Boundary Score (Recognises personal capacity and avoids overcommitting): [boundary_score]"

        frame:
            text "Communication Score (Informs others early and explains constraints constructively): [communication_score]"

        frame:
            text "Team Responsibility Score (Manages the impact on the charity): [responsibility_score]"

label start:

    show screen confidence_ui

    "Welcome! To continue, please press left click on your mouse / tap your mousepad while your cursor is on the game."

    "Great! This is a simulated scenario based on Balancing Commitments and Wellbeing."

    "Please note that this is a fictional video game, and there are no real names used."

    "During the game, you will have the option to 'choose your response' through key points."

    "There are no right or wrong answers, and many options will increase one score while lowering others. That is life!"

    "Once you are ready, press left click one more time and the simulated scenario will start!"

    # Scenario Start

    "Balancing Commitments and Wellbeing: Scenario Start"

    "Monday, 7:42 PM."

    "Your laptop is open. Three browser tabs are displaying deadlines, your phone is vibrating, and a mug of tea has been sitting untouched long enough to qualify as a historical artefact."

    y "{i}Right. Let's assess the situation rationally.{/i}"

    y "{i}I have a university assignment due Wednesday. I have a work deadline on Thursday. And I promised the charity that I would review a document before Friday's meeting.{/i}"

    y "{i}Three perfectly reasonable commitments. Individually manageable. Collectively, apparently a government experiment designed to discover how much stress one human being can absorb.{/i}"

    "Your phone vibrates again. A message from Person A appears."

    a "Hey! Have you got a minute?"

    y "{i}That question has never once meant one minute.{/i}"

    y "Hey. What's up?"

    a "Sorry to message so late. I know everyone's busy, but I've run into a problem with the charity's funding proposal."

    a "The draft needs reviewing before the board meeting on Friday. I thought I had most of it covered, but some of the figures don't match the latest budget."

    y "How much needs doing?"

    a "The figures need checking, the impact section needs updating, and we need someone to review the final version. I was hoping you could help me get it sorted by Wednesday evening."

    y "{i}Wednesday evening.{/i}"

    y "{i}The same Wednesday evening that my university assignment is due. The assignment I have been working on for three weeks. The assignment that currently consists of an introduction, two paragraphs and a deeply optimistic conclusion.{/i}"

    y "I might be able to help. How much work do you think it is?"

    a "A few hours, probably. Maybe four if the figures are a mess."

    y "{i}Four hours. That's almost a whole evening, assuming time has stopped existing for food, sleep and basic hygiene.{/i}"

    a "I wouldn't ask if it wasn't important. The funding could make a real difference to the people we support."

    y "{i}And that's the difficult part. This isn't meaningless admin. The proposal matters. People are relying on us to make sensible decisions and use the charity's resources properly.{/i}"

    y "{i}But my other commitments matter too. I do not want to become a person who survives exclusively on caffeine and calendar notifications.{/i}"

    "You pause before replying."

    menu:
            "How do you respond to Person A?"

            "Agree to do it all, even though the deadline is unrealistic.":
                $ boundary_score += -2
                $ communication_score += -1
                $ responsibility_score += 2

                y "Sure. Send everything over. I'll get it done by Wednesday."

                a "Really? Thank you. That takes a massive weight off my shoulders."

                y "{i}They sound relieved. That should feel good. So why does my stomach feel like it has just received an eviction notice?{/i}"

                y "{i}I've agreed without checking what I can realistically deliver. I might pull it off, but I've made a promise before understanding the full cost.{/i}"

            "Explain your deadline and ask what the highest-priority tasks are.":
                $ boundary_score += 2
                $ communication_score += 2
                $ responsibility_score += 1

                y "I want to help, but I've got an assignment due Wednesday evening. I can't promise to complete four hours of work by then."

                y "Could we identify which parts of the proposal are most urgent? I might be able to review a specific section or help find another person to share the work."

                a "That's fair. I hadn't realised your deadline was that close."

                y "{i}It's uncomfortable to say no to part of a request. But explaining what I can do is more useful than making a promise I might break.{/i}"

            "Tell Person A that the proposal is their problem to solve.":
                $ boundary_score += 1
                $ communication_score += -1
                $ responsibility_score += -2

                y "I'm busy with my own deadlines. You'll need to find someone else."

                a "Oh. Right. Okay."

                y "{i}My time is limited, and I'm allowed to protect it. But I haven't asked what support is available, or whether there's a smaller task I could reasonably take on.{/i}"

                y "{i}A boundary doesn't have to be a slammed door. Although, admittedly, a slammed door would be quite satisfying right now.{/i}"

    "Tuesday, 12:35 PM."

    "You are between commitments when Person A calls."

    a "Have you had a chance to look at the proposal?"

    y "Not properly yet. What's happened?"

    a "I checked the budget again this morning. The figures are more complicated than I thought, and the person who usually handles them is unavailable until Thursday."

    a "I'm worried we'll have to present something incomplete at the meeting."

    y "{i}There it is. The problem has grown while I've been trying to keep everything else moving.{/i}"

    y "{i}I could ignore the call and protect my afternoon. I could agree to take over the whole proposal. Or I could help establish what is actually possible before anyone makes another promise.{/i}"

    y "Have you spoken to the others about the missing figures?"

    a "Not yet. I didn't want to worry everyone before I had a solution."

    y "I can see why you'd want to fix it first. But if the deadline is at risk, the others need to know early enough to help."

    a "I know. I just don't want people thinking I've failed to prepare."

    y "{i}That sounds familiar. I sometimes treat asking for help as evidence that I should have been able to do everything myself.{/i}"

    y "{i}It is a particularly inefficient habit. Unfortunately, humans are not renowned for being efficient about their insecurities.{/i}"

    a "What do you think we should do?"

    menu:
            "How do you handle the growing workload?"

            "Take ownership of the entire proposal so Person A doesn't feel pressured.":
                $ boundary_score += -1
                $ communication_score += 0
                $ responsibility_score += 2

                y "I'll take over the proposal and try to get it finished. We can discuss the details later."

                a "Are you sure? I really appreciate it."

                y "{i}I'm trying to help, but I may have replaced one person's problem with two people's problems. If I cannot finish the work, the charity still has a problem, and now my other commitments are at risk too.{/i}"

            "Discuss what can realistically be completed and notify the relevant staff.":
                $ boundary_score += 1
                $ communication_score += 1
                $ responsibility_score += 1

                y "Let's list what actually needs to be finished before Friday and what can wait. We should also let the others know that the budget figures are unresolved."

                y "That gives us a chance to divide the work properly instead of hoping someone can absorb it all."

                a "I was worried they'd think I'd handled it badly."

                y "They might have questions, but giving them time to help is better than telling them at the last minute."

                a "Okay. I'll send a message to the group and explain what's missing."

                y "{i}This feels more constructive. I'm not abandoning the task, but I'm not pretending I can solve everything alone either.{/i}"

            "Tell Person A to stop worrying and just work harder.":
                $ boundary_score += 0
                $ communication_score += -1
                $ responsibility_score += 0

                y "We've all got deadlines. We just need to push through and get it done."

                a "Right. I'll keep working on it."

                y "{i}I've offered a slogan instead of a solution. Very efficient if the goal is to make someone feel worse without changing anything.{/i}"

    "Tuesday, 8:10 PM."

    "You return to your laptop. Your assignment is still unfinished, and a work email has arrived asking for revisions to a report due Thursday."

    y "{i}I have approximately two hours before I need to stop working if I want a reasonable amount of sleep.{/i}"

    y "{i}I could spend those hours on the assignment, the charity proposal, or my work report. There is no option where I magically become three people.{/i}"

    "Another message appears from Person A."

    a "I've updated the group. One person can check the figures tomorrow, and another can review the impact section. Could you look over the final document on Thursday evening?"

    y "{i}Thursday evening. My work report is due that day. I don't know how long the revisions will take.{/i}"

    y "Thanks for organising that. Thursday evening might be difficult because of my work deadline. Can we agree on a time after I know how much revision is needed?"

    a "Of course. Would it help if I sent you the current draft now, so you can see what needs reviewing?"

    y "Yes, as long as we're clear that I haven't committed to reviewing the whole document by a fixed time yet."

    a "That's fair. I'll send it over."

    y "{i}I'm noticing something. Saying what I can and cannot do doesn't automatically make people angry. Sometimes it gives them the information they need to plan around me.{/i}"

    y "{i}Who knew that communicating clearly could be more effective than silently panicking? Someone probably wrote an entire book about it.{/i}"

    "Wednesday, 6:20 PM."

    "You submit your university assignment with eleven minutes to spare. You do not celebrate. You simply close the laptop and stare at the wall for a moment."

    y "{i}Submitted. Not perfect, perhaps, but submitted. A rare victory for the concept of finishing things.{/i}"

    "Your phone rings. It is Person A."

    a "How did the assignment go?"

    y "It's submitted. I'm relieved, but I've still got my work report to finish."

    a "I'm glad you got it done. The others have checked the figures, and the proposal is nearly ready. We still need someone to check the final version."

    a "Would you have time tomorrow, if I send it over in the morning?"

    y "{i}I want to help. I also know that saying yes now could create another deadline I cannot meet. The final document might need a quick proofread, or it might need another four hours of work.{/i}"

    y "{i}Being responsible means taking the charity seriously. It also means being honest about the quality and amount of work I can deliver.{/i}"

    menu:
            "What do you agree to do?"

            "Promise to review the whole document tomorrow, regardless of your workload.":
                $ boundary_score += -3
                $ communication_score += 0
                $ responsibility_score += 3

                y "Yes, I'll review the whole thing tomorrow. Send it over and I'll fit it in."

                a "Brilliant. Thank you."

                y "{i}I have made another promise without checking the actual workload. I might manage it, but I have left no room for unexpected problems.{/i}"

            "Offer a defined amount of time and agree on priorities.":
                $ boundary_score += 1
                $ communication_score += 1
                $ responsibility_score += 1

                y "I can set aside an hour tomorrow evening after my work report is submitted. If you send the document in the morning, I'll focus on checking the sections that still need attention."

                y "If it needs more than that, we'll need to agree who can do the remaining work or whether the deadline needs to be reconsidered."

                a "That works. I'll flag the sections that need the most attention."

                y "Good. That way, we know what I can realistically contribute, and you can plan around it."

                a "Thanks. I appreciate you being clear about it."

                y "{i}A specific offer is more useful than a vague promise. It gives Person A something they can actually plan around.{/i}"

            "Withdraw from the task entirely without discussing alternatives.":
                $ boundary_score += 2
                $ communication_score += -1
                $ responsibility_score += -2

                y "I can't do it. I've got too much going on."

                a "Okay. I'll see if anyone else can help."

                y "{i}I may genuinely need to step back. But I haven't explained what I can offer, helped identify the remaining work, or checked whether the plan is still realistic.{/i}"

    "Thursday, 7:15 PM."

    "Your work report has been submitted. Your inbox is finally quiet."

    "You open the charity's latest message. The proposal is ready for the Friday meeting, and Person A has thanked everyone who contributed."

    a "We've got the proposal ready. Thanks for helping us work through it."

    y "I'm glad we got it sorted."

    a "I think I learned something from this week. I assumed I had to solve the problem before telling anyone about it."

    y "I can relate to that. I sometimes say yes because I don't want to disappoint people, even when I haven't worked out whether I can deliver."

    a "It's difficult to balance everything. The charity matters, but so do the people doing the work."

    y "{i}That's probably the point I needed to remember. A charity doesn't benefit from  s who exhaust themselves trying to prove they're committed.{/i}"

    y "{i}But boundaries aren't an excuse to disengage, either. Other people depend on us, and we need to communicate, share responsibility and make decisions that protect the work we're here to do.{/i}"

    a "Next time, I think I'll raise the problem earlier and ask for help before the deadline becomes urgent."

    y "And I'll check my actual capacity before agreeing to anything. At least, that's the plan."

    a "A plan is a start."

    y "{i}A plan, a calendar, and possibly a second mug of tea. The foundations of responsible leadership.{/i}"

    # Personal endings
    "Your decisions have shaped how you managed your commitments, communicated with others, and supported the charity."

    if boundary_score < 0:
        "Based on your chosen responses, you may have a tendency to overcommit without realising."

        "Advice: Before committing to a task, assess your existing workload and be honest about your availability."

        "Setting boundaries is not selfish. It helps you make commitments you can actually fulfil."
        
    elif boundary_score == 0:
        "Based on your chosen responses, you showed some awareness of your limits."

        "But, your decisions did not consistently demonstrate effective boundary-setting."

        "Advice: Practise distinguishing between what you would like to do and what you can realistically do." 
            
        "Offer specific, manageable contributions rather than making open-ended promises."

    else:
        "You demonstrated an ability to recognise your limits and set realistic expectations around your commitments."

        "Advice: Continue communicating your capacity early." 
            
        "Remember that setting a boundary works best when you also help identify a practical way forward."

    if communication_score < 0:
        "Based on your chosen responses, you may not always be fully clear to other people."

        "Your decisions may have left others uncertain about your availability, priorities, or the support you could provide."

        "Advice: Communicate early and directly when difficulties arise." 
        
        "Explain what you can do, what you cannot do, and when others should expect an update."

    elif communication_score == 0:
        "Based on your chosen responses, you showed some confidence communicating to other people."

        "Advice: Ask questions before making commitments." 
            
        "If a deadline is at risk, raise the issue early rather than waiting until the situation becomes urgent."

    else:
        "Based on your chosen responses, you demonstrated constructive communication by and discussing expectations with others."

        "Advice: Keep communication collaborative and explain your position." 
            
        "Also, listen to other perspectives, and agree on clear next steps wherever possible."

    if responsibility_score < 0:
        "Based on your chosen responses, you may not have adequately considered the impact of your actions on others."

        "Advice: Consider who depends on the work being completed." 
        
        "When you cannot take on a task, communicate this promptly and help identify alternatives where possible."

    elif responsibility_score == 0:
        "Based on your chosen responses, you considered some of the charity's needs."

        "There may have been opportunities to share responsibility or plan more effectively."

        "Advice: Focus on solutions rather than simply accepting or rejecting tasks." 
            
        "Clarify priorities, involve relevant  staff and agree who is responsible for each action."

    else:
        "You demonstrated consideration for the charity's needs while recognising that responsibility should be shared."

        "Advice: Continue balancing organisational priorities with individual capacity." 
            
        "Effective leadership means supporting the charity without assuming that one person must solve every problem."

    "Human-centred leadership is not about always saying yes, or always protecting your own time." 
    
    "It is about making considered decisions that respect both people and responsibilities."

    "You close your laptop."

    "For once, tomorrow's to-do list contains a realistic number of tasks."

    "Simulated Scenario Finished! Press left click on your mouse / tap your mousepad to return to the menu."

    return
