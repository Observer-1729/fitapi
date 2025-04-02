from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return{"message": "Welcome to fitconnect api"}

@app.get("/diet")
def diet():
    diet = [
  {
    "ID": 1,
    "Name": "Apple",
    "image": "https://imgur.com/GTPCfWt",
    "Amount": "1",
    "Recipe 1": "Apple Chia Pudding",
    "Recipe 1 Description": "Soak chia seeds in almond milk overnight. Add chopped apples and a dash of cinnamon.",
    "Recipe 2": "Apple & Nut Salad",
    "Recipe 2 Description": "Toss apple slices with walnuts, yogurt, and honey.",
    "Recipe 3": "Apple & Oats Energy Balls",
    "Recipe 3 Description": "Blend apple, oats, peanut butter, and cinnamon."
  },
  {
    "ID": 2,
    "Name": "Banana",
    "image": "https://imgur.com/a/9Q4Ye9r",
    "Amount": "1",
    "Recipe 1": "Banana Almond Smoothie",
    "Recipe 1 Description": "Blend banana with almond milk, flaxseeds, and dates.",
    "Recipe 2": "Banana Protein Pancakes",
    "Recipe 2 Description": "Mash banana, mix with oats and curd, and cook on a low flame.",
    "Recipe 3": "Banana Peanut Butter Bites",
    "Recipe 3 Description": "Slice banana, top with peanut butter, and freeze."
  },
  {
    "ID": 3,
    "Name": "Oranges",
    "image": "https://imgur.com/aDyOlKZ",
    "Amount": "1",
    "Recipe 1": "Orange & Carrot Juice",
    "Recipe 1 Description": "Blend fresh orange juice with carrot and ginger.",
    "Recipe 2": "Citrus Salad",
    "Recipe 2 Description": "Mix oranges with spinach, nuts, and a light olive oil dressing.",
    "Recipe 3": "Orange Chia Drink",
    "Recipe 3 Description": "Add chia seeds to fresh orange juice and let it soak."
  },
  {
    "ID": 4,
    "Name": "Carrots",
    "image": "https://imgur.com/hFlgzrn",
    "Amount": "100g",
    "Recipe 1": "Carrot & Moong Dal Soup",
    "Recipe 1 Description": "Boil carrots with moong dal and blend for a protein-rich soup.",
    "Recipe 2": "Steamed Carrot Sticks",
    "Recipe 2 Description": "Steam carrot sticks and sprinkle black salt and lemon.",
    "Recipe 3": "Carrot & Curd Dip",
    "Recipe 3 Description": "Grate carrots and mix with yogurt for a healthy dip."
  },
  {
    "ID": 5,
    "Name": "Green Beans",
    "image": "https://imgur.com/Rcvsg9Q",
    "Amount": "100g",
    "Recipe 1": "Stir-Fried Green Beans with Sesame",
    "Recipe 1 Description": "Cook beans with garlic, sesame seeds, and a drizzle of olive oil.",
    "Recipe 2": "Steamed Beans & Chickpeas Salad",
    "Recipe 2 Description": "Mix steamed beans with boiled chickpeas and lemon.",
    "Recipe 3": "Green Beans & Quinoa Stir-Fry",
    "Recipe 3 Description": "Toss beans with cooked quinoa and turmeric."
  },
  {
    "ID": 6,
    "Name": "Broccoli",
    "image": "https://imgur.com/PCXqXc9",
    "Amount": "100g",
    "Recipe 1": "Broccoli & Almond Soup",
    "Recipe 1 Description": "Blend steamed broccoli with almonds and black pepper.",
    "Recipe 2": "Broccoli Stir Fry",
    "Recipe 2 Description": "Stir-fry with garlic, ginger, and coconut oil.",
    "Recipe 3": "Broccoli & Paneer Bowl",
    "Recipe 3 Description": "Sauté paneer cubes with steamed broccoli and mild spices."
  },
  {
    "ID": 7,
    "Name": "Spinach",
    "image": "https://imgur.com/ZGeMeEx",
    "Amount": "100g",
    "Recipe 1": "Spinach & Chickpea Salad",
    "Recipe 1 Description": "Mix fresh spinach with chickpeas, olive oil, and lemon juice.",
    "Recipe 2": "Spinach Smoothie",
    "Recipe 2 Description": "Blend spinach with banana, yogurt, and flaxseeds.",
    "Recipe 3": "Garlic Spinach Stir-Fry",
    "Recipe 3 Description": "Sauté spinach with garlic and olive oil."
  },
 {
    "ID": 8,
    "Name": "Sweet Potato",
    "image": "https://imgur.com/EmH2pet",
    "Amount": "150g",
    "Recipe 1": "Baked Sweet Potato Fries",
    "Recipe 1 Description": "Cut sweet potatoes into fries, toss with olive oil and bake.",
    "Recipe 2": "Sweet Potato Mash",
    "Recipe 2 Description": "Boil and mash sweet potatoes with black pepper and a dash of ghee.",
    "Recipe 3": "Sweet Potato & Chickpea Salad",
    "Recipe 3 Description": "Roast sweet potatoes and mix with chickpeas and lemon dressing."
  },
  {
    "ID": 9,
    "Name": "Rajma (Kidney Beans)",
    "image": "https://imgur.com/akxXomK",
    "Amount": "100g",
    "Recipe 1": "Rajma Masala",
    "Recipe 1 Description": "Cook kidney beans with tomatoes, onions, and Indian spices.",
    "Recipe 2": "Rajma Salad",
    "Recipe 2 Description": "Mix boiled kidney beans with cucumber, tomatoes, and lemon dressing.",
    "Recipe 3": "Rajma Soup",
    "Recipe 3 Description": "Blend cooked kidney beans into a thick soup with garlic and pepper."
  },
  {
    "ID": 10,
    "Name": "Brown Rice",
    "image": "https://imgur.com/xK3BJGM",
    "Amount": "100g",
    "Recipe 1": "Brown Rice & Vegetable Stir-Fry",
    "Recipe 1 Description": "Cook brown rice with sautéed vegetables and soy sauce.",
    "Recipe 2": "Brown Rice & Lentil Khichdi",
    "Recipe 2 Description": "Cook brown rice with lentils, turmeric, and cumin for a healthy dish.",
    "Recipe 3": "Brown Rice Pulao",
    "Recipe 3 Description": "Sauté brown rice with spices and mixed vegetables."
  },
  {
    "ID": 11,
    "Name": "Quinoa",
    "image": "https://imgur.com/349edzZ",
    "Amount": "75g",
    "Recipe 1": "Quinoa Upma",
    "Recipe 1 Description": "Cook quinoa with onions, tomatoes, and mustard seeds.",
    "Recipe 2": "Quinoa & Black Bean Salad",
    "Recipe 2 Description": "Mix quinoa with black beans, bell peppers, and lemon dressing.",
    "Recipe 3": "Quinoa Porridge",
    "Recipe 3 Description": "Cook quinoa with almond milk and cinnamon."
  },
  {
    "ID": 12,
    "Name": "Milk",
    "image": "https://imgur.com/bUMt9w6",
    "Amount": "250ml",
    "Recipe 1": "Milk Smoothie",
    "Recipe 1 Description": "Blend milk with banana, peanut butter, and oats.",
    "Recipe 2": "Masala Milk",
    "Recipe 2 Description": "Boil milk with turmeric, saffron, and almonds.",
    "Recipe 3": "Chocolate Milkshake",
    "Recipe 3 Description": "Blend milk with cocoa powder and honey."
  },
  {
    "ID": 13,
    "Name": "Curd(Yogurt)",
    "image": "https://imgur.com/XiyGXxF",
    "Amount": "200g",
    "Recipe 1": "Raita",
    "Recipe 1 Description": "Mix curd with cucumber, cumin, and salt.",
    "Recipe 2": "Yogurt Smoothie",
    "Recipe 2 Description": "Blend curd with banana and honey.",
    "Recipe 3": "Spiced Buttermilk",
    "Recipe 3 Description": "Mix curd, water, salt, and cumin powder."
  },
  {
    "ID": 14,
    "Name": "Oats",
    "image": "https://imgur.com/o98gLA7",
    "Amount": "50g",
    "Recipe 1": "Oats Porridge",
    "Recipe 1 Description": "Cook with milk and add fruits.",
    "Recipe 2": "Oats Chilla", 
    "Recipe 2 Description": "Make a batter with oats, curd, and veggies, then cook like pancakes.",
    "Recipe 3": "Oats Smoothie",
    "Recipe 3 Description": "Blend oats, banana, and yogurt."
  },
  {
    "ID": 15,
    "Name": "Paneer(Cottage Cheeze)",
    "image": "https://imgur.com/a/L1sS1Te",
    "Amount": "150g",
    "Recipe 1": "Paneer Bhurji",
    "Recipe 1 Description": "Scramble paneer with onion and spices.",
    "Recipe 2": "Paneer Tikka",
    "Recipe 2 Description": "Marinate and grill paneer.",
    "Recipe 3": "Palak Paneer",
    "Recipe 3 Description": "Cook paneer with spinach gravy."
  },
  {
    "ID": 16,
    "Name": "Roti(Whole Wheat)",
    "image": "https://imgur.com/Pp46pGH",
    "Amount": "2pcs",
    "Recipe 1": "Roti Pizza",
    "Recipe 1 Description": "Use roti as a base and top with veggies and cheese.",
    "Recipe 2": "Roti Wrap",
    "Recipe 2 Description": "Fill with paneer or rajma.",
    "Recipe 3": "Roti Nachos",
    "Recipe 3 Description": "Cut and bake roti into crispy chips."
  }
    ]

    return {"diet" : diet}

@app.get("/exercise")
def exercise():
    exercise = [
  {
    "id": 1,
    "exercise": "Wide Push-Ups",
    "gif": "https://imgur.com/a/63nUDYf",
    "description": "A variation of the standard push-up that targets the chest muscles more intensely by widening the hand placement.",
    "reps/time": "3 sets of 12 reps"
  },
  {
    "id": 2,
    "exercise": "Diamond Push-Ups",
    "gif": "https://imgur.com/a/0FNpzkx",
    "description": "A push-up variation where hands are placed close together to form a diamond shape, focusing on triceps and inner chest.",
    "reps/time": "3 sets of 12 reps"
  },
 {
    "id": 3,
    "exercise": "Knee Push-Ups",
    "gif": "https://imgur.com/a/VtSmEtO",
    "description": "A beginner-friendly push-up performed on the knees instead of toes, reducing difficulty while strengthening the upper body.",
    "reps/time": "3 sets of 12 reps"
  },
  {
    "id": 4,
    "exercise": "Incline Push-Ups",
    "gif": "https://imgur.com/a/O3udkxj",
    "description": "A push-up performed with hands elevated on a surface like a bench, reducing difficulty and focusing on lower chest.",
    "reps/time": "3 sets of 12 reps"
  },
  {
    "id": 5,
    "exercise": "Decline Push-Ups",
    "gif": "https://imgur.com/a/CyNE1uB",
    "description": "A push-up with feet elevated, increasing difficulty and focusing more on the upper chest and shoulders.",
    "reps/time": "3 sets of 12 reps"
  },
  {
    "id": 6,
    "exercise": "Push-Ups",
    "gif": "https://imgur.com/a/P5eB7C6",
    "description": "A fundamental bodyweight exercise targeting the chest, shoulders, and triceps while engaging the core.",
    "reps/time": "3 sets of 12 reps"
  },
  {
    "id": 7,
    "exercise": "Jump Squats",
    "gif": "https://imgur.com/a/wRs3hoM",
    "description": "An explosive squat variation where you jump at the top, improving leg strength and cardiovascular endurance.",
    "reps/time": "3 sets of 12 reps"
  },
  {
    "id": 8,
    "exercise": "Bulgarian Split Squats",
    "gif": " https://imgur.com/a/dNJ9f8A",
    "description": "A single-leg squat performed with one foot elevated behind, targeting the quadriceps, glutes, and balance.",
    "reps/time": "3 sets of 12 reps"
  },
  {
    "id": 9,
    "exercise": "Squats",
    "gif": "https://imgur.com/a/MJZOjp1",
    "description": "A fundamental lower-body exercise targeting the quadriceps, hamstrings, and glutes.",
    "reps/time": "3 sets of 12 reps"
  },
  {
    "id": 10,
    "exercise": "Pistol Squats",
    "gif": "https://imgur.com/a/2oUnsTL",
    "description": "A challenging single-leg squat that enhances strength, balance, and flexibility.",
    "reps/time": "3 sets of 12 reps"
  },
  {
    "id": 11,
    "exercise": "Single-Leg Glute Bridges",
    "description": "A hip bridge performed on one leg, targeting the glutes and hamstrings while improving stability.",
    "gif": "https://imgur.com/a/F3hdhuA",
    "reps/time": "3 sets of 12 reps"
  },
  {
    "id": 12,
    "exercise": "Reverse Lunges",
    "gif": "https://imgur.com/a/6DOH98k",
    "description": "A lunge variation stepping backward, reducing knee strain while strengthening the legs and glutes.",
    "reps/time": "3 sets of 12 reps"
  },
  {
    "id": 13,
    "exercise": "Walking Lunges",
    "gif": "https://imgur.com/a/2gNllT5",
    "description": "A dynamic lunge exercise performed while moving forward, engaging the legs and improving coordination.",
    "reps/time": "45 sec"
  },
  {
    "id": 14,
    "exercise": "Lunges",
    "gif": "https://imgur.com/a/871tN35",
    "description": "A lower-body exercise where one leg steps forward and bends at the knee, strengthening the quadriceps and glutes.",
    "reps/time": "3 sets of 12 reps"
  },
  {
    "id": 15,
    "exercise": "Jumping Lunges",
    "gif": "https://imgur.com/a/mT0YImX",
    "description": "An explosive lunge variation involving jumps between each rep, enhancing leg power and cardiovascular fitness.",
    "reps/time": "3 sets of 12 reps"
  },
  {
    "id": 16,
    "exercise": "Mountain Climbers",
    "gif": "https://imgur.com/a/7gzT4HV",
    "description": "A full-body cardio exercise mimicking a climbing motion, engaging the core, shoulders, and legs.",
    "reps/time": "45 sec"
  },
  {
    "id": 17,
    "exercise": "Cross-Body Mountain Climbers",
    "gif": "https://imgur.com/a/XLVHZtD",
    "description": "A variation of mountain climbers where knees are brought diagonally towards the opposite elbow, engaging obliques.",
    "reps/time": "45 sec"
  },
  {
    "id": 18,
    "exercise": "Skaters",
    "gif": "https://imgur.com/a/n8nCVzl",
    "description": "A lateral jumping exercise mimicking a skating motion, improving agility and lower-body strength.",
    "reps/time": "45 sec"
  },
  {
    "id": 19,
    "exercise": "Burpees",
    "gif": "https://imgur.com/a/FGvQXsn",
    "description": "A full-body exercise combining a squat, push-up, and jump to build strength and endurance.",
    "reps/time": "45 sec"
  },
  {
    "id": 20,
    "exercise": "High Knees",
    "gif": " https://imgur.com/a/tLgs658",
    "description": " A cardio exercise involving rapid knee lifts, improving speed, endurance, and coordination.",
    "reps/time": "45 sec"
  },
  {
    "id": 21,
    "exercise": "Jumping Jacks",
    "gif":"https://imgur.com/a/Wn2yVCu",
    "description": " A classic cardio movement where arms and legs move outward and inward rhythmically.",
    "reps/time": "45 sec"
  },
  {
    "id": 22,
    "exercise": "Butt Kicks",
    "gif": "https://imgur.com/a/yW4QUfO",
    "description": " A cardio drill where heels are kicked towards the glutes, engaging hamstrings and improving endurance.",
    "reps/time": "45 sec"
  },
  {
    "id": 23,
    "exercise": "Shadow Boxing",
    "gif": "https://imgur.com/a/yHMrmfS",
    "description": "A cardiovascular exercise mimicking boxing movements to enhance agility and endurance.",
    "reps/time": "45 sec"
  },
  {
    "id": 24,
    "exercise": "Russian Twists",
    "gif": " https://imgur.com/a/IFOc0Hw",
    "description": "A core exercise where you twist the torso while seated, targeting obliques and improving rotational strength.",
    "reps/time": "30 sec per side"
  },
  {
    "id": 25,
    "exercise": "Leg Raises",
    "gif": "https://imgur.com/a/yjorjwE",
    "description": "An abdominal exercise where legs are lifted while lying down, strengthening the lower abs.",
    "reps/time": "30 sec per side"
  },
  {
    "id": 26,
    "exercise": "Plank",
    "gif": "https://imgur.com/a/RzqPZSo",
    "description": "A core-strengthening exercise where you hold your body in a straight line, supported by your forearms and toes. Improves core stability and endurance.",
    "reps/time": "30 sec per side"
  },
  {
    "id": 27,
    "exercise": "Side Plank",
    "gif": "https://imgur.com/a/uayNaPE",
    "description": "A variation of the plank where you balance on one forearm and the side of your foot, engaging the obliques and core.",
    "reps/time": "30 sec per side"
  },
  {
    "id": 28,
    "exercise": "Reverse Plank",
    "gif": "https://imgur.com/a/cEuMIP1",
    "description": "A back-strengthening exercise where you hold a straight-body position while supporting yourself with your hands behind you. Targets the core and glutes.",
    "reps/time": "30 sec per side"
  },
  {
    "id": 29,
    "exercise": "Bicycle Crunches",
    "gif": "https://imgur.com/a/wq5sLxX",
    "description": "A dynamic ab exercise where you alternate bringing your elbow to the opposite knee while performing a cycling motion with your legs.",
    "reps/time": "30 sec per side"
  },
  {
    "id": 30,
    "exercise": "Flutter Kicks",
    "gif": "https://imgur.com/a/PGHtWSr",
    "description": "A core exercise where you lie on your back and alternate kicking your legs up and down while keeping them straight.",
    "reps/time": "30 sec per side"
  },
  {
    "id": 31,
    "exercise": "Heel Taps",
    "gif": "https://imgur.com/a/yrouZ7M",
    "description": "A side abdominal exercise where you lie on your back and tap your heels alternately by engaging the obliques.",
    "reps/time": "30 sec per side"
  },
  {
    "id": 32,
    "exercise": "Toe Touches",
    "gif": "https://imgur.com/a/cKCLDUH",
    "description": "An abdominal move where you lie on your back and reach for your toes, engaging your upper abs.",
    "reps/time": "30 sec per side"
  },
  {
    "id": 33,
    "exercise": "Plank Shoulder Taps",
    "gif": "https://imgur.com/a/LbzDR5m",
    "description": "A variation of the plank where you alternate tapping your opposite shoulder while maintaining stability in your core.",
    "reps/time": "30 sec per side"
  },
  {
    "id": 34,
    "exercise": "Glute Bridges",
    "gif": "https://imgur.com/a/qZBdUkR",
    "description": "A lower-body exercise where you lie on your back, push through your heels, and lift your hips, targeting the glutes and hamstrings.",
    "reps/time": "3 sets of 12 reps"
  },
  {
    "id": 35,
    "exercise": "Hip Thrusts",
    "gif": "https://imgur.com/a/L4V1hmF",
    "description": "A glute-focused exercise where you rest your upper back on a bench and thrust your hips upward while engaging your glutes.",
    "reps/time": "3 sets of 12 reps"
  },
  {
    "id": 36,
    "exercise": "Fire Hydrants",
    "gif": "https://imgur.com/a/j1RRclU",
    "description": "A lower-body move where you lift your knee outward from a tabletop position, targeting the glutes and hip mobility.",
    "reps/time": "3 sets of 12 reps"
  },
  {
    "id": 37,
    "exercise": "Donkey Kicks",
    "gif": "https://imgur.com/a/mYZiQsM",
    "description": "A glute exercise where you kick one leg backward while keeping your knee bent, working on glute activation.",
    "reps/time": "3 sets of 12 reps"
  },
  {
    "id": 38,
    "exercise": "Wall Sit",
    "gif": "https://imgur.com/a/FF9MlBP",
    "description": "A lower-body endurance exercise where you hold a squat position with your back against a wall.",
    "reps/time": "3 sets of 12 reps"
  },
  {
    "id": 39,
    "exercise": "Step-Ups",
    "gif": "https://imgur.com/a/B5Ai8r8",
    "description": "A functional movement where you step onto an elevated surface, engaging your legs and glutes.",
    "reps/time": "3 sets of 12 reps"
  },
  {
    "id": 40,
    "exercise": "Tricep Dips",
    "gif": "https://imgur.com/a/Q142TcD",
    "description": "An upper-body exercise where you lower and raise your body using a chair or bench, targeting the triceps.",
    "reps/time": "3 sets of 12 reps"
  },
 {
    "id": 41,
    "exercise": "Superman Exercise",
    "gif": "https://imgur.com/a/nUmQ8jo",
    "description": "A back-strengthening move where you lie on your stomach and lift your arms and legs simultaneously to engage the lower back.",
    "reps/time": "30 sec per side"
  },
  {
    "id": 42,
    "exercise": "Bird Dog",
    "gif": "https://imgur.com/a/rrGeUQb",
    "description": "A core and balance exercise where you extend one arm and the opposite leg while maintaining stability in a tabletop position.",
    "reps/time": "30 sec per side"
  }
    ]
    return{"exercise": exercise}