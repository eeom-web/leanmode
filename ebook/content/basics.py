"""Front matter and reference pages of the e-book (English copy, US spelling, metric with US units)."""

TITLE = "THE 30-DAY WEIGHT LOSS PLAN"

HOW_TO_USE = [
    ("Open the day's page every morning.",
     "Each day is a single page you can read in a few minutes."),
    ("Look at the focus of the day first.",
     "Every day you focus on one thing. The rest will soon feel familiar."),
    ("Follow the nutrition tips.",
     "The meals are examples. Swap them for something similar whenever you like."),
    ("Hit your movement goal.",
     "On training days, do the workout too. The exercises are explained on p. {p:egzersiz}."),
    ("Do the task of the day.", "One small step that belongs to that day."),
    ("Tick the boxes in the evening.",
     "Every box you tick makes your progress visible."),
]

MISSED_DAY = ("If you miss a day, don't start over. Just pick up where you left off. "
              "30 days doesn't mean 30 perfect days in a row.")

DISCLAIMER = (
    "This guide is for general information only and does not replace medical advice, diagnosis or treatment. "
    "If you have a chronic condition, take medication regularly, are pregnant or breastfeeding, or have a "
    "history of eating disorders, talk to your doctor or a registered dietitian before changing how you eat "
    "or exercise. Stop right away if you feel pain, dizziness, chest pain or shortness of breath during "
    "exercise. Results vary from person to person."
)

INTRO = {
    "title": "Why a 30-day plan?",
    "paragraphs": [
        "There is so much information about losing weight that a lack of knowledge is rarely the problem. "
        "The hard part is knowing where to start and what to do today. A new diet one day, another rule "
        "the next... After a while it's easy to get tired and give up.",
        "This plan takes a different approach:",
    ],
    "points": [
        ("No new diet every day.", "Just familiar foods you can easily find at the grocery store."),
        ("You don't change everything at once.", "You add one small step each day."),
        ("You don't have to be perfect.", "Following most of the plan is enough."),
    ],
    "closing": (
        "At the end of the 30 days, the goal isn't to finish a temporary diet. It's to have built a routine "
        "for eating, moving and training that works for you."
    ),
    "expectation": (
        "Everyone starts from a different place, with a different body and a different daily life, so "
        "results vary too. Your weight can fluctuate, especially in the first days, because of water and "
        "digestion. This plan isn't about a quick change. It's about a start you can keep up."
    ),
}

BASICS = [
    ("Calorie deficit",
     "Your body uses energy all day long. Losing weight comes down to taking in a little less energy than "
     "you use, over a period of time. This is called a calorie deficit. The key word is “little”: eating "
     "too little brings tiredness, strong hunger and the urge to quit. You don't have to count calories in "
     "this plan. We aim for a moderate deficit with the plate method, hand portions and more movement.",
     "The plate method, hand portions and a bit more movement every day."),
    ("Protein",
     "Eggs, yogurt, cheese, chicken, fish, meat and legumes are sources of protein. Protein can help you "
     "stay full for longer and helps protect your muscles while you lose weight. Throughout the plan, "
     "every main meal will include a source of protein.",
     "From day 3: one palm of protein with every main meal."),
    ("Fiber",
     "Vegetables, fruit, legumes and whole grains contain fiber. High-fiber foods are filling, support "
     "digestion and help you feel satisfied. A simple goal: half your plate vegetables.",
     "From day 5: half your plate vegetables at lunch and dinner."),
    ("Water",
     "Drinking enough matters for your energy and your overall health, and thirst is sometimes mistaken "
     "for hunger. For most adults, about 8–10 glasses a day (2–2.5 liters, about 70–85 fl oz) is a good "
     "start. You need more in hot weather and when you exercise. If you have to limit fluids for health "
     "reasons, follow your doctor's advice.",
     "From day 2: 8–10 glasses of water a day."),
    ("Daily movement",
     "The steps you take during the day matter as much as your workouts. Walking, taking the stairs, "
     "standing during phone calls... Daily movement increases the energy you use, and for most people "
     "it's the easiest way to start.",
     "A walk every day; the step goal grows step by step."),
    ("Strength training",
     "When you lose weight, you can lose muscle as well as fat. Regular strength training can help you "
     "keep your muscles and get stronger. This plan includes short full-body workouts three times a week "
     "that you can do at home.",
     "3 short workouts a week, 13 workouts in 30 days."),
    ("Sleep and recovery",
     "Too little sleep can affect your appetite, your energy and your motivation. Most adults are advised "
     "to get 7–9 hours of sleep. Rest days are part of the plan too: your muscles recover between "
     "workouts.",
     "At least 1 rest day a week and a sleep routine from day 16."),
]

HABIT_ROADMAP = [
    (1, "Daily movement"), (2, "Water and first workout"), (3, "Protein with every main meal"),
    (5, "Half your plate vegetables"), (6, "The plate method"), (8, "Hand portions"),
    (9, "Watch liquid calories"), (10, "Eat slowly"), (11, "Shopping list"),
    (12, "Prepare ahead"), (15, "The 10-minute rule"), (16, "Sleep routine"),
    (22, "Habit stacking"), (24, "The hunger scale"),
]

NOT_IN_PLAN = [
    "No starving.",
    "No list of forbidden foods.",
    "No eating the same thing for days.",
    "No detoxes, “miracle” teas or “fat-burning” products.",
]

PLATE = {
    "title": "How to build your plate",
    "lead": ("The easiest way to balance your portions without counting calories: the plate method and hand "
             "portions. Your hand is always with you, and it's in proportion to your body."),
    "parts": [
        ("Vegetables", "half your plate"),
        ("Protein", "a quarter of your plate"),
        ("Carbs", "a quarter of your plate"),
        ("Fat", "a small amount"),
    ],
    "hand": [
        ("Protein", "1 palm",
         "100–150 g (3.5–5 oz) cooked chicken, meat or fish · 2–3 eggs · 1 bowl (200 g, about 3/4 cup) yogurt"),
        ("Carbs", "1 fist",
         "3/4 cup cooked rice, quinoa or pasta · 1 medium potato · 1–2 thin slices of whole-grain bread"),
        ("Vegetables", "2 handfuls",
         "Salad, steamed or roasted vegetables, a vegetable stew"),
        ("Fat", "1 thumb",
         "1 tablespoon olive oil · 10–12 almonds · 5–6 olives"),
    ],
    "adjust": (
        "These portions are a starting point. If you're larger, very physically active, or get very hungry "
        "again soon after a meal, increase your protein and carb portions a little. Men and very active "
        "people can often go up to about 1.5–2 times the protein and carb portions."
    ),
    "rhythm": ("Daily rhythm: 3 main meals and 1 snack when you're really hungry. "
               "The snack is optional."),
    "units": "Measures used in this plan: 1 bowl of yogurt: about 200 g (3/4 cup) · 1 glass: about 200 ml (7 fl oz) · "
             "1 matchbox-sized piece of cheese: about 30 g (1 oz)",
}

SHOPPING = [
    ("Protein", ["Eggs", "Chicken breast / thighs", "Turkey", "Lean ground beef", "Fish (salmon, cod, sardines)",
                 "Canned tuna", "Yogurt, kefir", "Greek yogurt or skyr", "Cottage cheese, feta"]),
    ("Carbs", ["Oats", "Rice", "Quinoa or bulgur", "Whole-grain bread / wraps", "Whole-wheat pasta",
               "Potatoes"]),
    ("Legumes", ["Red lentils", "Green lentils", "Chickpeas", "Beans (canned is fine)",
                 "Roasted chickpeas"]),
    ("Vegetables", ["Tomatoes, cucumbers, peppers", "Spinach, lettuce, arugula", "Broccoli, zucchini, carrots",
                    "Onions, garlic", "Frozen mixed vegetables"]),
    ("Fruit", ["Apples, pears", "Bananas", "Oranges / clementines", "Strawberries or blueberries (frozen is fine)"]),
    ("Healthy fats", ["Olive oil", "Olives", "Walnuts, almonds, hazelnuts"]),
    ("Other", ["Hummus", "Lemons", "Spices (chili flakes, cumin, oregano, cinnamon)", "Sparkling water"]),
]

SHOPPING_TIP = ("Frozen vegetables and fruit are just as useful as fresh: practical, long-lasting and "
                "easy to prepare.")

WARMUP = [
    ("Marching in place", "1 minute"),
    ("Arm circles (forward and back)", "10 + 10"),
    ("Hip circles", "10 reps"),
    ("Slow half squats", "10 reps"),
    ("Cat-cow (on all fours)", "8 reps"),
]

MOBILITY = [
    ("Cat-cow", "8 reps", "On all fours, slowly round and then arch your back."),
    ("Hip flexor stretch", "30 sec each side", "One knee on the floor, lean gently forward without arching your lower back."),
    ("Chest opener", "8 reps each side", "Lying on your side, sweep your top arm back in an arc."),
    ("Hamstring stretch", "30 sec each side", "One heel forward, knees slightly bent; hinge forward from the hips."),
    ("Child's pose", "45 sec", "Knees on the floor, sit your hips back toward your heels, arms stretched forward."),
    ("Deep breathing", "1 minute", "Breathe in through your nose for 4 seconds, out through your mouth for 6."),
]

INTERVAL_WALK = ("Brisk walk: Start at a comfortable pace, then alternate 2 minutes brisk and 2 minutes easy. "
                 "On the brisk part you can still talk, but you couldn't sing.")

TRAINING_RULES = [
    "Warm up for 5 minutes before every workout.",
    "Finish every set with 2–3 reps left in the tank.",
    "Good form matters more than the number of reps.",
    "Stop if you feel sharp or increasing pain.",
    "If an exercise feels too hard, choose the easier version. That's not a step back, it's the right start.",
]

EXERCISES = [
    {
        "name": "Squat",
        "how": ["Feet shoulder-width apart, toes turned slightly out.",
                "Push your hips back and down as if sitting on a chair; chest up, knees in line with your toes.",
                "Push through your heels to stand up."],
        "easy": "Sit down on a chair behind you and stand back up.",
        "hard": "Take 3 seconds to lower or wear a backpack.",
    },
    {
        "name": "Reverse lunge",
        "how": ["Stand tall and take a big step back with one foot.",
                "Bend both knees and lower down; your back knee comes close to the floor.",
                "Push through your front heel to return. Reps are per leg."],
        "easy": "Hold on to a wall or chair and go down less.",
        "hard": "Hold a water bottle in each hand.",
    },
    {
        "name": "Push-up",
        "how": ["Hands under your shoulders; a straight line from head to heels.",
                "Lower your chest under control; elbows at about 45 degrees to your body.",
                "Push through your palms to come back up."],
        "easy": "From easy to hard: wall push-up, incline push-up on a table or counter, knee push-up.",
        "hard": "Classic push-up, 3 seconds down.",
    },
    {
        "name": "Row",
        "how": ["Anchor a resistance band securely, or use a backpack with books inside.",
                "With the backpack: knees slightly bent, back flat, lean forward; pull the bag toward your belly.",
                "Squeeze your shoulder blades together, then lower under control."],
        "easy": "Lighter backpack or looser band.",
        "hard": "Heavier backpack; hold for 2 seconds at the top.",
    },
    {
        "name": "Glute bridge",
        "how": ["Lie on your back; knees bent, feet flat on the floor, hip-width apart.",
                "Push through your heels to lift your hips; shoulders to knees in a straight line.",
                "Squeeze your glutes for 1 second at the top, lower slowly."],
        "easy": "Lift your hips less.",
        "hard": "Do it on one leg or hold for 3 seconds at the top.",
    },
    {
        "name": "Plank",
        "how": ["Elbows under your shoulders, forearms on the floor.",
                "Your body is straight from head to heels; hips neither up nor down.",
                "Brace your stomach lightly and keep breathing."],
        "easy": "Knees on the floor or hands on a table.",
        "hard": "Add 10 seconds.",
    },
    {
        "name": "Dead bug",
        "how": ["Lie on your back; arms toward the ceiling, knees bent at 90 degrees in the air.",
                "Keep your lower back close to the floor; slowly extend your right arm and left leg, then return.",
                "Continue with the other side. Reps are per side."],
        "easy": "Move only your legs and tap your heel on the floor.",
        "hard": "Go slower and pause for 2 seconds when extended.",
    },
    {
        "name": "Wall sit",
        "how": ["Lean your back against a wall, feet about one step away from it.",
                "Slide down until your knees are bent to about 90 degrees.",
                "Weight in your heels; hold for the time given."],
        "easy": "Bend your knees less and stay higher.",
        "hard": "Add 10–15 seconds.",
    },
]

PROGRESS_ROWS = ["Weight (kg / lb)", "Waist (cm / in)", "Hips (cm / in)", "Average daily steps",
                 "Workouts this week (number)", "Energy (1–5)", "Sleep (average hours)",
                 "How do my clothes fit?"]
PROGRESS_COLS = ["Day 1", "Day 7", "Day 14", "Day 21", "Day 30"]

MEASURE_HOW = [
    ("Scale", "In the morning, after using the bathroom and before breakfast; always on the same scale."),
    ("Waist", "At belly-button height, without pulling your stomach in or holding your breath."),
    ("Photo (optional)", "Same light, same clothes; from the front and the side."),
]

FLUCTUATION = (
    "A salty dinner, how much you drank, digestion, your hormonal cycle and a hard workout can change the "
    "number on the scale by 1–2 kg (2–4 lb) from one day to the next. That doesn't mean you lost or gained "
    "fat. Look at the trend over the weeks, not at a single weigh-in. Your energy, sleep, strength and how "
    "your clothes fit are part of your progress too."
)

HABITS = [
    ("Movement goal", 1),
    ("Water (8–10 glasses)", 2),
    ("Workout (on planned days)", 2),
    ("Protein with every main meal", 3),
    ("Half your plate vegetables", 5),
    ("Meal plan / prep", 11),
    ("Sleep routine", 16),
]
