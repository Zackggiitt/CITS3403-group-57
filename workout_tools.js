// Exercise Data
const exercises = {
    chest: [
        {
            name: "Bench Press",
            image: "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b",
            video: "https://www.youtube.com/embed/rT7DgCr-3pg",
            instructions: "1. Lie on bench with feet flat\n2. Grip bar slightly wider than shoulders\n3. Lower bar to mid-chest\n4. Press up until arms are straight",
            muscles: "Pectoralis Major, Triceps, Anterior Deltoids",
            calories: 10
        },
        {
            name: "Dumbbell Bench Press",
            image: "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b",
            video: "https://www.youtube.com/embed/VmB1G1K7v94",
            instructions: "1. Lie on bench with dumbbells at chest\n2. Press dumbbells up until arms straight\n3. Lower with control\n4. Keep wrists straight",
            muscles: "Pectoralis Major, Triceps, Anterior Deltoids",
            calories: 8
        },
        {
            name: "Incline Bench Press",
            image: "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b",
            video: "https://www.youtube.com/embed/8iPEnn-ltC8",
            instructions: "1. Set bench to 30-45 degree angle\n2. Grip bar slightly wider than shoulders\n3. Lower bar to upper chest\n4. Press up until arms straight",
            muscles: "Upper Pectoralis, Anterior Deltoids",
            calories: 9
        },
        {
            name: "Decline Bench Press",
            image: "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b",
            video: "https://www.youtube.com/embed/LfyQBUKR8SE",
            instructions: "1. Set bench to 15-30 degree decline\n2. Grip bar slightly wider than shoulders\n3. Lower bar to lower chest\n4. Press up until arms straight",
            muscles: "Lower Pectoralis, Triceps",
            calories: 9
        },
        {
            name: "Dumbbell Flyes",
            image: "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b",
            video: "https://www.youtube.com/embed/eozdVDA78K0",
            instructions: "1. Lie on bench with dumbbells above chest\n2. Lower arms in arc motion\n3. Keep slight bend in elbows\n4. Return to start position",
            muscles: "Pectoralis Major, Anterior Deltoids",
            calories: 7
        },
        {
            name: "Chest Press Machine",
            image: "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b",
            video: "https://www.youtube.com/embed/taI4XduLpTk",
            instructions: "1. Adjust seat height\n2. Grip handles at chest level\n3. Press handles forward\n4. Control return to start",
            muscles: "Pectoralis Major, Triceps",
            calories: 8
        },
        {
            name: "Pec Deck / Chest Fly Machine",
            image: "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b",
            video: "https://www.youtube.com/embed/eaTpDgG2Lug",
            instructions: "1. Adjust seat height\n2. Place forearms on pads\n3. Bring arms together\n4. Control return to start",
            muscles: "Pectoralis Major, Anterior Deltoids",
            calories: 7
        },
        {
            name: "Dips for Chest",
            image: "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b",
            video: "https://www.youtube.com/embed/2z8JmcrW-As",
            instructions: "1. Support body on parallel bars\n2. Lean forward slightly\n3. Lower body until shoulders below elbows\n4. Push back up",
            muscles: "Lower Pectoralis, Triceps, Anterior Deltoids",
            calories: 9
        },
        {
            name: "Push-ups",
            image: "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b",
            video: "https://www.youtube.com/embed/IODxDxX7oi4",
            instructions: "1. Start in plank position\n2. Lower body until chest nearly touches ground\n3. Push back up to start\n4. Keep core engaged",
            muscles: "Pectoralis Major, Triceps, Core",
            calories: 6
        },
        {
            name: "Incline Push-ups",
            image: "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b",
            video: "https://www.youtube.com/embed/3WDI0pCzEnA",
            instructions: "1. Place hands on elevated surface\n2. Keep body straight\n3. Lower chest to surface\n4. Push back up",
            muscles: "Upper Pectoralis, Triceps, Core",
            calories: 5
        }
    ],
    back: [
        {
            name: "Pull-ups",
            image: "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b",
            video: "https://www.youtube.com/embed/eGo4IYlbE5g",
            instructions: "1. Hang from bar with overhand grip\n2. Pull body up until chin clears bar\n3. Lower with control\n4. Keep core engaged",
            muscles: "Latissimus Dorsi, Biceps, Trapezius",
            calories: 10
        },
        {
            name: "Lat Pulldown",
            image: "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b",
            video: "https://www.youtube.com/embed/CAZ7EGqv4Go",
            instructions: "1. Sit with thighs under pads\n2. Pull bar to upper chest\n3. Control return to start\n4. Keep chest up",
            muscles: "Latissimus Dorsi, Biceps, Trapezius",
            calories: 7
        },
        {
            name: "Barbell Row",
            image: "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b",
            video: "https://www.youtube.com/embed/9EGnuK5hJ9c",
            instructions: "1. Bend at hips with back straight\n2. Pull barbell to lower chest\n3. Lower with control\n4. Keep core engaged",
            muscles: "Latissimus Dorsi, Rhomboids, Trapezius",
            calories: 9
        },
        {
            name: "Dumbbell Row",
            image: "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b",
            video: "https://www.youtube.com/embed/roCP6wCXPqo",
            instructions: "1. Place hand and knee on bench\n2. Pull dumbbell to hip\n3. Lower with control\n4. Keep back straight",
            muscles: "Latissimus Dorsi, Rhomboids, Trapezius",
            calories: 8
        },
        {
            name: "Seated Cable Row",
            image: "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b",
            video: "https://www.youtube.com/embed/GZbfZ033f74",
            instructions: "1. Sit with feet on platform\n2. Pull handle to abdomen\n3. Squeeze shoulder blades\n4. Control return",
            muscles: "Latissimus Dorsi, Rhomboids, Trapezius",
            calories: 7
        },
        {
            name: "T-Bar Row",
            image: "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b",
            video: "https://www.youtube.com/embed/j3Igk5nyZEI",
            instructions: "1. Stand over T-bar\n2. Pull weight to chest\n3. Lower with control\n4. Keep back straight",
            muscles: "Latissimus Dorsi, Rhomboids, Trapezius",
            calories: 9
        },
        {
            name: "Deadlift",
            image: "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b",
            video: "https://www.youtube.com/embed/1ZXobu7JvvE",
            instructions: "1. Stand with feet hip-width\n2. Bend at hips and knees\n3. Lift bar by extending hips\n4. Lower with control",
            muscles: "Hamstrings, Glutes, Lower Back",
            calories: 15
        },
        {
            name: "Reverse Flyes",
            image: "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b",
            video: "https://www.youtube.com/embed/eaTpDgG2Lug",
            instructions: "1. Bend at hips with dumbbells\n2. Raise arms to sides\n3. Squeeze shoulder blades\n4. Lower with control",
            muscles: "Rear Deltoids, Trapezius, Rhomboids",
            calories: 6
        },
        {
            name: "Superman",
            image: "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b",
            video: "https://www.youtube.com/embed/cc6UVRS7PW4",
            instructions: "1. Lie face down\n2. Lift arms and legs\n3. Hold position\n4. Lower with control",
            muscles: "Lower Back, Glutes, Hamstrings",
            calories: 4
        },
        {
            name: "Face Pull",
            image: "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b",
            video: "https://www.youtube.com/embed/rep-qVOkqgk",
            instructions: "1. Use rope attachment on cable\n2. Pull towards face\n3. Squeeze shoulder blades\n4. Control return",
            muscles: "Rear Deltoids, Trapezius, Rhomboids",
            calories: 5
        }
    ],
    shoulders: [
        {
            name: "Lateral Raises",
            image: "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b",
            video: "https://www.youtube.com/embed/3VfM1HBK_0w",
            instructions: "1. Hold dumbbells at sides\n2. Raise arms to shoulder height\n3. Lower with control\n4. Keep slight bend in elbows",
            muscles: "Lateral Deltoids, Trapezius",
            calories: 6
        },
        {
            name: "Front Raises",
            image: "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b",
            video: "https://www.youtube.com/embed/-t7fuZ0KhDA",
            instructions: "1. Hold dumbbells in front\n2. Raise arms to shoulder height\n3. Lower with control\n4. Keep slight bend in elbows",
            muscles: "Anterior Deltoids, Upper Chest",
            calories: 6
        },
        {
            name: "Dumbbell Shoulder Press",
            image: "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b",
            video: "https://www.youtube.com/embed/qEwKCR5JCog",
            instructions: "1. Hold dumbbells at shoulders\n2. Press overhead until arms straight\n3. Lower with control\n4. Keep core tight",
            muscles: "Deltoids, Triceps, Upper Chest",
            calories: 8
        },
        {
            name: "Barbell Overhead Press",
            image: "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b",
            video: "https://www.youtube.com/embed/2yjwXTZQDDI",
            instructions: "1. Hold barbell at shoulder level\n2. Press overhead until arms straight\n3. Lower with control\n4. Keep core tight",
            muscles: "Deltoids, Triceps, Upper Chest",
            calories: 9
        },
        {
            name: "Arnold Press",
            image: "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b",
            video: "https://www.youtube.com/embed/6Z15HBGQD3c",
            instructions: "1. Start with palms facing you\n2. Rotate arms as you press\n3. Lower with rotation\n4. Keep core tight",
            muscles: "Deltoids, Triceps, Upper Chest",
            calories: 8
        },
        {
            name: "Dumbbell Shrugs",
            image: "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b",
            video: "https://www.youtube.com/embed/cJRVVxmytaM",
            instructions: "1. Hold dumbbells at sides\n2. Raise shoulders to ears\n3. Hold at top\n4. Lower with control",
            muscles: "Trapezius, Upper Back",
            calories: 5
        },
        {
            name: "Upright Row",
            image: "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b",
            video: "https://www.youtube.com/embed/amCU-ziHITM",
            instructions: "1. Hold barbell with narrow grip\n2. Pull bar to chin\n3. Keep elbows high\n4. Lower with control",
            muscles: "Deltoids, Trapezius, Biceps",
            calories: 7
        },
        {
            name: "Reverse Flyes",
            image: "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b",
            video: "https://www.youtube.com/embed/eaTpDgG2Lug",
            instructions: "1. Bend at hips with dumbbells\n2. Raise arms to sides\n3. Squeeze shoulder blades\n4. Lower with control",
            muscles: "Rear Deltoids, Trapezius, Rhomboids",
            calories: 6
        }
    ],
    arms: {
        biceps: [
            {
                name: "Dumbbell Curl",
                image: "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b",
                video: "https://www.youtube.com/embed/ykJmrZ5v0Oo",
                instructions: "1. Hold dumbbells at sides\n2. Curl weights to shoulders\n3. Lower with control\n4. Keep elbows stationary",
                muscles: "Biceps Brachii, Brachialis",
                calories: 5
            },
            {
                name: "Barbell Curl",
                image: "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b",
                video: "https://www.youtube.com/embed/kwG2ipFRgfo",
                instructions: "1. Hold barbell with underhand grip\n2. Curl bar to shoulders\n3. Lower with control\n4. Keep elbows close to body",
                muscles: "Biceps Brachii, Brachialis",
                calories: 6
            },
            {
                name: "Seated Alternating Curl",
                image: "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b",
                video: "https://www.youtube.com/embed/soxrZlIl35U",
                instructions: "1. Sit on bench with dumbbells\n2. Alternate curling each arm\n3. Keep back straight\n4. Control movement",
                muscles: "Biceps Brachii, Brachialis",
                calories: 5
            },
            {
                name: "Preacher Curl",
                image: "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b",
                video: "https://www.youtube.com/embed/fIWP-FRFNU0",
                instructions: "1. Rest arms on preacher bench\n2. Curl weight up\n3. Lower with control\n4. Keep back straight",
                muscles: "Biceps Brachii, Brachialis",
                calories: 6
            },
            {
                name: "Close-grip Lat Pulldown for Biceps",
                image: "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b",
                video: "https://www.youtube.com/embed/CAZ7EGqv4Go",
                instructions: "1. Use close grip attachment\n2. Pull bar to chest\n3. Focus on biceps\n4. Control return",
                muscles: "Biceps Brachii, Brachialis",
                calories: 7
            }
        ],
        triceps: [
            {
                name: "Close-grip Bench Press",
                image: "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b",
                video: "https://www.youtube.com/embed/6Z15HBGQD3c",
                instructions: "1. Lie on bench with close grip\n2. Lower bar to chest\n3. Press up until arms straight\n4. Keep elbows close",
                muscles: "Triceps, Chest",
                calories: 8
            },
            {
                name: "Triceps Pushdown",
                image: "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b",
                video: "https://www.youtube.com/embed/2-LAMcpzODU",
                instructions: "1. Use rope or bar attachment\n2. Push down until arms straight\n3. Control return\n4. Keep elbows at sides",
                muscles: "Triceps",
                calories: 6
            },
            {
                name: "Skull Crushers",
                image: "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b",
                video: "https://www.youtube.com/embed/d_KZxkY_0cM",
                instructions: "1. Lie on bench with barbell\n2. Lower bar to forehead\n3. Extend arms\n4. Keep elbows stationary",
                muscles: "Triceps",
                calories: 7
            },
            {
                name: "One-arm Dumbbell Overhead Extension",
                image: "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b",
                video: "https://www.youtube.com/embed/6Z15HBGQD3c",
                instructions: "1. Hold dumbbell overhead\n2. Lower behind head\n3. Extend arm\n4. Keep elbow stationary",
                muscles: "Triceps",
                calories: 5
            },
            {
                name: "Dips",
                image: "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b",
                video: "https://www.youtube.com/embed/2z8JmcrW-As",
                instructions: "1. Support body on parallel bars\n2. Lower body by bending elbows\n3. Push back up\n4. Keep elbows close",
                muscles: "Triceps, Chest, Shoulders",
                calories: 7
            }
        ]
    },
    legs: [
        {
            name: "Squats",
            image: "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b",
            video: "https://www.youtube.com/embed/aclHkVaku9U",
            instructions: "1. Stand with feet shoulder-width\n2. Lower body by bending knees\n3. Keep chest up and back straight\n4. Push through heels to stand",
            muscles: "Quadriceps, Glutes, Hamstrings",
            calories: 12
        },
        {
            name: "Barbell Back Squat",
            image: "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b",
            video: "https://www.youtube.com/embed/SW_C1A-rejs",
            instructions: "1. Place bar on upper back\n2. Lower body until thighs parallel\n3. Keep chest up\n4. Push through heels",
            muscles: "Quadriceps, Glutes, Hamstrings",
            calories: 15
        },
        {
            name: "Dumbbell Squat",
            image: "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b",
            video: "https://www.youtube.com/embed/gsNoPYwWXeM",
            instructions: "1. Hold dumbbells at sides\n2. Lower body until thighs parallel\n3. Keep chest up\n4. Push through heels",
            muscles: "Quadriceps, Glutes, Hamstrings",
            calories: 10
        },
        {
            name: "Bulgarian Split Squat",
            image: "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b",
            video: "https://www.youtube.com/embed/2C-uNgKwPLE",
            instructions: "1. Place back foot on bench\n2. Lower body until front thigh parallel\n3. Keep chest up\n4. Push through front heel",
            muscles: "Quadriceps, Glutes, Hamstrings",
            calories: 8
        },
        {
            name: "Leg Press",
            image: "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b",
            video: "https://www.youtube.com/embed/IZxyjW7MPJQ",
            instructions: "1. Adjust seat position\n2. Place feet on platform\n3. Lower weight until knees at 90 degrees\n4. Push through heels",
            muscles: "Quadriceps, Glutes, Hamstrings",
            calories: 12
        },
        {
            name: "Lunges",
            image: "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b",
            video: "https://www.youtube.com/embed/QOVaHwm-Q6U",
            instructions: "1. Step forward with one leg\n2. Lower body until back knee nearly touches ground\n3. Push back to start\n4. Keep torso upright",
            muscles: "Quadriceps, Glutes, Hamstrings",
            calories: 8
        },
        {
            name: "Walking Lunges",
            image: "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b",
            video: "https://www.youtube.com/embed/L8fvypPrzzs",
            instructions: "1. Step forward into lunge\n2. Push through front heel\n3. Bring back leg forward\n4. Repeat with other leg",
            muscles: "Quadriceps, Glutes, Hamstrings",
            calories: 9
        },
        {
            name: "Leg Curl",
            image: "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b",
            video: "https://www.youtube.com/embed/1Tq3QdYUuHs",
            instructions: "1. Lie face down on machine\n2. Place ankles under pad\n3. Curl legs up\n4. Control return",
            muscles: "Hamstrings",
            calories: 6
        },
        {
            name: "Leg Extension",
            image: "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b",
            video: "https://www.youtube.com/embed/YyvSfVjQeL0",
            instructions: "1. Sit on machine\n2. Place ankles under pad\n3. Extend legs\n4. Control return",
            muscles: "Quadriceps",
            calories: 6
        },
        {
            name: "Romanian Deadlift",
            image: "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b",
            video: "https://www.youtube.com/embed/JCXUYuzwNrM",
            instructions: "1. Hold barbell with overhand grip\n2. Hinge at hips\n3. Lower bar along legs\n4. Return to start",
            muscles: "Hamstrings, Glutes, Lower Back",
            calories: 10
        },
        {
            name: "Standing Calf Raise",
            image: "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b",
            video: "https://www.youtube.com/embed/JByVl2QvwxM",
            instructions: "1. Stand on edge of platform\n2. Raise heels as high as possible\n3. Lower heels below platform\n4. Repeat",
            muscles: "Gastrocnemius, Soleus",
            calories: 5
        },
        {
            name: "Seated Calf Raise",
            image: "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b",
            video: "https://www.youtube.com/embed/JByVl2QvwxM",
            instructions: "1. Sit on machine\n2. Place balls of feet on platform\n3. Raise heels as high as possible\n4. Lower below platform",
            muscles: "Soleus",
            calories: 5
        }
    ],
    core: [
        {
            name: "Sit-ups",
            image: "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b",
            video: "https://www.youtube.com/embed/1fbU_MkV7NE",
            instructions: "1. Lie on back with knees bent\n2. Place hands behind head\n3. Curl torso up\n4. Lower with control",
            muscles: "Rectus Abdominis, Hip Flexors",
            calories: 5
        },
        {
            name: "Crunches",
            image: "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b",
            video: "https://www.youtube.com/embed/Xyd_fa5zoEU",
            instructions: "1. Lie on back with knees bent\n2. Place hands behind head\n3. Lift shoulders off ground\n4. Lower with control",
            muscles: "Rectus Abdominis",
            calories: 4
        },
        {
            name: "Russian Twists",
            image: "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b",
            video: "https://www.youtube.com/embed/wkD8rjkodUI",
            instructions: "1. Sit with knees bent\n2. Lean back slightly\n3. Twist torso side to side\n4. Keep core engaged",
            muscles: "Obliques, Rectus Abdominis",
            calories: 5
        },
        {
            name: "Plank",
            image: "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b",
            video: "https://www.youtube.com/embed/pSHjTRCQxIw",
            instructions: "1. Start in push-up position\n2. Support body on forearms\n3. Keep body straight\n4. Hold position",
            muscles: "Rectus Abdominis, Transverse Abdominis, Obliques",
            calories: 4
        },
        {
            name: "Side Plank",
            image: "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b",
            video: "https://www.youtube.com/embed/K2VljzCC16g",
            instructions: "1. Lie on side\n2. Support body on forearm\n3. Lift hips off ground\n4. Hold position",
            muscles: "Obliques, Transverse Abdominis",
            calories: 4
        },
        {
            name: "Hanging Leg Raises",
            image: "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b",
            video: "https://www.youtube.com/embed/l4kQd9eWclE",
            instructions: "1. Hang from bar\n2. Raise legs to 90 degrees\n3. Lower with control\n4. Keep core engaged",
            muscles: "Lower Abs, Hip Flexors",
            calories: 6
        },
        {
            name: "Reverse Crunch",
            image: "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b",
            video: "https://www.youtube.com/embed/Xyd_fa5zoEU",
            instructions: "1. Lie on back with legs up\n2. Lift hips off ground\n3. Lower with control\n4. Keep core engaged",
            muscles: "Lower Abs, Hip Flexors",
            calories: 5
        },
        {
            name: "Mountain Climbers",
            image: "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b",
            video: "https://www.youtube.com/embed/cnyTQDSE884",
            instructions: "1. Start in push-up position\n2. Bring knee to chest\n3. Alternate legs\n4. Keep core tight",
            muscles: "Rectus Abdominis, Hip Flexors",
            calories: 7
        },
        {
            name: "Bicycle Crunches",
            image: "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b",
            video: "https://www.youtube.com/embed/9FGilxCbdz8",
            instructions: "1. Lie on back with hands behind head\n2. Bring opposite elbow to knee\n3. Alternate sides\n4. Keep core engaged",
            muscles: "Rectus Abdominis, Obliques",
            calories: 6
        },
        {
            name: "Leg Raises",
            image: "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b",
            video: "https://www.youtube.com/embed/l4kQd9eWclE",
            instructions: "1. Lie on back with legs straight\n2. Raise legs to 90 degrees\n3. Lower with control\n4. Keep lower back pressed to floor",
            muscles: "Lower Abs, Hip Flexors",
            calories: 6
        }
    ]
};

// Initialize the page
document.addEventListener('DOMContentLoaded', function () {
    loadExercises();
    initializeCalorieChart();
    setupEventListeners();
    initializeCalorieCalculator();
});

// Load exercises into the grid
function loadExercises(category = 'all') {
    const container = document.getElementById('exercises-container');
    container.innerHTML = '';

    let exercisesToShow = [];
    if (category === 'all') {
        Object.values(exercises).forEach(categoryExercises => {
            exercisesToShow = exercisesToShow.concat(categoryExercises);
        });
    } else {
        exercisesToShow = exercises[category] || [];
    }

    exercisesToShow.forEach(exercise => {
        const card = createExerciseCard(exercise);
        container.appendChild(card);
    });
}

// Create exercise card element
function createExerciseCard(exercise) {
    const card = document.createElement('div');
    card.className = 'exercise-card';
    card.innerHTML = `
        <img src="${exercise.image}" alt="${exercise.name}">
        <div class="exercise-card-content">
            <h3>${exercise.name}</h3>
            <button class="view-details" data-exercise='${JSON.stringify(exercise)}'>View Details</button>
        </div>
    `;
    return card;
}

// Initialize calorie chart
function initializeCalorieChart() {
    const ctx = document.getElementById('calorieChart').getContext('2d');
    const chart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
            datasets: [{
                label: 'Calories Burned',
                data: [0, 0, 0, 0, 0, 0, 0],
                backgroundColor: 'rgba(76, 175, 80, 0.6)',
                borderColor: 'rgba(76, 175, 80, 1)',
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
    window.calorieChart = chart;
}

// Calorie Calculator Functions
function initializeCalorieCalculator() {
    const calculatorForm = document.getElementById('calorie-calculator-form');
    if (calculatorForm) {
        calculatorForm.addEventListener('submit', function (e) {
            e.preventDefault();
            calculateCalories();
        });
    }
}

function calculateCalories() {
    const weight = parseFloat(document.getElementById('weight').value);
    const duration = parseFloat(document.getElementById('duration').value);
    const intensity = document.getElementById('intensity').value;

    if (isNaN(weight) || isNaN(duration)) {
        showAlert('Please enter valid weight and duration');
        return;
    }

    let caloriesPerMinute;
    switch (intensity) {
        case 'low':
            caloriesPerMinute = 3.5;
            break;
        case 'moderate':
            caloriesPerMinute = 7;
            break;
        case 'high':
            caloriesPerMinute = 10;
            break;
        default:
            caloriesPerMinute = 5;
    }

    const caloriesBurned = Math.round(caloriesPerMinute * duration * (weight / 70));
    document.getElementById('calories-result').textContent = caloriesBurned;
    document.getElementById('calories-result-container').style.display = 'block';
}

// Setup event listeners
function setupEventListeners() {
    // Category filter
    document.getElementById('category-filter').addEventListener('change', function (e) {
        loadExercises(e.target.value);
    });

    // Search filter
    document.getElementById('exercise-search').addEventListener('input', function (e) {
        const searchTerm = e.target.value.toLowerCase();
        const cards = document.querySelectorAll('.exercise-card');
        cards.forEach(card => {
            const title = card.querySelector('h3').textContent.toLowerCase();
            card.style.display = title.includes(searchTerm) ? 'block' : 'none';
        });
    });

    // Category cards
    document.querySelectorAll('.category-card').forEach(card => {
        card.addEventListener('click', function () {
            const category = this.dataset.category;
            document.getElementById('category-filter').value = category;
            loadExercises(category);
        });
    });

    // Exercise details modal
    document.addEventListener('click', function (e) {
        if (e.target.classList.contains('view-details')) {
            const exercise = JSON.parse(e.target.dataset.exercise);
            showExerciseModal(exercise);
        }
    });

    // Close modal
    document.querySelector('.close-modal').addEventListener('click', function () {
        document.getElementById('exercise-modal').style.display = 'none';
    });

    // Add to workout
    document.querySelector('.add-to-workout').addEventListener('click', function () {
        const exercise = JSON.parse(this.dataset.exercise);
        addToWorkout(exercise);
    });

    // Calorie Calculator
    const calculatorForm = document.getElementById('calorie-calculator-form');
    if (calculatorForm) {
        calculatorForm.addEventListener('submit', function (e) {
            e.preventDefault();
            calculateCalories();
        });
    }
}

// Show exercise modal
function showExerciseModal(exercise) {
    const modal = document.getElementById('exercise-modal');
    document.getElementById('modal-exercise-name').textContent = exercise.name;
    document.getElementById('modal-exercise-instructions').textContent = exercise.instructions;
    document.getElementById('modal-exercise-muscles').textContent = exercise.muscles;
    document.getElementById('modal-exercise-calories').textContent = `${exercise.calories} calories per set`;

    // Update video iframe
    const videoIframe = document.getElementById('exercise-video');
    const videoId = exercise.video.split('/').pop();
    videoIframe.src = `https://www.youtube.com/embed/${videoId}`;

    document.querySelector('.add-to-workout').dataset.exercise = JSON.stringify(exercise);
    modal.style.display = 'block';
}

// Add exercise to workout
function addToWorkout(exercise) {
    const day = prompt('Which day would you like to add this exercise to? (Monday-Sunday)');
    if (day) {
        const dayIndex = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'].indexOf(day.toLowerCase());
        if (dayIndex !== -1) {
            const slot = document.querySelector(`.workout-slot[data-day="${day.toLowerCase()}"]`);
            if (slot) {
                const exerciseElement = document.createElement('div');
                exerciseElement.className = 'workout-exercise';
                exerciseElement.innerHTML = `
                    <h4>${exercise.name}</h4>
                    <p>${exercise.calories} calories/set</p>
                `;
                slot.appendChild(exerciseElement);
                updateCalorieChart(dayIndex, exercise.calories);
            }
        }
    }
}

// Update calorie chart
function updateCalorieChart(dayIndex, calories) {
    const chart = window.calorieChart;
    chart.data.datasets[0].data[dayIndex] += calories;
    chart.update();
} 