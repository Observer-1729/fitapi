def getExercise():
  exercise = [
    {
      "id": "1",
      "exercise": "Wide Push-Ups",
      "gif": "https://i.imgur.com/uhZ7dP8.gif",
      "description": "A variation of the standard push-up that targets the chest muscles more intensely by widening the hand placement.",
      "reps/time": "3 sets of 12 reps"
    },
    {
      "id": "2",
      "exercise": "Diamond Push-Ups",
      "gif": "https://i.imgur.com/CjMZ59T.gif",
      "description": "A push-up variation where hands are placed close together to form a diamond shape, focusing on triceps and inner chest.",
      "reps/time": "3 sets of 12 reps"
    },
    {
      "id": "3",
      "exercise": "Knee Push-Ups",
      "gif": "https://i.imgur.com/41vniIo.gif",
      "description": "A beginner-friendly push-up performed on the knees instead of toes, reducing difficulty while strengthening the upper body.",
      "reps/time": "3 sets of 12 reps"
    },
    {
      "id": "4",
      "exercise": "Incline Push-Ups",
      "gif": "https://i.imgur.com/SUJVScC.gif",
      "description": "A push-up performed with hands elevated on a surface like a bench, reducing difficulty and focusing on lower chest.",
      "reps/time": "3 sets of 12 reps"
    },
    {
      "id": "5",
      "exercise": "Decline Push-Ups",
      "gif": "https://i.imgur.com/CIZxzpI.gif",
      "description": "A push-up with feet elevated, increasing difficulty and focusing more on the upper chest and shoulders.",
      "reps/time": "3 sets of 12 reps"
    },
    {
      "id": "6",
      "exercise": "Push-Ups",
      "gif": "https://i.imgur.com/UgeB6NM.gif",
      "description": "A fundamental bodyweight exercise targeting the chest, shoulders, and triceps while engaging the core.",
      "reps/time": "3 sets of 12 reps"
    },
    {
      "id": "7",
      "exercise": "Jump Squats",
      "gif": "https://i.imgur.com/QejUY5f.gif",
      "description": "An explosive squat variation where you jump at the top, improving leg strength and cardiovascular endurance.",
      "reps/time": "3 sets of 12 reps"
    },
    {
      "id": "8",
      "exercise": "Bulgarian Split Squats",
      "gif": "https://i.imgur.com/K3UgQOs.gif",
      "description": "A single-leg squat performed with one foot elevated behind, targeting the quadriceps, glutes, and balance.",
      "reps/time": "3 sets of 12 reps"
    },
    {
      "id": "9",
      "exercise": "Squats",
      "gif": "https://i.imgur.com/e1nVVzK.gif",
      "description": "A fundamental lower-body exercise targeting the quadriceps, hamstrings, and glutes.",
      "reps/time": "3 sets of 12 reps"
    },
    {
      "id": "10",
      "exercise": "Pistol Squats",
      "gif": "https://i.imgur.com/Fx93V3K.gif",
      "description": "A challenging single-leg squat that enhances strength, balance, and flexibility.",
      "reps/time": "3 sets of 12 reps"
    },
    {
      "id": "11",
      "exercise": "Single-Leg Glute Bridges",
      "gif": "https://i.imgur.com/AzrUaXu.gif",
      "description": "A hip bridge performed on one leg, targeting the glutes and hamstrings while improving stability.",
      "reps/time": "3 sets of 12 reps"
    },
    {
      "id": "12",
      "exercise": "Reverse Lunges",
      "gif": "https://i.imgur.com/nxkXCud.gif",
      "description": "A lunge variation stepping backward, reducing knee strain while strengthening the legs and glutes.",
      "reps/time": "3 sets of 12 reps"
    },
    {
      "id": "13",
      "exercise": "Walking Lunges",
      "gif": "https://i.imgur.com/upeqb5q.gif",
      "description": "A dynamic lunge exercise performed while moving forward, engaging the legs and improving coordination.",
      "reps/time": "45 sec"
    },
    {
      "id": "14",
      "exercise": "Lunges",
      "gif": "https://i.imgur.com/A59eQrh.gif",
      "description": "A lower-body exercise where one leg steps forward and bends at the knee, strengthening the quadriceps and glutes.",
      "reps/time": "3 sets of 12 reps"
    },
    {
      "id": "15",
      "exercise": "Jumping Lunges",
      "gif": "https://i.imgur.com/nxkXCud.gif",
      "description": "An explosive lunge variation involving jumps between each rep, enhancing leg power and cardiovascular fitness.",
      "reps/time": "3 sets of 12 reps"
    },
    {
      "id": "16",
      "exercise": "Mountain Climbers",
      "gif": "https://i.imgur.com/sJb8aq9.gif",
      "description": "A full-body cardio exercise mimicking a climbing motion, engaging the core, shoulders, and legs.",
      "reps/time": "45 sec"
    },
    {
      "id": "17",
      "exercise": "Cross-Body Mountain Climbers",
      "gif": "https://i.imgur.com/YfakbN3.gif",
      "description": "A variation of mountain climbers where knees are brought diagonally towards the opposite elbow, engaging obliques.",
      "reps/time": "45 sec"
    },
    {
      "id": "18",
      "exercise": "Skaters",
      "gif": "https://i.imgur.com/HIvG1bi.gif",
      "description": "A lateral jumping exercise mimicking a skating motion, improving agility and lower-body strength.",
      "reps/time": "45 sec"
    },
    {
      "id": "19",
      "exercise": "Burpees",
      "gif": "https://i.imgur.com/RQCGsV1.gif",
      "description": "A full-body exercise combining a squat, push-up, and jump to build strength and endurance.",
      "reps/time": "45 sec"
    },
    {
      "id": "20",
      "exercise": "High Knees",
      "gif": "https://i.imgur.com/crImGbi.gif",
      "description": "A cardio exercise involving rapid knee lifts, improving speed, endurance, and coordination.",
      "reps/time": "45 sec"
    },
    {
      "id": "21",
      "exercise": "Jumping Jacks",
      "gif": "https://i.imgur.com/dkHYyyp.gif",
      "description": "A classic cardio movement where arms and legs move outward and inward rhythmically.",
      "reps/time": "45 sec"
    },
    {
      "id": "22",
      "exercise": "Butt Kicks",
      "gif": "https://i.imgur.com/qNgad00.gif",
      "description": "A cardio drill where heels are kicked towards the glutes, engaging hamstrings and improving endurance.",
      "reps/time": "45 sec"
    },
    {
      "id": "23",
      "exercise": "Shadow Boxing",
      "gif": "https://i.imgur.com/B1jUYRp.gif",
      "description": "A cardiovascular exercise mimicking boxing movements to enhance agility and endurance.",
      "reps/time": "45 sec"
    },
    {
      "id": "24",
      "exercise": "Russian Twists",
      "gif": "https://i.imgur.com/h9uZcWm.gif",
      "description": "A core exercise where you twist the torso while seated, targeting obliques and improving rotational strength.",
      "reps/time": "30 sec per side"
    },
    {
      "id": "25",
      "exercise": "Leg Raises",
      "gif": "https://i.imgur.com/eeV3xTK.gif",
      "description": "An abdominal exercise where legs are lifted while lying down, strengthening the lower abs.",
      "reps/time": "30 sec per side"
    },
    {
      "id": "26",
      "exercise": "Plank",
      "gif": "https://i.imgur.com/BBpWDOu.gif",
      "description": "A core-strengthening exercise where you hold your body in a straight line, supported by your forearms and toes. Improves core stability and endurance.",
      "reps/time": "30 sec per side"
    },
    {
      "id": "27",
      "exercise": "Side Plank",
      "gif": "https://i.imgur.com/ihYbgyh.gif",
      "description": "A variation of the plank where you balance on one forearm and the side of your foot, engaging the obliques and core.",
      "reps/time": "30 sec per side"
    },
    {
      "id": "28",
      "exercise": "Reverse Plank",
      "gif": "https://i.imgur.com/GOXKHEo.gif",
      "description": "A back-strengthening exercise where you hold a straight-body position while supporting yourself with your hands behind you. Targets the core and glutes.",
      "reps/time": "30 sec per side"
    },
    {
      "id": "29",
      "exercise": "Bicycle Crunches",
      "gif": "https://i.imgur.com/uPEIAIy.gif",
      "description": "A dynamic ab exercise where you alternate bringing your elbow to the opposite knee while performing a cycling motion with your legs.",
      "reps/time": "30 sec per side"
    },
    {
      "id": "30",
      "exercise": "Flutter Kicks",
      "gif": "https://i.imgur.com/iuUqh7y.gif",
      "description": "A core exercise where you lie on your back and alternate kicking your legs up and down while keeping them straight.",
      "reps/time": "30 sec per side"
    },
    {
      "id": "31",
      "exercise": "Heel Taps",
      "gif": "https://i.imgur.com/8Bto719.gif",
      "description": "A side abdominal exercise where you lie on your back and tap your heels alternately by engaging the obliques.",
      "reps/time": "30 sec per side"
    },
    {
      "id": "32",
      "exercise": "Toe Touches",
      "gif": "https://i.imgur.com/7V8bUp7.gif",
      "description": "An abdominal move where you lie on your back and reach for your toes, engaging your upper abs.",
      "reps/time": "30 sec per side"
    },
    {
      "id": "33",
      "exercise": "Plank Shoulder Taps",
      "gif": "https://i.imgur.com/vTZI8M6.gif",
      "description": "A variation of the plank where you alternate tapping your opposite shoulder while maintaining stability in your core.",
      "reps/time": "30 sec per side"
    },
    {
      "id": "34",
      "exercise": "Glute Bridges",
      "gif": "https://i.imgur.com/VFL5KL5.gif",
      "description": "A lower-body exercise where you lie on your back, push through your heels, and lift your hips, targeting the glutes and hamstrings.",
      "reps/time": "3 sets of 12 reps"
    },
    {
      "id": "35",
      "exercise": "Hip Thrusts",
      "gif": "https://i.imgur.com/OSmKgB9.gif",
      "description": "A glute-focused exercise where you rest your upper back on a bench and thrust your hips upward while engaging your glutes.",
      "reps/time": "3 sets of 12 reps"
    },
    {
      "id": "36",
      "exercise": "Fire Hydrants",
      "gif": "https://i.imgur.com/l593ebU.gif",
      "description": "A lower-body move where you lift your knee outward from a tabletop position, targeting the glutes and hip mobility.",
      "reps/time": "3 sets of 12 reps"
    },
    {
      "id": "37",
      "exercise": "Donkey Kicks",
      "gif": "https://i.imgur.com/VchU7Xm.gif",
      "description": "A glute exercise where you kick one leg backward while keeping your knee bent, working on glute activation.",
      "reps/time": "3 sets of 12 reps"
    },
    {
      "id": "38",
      "exercise": "Wall Sit",
      "gif": "https://i.imgur.com/PVMwKIx.gif",
      "description": "A lower-body endurance exercise where you hold a squat position with your back against a wall.",
      "reps/time": "3 sets of 12 reps"
    },
    {
      "id": "39",
      "exercise": "Step-Ups",
      "gif": "https://i.imgur.com/UJrWYHQ.gif",
      "description": "A functional movement where you step onto an elevated surface, engaging your legs and glutes.",
      "reps/time": "3 sets of 12 reps"
    },
    {
      "id": "40",
      "exercise": "Tricep Dips",
      "gif": "https://i.imgur.com/qzI4WNa.gif",
      "description": "An upper-body exercise where you lower and raise your body using a chair or bench, targeting the triceps.",
      "reps/time": "3 sets of 12 reps"
    },
    {
      "id": "41",
      "exercise": "Superman Exercise",
      "gif": "https://i.imgur.com/FYkGvbX.gif",
      "description": "A back-strengthening move where you lie on your stomach and lift your arms and legs simultaneously to engage the lower back.",
      "reps/time": "30 sec per side"
    },
    {
      "id": "42",
      "exercise": "Bird Dog",
      "gif": "https://i.imgur.com/9HbeU0D.gif",
      "description": "A core and balance exercise where you extend one arm and the opposite leg while maintaining stability in a tabletop position.",
      "reps/time": "30 sec per side"
    }
  ]
  return exercise