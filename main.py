from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return{"message": "Welcome to fitconnect api"}

@app.get("/diet")
def diet():
    diet = [
  {
    "ID": "1",
    "Name": "Apple",
    "image": "https://i.imgur.com/BV8ZfQ6.jpg",
    "Amount": "1",
    "Recipe 1": "Apple Chia Pudding",
    "Recipe 1 Description": "Soak chia seeds in almond milk overnight. Add chopped apples and a dash of cinnamon.",
    "Recipe 2": "Apple & Nut Salad",
    "Recipe 2 Description": "Toss apple slices with walnuts, yogurt, and honey.",
    "Recipe 3": "Apple & Oats Energy Balls",
    "Recipe 3 Description": "Blend apple, oats, peanut butter, and cinnamon."
  },
  {
    "ID": "2",
    "Name": "Banana",
    "image": "https://i.imgur.com/xjDCBVS.jpg",
    "Amount": "1",
    "Recipe 1": "Banana Almond Smoothie",
    "Recipe 1 Description": "Blend banana with almond milk, flaxseeds, and dates.",
    "Recipe 2": "Banana Protein Pancakes",
    "Recipe 2 Description": "Mash banana, mix with oats and curd, and cook on a low flame.",
    "Recipe 3": "Banana Peanut Butter Bites",
    "Recipe 3 Description": "Slice banana, top with peanut butter, and freeze."
  },
  {
    "ID": "3",
    "Name": "Oranges",
    "image": "https://i.imgur.com/idkOIO9.jpg",
    "Amount": "1",
    "Recipe 1": "Orange & Carrot Juice",
    "Recipe 1 Description": "Blend fresh orange juice with carrot and ginger.",
    "Recipe 2": "Citrus Salad",
    "Recipe 2 Description": "Mix oranges with spinach, nuts, and a light olive oil dressing.",
    "Recipe 3": "Orange Chia Drink",
    "Recipe 3 Description": "Add chia seeds to fresh orange juice and let it soak."
  },
  {
    "ID": "4",
    "Name": "Carrots",
    "image": "https://i.imgur.com/BXDMquH.jpg",
    "Amount": "100g",
    "Recipe 1": "Carrot & Moong Dal Soup",
    "Recipe 1 Description": "Boil carrots with moong dal and blend for a protein-rich soup.",
    "Recipe 2": "Steamed Carrot Sticks",
    "Recipe 2 Description": "Steam carrot sticks and sprinkle black salt and lemon.",
    "Recipe 3": "Carrot & Curd Dip",
    "Recipe 3 Description": "Grate carrots and mix with yogurt for a healthy dip."
  },
  {
    "ID": "5",
    "Name": "Green Beans",
    "image": "https://i.imgur.com/XmhZ9Z0.jpg",
    "Amount": "100g",
    "Recipe 1": "Stir-Fried Green Beans with Sesame",
    "Recipe 1 Description": "Cook beans with garlic, sesame seeds, and a drizzle of olive oil.",
    "Recipe 2": "Steamed Beans & Chickpeas Salad",
    "Recipe 2 Description": "Mix steamed beans with boiled chickpeas and lemon.",
    "Recipe 3": "Green Beans & Quinoa Stir-Fry",
    "Recipe 3 Description": "Toss beans with cooked quinoa and turmeric."
  },
  {
    "ID": "6",
    "Name": "Broccoli",
    "image": "https://i.imgur.com/3dbJfw6.jpg",
    "Amount": "100g",
    "Recipe 1": "Broccoli & Almond Soup",
    "Recipe 1 Description": "Blend steamed broccoli with almonds and black pepper.",
    "Recipe 2": "Broccoli Stir Fry",
    "Recipe 2 Description": "Stir-fry with garlic, ginger, and coconut oil.",
    "Recipe 3": "Broccoli & Paneer Bowl",
    "Recipe 3 Description": "Sauté paneer cubes with steamed broccoli and mild spices."
  },
  {
    "ID": "7",
    "Name": "Spinach",
    "image": "https://i.imgur.com/x3fKCoS.jpg",
    "Amount": "100g",
    "Recipe 1": "Spinach & Chickpea Salad",
    "Recipe 1 Description": "Mix fresh spinach with chickpeas, olive oil, and lemon juice.",
    "Recipe 2": "Spinach Smoothie",
    "Recipe 2 Description": "Blend spinach with banana, yogurt, and flaxseeds.",
    "Recipe 3": "Garlic Spinach Stir-Fry",
    "Recipe 3 Description": "Sauté spinach with garlic and olive oil."
  },
 {
    "ID": "8",
    "Name": "Sweet Potato",
    "image": "https://i.imgur.com/HKA9vSE.jpg",
    "Amount": "150g",
    "Recipe 1": "Baked Sweet Potato Fries",
    "Recipe 1 Description": "Cut sweet potatoes into fries, toss with olive oil and bake.",
    "Recipe 2": "Sweet Potato Mash",
    "Recipe 2 Description": "Boil and mash sweet potatoes with black pepper and a dash of ghee.",
    "Recipe 3": "Sweet Potato & Chickpea Salad",
    "Recipe 3 Description": "Roast sweet potatoes and mix with chickpeas and lemon dressing."
  },
  {
    "ID": "9",
    "Name": "Rajma (Kidney Beans)",
    "image": "https://i.imgur.com/PjQ1Ah0.jpg",
    "Amount": "100g",
    "Recipe 1": "Rajma Masala",
    "Recipe 1 Description": "Cook kidney beans with tomatoes, onions, and Indian spices.",
    "Recipe 2": "Rajma Salad",
    "Recipe 2 Description": "Mix boiled kidney beans with cucumber, tomatoes, and lemon dressing.",
    "Recipe 3": "Rajma Soup",
    "Recipe 3 Description": "Blend cooked kidney beans into a thick soup with garlic and pepper."
  },
  {
    "ID": "10",
    "Name": "Brown Rice",
    "image": "https://i.imgur.com/1a3VKqv.jpg",
    "Amount": "100g",
    "Recipe 1": "Brown Rice & Vegetable Stir-Fry",
    "Recipe 1 Description": "Cook brown rice with sautéed vegetables and soy sauce.",
    "Recipe 2": "Brown Rice & Lentil Khichdi",
    "Recipe 2 Description": "Cook brown rice with lentils, turmeric, and cumin for a healthy dish.",
    "Recipe 3": "Brown Rice Pulao",
    "Recipe 3 Description": "Sauté brown rice with spices and mixed vegetables."
  },
  {
    "ID": "11",
    "Name": "Quinoa",
    "image": "https://i.imgur.com/cZDR56M.jpg",
    "Amount": "75g",
    "Recipe 1": "Quinoa Upma",
    "Recipe 1 Description": "Cook quinoa with onions, tomatoes, and mustard seeds.",
    "Recipe 2": "Quinoa & Black Bean Salad",
    "Recipe 2 Description": "Mix quinoa with black beans, bell peppers, and lemon dressing.",
    "Recipe 3": "Quinoa Porridge",
    "Recipe 3 Description": "Cook quinoa with almond milk and cinnamon."
  },
  {
    "ID": "12",
    "Name": "Milk",
    "image": "https://i.imgur.com/m50Nhw5.jpg",
    "Amount": "250ml",
    "Recipe 1": "Milk Smoothie",
    "Recipe 1 Description": "Blend milk with banana, peanut butter, and oats.",
    "Recipe 2": "Masala Milk",
    "Recipe 2 Description": "Boil milk with turmeric, saffron, and almonds.",
    "Recipe 3": "Chocolate Milkshake",
    "Recipe 3 Description": "Blend milk with cocoa powder and honey."
  },
  {
    "ID": "13",
    "Name": "Curd(Yogurt)",
    "image": "https://i.imgur.com/Ju1ZJI4.jpg",
    "Amount": "200g",
    "Recipe 1": "Raita",
    "Recipe 1 Description": "Mix curd with cucumber, cumin, and salt.",
    "Recipe 2": "Yogurt Smoothie",
    "Recipe 2 Description": "Blend curd with banana and honey.",
    "Recipe 3": "Spiced Buttermilk",
    "Recipe 3 Description": "Mix curd, water, salt, and cumin powder."
  },
  {
    "ID": "14",
    "Name": "Oats",
    "image": "https://i.imgur.com/RM0MvyI.jpg",
    "Amount": "50g",
    "Recipe 1": "Oats Porridge",
    "Recipe 1 Description": "Cook with milk and add fruits.",
    "Recipe 2": "Oats Chilla", 
    "Recipe 2 Description": "Make a batter with oats, curd, and veggies, then cook like pancakes.",
    "Recipe 3": "Oats Smoothie",
    "Recipe 3 Description": "Blend oats, banana, and yogurt."
  },
  {
    "ID": "15",
    "Name": "Paneer(Cottage Cheeze)",
    "image": "https://i.imgur.com/eB1Qh3i.png",
    "Amount": "150g",
    "Recipe 1": "Paneer Bhurji",
    "Recipe 1 Description": "Scramble paneer with onion and spices.",
    "Recipe 2": "Paneer Tikka",
    "Recipe 2 Description": "Marinate and grill paneer.",
    "Recipe 3": "Palak Paneer",
    "Recipe 3 Description": "Cook paneer with spinach gravy."
  },
  {
    "ID": "16",
    "Name": "Roti(Whole Wheat)",
    "image": "https://i.imgur.com/BqDMmMc.jpg",
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
    "id": "1",
    "exercise": "Wide Push-Ups",
    "gif": "https://i.imgur.com/uhZ7dP8.gifv",
    "description": "A variation of the standard push-up that targets the chest muscles more intensely by widening the hand placement.",
    "reps/time": "3 sets of 12 reps"
  },
  {
    "id": "2",
    "exercise": "Diamond Push-Ups",
    "gif": "https://i.imgur.com/CjMZ59T.gifv",
    "description": "A push-up variation where hands are placed close together to form a diamond shape, focusing on triceps and inner chest.",
    "reps/time": "3 sets of 12 reps"
  },
 {
    "id": "3",
    "exercise": "Knee Push-Ups",
    "gif": "https://i.imgur.com/41vniIo.gifv",
    "description": "A beginner-friendly push-up performed on the knees instead of toes, reducing difficulty while strengthening the upper body.",
    "reps/time": "3 sets of 12 reps"
  },
  {
    "id": "4",
    "exercise": "Incline Push-Ups",
    "gif": "https://i.imgur.com/SUJVScC.gifv",
    "description": "A push-up performed with hands elevated on a surface like a bench, reducing difficulty and focusing on lower chest.",
    "reps/time": "3 sets of 12 reps"
  },
  {
    "id": "5",
    "exercise": "Decline Push-Ups",
    "gif": "https://i.imgur.com/CIZxzpI.gifv",
    "description": "A push-up with feet elevated, increasing difficulty and focusing more on the upper chest and shoulders.",
    "reps/time": "3 sets of 12 reps"
  },
  {
    "id": "6",
    "exercise": "Push-Ups",
    "gif": "https://i.imgur.com/UgeB6NM.gifv",
    "description": "A fundamental bodyweight exercise targeting the chest, shoulders, and triceps while engaging the core.",
    "reps/time": "3 sets of 12 reps"
  },
  {
    "id": "7",
    "exercise": "Jump Squats",
    "gif": "https://i.imgur.com/QejUY5f.gifv",
    "description": "An explosive squat variation where you jump at the top, improving leg strength and cardiovascular endurance.",
    "reps/time": "3 sets of 12 reps"
  },
  {
    "id": "8",
    "exercise": "Bulgarian Split Squats",
    "gif": "https://i.imgur.com/K3UgQOs.gifv",
    "description": "A single-leg squat performed with one foot elevated behind, targeting the quadriceps, glutes, and balance.",
    "reps/time": "3 sets of 12 reps"
  },
  {
    "id": "9",
    "exercise": "Squats",
    "gif": "https://i.imgur.com/e1nVVzK.gifv",
    "description": "A fundamental lower-body exercise targeting the quadriceps, hamstrings, and glutes.",
    "reps/time": "3 sets of 12 reps"
  },
  {
    "id": "10",
    "exercise": "Pistol Squats",
    "gif": "https://i.imgur.com/Fx93V3K.gifv",
    "description": "A challenging single-leg squat that enhances strength, balance, and flexibility.",
    "reps/time": "3 sets of 12 reps"
  },
  {
    "id": "11",
    "exercise": "Single-Leg Glute Bridges",
    "description": "A hip bridge performed on one leg, targeting the glutes and hamstrings while improving stability.",
    "gif": "https://i.imgur.com/AzrUaXu.gifv",
    "reps/time": "3 sets of 12 reps"
  },
  {
    "id": "12",
    "exercise": "Reverse Lunges",
    "gif": "https://i.imgur.com/nxkXCud.gifv",
    "description": "A lunge variation stepping backward, reducing knee strain while strengthening the legs and glutes.",
    "reps/time": "3 sets of 12 reps"
  },
  {
    "id": "13",
    "exercise": "Walking Lunges",
    "gif": "https://i.imgur.com/upeqb5q.gifv",
    "description": "A dynamic lunge exercise performed while moving forward, engaging the legs and improving coordination.",
    "reps/time": "45 sec"
  },
  {
    "id": "14",
    "exercise": "Lunges",
    "gif": "https://i.imgur.com/A59eQrh.gifv",
    "description": "A lower-body exercise where one leg steps forward and bends at the knee, strengthening the quadriceps and glutes.",
    "reps/time": "3 sets of 12 reps"
  },
  {
    "id": "15",
    "exercise": "Jumping Lunges",
    "gif": "https://i.imgur.com/nxkXCud.gifv",
    "description": "An explosive lunge variation involving jumps between each rep, enhancing leg power and cardiovascular fitness.",
    "reps/time": "3 sets of 12 reps"
  },
  {
    "id": "16",
    "exercise": "Mountain Climbers",
    "gif": "https://i.imgur.com/sJb8aq9.gifv",
    "description": "A full-body cardio exercise mimicking a climbing motion, engaging the core, shoulders, and legs.",
    "reps/time": "45 sec"
  },
  {
    "id": "17",
    "exercise": "Cross-Body Mountain Climbers",
    "gif": "https://i.imgur.com/YfakbN3.gifv",
    "description": "A variation of mountain climbers where knees are brought diagonally towards the opposite elbow, engaging obliques.",
    "reps/time": "45 sec"
  },
  {
    "id": "18",
    "exercise": "Skaters",
    "gif": "https://i.imgur.com/HIvG1bi.gifv",
    "description": "A lateral jumping exercise mimicking a skating motion, improving agility and lower-body strength.",
    "reps/time": "45 sec"
  },
  {
    "id": "19",
    "exercise": "Burpees",
    "gif": "https://i.imgur.com/RQCGsV1.gifv",
    "description": "A full-body exercise combining a squat, push-up, and jump to build strength and endurance.",
    "reps/time": "45 sec"
  },
  {
    "id": "20",
    "exercise": "High Knees",
    "gif": "https://i.imgur.com/crImGbi.gifv",
    "description": " A cardio exercise involving rapid knee lifts, improving speed, endurance, and coordination.",
    "reps/time": "45 sec"
  },
  {
    "id": "21",
    "exercise": "Jumping Jacks",
    "gif":"https://i.imgur.com/dkHYyyp.gifv",
    "description": " A classic cardio movement where arms and legs move outward and inward rhythmically.",
    "reps/time": "45 sec"
  },
  {
    "id": "22",
    "exercise": "Butt Kicks",
    "gif": "https://i.imgur.com/qNgad00.gifv",
    "description": " A cardio drill where heels are kicked towards the glutes, engaging hamstrings and improving endurance.",
    "reps/time": "45 sec"
  },
  {
    "id": "23",
    "exercise": "Shadow Boxing",
    "gif": "https://i.imgur.com/B1jUYRp.gifv",
    "description": "A cardiovascular exercise mimicking boxing movements to enhance agility and endurance.",
    "reps/time": "45 sec"
  },
  {
    "id": "24",
    "exercise": "Russian Twists",
    "gif": "https://i.imgur.com/h9uZcWm.gifv",
    "description": "A core exercise where you twist the torso while seated, targeting obliques and improving rotational strength.",
    "reps/time": "30 sec per side"
  },
  {
    "id": "25",
    "exercise": "Leg Raises",
    "gif": "https://i.imgur.com/eeV3xTK.gifv",
    "description": "An abdominal exercise where legs are lifted while lying down, strengthening the lower abs.",
    "reps/time": "30 sec per side"
  },
  {
    "id": "26",
    "exercise": "Plank",
    "gif": "https://i.imgur.com/BBpWDOu.gifv",
    "description": "A core-strengthening exercise where you hold your body in a straight line, supported by your forearms and toes. Improves core stability and endurance.",
    "reps/time": "30 sec per side"
  },
  {
    "id": "27",
    "exercise": "Side Plank",
    "gif": "https://i.imgur.com/RPenBYW.jpg",
    "description": "A variation of the plank where you balance on one forearm and the side of your foot, engaging the obliques and core.",
    "reps/time": "30 sec per side"
  },
  {
    "id": "28",
    "exercise": "Reverse Plank",
    "gif": "https://i.imgur.com/XbQKaE2.jpg",
    "description": "A back-strengthening exercise where you hold a straight-body position while supporting yourself with your hands behind you. Targets the core and glutes.",
    "reps/time": "30 sec per side"
  },
  {
    "id": "29",
    "exercise": "Bicycle Crunches",
    "gif": "https://i.imgur.com/uPEIAIy.gifv",
    "description": "A dynamic ab exercise where you alternate bringing your elbow to the opposite knee while performing a cycling motion with your legs.",
    "reps/time": "30 sec per side"
  },
  {
    "id": "30",
    "exercise": "Flutter Kicks",
    "gif": "https://i.imgur.com/iuUqh7y.gifv",
    "description": "A core exercise where you lie on your back and alternate kicking your legs up and down while keeping them straight.",
    "reps/time": "30 sec per side"
  },
  {
    "id": "31",
    "exercise": "Heel Taps",
    "gif": "https://i.imgur.com/8Bto719.gifv",
    "description": "A side abdominal exercise where you lie on your back and tap your heels alternately by engaging the obliques.",
    "reps/time": "30 sec per side"
  },
  {
    "id": "32",
    "exercise": "Toe Touches",
    "gif": "https://i.imgur.com/7V8bUp7.gifv",
    "description": "An abdominal move where you lie on your back and reach for your toes, engaging your upper abs.",
    "reps/time": "30 sec per side"
  },
  {
    "id": "33",
    "exercise": "Plank Shoulder Taps",
    "gif": "https://i.imgur.com/vTZI8M6.gifv",
    "description": "A variation of the plank where you alternate tapping your opposite shoulder while maintaining stability in your core.",
    "reps/time": "30 sec per side"
  },
  {
    "id": "34",
    "exercise": "Glute Bridges",
    "gif": "https://i.imgur.com/VFL5KL5.gifv",
    "description": "A lower-body exercise where you lie on your back, push through your heels, and lift your hips, targeting the glutes and hamstrings.",
    "reps/time": "3 sets of 12 reps"
  },
  {
    "id": "35",
    "exercise": "Hip Thrusts",
    "gif": "https://i.imgur.com/OSmKgB9.gifv",
    "description": "A glute-focused exercise where you rest your upper back on a bench and thrust your hips upward while engaging your glutes.",
    "reps/time": "3 sets of 12 reps"
  },
  {
    "id": "36",
    "exercise": "Fire Hydrants",
    "gif": "https://i.imgur.com/l593ebU.gifv",
    "description": "A lower-body move where you lift your knee outward from a tabletop position, targeting the glutes and hip mobility.",
    "reps/time": "3 sets of 12 reps"
  },
  {
    "id": "37",
    "exercise": "Donkey Kicks",
    "gif": "https://i.imgur.com/VchU7Xm.gifv",
    "description": "A glute exercise where you kick one leg backward while keeping your knee bent, working on glute activation.",
    "reps/time": "3 sets of 12 reps"
  },
  {
    "id": "38",
    "exercise": "Wall Sit",
    "gif": "https://i.imgur.com/PVMwKIx.gifv",
    "description": "A lower-body endurance exercise where you hold a squat position with your back against a wall.",
    "reps/time": "3 sets of 12 reps"
  },
  {
    "id": "39",
    "exercise": "Step-Ups",
    "gif": "https://i.imgur.com/UJrWYHQ.gifv",
    "description": "A functional movement where you step onto an elevated surface, engaging your legs and glutes.",
    "reps/time": "3 sets of 12 reps"
  },
  {
    "id": "40",
    "exercise": "Tricep Dips",
    "gif": "https://i.imgur.com/qzI4WNa.gifv",
    "description": "An upper-body exercise where you lower and raise your body using a chair or bench, targeting the triceps.",
    "reps/time": "3 sets of 12 reps"
  },
 {
    "id": "41",
    "exercise": "Superman Exercise",
    "gif": "https://i.imgur.com/FYkGvbX.gifv",
    "description": "A back-strengthening move where you lie on your stomach and lift your arms and legs simultaneously to engage the lower back.",
    "reps/time": "30 sec per side"
  },
  {
    "id": "42",
    "exercise": "Bird Dog",
    "gif": "https://i.imgur.com/9HbeU0D.gifv",
    "description": "A core and balance exercise where you extend one arm and the opposite leg while maintaining stability in a tabletop position.",
    "reps/time": "30 sec per side"
  }
    ]
    return{"exercise": exercise}