"""Phases, workouts and the 30 daily pages (English copy, US spelling, metric with US units)."""

PHASES = [
    {
        "n": 1, "days": (1, 7), "name": "BUILD THE FOUNDATION",
        "lead": "The first week isn't about changing everything. You're laying the foundation: regular meals, "
                "water, more movement and your first workouts.",
        "goals": ["Understand your starting point", "Bring structure to your meals", "Build a water routine",
                  "Move more every day", "Start your first simple habits", "Do your first workouts"],
        "habits": ["Movement goal", "Water", "Protein", "Vegetables", "Plate method"],
        "note": "You may feel slightly sore in the first few days. That's normal and usually "
                "fades within a few days.",
    },
    {
        "n": 2, "days": (8, 14), "name": "STRENGTHEN THE ROUTINE",
        "lead": "The foundation is in place. Now you're making the structure stronger: portions, planning and "
                "regular workouts.",
        "goals": ["Structure your meals better", "Keep your portions in check",
                  "Fit protein and vegetables into every meal", "Move more",
                  "Train regularly", "Notice your first progress"],
        "habits": ["Hand portions", "Liquid calories", "Eating slowly", "Shopping list", "Meal prep"],
        "note": "The workouts go up to 3 sets. If that feels too hard, stay at 2 sets; "
                "doing it regularly matters more than doing more.",
    },
    {
        "n": 3, "days": (15, 21), "name": "STAY CONSISTENT",
        "lead": "The plan feels familiar now. This week you prepare for the hard moments of real life: "
                "sudden cravings, invitations, tired days.",
        "goals": ["Understand sudden cravings", "Handle tricky everyday situations",
                  "Plan for eating out", "Prepare for dips in motivation",
                  "Turn discipline into a system", "Keep moving and training"],
        "habits": ["The 10-minute rule", "Sleep routine", "Eating-out plan", "Worst-day plan"],
        "note": "In this phase, the lowering part of squats, push-ups and lunges takes 3 seconds. "
                "Slower, more controlled.",
    },
    {
        "n": 4, "days": (22, 30), "name": "MAKE IT YOUR SYSTEM",
        "lead": "The final phase. You make what you've learned stick and build your own system for "
                "life after day 30.",
        "goals": ["Lock in your habits", "Review your progress",
                  "Read setbacks the right way", "Long-term eating plan",
                  "Long-term movement plan", "Long-term training routine",
                  "Get ready for life after day 30"],
        "habits": ["Habit stacking", "Weekend plan", "Hunger scale", "Next-steps plan"],
        "note": "You can do 4 sets in this phase. If that's too hard, stay at 3 sets; you'll still make progress.",
    },
]

# Workouts per phase. rows: (exercise, prescription)
WORKOUTS = {
    ("A", 1): {"rest": "60–90 sec", "rows": [("Squat", "2 × 10"), ("Push-up (easier version)", "2 × 8"),
                                             ("Row", "2 × 10"), ("Glute bridge", "2 × 12"),
                                             ("Plank", "2 × 20 sec")]},
    ("B", 1): {"rest": "60–90 sec", "rows": [("Reverse lunge", "2 × 8 per leg"), ("Row", "2 × 10"),
                                             ("Push-up (easier version)", "2 × 8"), ("Dead bug", "2 × 6 per side"),
                                             ("Wall sit", "2 × 20 sec")]},
    ("A", 2): {"rest": "60–75 sec", "rows": [("Squat", "3 × 12"), ("Push-up", "3 × 8–10"),
                                             ("Row", "3 × 12"), ("Glute bridge", "3 × 15"),
                                             ("Plank", "3 × 25 sec")]},
    ("B", 2): {"rest": "60–75 sec", "rows": [("Reverse lunge", "3 × 10 per leg"), ("Row", "3 × 12"),
                                             ("Push-up", "3 × 8–10"), ("Dead bug", "3 × 8 per side"),
                                             ("Wall sit", "3 × 30 sec")]},
    ("A", 3): {"rest": "60 sec", "rows": [("Squat (3 sec down)", "3 × 12"), ("Push-up (3 sec down)", "3 × 10"),
                                          ("Row (1 sec squeeze at top)", "3 × 12"), ("Glute bridge (2 sec at top)", "3 × 15"),
                                          ("Plank", "3 × 30 sec")]},
    ("B", 3): {"rest": "60 sec", "rows": [("Reverse lunge (3 sec down)", "3 × 12 per leg"),
                                          ("Row (1 sec squeeze at top)", "3 × 12"), ("Push-up (3 sec down)", "3 × 10"),
                                          ("Dead bug", "3 × 10 per side"), ("Wall sit", "3 × 40 sec")]},
    ("A", 4): {"rest": "60 sec", "rows": [("Squat", "4 × 12"), ("Push-up", "4 × 10"),
                                          ("Row", "4 × 12"), ("Glute bridge", "3 × 15"),
                                          ("Plank", "3 × 40 sec")]},
    ("B", 4): {"rest": "60 sec", "rows": [("Reverse lunge", "3 × 12 per leg"), ("Row", "4 × 12"),
                                          ("Push-up", "3 × 10–12"), ("Dead bug", "3 × 10 per side"),
                                          ("Wall sit", "3 × 45 sec")]},
}


def workout(letter, phase, note=None, extra=None):
    w = WORKOUTS[(letter, phase)]
    return {"kind": "strength", "name": f"Workout {letter}", "type": "Full-body strength",
            "rest": w["rest"], "rows": w["rows"], "note": note, "extra": extra}


def recovery(label, text):
    return {"kind": "recovery", "name": label, "text": text}


MOBILITY_TEXT = "10-minute mobility routine (p. {p:isinma})."

DAYS = [
    # ------------------------------------------------------------------ PHASE 1
    {
        "n": 1, "title": "Find your starting point",
        "focus": "Today you're not trying to do anything perfectly. You're just seeing where you are: "
                 "taking your measurements and observing a normal day.",
        "nutrition": "Set up a rhythm of 3 main meals and write down or photograph what you eat. No judging, just observing.",
        "meals": [
            ("Breakfast", "2 boiled eggs, 1 slice whole-grain bread, tomato, cucumber, 5 olives"),
            ("Lunch", "1 bowl lentil soup, 1 palm grilled chicken, a big green salad"),
            ("Snack", "1 apple and 10 raw almonds (if you're hungry)"),
            ("Dinner", "Chicken stir-fry (1 palm chicken, peppers, tomato, onion), 1 fist rice or bulgur, 1 bowl yogurt"),
        ],
        "movement": ("20-minute walk",
                     "If your phone or watch counts steps, write down today's step count. That's your starting value."),
        "training": recovery("No workout",
                             "If you like, try the warm-up on p. {p:isinma} once to get to know the exercises."),
        "tip": "Don't try to change everything on day one. Big starts usually end quickly; "
               "small starts keep going.",
        "task": "Fill in the Day 1 column of the Progress Tracker (p. {p:ilerleme}): weight, waist and today's steps.",
    },
    {
        "n": 2, "title": "Build your water routine",
        "focus": "Today's focus is water. Drinking regularly throughout the day is one of the simplest habits, and one of the most often forgotten.",
        "nutrition": "Drink 1 glass of water with every meal. Try swapping sugary drinks for water today.",
        "meals": [
            ("Breakfast", "Oat bowl: 4 tablespoons oats (40 g, about 1/2 cup), 1 bowl yogurt, half a banana, cinnamon"),
            ("Lunch", "Tuna salad: 1 can drained tuna, 1/2 cup cooked chickpeas, "
                      "lettuce, tomato, cucumber, lemon, 1 teaspoon olive oil"),
            ("Snack", "1 glass of kefir or milk and 1 clementine"),
            ("Dinner", "Baked skinless chicken thigh (1 palm), roasted vegetables (zucchini, peppers, carrots), 1 medium boiled potato"),
        ],
        "movement": ("20-minute walk", "At a different time from your workout, for example at lunchtime."),
        "training": workout("A", 1, note="First workout: focus on learning the technique. Check the exercises on p. {p:egzersiz}."),
        "tip": "Keep water where you can see it. A bottle on your desk is often the best reminder.",
        "task": "Get a water bottle ready and aim for about 8 glasses of water over the day.",
    },
    {
        "n": 3, "title": "Protein with every main meal",
        "focus": "Protein can help you stay full for longer and helps protect your muscles. Today you add a protein source to every main meal.",
        "nutrition": "Breakfast, lunch and dinner: every plate includes eggs, yogurt, cheese, chicken, fish, meat or legumes.",
        "meals": [
            ("Breakfast", "Feta omelet: 2 eggs, 1 matchbox-sized piece of feta, 1 handful spinach; 1 slice whole-grain bread"),
            ("Lunch", "1 bowl white bean stew, 1/2 fist rice or 1 slice bread, tzatziki"),
            ("Snack", "1 bowl Greek yogurt or skyr, a few strawberries"),
            ("Dinner", "Grilled meatballs (1 palm, 4–5 pieces), white bean salad or a chopped tomato-cucumber salad"),
        ],
        "movement": ("25-minute walk", "Followed by 10 minutes of mobility."),
        "training": recovery("Active recovery", MOBILITY_TEXT),
        "tip": "Protein sources: eggs, yogurt, kefir, feta, cottage cheese, chicken, turkey, fish, "
               "tuna, red meat, lentils, chickpeas, beans. Pick at least one from this list for every main meal.",
        "task": "Choose and write down the protein sources for tomorrow's three main meals now.",
    },
    {
        "n": 4, "title": "Move more every day",
        "focus": "Movement outside your workouts matters too. Today you add small movement breaks to your day.",
        "nutrition": "Protein with every main meal continues. When you crave something sweet, try a piece of fruit first.",
        "meals": [
            ("Breakfast", "Breakfast plate: 2 eggs, 1 matchbox-sized piece of feta, tomato, cucumber, greens, 1 slice whole-grain bread"),
            ("Lunch", "Chicken wrap: 1 whole-wheat wrap, 1 palm chicken, lettuce, tomato, yogurt sauce"),
            ("Snack", "Carrot and cucumber sticks, 2 tablespoons hummus"),
            ("Dinner", "Baked salmon or white fish (1 palm), steamed broccoli, 1 fist rice or bulgur"),
        ],
        "movement": ("25-minute walk + 3 movement breaks",
                     "Every 1–2 hours, get up for 3–5 minutes: take the stairs, stand during a phone call, walk a short loop."),
        "training": workout("B", 1),
        "tip": "Stairs instead of the elevator, walking instead of driving short distances. Small choices add up by the end of the day.",
        "task": "Set 3 reminders on your phone: a short movement break at 11 a.m., 3 p.m. and 6 p.m.",
    },
    {
        "n": 5, "title": "Add more vegetables",
        "focus": "Vegetables are filling, contain fiber and make your plate satisfying. Today there are vegetables in at least two meals.",
        "nutrition": "At lunch and dinner, fill about half your plate with vegetables.",
        "meals": [
            ("Breakfast", "Scrambled eggs with tomatoes and peppers (2 eggs), 1 slice whole-grain bread, cucumber"),
            ("Lunch", "A big portion of green beans cooked in olive oil, 1 bowl yogurt, 1 slice whole-grain bread"),
            ("Snack", "1 pear and 1 matchbox-sized piece of feta"),
            ("Dinner", "Spinach with lean ground meat, 1 bowl yogurt, 1/2 fist rice or 1 slice bread"),
        ],
        "movement": ("30-minute walk", "Followed by 10 minutes of mobility."),
        "training": recovery("Active recovery",
                             "Your muscles may feel a little sore after yesterday's workout. " + MOBILITY_TEXT),
        "tip": "Ready-to-eat vegetables beat good intentions. Keep chopped carrots, cucumber and tomatoes on the front shelf of your fridge.",
        "task": "Prep vegetables for 2–3 days: wash, chop and store them in a container in the fridge.",
    },
    {
        "n": 6, "title": "Build your plate",
        "focus": "The plate method is the easiest way to balance your portions without counting calories: half vegetables, "
                 "a quarter protein, a quarter carbs.",
        "nutrition": "Today, build your lunch and dinner using the plate method (p. {p:tabak}).",
        "meals": [
            ("Breakfast", "Greek yogurt bowl: 1 bowl Greek yogurt or skyr, 1 handful fruit, 1 tablespoon oats, 2 walnut halves"),
            ("Lunch", "1 palm grilled chicken, 1 fist rice or bulgur, half the plate chopped salad"),
            ("Snack", "1 boiled egg and 1 piece of fruit"),
            ("Dinner", "1 bowl chickpea stew with meat, half the plate seasonal salad, 1 bowl tzatziki"),
        ],
        "movement": ("25-minute walk", "At an easy pace; you should be able to chat."),
        "training": workout("A", 1, note="The exercises feel more familiar now. Same sets and reps, better technique."),
        "tip": "Use a smaller plate. The plate looks full while the portion stays reasonable.",
        "task": "Take a photo of a meal you built with the plate method. Use it as an example in the days ahead.",
    },
    {
        "n": 7, "title": "Review your first week",
        "focus": "One week done. Today you're not grading yourself; you're just looking at what worked.",
        "nutrition": "Keep your meal rhythm, even on the weekend. If you eat out, choose one protein and one vegetable.",
        "meals": [
            ("Breakfast", "2 eggs (boiled or scrambled with vegetables), 1 matchbox-sized piece of feta, 5 olives, lots of greens, 1–2 slices whole-grain bread"),
            ("Lunch", "1 bowl lentil soup, 1 bowl yogurt, seasonal salad, 1 slice bread"),
            ("Snack", "1 glass of kefir and a few slices of fruit"),
            ("Dinner", "Baked meatballs (1 palm) with vegetables (zucchini, peppers, tomatoes), 1 medium potato"),
        ],
        "movement": ("40-minute long walk", "In a park, by the water or in nature; at a pace where you can talk."),
        "training": recovery("Rest day", "Your muscles get stronger as they recover between workouts."),
        "tip": "Progress isn't just the number on the scale. Your energy, your sleep, your breath on the stairs and how your clothes fit are part of it too.",
        "task": "Fill in the Week 1 Review (p. {p:hafta1}) and write your Day 7 values in the Progress Tracker.",
    },
    # ------------------------------------------------------------------ PHASE 2
    {
        "n": 8, "title": "Measure portions with your hand",
        "focus": "No scale or app needed: your palm, fist and thumb are always with you. "
                 "Today you measure your portions with your hand.",
        "nutrition": "Every main meal: 1 palm protein, 1 fist carbs, 2 handfuls vegetables, 1 thumb fat (p. {p:tabak}).",
        "meals": [
            ("Breakfast", "Oat bowl: 40 g (1/2 cup) oats, 1 bowl yogurt, 1 handful strawberries or blueberries, 1 thumb-sized portion of walnuts"),
            ("Lunch", "Chicken stir-fry (1 palm), 1 fist rice or bulgur, 2 handfuls salad"),
            ("Snack", "1 glass of kefir and 1 apple"),
            ("Dinner", "Grilled turkey or chicken breast (1 palm), 1 fist roasted potatoes, 2 handfuls steamed vegetables, 1 teaspoon olive oil"),
        ],
        "movement": ("7,000 steps or a 35-minute walk", "If your starting average is very low, add about 1,000 steps to it instead."),
        "training": workout("A", 2, note="New phase: the workouts go up to 3 sets."),
        "tip": "Serve your portion onto your plate before you start eating. Don't keep the pot or serving dish on the table.",
        "task": "Make all three main meals with hand portions today. Note which portion is different from what you're used to.",
    },
    {
        "n": 9, "title": "Watch what you drink",
        "focus": "Sugary drinks, fruit juice and sweetened coffee can add a lot of energy without you noticing. "
                 "Today you look at what you drink.",
        "nutrition": "Today's drinks: water, sparkling water, plain tea, black coffee and unsweetened kefir. If you add sugar to your tea, cut it in half.",
        "meals": [
            ("Breakfast", "Scrambled eggs with vegetables (2 eggs), 1 matchbox-sized piece of feta, 1 slice whole-grain bread, cucumber"),
            ("Lunch", "6 lentil patties, lots of greens and lemon, 1 bowl yogurt"),
            ("Snack", "1 handful roasted chickpeas and 1 glass of kefir"),
            ("Dinner", "Baked salmon (1 palm), 1 fist rice or bulgur, arugula salad"),
        ],
        "movement": ("35-minute brisk walk",
                     "10 min easy + 5 × (2 min brisk, 2 min easy) + 5 min easy. On the brisk part you can still talk, but you couldn't sing."),
        "training": recovery("Cardio day", "No strength workout today; the brisk walk is your cardio session."),
        "tip": "Eat the fruit instead of drinking the juice. The fiber keeps you fuller.",
        "task": "Write down everything you drink today. In the evening, mark the sugary ones and swap one of them tomorrow.",
    },
    {
        "n": 10, "title": "Eat slowly",
        "focus": "It takes a while for the feeling of fullness to reach your brain. Today you stretch at least one meal over 20 minutes.",
        "nutrition": "Put your fork down between bites. No phone or screens while you eat.",
        "meals": [
            ("Breakfast", "2 boiled eggs, 2 tablespoons cottage cheese, tomato, cucumber, greens, 1 slice whole-grain bread"),
            ("Lunch", "Chicken bulgur salad: 1 palm chicken, 1 fist bulgur or quinoa, tomato, cucumber, parsley, lemon"),
            ("Snack", "1 bowl Greek yogurt, cinnamon"),
            ("Dinner", "Zucchini or okra stewed with meat (1 palm meat), 1 bowl yogurt, 1 slice bread"),
        ],
        "movement": ("7,000 steps or a 35-minute walk", "A short 10-minute walk after a meal counts too."),
        "training": workout("B", 2),
        "tip": "Start your meal with a salad or soup. That way you eat the main dish more calmly.",
        "task": "Set a timer at dinner and stretch the meal over at least 20 minutes.",
    },
    {
        "n": 11, "title": "Plan your shopping",
        "focus": "You eat what's in the house. Today you write a shopping list that fits the plan.",
        "nutrition": "Shop on a full stomach and stick to the list. The basic list is on p. {p:alisveris}.",
        "meals": [
            ("Breakfast", "Oatmeal: cook 40 g (1/2 cup) oats in 1 cup of milk, add half a banana and cinnamon; 1 boiled egg on the side"),
            ("Lunch", "Leftovers from last night's dinner or a tuna salad with lots of greens"),
            ("Snack", "Carrot sticks and 2 tablespoons hummus"),
            ("Dinner", "1 bowl red lentil stew, 1 fist rice or bulgur, 1 bowl yogurt, salad"),
        ],
        "movement": ("7,000 steps", "Followed by 10 minutes of mobility."),
        "training": recovery("Active recovery", MOBILITY_TEXT),
        "tip": "At the store, start with produce, meat and dairy. If packaged snacks aren't on your list, they don't go in your cart.",
        "task": "Write a shopping list for the next 3–4 days and go shopping.",
    },
    {
        "n": 12, "title": "Prepare ahead",
        "focus": "Tired evenings are the hardest moments. Today you prepare food for 2–3 meals in advance.",
        "nutrition": "One pot of protein, one pot of grains and one tray of roasted vegetables: the base for a few days is ready.",
        "meals": [
            ("Breakfast", "Cheese omelet (2 eggs, 1 matchbox-sized piece of cheese, peppers), tomato, 1 slice whole-grain bread"),
            ("Lunch", "Your prepped chicken (1 palm), 1 fist rice or bulgur, roasted vegetables"),
            ("Snack", "1 glass of kefir and 1 handful strawberries"),
            ("Dinner", "Baked meatballs (1 palm), roasted vegetables and potatoes, tzatziki"),
        ],
        "movement": ("7,000 steps or a 35-minute walk", "Spread your steps over the day: morning, lunchtime and evening."),
        "training": workout("A", 2),
        "tip": "Tie your prep to a fixed time, for example 45 minutes every Sunday and Wednesday evening.",
        "task": "Cook protein and grains for at least 2 meals, portion them out and put them in the fridge.",
    },
    {
        "n": 13, "title": "Choose snacks on purpose",
        "focus": "Snacking isn't forbidden. The goal is to choose consciously when and what you snack on.",
        "nutrition": "Snack when you're really hungry: protein and fiber together. Ready-made alternatives instead of packaged snacks.",
        "meals": [
            ("Breakfast", "1 bowl Greek yogurt, 1 handful fruit, 1 tablespoon oats, 1 teaspoon honey if you like"),
            ("Lunch", "1 bowl lentil soup, 1 palm grilled chicken, chopped salad"),
            ("Snack", "1 apple and 10 almonds, or 1 boiled egg and cucumber"),
            ("Dinner", "Whole-wheat pasta with tuna (1 fist pasta, half a can of tuna, tomato sauce), a big green salad"),
        ],
        "movement": ("45-minute long walk", "In a park, by the water or in nature; with someone if you like."),
        "training": recovery("Rest day", "The long walk is your active recovery today."),
        "tip": "Keep snacks out of sight and fruit at eye level. Your surroundings are stronger than your willpower.",
        "task": "Get 3 ready-to-eat healthy snacks at home (e.g. yogurt, fruit, boiled eggs) and put the packaged ones away in a cupboard.",
    },
    {
        "n": 14, "title": "See your first progress",
        "focus": "Two weeks done. Today you take your measurements and look at what has changed.",
        "nutrition": "A normal plan day. Remember the plate method at weekend meals.",
        "meals": [
            ("Breakfast", "Scrambled eggs with vegetables (2 eggs), 1 matchbox-sized piece of feta, 5 olives, lots of greens, 1 slice bread"),
            ("Lunch", "1 bowl bean stew with meat, 1/2 fist rice, tzatziki"),
            ("Snack", "1 glass of kefir and 1 clementine"),
            ("Dinner", "Baked chicken and vegetables, 1 medium potato"),
        ],
        "movement": ("20–30-minute easy walk", "Followed by 10 minutes of mobility."),
        "training": recovery("Rest day", MOBILITY_TEXT),
        "tip": "Change doesn't happen at the same speed every week. Your waist can shrink in a week when the scale doesn't move. Look at several measurements together.",
        "task": "Fill in the Week 2 Review (p. {p:hafta2}) and write your Day 14 values in the Progress Tracker.",
    },
    # ------------------------------------------------------------------ PHASE 3
    {
        "n": 15, "title": "Hunger or craving?",
        "focus": "Not every urge to eat is hunger. Today you learn to tell physical hunger apart from a sudden craving.",
        "nutrition": "The 10-minute rule: when a sudden craving hits, wait 10 minutes and drink a glass of water. "
                     "If the craving is still there, choose a small portion on purpose.",
        "meals": [
            ("Breakfast", "Oat bowl: 40 g (1/2 cup) oats, 1 bowl yogurt, 1 handful fruit, 1 tablespoon hazelnuts"),
            ("Lunch", "Chicken wrap (whole-wheat wrap, 1 palm chicken, vegetables, yogurt sauce), 1 glass of kefir"),
            ("Snack", "1 bowl Greek yogurt, or 1 boiled egg and 1 piece of fruit"),
            ("Dinner", "Grilled fish (1 palm), 1 fist rice or bulgur, arugula and tomato salad"),
        ],
        "movement": ("8,000 steps or a 40-minute walk", "If your starting average is low, add about 1,000 steps to last week instead."),
        "training": workout("A", 3, note="New phase: take 3 seconds to lower. Slower is harder, but more controlled."),
        "tip": "Physical hunger comes on slowly and many foods will satisfy it. A craving comes on suddenly and usually wants one specific food.",
        "task": "If you get a sudden craving today, note the time, what you wanted and how you felt in that moment (bored, tired, stressed).",
    },
    {
        "n": 16, "title": "Sleep and appetite",
        "focus": "Have you noticed you're hungrier after a bad night's sleep? Today you start a sleep routine.",
        "nutrition": "Finish dinner 2–3 hours before bed. No coffee or energy drinks in the afternoon.",
        "meals": [
            ("Breakfast", "2 eggs, 1 matchbox-sized piece of feta, tomato, cucumber, 1 slice whole-grain bread"),
            ("Lunch", "1 bowl chickpea stew or chickpeas with spinach, 1 bowl yogurt, 1 slice bread"),
            ("Snack", "1 apple and 10 almonds"),
            ("Dinner", "Chicken stir-fry (1 palm), steamed vegetables, 1/2 fist rice"),
        ],
        "movement": ("40-minute brisk walk", "10 min easy + 6 × (2 min brisk, 2 min easy) + 6 min easy."),
        "training": recovery("Cardio day", "No strength workout today; the brisk walk is your cardio session."),
        "tip": "Going to bed and getting up at the same time every day is the simplest way to support your sleep. Keep the difference under 1 hour, even on weekends.",
        "task": "Pick a bedtime for tonight and turn off screens 30 minutes before bed.",
    },
    {
        "n": 17, "title": "Eating out",
        "focus": "Restaurant, café or business lunch: your plan works when you eat out too. Today you build a simple strategy for eating out.",
        "nutrition": "On the menu, choose the protein first (grilled, baked, boiled), then the vegetables. Pick either bread or rice, not both.",
        "meals": [
            ("Breakfast", "Scrambled eggs with vegetables (2 eggs), 1 slice whole-grain bread, cucumber"),
            ("Lunch", "Eating out: grilled meatballs or chicken skewers, a chopped salad, a half portion of rice; water or unsweetened tea"),
            ("Snack", "1 glass of kefir"),
            ("Dinner", "Baked chicken with vegetables (1 palm), 1 bowl yogurt"),
        ],
        "movement": ("8,000 steps or a 40-minute walk", "If you eat out, get off one stop early on the way back and walk."),
        "training": workout("B", 3),
        "tip": "If the portion is large, set half aside right away and ask for a to-go box. Deciding before you start is easier than deciding while you're hungry.",
        "task": "Choose “my order” for 2 places you go often and write it down.",
    },
    {
        "n": 18, "title": "Invitations and visits",
        "focus": "Family dinners, coffee with friends, holiday visits: social occasions are part of life. "
                 "Today you plan how to prepare for them.",
        "nutrition": "Don't arrive very hungry; have a small protein snack beforehand. At the table, take salad and protein first "
                     "and choose a small portion of dessert.",
        "meals": [
            ("Breakfast", "1 bowl Greek yogurt, 1 handful fruit, 1 tablespoon oats"),
            ("Lunch", "Your prepped chicken and grains, lots of salad"),
            ("Snack", "Before the invitation: 1 boiled egg and cucumber"),
            ("Dinner", "At the invitation: half your plate salad and vegetables, one protein (meat, chicken, meatballs), 1–2 spoonfuls of rice or pastry; a small portion of dessert"),
        ],
        "movement": ("8,000 steps", "Followed by 10 minutes of mobility."),
        "training": recovery("Active recovery", MOBILITY_TEXT),
        "tip": "Saying “It was delicious, I'm really full” isn't rude. Asking for a cup of tea when someone insists on seconds is another option.",
        "task": "If you have an invitation or get-together next week, write your plan for it in 2 sentences.",
    },
    {
        "n": 19, "title": "When motivation drops",
        "focus": "Motivation varies from day to day, and that's normal. Today you prepare your “worst-day plan”.",
        "nutrition": "When you're tired, pick the simplest meal: eggs, yogurt, a ready-made salad. That counts too.",
        "meals": [
            ("Breakfast", "2 boiled eggs, 1 slice whole-grain bread, tomato and cucumber"),
            ("Lunch", "1 bowl lentil soup, tuna salad"),
            ("Snack", "1 bowl yogurt and 1 piece of fruit"),
            ("Dinner", "Vegetable omelet (2–3 eggs), lots of salad, 1 slice bread"),
        ],
        "movement": ("8,000 steps or a 40-minute walk", "If you don't feel like it, start with 10 minutes; more usually follows."),
        "training": workout("A", 3, extra="Finisher (optional): 3 × 30 sec brisk marching in place, 30 sec rest."),
        "tip": "Don't wait for motivation; make starting easy. Lay out your workout clothes the night before.",
        "task": "Write your worst-day plan: the 3 smallest steps for a very tired day "
                "(e.g. a 10-minute walk, a protein meal, 8 glasses of water).",
    },
    {
        "n": 20, "title": "One meal doesn't ruin the plan",
        "focus": "One meal can fall outside the plan. What matters is getting back to normal at the next meal. "
                 "Today you let go of all-or-nothing thinking.",
        "nutrition": "If you ate something off-plan, don't skip a meal to make up for it. Eat your next meal as planned.",
        "meals": [
            ("Breakfast", "Feta omelet (2 eggs), tomato, 1 slice whole-grain bread"),
            ("Lunch", "1 bowl chickpea stew with meat, 1/2 fist rice, tzatziki"),
            ("Snack", "1 handful roasted chickpeas and 1 clementine"),
            ("Dinner", "Baked salmon or white fish (1 palm), 1 fist roasted potatoes, green salad"),
        ],
        "movement": ("45–60-minute long walk", "Try a new route: a different park or neighborhood."),
        "training": recovery("Rest day", "The long walk is your active recovery today."),
        "tip": "A slice of cake doesn't ruin the plan. Saying “it's ruined anyway” and giving up on the whole day does. One meal is a tiny part of 30 days.",
        "task": "Write this sentence and put it where you can see it: “Even if one meal goes badly, I'll carry on at the next one.”",
    },
    {
        "n": 21, "title": "Review your third week",
        "focus": "Three weeks are behind you. Today you look at what has already become a habit.",
        "nutrition": "A normal plan day. Plan the meal you found hardest this week in advance today.",
        "meals": [
            ("Breakfast", "Oatmeal (40 g / 1/2 cup oats, milk), 1 handful fruit, 1 boiled egg"),
            ("Lunch", "Chicken salad: 1 palm chicken, greens, chickpeas, olive oil and lemon"),
            ("Snack", "1 glass of kefir and 1 apple"),
            ("Dinner", "Vegetables cooked with ground meat, 1 bowl yogurt, 1 slice bread"),
        ],
        "movement": ("20–30-minute easy walk", "Followed by 10 minutes of mobility."),
        "training": recovery("Rest day", MOBILITY_TEXT),
        "tip": "The things you now do without thinking are your new foundation. Protect that foundation before you add anything new.",
        "task": "Fill in the Week 3 Review (p. {p:hafta3}) and write your Day 21 values in the Progress Tracker.",
    },
    # ------------------------------------------------------------------ PHASE 4
    {
        "n": 22, "title": "Lock in your habits",
        "focus": "Welcome to the final phase. Today you choose 3 core habits you'll keep going after the 30 days.",
        "nutrition": "Eating feels familiar now: the plate method, protein with every main meal, half your plate vegetables.",
        "meals": [
            ("Breakfast", "2 eggs, 1 matchbox-sized piece of feta, 5 olives, tomato, cucumber, 1 slice whole-grain bread"),
            ("Lunch", "1 bowl white bean stew, 1/2 fist rice, salad"),
            ("Snack", "1 bowl Greek yogurt and 2 walnut halves"),
            ("Dinner", "Grilled chicken (1 palm), roasted vegetables, 1 fist rice or bulgur"),
        ],
        "movement": ("8,000–10,000 steps or a 45-minute walk", "This could be your long-term movement goal."),
        "training": workout("B", 4, note="Final phase: you can do 4 sets. If that's too hard, stay at 3 sets."),
        "tip": "Attach a new habit to an existing one: “After I pour my morning coffee, I drink 1 glass of water.”",
        "task": "Choose 3 habits you'll keep and write each one down, attached to one of your existing routines.",
    },
    {
        "n": 23, "title": "Weekend strategy",
        "focus": "A plan that runs smoothly during the week can easily fall apart on the weekend. Today you build a simple plan for weekends.",
        "nutrition": "3 main meals on weekends too. If you had a late, big breakfast, keep lunch light.",
        "meals": [
            ("Breakfast", "Scrambled eggs with vegetables (2 eggs), 1 matchbox-sized piece of feta, lots of greens, 1–2 slices whole-grain bread"),
            ("Lunch", "Light lunch: 1 bowl lentil soup and 1 bowl yogurt"),
            ("Snack", "1 piece of fruit and 10 almonds"),
            ("Dinner", "Grilled meatballs (1 palm), white bean salad, lots of salad"),
        ],
        "movement": ("40-minute brisk walk", "Or an activity you enjoy: cycling, swimming, dancing."),
        "training": recovery("Cardio day", "No strength workout today. Move with an activity you enjoy."),
        "tip": "Make weekend movement social: a walk with a friend, a bike ride with your family, a long stroll through the market.",
        "task": "Set 1 activity for this weekend and, if you're eating out, 1 meal plan.",
    },
    {
        "n": 24, "title": "The hunger scale",
        "focus": "There's a difference between being full and being stuffed. Today you notice your fullness on a scale from 1 to 10.",
        "nutrition": "1 = very hungry, 5 = neutral, 10 = overly full. Start a meal at around 3–4 and stop at around 6–7 (comfortably full).",
        "meals": [
            ("Breakfast", "Oat bowl: 40 g (1/2 cup) oats, 1 bowl yogurt, 1 handful fruit, 1 tablespoon hazelnuts"),
            ("Lunch", "Tuna sandwich: 2 slices whole-grain bread, half a can of tuna, lettuce, tomato; a glass of kefir on the side"),
            ("Snack", "Carrot sticks and 2 tablespoons hummus"),
            ("Dinner", "Baked fish (1 palm), steamed broccoli and carrots, 1 medium potato"),
        ],
        "movement": ("8,000–10,000 steps", "Try adding a 15-minute walk at lunchtime."),
        "training": workout("A", 4),
        "tip": "It's fine to leave food on your plate. Swap the “clean your plate” habit for a “listen to my fullness” habit.",
        "task": "Note your hunger score (1–10) before and after every main meal.",
    },
    {
        "n": 25, "title": "Measure your progress",
        "focus": "Before the final days, you take your measurements. The goal is to look at the overall trend, not a single number.",
        "nutrition": "A normal plan day. Measure in the morning, before breakfast.",
        "meals": [
            ("Breakfast", "2 boiled eggs, 2 tablespoons cottage cheese, tomato, cucumber, 1 slice whole-grain bread"),
            ("Lunch", "6 lentil patties, lots of greens, 1 bowl yogurt"),
            ("Snack", "1 glass of kefir and 1 pear"),
            ("Dinner", "Chicken stir-fry (1 palm), 1 fist rice or bulgur, tzatziki"),
        ],
        "movement": ("9,000 steps", "Followed by 10 minutes of mobility."),
        "training": recovery("Active recovery", MOBILITY_TEXT),
        "tip": "Use your measurements to adjust the plan, not to judge yourself. Something that didn't go as expected isn't a failure; it's new information.",
        "task": "Take your weight and waist and compare them with Day 1. Below the Progress Tracker, write at least 1 positive change (energy, sleep, strength, clothes).",
    },
    {
        "n": 26, "title": "Long-term eating",
        "focus": "Eating for the long term isn't eating perfectly. Today you build a flexible structure for life after the 30 days.",
        "nutrition": "A simple rule: most of your meals follow the plan, and you make planned room for foods you love.",
        "meals": [
            ("Breakfast", "Feta omelet (2 eggs), spinach, 1 slice whole-grain bread"),
            ("Lunch", "Vegetables stewed with meat, 1 bowl yogurt, 1 slice bread"),
            ("Snack", "1 bowl Greek yogurt and 1 handful fruit"),
            ("Dinner", "Grilled meatballs (1 palm), 1/2 fist rice, lots of salad"),
        ],
        "movement": ("8,000–10,000 steps", "On days you sit a lot, remember to get up once an hour."),
        "training": workout("B", 4),
        "tip": "Instead of banning a dessert you love, add a small portion of it to your weekly plan. What's planned doesn't cause guilt.",
        "task": "Write a list of 5 easy meals you can repeat every week after the 30 days (e.g. veggie scrambled eggs, chicken stir-fry, lentil soup).",
    },
    {
        "n": 27, "title": "Long-term movement",
        "focus": "You've added walking to your daily life. Today you plan how to keep it up in the long run.",
        "nutrition": "A normal plan day. Before a long activity, have a light snack: fruit and yogurt.",
        "meals": [
            ("Breakfast", "1 bowl Greek yogurt, 1 handful fruit, 1 tablespoon oats"),
            ("Lunch", "Chicken salad (1 palm chicken), 1 slice whole-grain bread"),
            ("Snack", "1 banana and 1 glass of kefir"),
            ("Dinner", "Baked salmon (1 palm), 1 fist rice or bulgur, roasted vegetables"),
        ],
        "movement": ("60 minutes of activity", "A long walk or a new activity you enjoy: cycling, swimming, dancing, hiking."),
        "training": recovery("Active day", "No strength workout today; the long activity is your workout."),
        "tip": "The best kind of movement is the one you enjoy and can do regularly.",
        "task": "Write your movement plan for the next 4 weeks: how many walking days, how many workout days, which day for a long activity.",
    },
    {
        "n": 28, "title": "Long-term training",
        "focus": "The last workout of the plan. Today you compare it with your first workout on day 2 and set your routine for afterwards.",
        "nutrition": "A normal plan day. Include protein in the meal after your workout.",
        "meals": [
            ("Breakfast", "Scrambled eggs with vegetables (2 eggs), 1 matchbox-sized piece of feta, 1 slice whole-grain bread"),
            ("Lunch", "1 bowl white bean or chickpea stew, 1/2 fist rice, tzatziki"),
            ("Snack", "1 glass of kefir and 1 apple"),
            ("Dinner", "Grilled chicken (1 palm), 1 fist roasted potatoes, lots of salad"),
        ],
        "movement": ("8,000–10,000 steps", "At a different time from your workout."),
        "training": workout("A", 4, extra="Rep test: in your last set of squats and push-ups, count your reps with good form. "
                                            "How do they feel compared with day 2?"),
        "tip": "To keep getting stronger, make the exercises a little harder over time: more reps, one more set, a harder version.",
        "task": "Choose 2–3 workout days a week for after the 30 days and put them in your calendar.",
    },
    {
        "n": 29, "title": "Plan your next 4 weeks",
        "focus": "Tomorrow is day 30. Today you plan the next 4 weeks, so you know what to do when the plan ends.",
        "nutrition": "A normal plan day. Write next week's shopping list today.",
        "meals": [
            ("Breakfast", "Oatmeal (40 g / 1/2 cup oats, milk), half a banana, 1 tablespoon hazelnuts"),
            ("Lunch", "Your prepped chicken and grains, lots of salad"),
            ("Snack", "1 boiled egg and 1 clementine"),
            ("Dinner", "1 bowl red lentil stew, 1 bowl yogurt, salad"),
        ],
        "movement": ("30-minute walk", "Followed by 10 minutes of mobility."),
        "training": recovery("Active recovery", MOBILITY_TEXT),
        "tip": "Planning reduces decision fatigue. Knowing in advance what you'll eat and when you'll move makes the day easier.",
        "task": "Fill in the “Next 4 weeks” template (p. {p:devam}).",
    },
]

DAY30 = {
    "title": "DAY 30 – WHAT COMES NEXT?",
    "focus": "The last day of the plan. Today you look back, take your measurements and make your plan for what's next clear.",
    "nutrition": "A normal plan day. Celebrate with your favorite meal from the plan.",
    "meals": [
        ("Breakfast", "2 eggs, 1 matchbox-sized piece of feta, 5 olives, lots of greens, 1–2 slices whole-grain bread"),
        ("Lunch", "1 bowl lentil soup, chicken salad"),
        ("Snack", "1 bowl yogurt and 1 piece of fruit"),
        ("Dinner", "Your favorite meal from the plan, built with the plate method"),
    ],
    "movement": ("30–45-minute easy walk", "Your 30-day celebration walk."),
    "training": "No workout. The plan had 13 workouts; count how many you did and write it down.",
    "task": "Write your Day 30 values in the Progress Tracker (p. {p:ilerleme}) and answer the questions on the next page.",
    "questions": [
        "What did I learn in these 30 days?",
        "Which habits did I build?",
        "What worked well?",
        "What do I want to keep doing?",
        "What do I need to improve?",
    ],
}

WEEK_REVIEWS = {
    1: "The first week is usually the hardest, because everything is new. Every day you complete is a step.",
    2: "Don't worry if the number on the scale hasn't changed as much as you hoped. Look at your waist, your energy and your sleep too.",
    3: "You have a routine now. The final phase is about making that routine stick.",
}

WEEK_HABITS = ["Water (8–10 glasses)", "Protein with every main meal", "Half your plate vegetables", "Movement goal",
               "Workout (on planned days)"]

CONTINUE = {
    "title": "The 30 days are over. But the goal doesn't end here.",
    "lead": "In these 30 days you didn't finish a diet; you built a system. Now it's about keeping that system "
            "and improving it step by step.",
    "rules": [
        ("Keep the foundation.", "Protein with every main meal, half your plate vegetables, 8–10 glasses of water a day."),
        ("Plan your movement.", "Your daily step goal and 1 long activity a week."),
        ("2–3 workouts a week.", "Keep going with the same exercises and make them harder over time."),
        ("1 check-in a week.", "Measurements, energy and sleep. Make a small adjustment if needed."),
        ("The comeback rule.", "If a few days slip, don't start over. Start with your worst-day plan, "
                               "then open any day in Phase 2 and continue from there."),
    ],
    "progression": [
        ("Weeks 5–6", "Workouts A and B: 4 sets. Your step goal: 8,000–10,000."),
        ("Weeks 7–8", "Harder versions: e.g. from knee push-ups to classic push-ups, squats with a backpack."),
    ],
    "template_cols": ["Workout days", "Daily step goal", "My one focus habit", "Shopping / prep day"],
}

CLOSING = {
    "title": "You don't have to be perfect.\nYou just have to keep going.",
    "text": [
        "For 30 days you took a step every day. Some days were easy, some weren't. "
        "What matters is that you keep taking the next step.",
        "At LEAN MODE PRO we believe a simple, doable and sustainable path is the best start. "
        "You can open this guide again whenever you like and restart from any day.",
    ],
    "signoff": "Enjoy the journey.",
}
